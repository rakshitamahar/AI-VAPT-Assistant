from core.runner import run_command

result = run_command(["whoami"])

if result:
    print("Output:")
    print(result.stdout)

    print("Return Code:")
    print(result.returncode)
else:
    print("Command failed.")