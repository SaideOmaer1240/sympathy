from datetime import datetime, timedelta, timezone
import bcrypt
import jwt
from config import SECRET_KEY

def gerar_token_jwt(email, tipo_usuario):
    payload = {
        "sub": email,
        "role": tipo_usuario,
        "exp": datetime.now(timezone.utc) + timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verificar_token_jwt(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None

def hash_senha(senha):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(senha.encode('utf-8'), salt).decode('utf-8')

def verificar_senha(senha_fornecida, senha_armazenada):
    return bcrypt.checkpw(senha_fornecida.encode('utf-8'), senha_armazenada.encode('utf-8'))
