from functools import wraps
from starlette.responses import Response
from functools import wraps
from starlette.responses import Response
from starlette.responses import JSONResponse  

from starlette.requests import Request
def goodcookies(cookie_name: str):
    def decorator(func):
        @wraps(func)
        async def wrapper(req: Request, *args, **kwargs):
            # Chamada da função decorada
            response = await func(req, *args, **kwargs)

            # Pegar o valor a ser armazenado, assumindo que é passado como argumento
            value_to_store = kwargs.get('id')  # O ID deve ser passado como um parâmetro

            # Armazenar o valor no cookie se não for None
            if value_to_store is not None:
                response.set_cookie(key=cookie_name, value=str(value_to_store), httponly=True)

            return response
        return wrapper
    return decorator
