import logging
from pathlib import Path

from core.runner import run_command


def run_gobuster(target):
    """
    Run Gobuster DNS enumeration against an authorized target.
    """

    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / "gobuster.txt"

    # Clear previous results
    output_file.write_text("", encoding="utf-8")

    logging.info(f"Starting Gobuster DNS enumeration for {target}")

    result = run_command(
        [
            "gobuster",
            "dns",
            "--domain",
            target,
            "--wordlist",
            "wordlists/subdomains.txt",
            "--no-color",
            "--quiet"
        ],
        timeout=120
    )

    if result.stdout:
        output_file.write_text(
            result.stdout,
            encoding="utf-8"
        )

    logging.info(
        f"Gobuster completed with status: {result.status}"
    )

    return result

def run_nmap(target):
    """
    Run Nmap service and version detection against an authorized target.
    """

    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / "nmap.txt"

    # Clear previous results
    output_file.write_text("", encoding="utf-8")

    logging.info(f"Starting Nmap scan for {target}")

    result = run_command(
        [
            "nmap",
            "-sV",
            target
        ],
        timeout=180
    )

    if result.stdout:
        output_file.write_text(
            result.stdout,
            encoding="utf-8"
        )

    logging.info(
        f"Nmap completed with status: {result.status}"
    )

    return result
