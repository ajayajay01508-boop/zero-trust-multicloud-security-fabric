# policy.py - Policy Engine Example

from fastapi import HTTPException, status

def evaluate_policy(role: str, resource: str, action: str):
    # Simple placeholder policy
    if role == "admin":
        return True
    elif role == "user" and action == "read":
        return True
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Policy Engine: '{role}' cannot '{action}' on '{resource}'"
        )
