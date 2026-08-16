import logging
from pathlib import Path

from core.runner import run_command


def run_recon(target):
    """
    Run passive reconnaissance and return structured results.
    """

    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    logging.info(f"Starting reconnaissance for {target}")

    # -------------------------------------------------
    # Remove old reconnaissance output
    # -------------------------------------------------

    harvester_file = output_dir / "harvester.txt"
    gau_file = output_dir / "gau.txt"

    harvester_file.write_text("", encoding="utf-8")
    gau_file.write_text("", encoding="utf-8")

    results = []

    # -------------------------------------------------
    # theHarvester
    # -------------------------------------------------

    harvester_result = run_command(
        [
            "theHarvester",
            "-d",
            target,
            "-b",
            "crtsh"
        ],
        timeout=180
    )

    if harvester_result.stdout:
        harvester_file.write_text(
            harvester_result.stdout,
            encoding="utf-8"
        )

    results.append(harvester_result)

    # -------------------------------------------------
    # GAU
    # -------------------------------------------------

    gau_result = run_command(
        [
            "gau",
            "--providers",
            "otx",
            "--timeout",
            "15",
            target
        ],
        timeout=60
    )

    if gau_result.stdout:
        gau_file.write_text(
            gau_result.stdout,
            encoding="utf-8"
        )

    results.append(gau_result)

    logging.info("Reconnaissance completed.")

    return results
