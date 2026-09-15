import re
from pathlib import Path


def parse_nmap_output(file_path):
    """
    Parse basic Nmap service/version output.

    Returns structured information about the scanned host
    and discovered ports.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        return {
            "host": None,
            "status": "file_not_found",
            "ports": []
        }

    text = file_path.read_text(encoding="utf-8")

    result = {
        "host": None,
        "status": "unknown",
        "ports": []
    }

    # Extract target IP/hostname
    host_match = re.search(
        r"Nmap scan report for (.+)",
        text
    )

    if host_match:
        result["host"] = host_match.group(1).strip()

    # Determine whether host is up
    if "Host is up" in text:
        result["status"] = "up"
    elif "Host seems down" in text:
        result["status"] = "down"

    # Parse open ports
    port_pattern = re.compile(
        r"^(\d+)/(\w+)\s+"
        r"(open|closed|filtered)\s+"
        r"(\S+)"
        r"(?:\s+(.*))?$",
        re.MULTILINE
    )

    for match in port_pattern.finditer(text):

        port = {
            "port": int(match.group(1)),
            "protocol": match.group(2),
            "state": match.group(3),
            "service": match.group(4),
            "version": (match.group(5) or "").strip()
        }

        result["ports"].append(port)

    return result
