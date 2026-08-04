import argparse
import logging
from core.logger import setup_logger
from modules.recon import run_recon

def print_banner():
    """Diplay the application banner."""
    print("=" * 50)
    print("   AI-Powered VAPT Assitant")
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
    setup_logger()

    print_banner()

    args = get_arguments()

    logging.info(f"Target selected: {args.target}")
    
    run_recon(args.target)


if __name__ == "__main__":
    main()