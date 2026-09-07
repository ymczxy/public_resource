import math


ERROR_ORDER = [
    "manifest_type",
    "schema_version",
    "asset_id",
    "units",
    "lods_type",
    "lod_item",
    "lod_order",
    "attachments_type",
    "attachment_item",
    "attachment_duplicate",
]


def _is_nonblank_string(value):
    return isinstance(value, str) and bool(value.strip())


def _is_strict_positive_int(value):
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def _is_finite_number(value):
    if isinstance(value, bool):
        return False
    if isinstance(value, int):
        return True
    return isinstance(value, float) and math.isfinite(value)


def validate_asset(value):
    if not isinstance(value, dict):
        return ["manifest_type"]

    errors = set()

    if value.get("schema_version") != "ga.asset/1":
        errors.add("schema_version")

    if not _is_nonblank_string(value.get("asset_id")):
        errors.add("asset_id")

    if value.get("units") != "m" or not isinstance(value.get("units"), str):
        errors.add("units")

    lods = value.get("lods")
    if not isinstance(lods, list) or not lods:
        errors.add("lods_type")
    else:
        lod_values = []
        lod_invalid = False
        for item in lods:
            if not isinstance(item, dict) or not _is_strict_positive_int(item.get("triangles")):
                lod_invalid = True
                continue
            lod_values.append(item["triangles"])
        if lod_invalid:
            errors.add("lod_item")
        elif any(a <= b for a, b in zip(lod_values, lod_values[1:])):
            errors.add("lod_order")

    attachments = value.get("attachments")
    if not isinstance(attachments, list):
        errors.add("attachments_type")
    else:
        seen_names = set()
        duplicate = False
        invalid_item = False

        for item in attachments:
            if isinstance(item, dict):
                name = item.get("name")
                if _is_nonblank_string(name):
                    if name in seen_names:
                        duplicate = True
                    else:
                        seen_names.add(name)

                position = item.get("position")
                if (
                    not _is_nonblank_string(name)
                    or not isinstance(position, list)
                    or len(position) != 3
                    or not all(_is_finite_number(component) for component in position)
                ):
                    invalid_item = True
            else:
                invalid_item = True

        if invalid_item:
            errors.add("attachment_item")
        if duplicate:
            errors.add("attachment_duplicate")

    return [code for code in ERROR_ORDER if code in errors]
