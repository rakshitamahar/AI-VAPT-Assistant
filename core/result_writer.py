import json
from pathlib import Path


def save_results(target, results):
    """
    Save structured reconnaissance results as JSON.
    """

    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    tools = {}

    for result in results:
        output_file = None

        if result.tool == "theHarvester":
            output_file = "harvester.txt"

        elif result.tool == "gau":
            output_file = "gau.txt"

        tools[result.tool] = {
            "status": result.status,
            "return_code": result.return_code,
            "output_file": output_file,
            "error": result.error
        }

    data = {
        "target": target,
        "tools": tools
    }

    output_file = output_dir / "recon_results.json"

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            data,
            file,
            indent=4
        )

    return output_file
