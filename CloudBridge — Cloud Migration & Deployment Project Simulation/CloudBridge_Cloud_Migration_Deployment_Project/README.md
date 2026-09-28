# CloudBridge — Cloud Migration & Deployment Project Simulation

> **Self-directed portfolio project / simulation — not professional client work.**

CloudBridge simulates an enterprise migration of a Python demand-insights API from a legacy Ubuntu VM to a standardized containerized Kubernetes/cloud platform. The repository combines **technical implementation with project-delivery governance** so a technical project manager can demonstrate planning, stakeholder coordination, risk/dependency control, testing, cutover, handover, and technical fluency.

## Scenario

Fictional customer: **Northstar Retail**. Its demand-insights service runs on one Ubuntu VM with manual releases and limited observability. The target state is a repeatable platform using Ubuntu, Docker, Kubernetes, AWS EKS (target architecture), Terraform, GitHub Actions, and Python/FastAPI.

## Target business outcomes

| KPI | Baseline | Target |
|---|---:|---:|
| Release cycle | 2–3 hours manual | <20 minutes |
| Recovery objective | ~4 hours | <60 minutes |
| Rollback | Manual | <10 minutes |
| Availability | Best effort | 99.9% |
| Infrastructure change | Manual | Version-controlled IaC |
| Operational visibility | Log inspection | Health + metrics + alerts |

*Targets are simulation assumptions, not real customer measurements.*

## What is in this repo

- Project charter and business case
- Requirements and acceptance gates
- Work breakdown structure and 16-week delivery plan
- Stakeholder register and RACI
- RAID log, risk matrix and dependency map
- Communication plan and change-control process
- Test/UAT plan and release acceptance criteria
- Cutover + rollback runbook
- Weekly status report, handover checklist and closure/lessons learned
- Working FastAPI service with unit tests
- Dockerfile and Kubernetes manifests
- Terraform target architecture for AWS/EKS
- GitHub Actions CI workflow
- Issue templates + PR template

## Lifecycle

`Discovery → Requirements → Architecture → Build → Test → UAT → Cutover → Hypercare → Handover → Closure`

## Architecture

```text
Users
  |
  v
Load Balancer / Ingress
  |
  v
Kubernetes / EKS
  |
  +--> FastAPI service --> Target data store
  |
  +--> Health / metrics / logs

GitHub --> GitHub Actions --> Container Registry --> Kubernetes
Terraform -------------------------------> AWS infrastructure
```

## Run locally

```bash
cd app
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/docs`.

Run tests:

```bash
pytest -q
```

Run smoke test from the repository root:

```bash
python scripts/local_smoke_test.py
```

## Docker

```bash
docker build -t cloudbridge-api ./app
docker run --rm -p 8000:8000 cloudbridge-api
```

## Kubernetes

The manifests are Kubernetes-compatible and include a Deployment, Service, readiness/liveness probes and HPA. Replace the example image with your registry image before real deployment.

## Terraform

Terraform describes a proposed AWS VPC + EKS target. It is intentionally **not applied** by this repository. Validate provider/module versions, IAM, security groups, encryption, logging, policy, and cost before any real cloud use.

## Honest interview positioning

> “I built a self-directed cloud migration and delivery simulation around a Python analytics API. I created the charter, WBS, stakeholder/RACI model, RAID log, risk and dependency plan, change-control process, UAT gates, cutover/rollback runbook and handover plan, then built deployment-ready Docker, Kubernetes, Terraform and CI/CD artifacts.”

Do not claim Northstar Retail is a real customer or that this project was deployed to production.

## License

MIT
