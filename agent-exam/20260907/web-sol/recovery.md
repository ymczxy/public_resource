# GA-EXAM-01 Cross-session Recovery

## Recovery source
- Repository: `ymczxy/public_resource`
- Exact handoff commit: `2bb40593ef6c88a5d55546e9bc0ef2e9f98e9b0d`
- Entry: `agent-exam/20260907/web-sol/session.md`
- Target write branch: `agent/ga-exam-20260907/web-sol`
- Pre-write branch check: branch HEAD exactly matched the handoff commit above.

## Recovered identity
- Task: `GA-EXAM-01`
- Contract/version: `ga.asset/1`
- Scope stated by handoff: isolated validator exercise only; no game-production repository changes.

## Recovered artifacts
The handoff directly identifies these sibling files: `solution.py`, `selftest.py`, `selftest.log`, and `engine.log`. They were read at the exact handoff commit. No background project repository was used.

## Linux re-verification
The exact `solution.py` and `selftest.py` content from the handoff commit were placed together in an isolated Linux directory and the provided self-test was re-run with Python 3 and no dependency installation.

Result: exit code `0`; stdout ends with `GA_EXAM_SELFTEST_OK cases=11 json_shape_probes=12`; stderr was empty. Full captured output is in `recovery.log`.

## Completed boundary recovered from the handoff
- An implementation of `validate_asset(value)` exists in `solution.py`.
- A minimal local verification harness exists in `selftest.py`.
- The original handoff records a passing self-test (`11` named cases and `12` JSON-shape probes).
- This recovery independently re-ran that same harness in the current Linux environment and reproduced a passing exit code `0`.
- The harness checks its listed expected results and checks non-mutation for those named cases; it also checks that its 12 JSON-shaped probes do not raise.

## Unverified / incomplete boundary
The handoff material is sufficient to recover the task identity, artifact locations, prior execution record, current implementation, minimal test harness, and the stated direction for further acceptance. It is **not sufficient to recover the complete normative requirements or a fully independent acceptance standard**.

Specifically missing from the handoff as authoritative requirements are:
1. The original complete validator specification, including the exact validity rule for every field and missing-field behavior.
2. An authoritative enumeration of all error codes and their mandated global order. The implementation contains an order, but implementation behavior is not a substitute for a requirement.
3. Authoritative precedence/suppression rules when multiple LOD conditions fail (the handoff only names an adversarial area to re-check).
4. Authoritative attachment-name duplicate semantics and the complete numeric/domain rules for attachment positions.
5. A normative statement defining the complete valid-input domain and whether additional/unknown keys matter.
6. An exhaustive acceptance corpus or independent oracle. `selftest.py` is explicitly described as a minimal harness and therefore cannot by itself establish full conformance.

Consequently, this recovery can verify that the checked-in implementation reproduces the checked-in minimal tests, but it cannot claim conformance to the missing original specification. Code behavior and test expectations were not promoted to requirements.

The prior `engine.log` records that Godot/Blender executables were not present in that environment and engine execution was not tested. This recovery did not expand scope to download or run Godot/Blender; only the original Python self-test was re-run as requested.
