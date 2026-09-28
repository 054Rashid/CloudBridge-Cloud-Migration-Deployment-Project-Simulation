# Risk Matrix

Probability × impact, both 1–5.

| ID | Risk | P | I | Score | Mitigation |
|---|---|---:|---:|---:|---|
| R-01 | Cloud/network delay | 3 | 5 | 15 | early validation |
| R-02 | Hidden migration dependency | 3 | 5 | 15 | dependency scan |
| R-03 | UAT delay | 3 | 4 | 12 | reserve buffer |
| R-04 | Cost exceeds envelope | 2 | 4 | 8 | budget alerts |
| R-05 | Rollback not executable | 2 | 5 | 10 | rehearsal |

Scores >=12 are reviewed weekly; critical blockers are escalated same business day.
