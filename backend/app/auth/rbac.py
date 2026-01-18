from fastapi import HTTPException, status, Depends
from app.auth.auth import zero_trust_auth

# Define role permissions
role_permissions = {
    "admin": ["read", "write", "delete"],
    "user": ["read"]
}

def require_role(action: str):
    def decorator(user=Depends(zero_trust_auth)):
        role = user.get("role")
        if not role or action not in role_permissions.get(role, []):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Role '{role}' cannot perform '{action}'"
            )
        return True
    return decorator
