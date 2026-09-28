# Test & UAT Plan

## Layers
- Unit: endpoint and validation behavior
- Integration: container startup/config assumptions
- Smoke: health + core API path
- Performance baseline: p95 target <500 ms
- UAT: business acceptance scenarios

## Severity
| Level | Meaning | Gate rule |
|---|---|---|
| Sev-1 | unusable/critical | zero open |
| Sev-2 | major blocked function | zero unless explicitly accepted |
| Sev-3 | workaround exists | may defer |
| Sev-4 | cosmetic | may defer |

## UAT exit criteria
100% Must requirements tested; no open Sev-1; no unowned Sev-2; Product Owner acceptance recorded.
