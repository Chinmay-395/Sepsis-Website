from urllib.parse import parse_qs
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections
from channels.auth import AuthMiddleware, AuthMiddlewareStack, UserLazyObject
from channels.db import database_sync_to_async
from channels.sessions import CookieMiddleware, SessionMiddleware

from rest_framework.authtoken.models import Token


@database_sync_to_async
def get_user(scope):
    close_old_connections()
    # print("THE NEW STUFF------------------------------------")
    # headers = dict(scope['headers'])
    # print("THE newER STUFF------------------------------------")
    # print("THE HEADER", headers)
    query_string = parse_qs(scope['query_string'].decode())
    token = query_string.get('token')
    if not token:
        return AnonymousUser()
    try:
        user = Token.objects.get(key=token[0])
        # print("THE USER is", user)
        # print("THE USER", user)
        # print("THE USERNAME", user.user)
        # print("THE USER email", user.user.email)
    except Exception as exception:
        return AnonymousUser()
    if not user.user.is_active:
        return AnonymousUser()
    return user.user  # basically we are sending the user model


class TokenAuthMiddleware(AuthMiddleware):
    async def resolve_scope(self, scope):
        print("**************************** THE SCOPE ******************************* \n", scope)
        print("************************************************************************************")
        scope['user']._wrapped = await get_user(scope)


def TokenAuthMiddlewareStack(inner):
    return CookieMiddleware(SessionMiddleware(TokenAuthMiddleware(inner)))
