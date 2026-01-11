# Zero Trust Policy Engine

def evaluate_policy(role: str, resource: str, action: str):
    """
    Simple example policy engine.
    Allows actions based on roles and resources.
    """
    # Example policy rules
    policy_rules = {
        "admin": ["read", "write", "delete"],
        "user": ["read", "write"],
        "guest": ["read"]
    }

    allowed_actions = policy_rules.get(role, [])

    if action not in allowed_actions:
        raise PermissionError(f"Role '{role}' is not allowed to perform '{action}' on '{resource}'")

    return True