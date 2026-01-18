# rbac.py - Role-Based Access Control

from fastapi import HTTPException, status

# Example role permissions
ROLE_PERMISSIONS = {
    "admin": ["read", "write", "delete"],
    "user": ["read"]
}

def require_role(role: str, action: str):
    permissions = ROLE_PERMISSIONS.get(role)
    if not permissions or action not in permissions:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"RBAC: Role '{role}' cannot perform '{action}'"
        )
    return True
