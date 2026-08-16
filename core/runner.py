import subprocess
import logging

from core.result import ToolResult


def run_command(command, timeout=180):
    """
    Execute a command and return a structured ToolResult.
    """

    tool_name = command[0]

    try:
        logging.info(f"Running command: {' '.join(command)}")

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout
        )

        if result.returncode == 0:
            if result.stdout.strip():
                status = "success"
            else:
                status = "empty"

            logging.info(
                f"{tool_name} completed with status: {status}"
            )

            return ToolResult(
                tool=tool_name,
                status=status,
                stdout=result.stdout,
                stderr=result.stderr,
                return_code=result.returncode
            )

        logging.error(
            f"{tool_name} failed with return code "
            f"{result.returncode}"
        )

        return ToolResult(
            tool=tool_name,
            status="failed",
            stdout=result.stdout,
            stderr=result.stderr,
            return_code=result.returncode,
            error=result.stderr.strip()
        )

    except FileNotFoundError:
        logging.error(f"{tool_name} not found")

        return ToolResult(
            tool=tool_name,
            status="not_found",
            error=f"{tool_name} is not installed or not in PATH"
        )

    except subprocess.TimeoutExpired:
        logging.error(
            f"{tool_name} timed out after {timeout} seconds"
        )

        return ToolResult(
            tool=tool_name,
            status="timeout",
            error=f"Command timed out after {timeout} seconds"
        )

    except Exception as e:
        logging.error(
            f"Unexpected error while running {tool_name}: {e}"
        )

        return ToolResult(
            tool=tool_name,
            status="failed",
            error=str(e)
        )
