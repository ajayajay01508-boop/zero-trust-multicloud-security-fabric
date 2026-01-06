# zero-trust-multicloud-security-fabric 

**Enterprise-grade Zero Trust Multi-Cloud Security Control Plane Application

## Overview
This project implements an enterprise-grade Zero-Trust Security Control Plane
that enforces identity-centric, policy-based access across AWS, Azure, and GCP.

The system removes implicit network trust and applies continuous verification
using OAuth 2.0, OpenID Connect, mTLS, and Policy-as-Code.

## Architecture
User
→ Security Dashboard (Frontend)  
→ Zero-Trust Control Plane Backend  
→ Policy Decision Engine (OPA)  
→ Zero-Trust Access Proxy (Envoy)  
→ AWS | Azure | GCP Services

## Key Components
- Frontend: Security Control Dashboard
- Backend: Zero-Trust Control Plane API
- Identity: Keycloak
- Policy: Open Policy Agent (OPA)
- Proxy: Envoy
- Runtime Security: Vault, Falco

## Project Status
Phase 0 completed –  architecture & project Foundation initialized.
