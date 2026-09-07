# GA-EXAM-01 Session Handoff

- Task: GA-EXAM-01
- Contract: ga.asset/1
- Scope: isolated validator exercise only; no game-production repository changes.

## Files
- solution.py — implementation of validate_asset(value)
- selftest.py — minimal local verification harness
- selftest.log — raw self-test stdout/stderr plus exit code
- engine.log — raw Godot/Blender executable probes and result

## Executed commands and results
### Python self-test
Command: `cd /mnt/data/ga-exam-01-web-sol && python3 selftest.py`
Result: exit code 0; `GA_EXAM_SELFTEST_OK cases=11 json_shape_probes=12`. See `selftest.log`.

### Engine executable probe
Commands: `command -v godot4`, `command -v godot`, `command -v blender`
Results: all exit code 1 / no path returned; therefore: 本环境未预装，本轮未测引擎. See `engine.log`.

## Next independent acceptance
1. Import `validate_asset` from `solution.py` in a clean Python 3 environment.
2. Re-run the provided valid example and adversarial cases for bool/NaN/infinity, very large JSON integers, LOD invalid-item order skipping, and exact-name duplicate detection.
3. Confirm error codes are unique and emitted only in the mandated global order.
4. Confirm input objects remain unchanged and JSON-representable inputs do not raise.

## 新会话复验记录与剩余限制
- 复验来源固定为提交 `2bb40593ef6c88a5d55546e9bc0ef2e9f98e9b0d`；未读取 Earth、Build3D、装备或其他背景仓库。
- 写入前确认分支 `agent/ga-exam-20260907/web-sol` 的 HEAD 仍精确等于上述固定提交。
- 在当前 Linux 环境中，以固定提交中的 `solution.py` 与 `selftest.py` 同目录、无依赖安装方式重新执行 `python3 selftest.py`。
- 新会话复验结果：stdout 末行为 `GA_EXAM_SELFTEST_OK cases=11 json_shape_probes=12`，stderr 为空，exit code `0`。完整记录见 `recovery.log`，恢复评估见 `recovery.md`。
- 剩余限制：现有 handoff 足以恢复任务号 `GA-EXAM-01`、契约 `ga.asset/1`、文件位置、既有执行记录及最小自测方向，但不足以恢复完整的规范性需求和完整独立验收标准。原始完整字段规则、权威错误码全集及顺序、冲突/抑制规则、附件重复语义、完整输入域与独立验收 oracle 均未在 handoff 中规范性给出；不得以 `solution.py` 的实际行为替代这些缺失需求。
- 原 `engine.log` 仅证明当时环境未发现 Godot/Blender，可执行引擎验证仍未完成；本次按范围仅复跑 Python 原自测，未下载或运行 Godot/Blender。
