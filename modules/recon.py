import logging
from pathlib import Path

from core.runner import run_command

def run_recon(target):
    """
    Run passive reconnaissance
    """

    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    logging.info(f"Starting reconnaissance for {target}")

    harvester_result = run_command([
        "theHarvester",
        "-d",
        target,
        "-b",
        "crtsh"
    ])

    if harvester_result:
        with open(output_dir / "harvester.txt", "w", encoding="utf-8") as file:
            file.write(harvester_result.stdout)

    gau_result = run_command([
        "gau",
        target
    ])

    if gau_result:
        with open(output_dir / "gau.txt", "w", encoding="utf-8") as file:
            file.write(gau_result.stdout)

    logging.info("Reconnaissance completed.")