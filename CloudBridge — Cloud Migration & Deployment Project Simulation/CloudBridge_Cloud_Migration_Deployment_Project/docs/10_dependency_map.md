# Dependency Map

| Dependency | Needed by | Owner | Risk if late |
|---|---|---|---|
| Repository | all streams | PM | High |
| Cloud access model | Terraform/K8s | Cloud | High |
| Registry | deployment | Cloud | High |
| Security review | go-live | Security | High |
| UAT users | UAT | Product | Medium |
| Monitoring | handover | Ops | Medium |
| Runbook approval | cutover | Ops | High |

Dependencies are reviewed at the weekly status meeting and escalated when their due date threatens the critical path.
