import argparse
import logging

from core.nmap_parser import parse_nmap_output
from modules.scanner import run_gobuster, run_nmap
from core.logger import setup_logger
from core.result_writer import save_results
from modules.recon import run_recon
from modules.vulnerability import analyze_nmap_services
from core.vulnerability_formatter import format_vulnerability_results


def print_banner():
    """Display the application banner."""
    print("=" * 50)
    print("      AI-Powered VAPT Assistant")
    print("=" * 50)


def get_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="AI-Powered VAPT Assistant"
    )

    parser.add_argument(
        "target",
        help="Target domain or IP address"
    )

    return parser.parse_args()


def main():
    """Main entry point of the application."""

    # Initialize logging
    setup_logger()

    # Display banner
    print_banner()

    # Get command-line arguments
    args = get_arguments()

    logging.info(f"Target selected: {args.target}")

    # Run reconnaissance
    results = run_recon(args.target)

    # Run Gobuster
    gobuster_result = run_gobuster(args.target)

    # Add Gobuster result to reconnaissance results
    results.append(gobuster_result)

    # Run Nmap
    nmap_result = run_nmap(args.target)

    # Add Nmap result to reconnaissance results
    results.append(nmap_result)

    # Parse Nmap output
    nmap_data = parse_nmap_output("outputs/nmap.txt")
    vulnerability_results = analyze_nmap_services(
        nmap_data
    )
    formatted_vulnerabilities = format_vulnerability_results(
    vulnerability_results
    )

    logging.info(
    f"Formatted vulnerability findings: "
    f"{len(formatted_vulnerabilities)}"
    )

    logging.info(
        f"Vulnerability analysis completed: "
        f"{len(vulnerability_results)} services analyzed"
    )

    logging.info(
        f"Nmap parsed successfully:"
        f" {len(nmap_data['ports'])} ports found"
    )

    # Save all structured reconnaissance results
    result_file = save_results(
    args.target,
    results,
    nmap_data,
    vulnerability_results,
    formatted_vulnerabilities
    )

    logging.info(
        f"Reconnaissance results saved to {result_file}"
    )

    print("\nReconnaissance completed.")
    print(f"Results saved to: {result_file}")


if __name__ == "__main__":
    main()
