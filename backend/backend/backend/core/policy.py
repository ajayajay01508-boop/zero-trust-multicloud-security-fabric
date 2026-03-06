from fastapi import HTTPException, status

def evaluate_policy(role: str, resource: str, action: str):
    if role == "admin":
        return True

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Policy Engine: Access denied"
    )
