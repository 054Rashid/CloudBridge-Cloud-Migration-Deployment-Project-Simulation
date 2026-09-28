# Cutover & Rollback Runbook

> **Simulation only.** Not authorization for a production deployment.

### T-24h
Confirm approval, backup/snapshot, monitoring, rollback owner, communications and cost guardrails.

### T-60m
Freeze non-essential changes; verify legacy health, target health, image version and configuration references.

### Cutover
1. Deploy target version.
2. Run health check.
3. Run smoke test.
4. Validate core endpoint.
5. Compare against baseline.
6. Announce success only after acceptance gates pass.

### Rollback triggers
Failed health checks, critical endpoint failure, regression, security violation, severe latency/error increase.

### Rollback
Stop promotion → route traffic back to previous stable path → validate → capture evidence → notify stakeholders → open incident/problem record → schedule RCA.

### Decision
Product Owner + Engineering Lead approve go/no-go after the readiness checklist is satisfied.
