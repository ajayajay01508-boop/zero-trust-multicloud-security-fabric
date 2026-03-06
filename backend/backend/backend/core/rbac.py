# Role-Based Access Control (RBAC)

from fastapi import Depends,
HTTPException, status
from typing import List

def require_role(required_roles:
List[str]):
def role_checker(user: dict =Depends(lambda: {"role": "admin"})):
                                     if user["role"] not in required_roles:
raise HTTPExecption( status_code=status.HTTP_403_FORBIDDEN, detail="Access denied: insufficent permissions")
retuen True
return role_checker
