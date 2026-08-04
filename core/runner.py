import subprocess
import logging


def run_command(command, timeout=60):
    """
    Execute a command and return its result.
    """

    try:
        logging.info(f"Running command: {' '.join(command)}")

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout
        )

        logging.info("Command completed successfully.")

        return result

    except FileNotFoundError:
        logging.error(f"Command not found: {command[0]}")
        return None

    except subprocess.TimeoutExpired:
        logging.error("Command timed out.")
        return None

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return None