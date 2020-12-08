from urllib.parse import parse_qs

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections
from channels.auth import AuthMiddleware, AuthMiddlewareStack, UserLazyObject
from channels.db import database_sync_to_async
from channels.sessions import CookieMiddleware, SessionMiddleware
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.authtoken.models import Token
# User = get_user_model()


# @database_sync_to_async
# def get_user(scope):
#     close_old_connections()
#     print("THE NEW STUFF------------------------------------")
#     query_string = parse_qs(scope['query_string'].decode())
#     token = query_string.get('token')
#     if not token:
#         return AnonymousUser()
#     try:
#         access_token = AccessToken(token[0])
#         user = User.objects.get(id=access_token['id'])
#     except Exception as exception:
#         return AnonymousUser()
#     if not user.is_active:
#         return AnonymousUser()
#     return user


# class TokenAuthMiddleware(AuthMiddleware):
#     async def resolve_scope(self, scope):
#         scope['user']._wrapped = await get_user(scope)


# def TokenAuthMiddlewareStack(inner):
#     return CookieMiddleware(SessionMiddleware(TokenAuthMiddleware(inner)))

class TokenAuthMiddleware:
    """
    Token authorization middleware for Django Channels 2
    """

    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        headers = dict(scope['headers'])
        print("THE NEW STUFF------------------------------------")
        if b'authorization' in headers:
            try:
                token_name, token_key = headers[b'authorization'].decode(
                ).split()
                if token_name == 'Token':
                    token = Token.objects.get(key=token_key)
                    scope['user'] = token.user
                    close_old_connections()
            except Token.DoesNotExist:
                scope['user'] = AnonymousUser()
        return self.inner(scope)


def TokenAuthMiddlewareStack(inner): return TokenAuthMiddleware(
    AuthMiddlewareStack(inner))
