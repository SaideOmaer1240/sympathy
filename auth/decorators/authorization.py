from functools import wraps
from starlette.responses import JSONResponse
from starlette.requests import Request
from auth.utils import verificar_token_jwt

def autenticar(role=None):
    def decorator(func):
        @wraps(func)
        async def wrapper(req: Request, *args, **kwargs):
            # Verificar se o token está presente nos cookies
            token = req.cookies.get("access_token")
            if not token:
                return JSONResponse(content={"message": "Acesso negado: token não encontrado."}, status_code=403)
            
            # Verificar e decodificar o token JWT
            payload = verificar_token_jwt(token)
            if not payload:
                return JSONResponse(content={"message": "Acesso negado: token inválido."}, status_code=403)
            
            # Se uma role específica for exigida, verificá-la
            if role and payload.get("role") != role:
                return JSONResponse(content={"message": "Acesso negado: permissão insuficiente."}, status_code=403)
            
            # Armazenar o payload no estado da requisição
            req.state.user = payload
            return await func(req, *args, **kwargs)
        
        return wrapper
    return decorator
