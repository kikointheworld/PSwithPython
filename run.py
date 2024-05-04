import subprocess


def run_command(command):
    print(f"Running command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True,
                                text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Command succeeded: {command}\nOutput:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(
            f"Error executing command: {command}\nError Code: {e.returncode}\nOutput:\n{e.stderr}")
    except KeyboardInterrupt:
        print("Script interrupted by user.")


def main():
    # Execute the Python script with the test cases text file
    run_command("python3 script.py studentid_testcases.txt")

    # Change directory and ensure it doesn't affect the global state of the script
    run_command(
        "cd 2024s_hw1/findutils-4.7.0/find && gcov -b ../*/*.gcda ../*/*/*.gcda")


if __name__ == "__main__":
    main()
