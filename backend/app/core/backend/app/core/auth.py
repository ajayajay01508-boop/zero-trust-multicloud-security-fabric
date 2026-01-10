from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def zero_trust_auth(token: str = Depends(oauth2_scheme)):
    if token != "trusted-device-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Zero Trust: Access Denied",
        )
    return {"device": "trusted", "access": "granted"}