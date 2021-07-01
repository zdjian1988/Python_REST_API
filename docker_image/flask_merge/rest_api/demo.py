from typing import Dict


def wrap(
    json_dict: Dict[str, object],
) -> Dict[str, object]:

    return {
        "wrap": json_dict,
    }
