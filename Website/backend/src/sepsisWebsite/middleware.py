from urllib.parse import parse_qs

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections
from channels.auth import AuthMiddleware, AuthMiddlewareStack, UserLazyObject
from channels.db import database_sync_to_async
from channels.sessions import CookieMiddleware, SessionMiddleware
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.authtoken.models import Token
User = get_user_model()


@database_sync_to_async
def get_user(scope):
    close_old_connections()
    print("THE NEW STUFF------------------------------------")
    headers = dict(scope['headers'])
    print("THE newER STUFF------------------------------------")
    print("THE HEADER", headers)
    # if b'token' in headers:
    #     token_name, token_key = headers[b'token'].decode().split()
    #     print(f"token \n {token_name} \n and value \n {token_key}")

    # if b'authorization' in headers:
    #     print("THE IF CONDITION RAN")
    #     try:
    #         token_name, token_key = headers[b'authorization'].decode(
    #         ).split()
    #         print('THE TOKEN NAME', token_name)
    #         print('THE TOKEN KEY', token_key)
    #         if token_name == 'Token':
    #             token = Token.objects.get(key=token_key)
    #             scope['user'] = token.user
    #             print("THE USER is", token.user)
    #             print("THE USER", token.user)
    #             print("THE USERNAME", token.user.user)
    #             print("THE USER email", token.user.user.email)
    #             close_old_connections()
    #     except Exception as exception:
    #         print("THE EXCEPTION ", exception)
    query_string = parse_qs(scope['query_string'].decode())
    token = query_string.get('token')
    if not token:
        return AnonymousUser()
    try:
        # access_token = AccessToken(token[0])
        # user = User.objects.get(id=access_token['id'])
        user = Token.objects.get(key=token[0])
        print("THE USER is", user)
        print("THE USER", user)
        print("THE USERNAME", user.user)
        print("THE USER email", user.user.email)
    except Exception as exception:
        return AnonymousUser()
    if not user.user.is_active:
        return AnonymousUser()
    return user


class TokenAuthMiddleware(AuthMiddleware):
    async def resolve_scope(self, scope):
        print("**************************** THE SCOPE ******************************* \n", scope)
        print("************************************************************************************")
        scope['user']._wrapped = await get_user(scope)


def TokenAuthMiddlewareStack(inner):
    return CookieMiddleware(SessionMiddleware(TokenAuthMiddleware(inner)))
