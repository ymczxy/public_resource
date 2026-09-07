import copy
import json
import math
from solution import validate_asset

VALID = {
    "schema_version": "ga.asset/1",
    "asset_id": "demo-crate",
    "units": "m",
    "lods": [{"triangles": 100}, {"triangles": 40}],
    "attachments": [{"name": "mount", "position": [0, 1, 2]}],
}

cases = [
    ("valid", VALID, []),
    ("manifest", [1, 2, 3], ["manifest_type"]),
    (
        "front_fields",
        {"schema_version": 1, "asset_id": "  ", "units": None, "lods": [{"triangles": 3}], "attachments": []},
        ["schema_version", "asset_id", "units"],
    ),
    (
        "lod_type",
        {"schema_version": "ga.asset/1", "asset_id": "a", "units": "m", "lods": [], "attachments": []},
        ["lods_type"],
    ),
    (
        "lod_item_skips_order",
        {"schema_version": "ga.asset/1", "asset_id": "a", "units": "m", "lods": [{"triangles": 10}, {"triangles": True}, {"triangles": 20}], "attachments": []},
        ["lod_item"],
    ),
    (
        "lod_order",
        {"schema_version": "ga.asset/1", "asset_id": "a", "units": "m", "lods": [{"triangles": 10}, {"triangles": 10}], "attachments": []},
        ["lod_order"],
    ),
    (
        "attachment_type",
        {"schema_version": "ga.asset/1", "asset_id": "a", "units": "m", "lods": [{"triangles": 10}], "attachments": {}},
        ["attachments_type"],
    ),
    (
        "attachment_invalid_and_duplicate_exact_untrimmed",
        {
            "schema_version": "ga.asset/1",
            "asset_id": "a",
            "units": "m",
            "lods": [{"triangles": 10}],
            "attachments": [
                {"name": "x", "position": [0, 1, math.inf]},
                {"name": "x", "position": [0, 1, 2]},
                {"name": " x ", "position": [0, 1, 2]},
            ],
        },
        ["attachment_item", "attachment_duplicate"],
    ),
    (
        "attachment_huge_int",
        {
            "schema_version": "ga.asset/1",
            "asset_id": "a",
            "units": "m",
            "lods": [{"triangles": 10}],
            "attachments": [{"name": "huge", "position": [10**1000, 0, 1]}],
        },
        [],
    ),
    (
        "attachment_bool_nan",
        {
            "schema_version": "ga.asset/1",
            "asset_id": "a",
            "units": "m",
            "lods": [{"triangles": 10}],
            "attachments": [
                {"name": "a", "position": [True, 1, 2]},
                {"name": "b", "position": [0.0, float("nan"), 2.0]},
            ],
        },
        ["attachment_item"],
    ),
    (
        "error_order",
        {
            "schema_version": None,
            "asset_id": "",
            "units": 1,
            "lods": [{"triangles": 2}, {"triangles": 3}],
            "attachments": [{"name": "dup", "position": [0, 0]}, {"name": "dup", "position": [0, 0, 0]}],
        },
        ["schema_version", "asset_id", "units", "lod_order", "attachment_item", "attachment_duplicate"],
    ),
]

for name, value, expected in cases:
    before = copy.deepcopy(value)
    result = validate_asset(value)
    if result != expected:
        raise AssertionError(f"{name}: expected {expected}, got {result}")
    if value != before:
        raise AssertionError(f"{name}: input mutated")
    print(f"PASS {name}: {json.dumps(result)}")

json_shapes = [None, True, False, 0, 1, -1, 1.5, "", "x", [], {}, [1, {"x": [None, True, "s"]}]]
for probe in json_shapes:
    try:
        validate_asset(copy.deepcopy(probe))
    except Exception as exc:
        raise AssertionError(f"JSON-shaped input raised: {probe!r}: {exc!r}") from exc

print(f"GA_EXAM_SELFTEST_OK cases={len(cases)} json_shape_probes={len(json_shapes)}")
