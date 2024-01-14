from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

PUBLIC_KEY = os.getenv("JWT_PUBLIC_KEY")
if not PUBLIC_KEY:
    raise Exception("JWT_PUBLIC_KEY environment variable not set")

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, PUBLIC_KEY, algorithms=["RS256"])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")