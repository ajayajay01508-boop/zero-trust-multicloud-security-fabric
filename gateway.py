# Zero Trust API Gateway
from fastapi import Request, HTTPException, status
from core.auth import verify_token
from core.rbac import require_role
from core.policy import evaluate_policy

def zero_trust_gateway(request: Request, role: str, resource: str, action: str):
    token = request.headers.get("Authorization")

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing authentication token"
        )

    verify_token(token)
    evaluate_policy(role, resource, action)

    return True
