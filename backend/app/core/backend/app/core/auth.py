"""
Zero Trust Authentication Module
Every request must prove identity
"""

def verify_identity(token: str) -> bool:
    """
    Simulated identity verification
    In real systems: JWT, OAuth, mTLS
    """
    if not token:
        return False

    trusted_tokens = ["trusted-service-token", "admin-token"]
    return token in trusted_tokens
