# GA-EXAM-01 Session Handoff

- Task: GA-EXAM-01
- Contract: ga.asset/1
- Scope: isolated validator exercise only; no game-production repository changes.

## Files
- solution.py — implementation of validate_asset(value)
- selftest.py — minimal local verification harness
- selftest.log — raw self-test stdout/stderr plus exit code
- engine.log — Godot/Blender probe and execution result, or explicit not-preinstalled note

## Executed commands and results
### Python self-test
Command: `cd /mnt/data/ga-exam-01-web-sol && python3 selftest.py`
Result: exit code 0. See `selftest.log` for raw output.

### Engine probe
Detected: None
Result: 本环境未预装，本轮未测引擎. See `engine.log`.

## Next independent acceptance
1. Import `validate_asset` from `solution.py` in a clean Python 3 environment.
2. Re-run the provided valid example and adversarial cases for bool/NaN/infinity, very large JSON integers, LOD invalid-item order skipping, and exact-name duplicate detection.
3. Confirm error codes are unique and emitted only in the mandated global order.
4. Confirm input objects remain unchanged and JSON-representable inputs do not raise.
