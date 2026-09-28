# Business Case

## Current state
The service runs on a single Ubuntu VM with manual releases, configuration drift risk, limited scaling, slow rollback and weak operational visibility.

## Target state
`GitHub → CI → container registry → Kubernetes/EKS → monitored service`, with infrastructure expressed in Terraform.

## Value hypothesis
A repeatable deployment path should reduce manual effort, improve auditability, shorten recovery time and create clearer ownership between engineering, QA, security and operations.

## Planning envelope
| Item | Assumption |
|---|---:|
| Delivery effort | 520 person-hours |
| Cloud POC envelope | USD 250 |
| Contingency | 15% |
| External vendor spend | USD 0 |
