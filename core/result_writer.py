import json
from pathlib import Path


def save_results(
    target,
    results,
    nmap_data=None,
    vulnerability_data=None,
    formatted_vulnerabilities=None
):
    """
    Save structured reconnaissance, vulnerability,
    and formatted evidence results.
    """

    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / "recon_results.json"

    tools = {}

    filename_map = {
        "theHarvester": "harvester.txt",
        "gau": "gau.txt",
        "gobuster": "gobuster.txt",
        "nmap": "nmap.txt"
    }

    for result in results:

        tool_name = result.tool

        tools[tool_name] = {
            "status": result.status,
            "return_code": result.return_code,
            "output_file": filename_map.get(
                tool_name
            ),
            "error": result.error
        }

    structured_results = {
        "target": target,
        "tools": tools,
        "nmap_data": nmap_data or {},
        "vulnerability_data": (
            vulnerability_data or []
        ),
        "formatted_vulnerabilities": (
            formatted_vulnerabilities or []
        )
    }

    output_file.write_text(
        json.dumps(
            structured_results,
            indent=4
        ),
        encoding="utf-8"
    )

    return output_file
