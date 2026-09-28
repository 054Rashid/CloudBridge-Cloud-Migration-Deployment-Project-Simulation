# Requirements & Acceptance

| ID | Requirement | Priority | Acceptance |
|---|---|---|---|
| FR-01 | Health endpoint | Must | `/health` healthy |
| FR-02 | Forecast endpoint | Must | valid request returns forecast |
| FR-03 | Containerization | Must | Docker build succeeds |
| FR-04 | Kubernetes deployment | Must | probes/resources defined |
| FR-05 | Automated CI | Must | PR/push tests run |
| FR-06 | Rollback procedure | Must | trigger + steps documented |
| FR-07 | Infrastructure as code | Should | Terraform target defined |
| FR-08 | Observability approach | Should | health/metrics/logs documented |

## Quality gates
**Build:** local service + tests + image build.  
**UAT:** all Must requirements tested, zero Sev-1 defects.  
**Go-live:** rollback ready, risks accepted/mitigated, stakeholder communication ready.  
**Handover:** operations ownership and support artifacts complete.
