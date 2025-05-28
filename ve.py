#import subprocess

#path = input("Enter the path you want to create virtual Environment")
#vename = input("Enter virtual Environment Name")
#command = subprocess.run(["python3","-m" ,"venv" , path , vename])

import os
import subprocess
import sys

def create_virtual_env(path: str, venv_name: str) -> bool:
    """
    Creates a Python virtual environment at the specified path.

    Args:
        path (str): The directory to create the virtual environment in.
        venv_name (str): The name of the virtual environment folder.

    Returns:
        bool: True if creation is successful, False otherwise.
    """
    full_path = os.path.join(path, venv_name)

    try:
        if not os.path.exists(path):
            os.makedirs(path)  # Create base directory if it doesn't exist

        print(f"Creating virtual environment at: {full_path}")
        subprocess.run(
            ["python3", "-m", "venv", full_path],
            check=True
        )
        print(f"✅ Virtual environment '{venv_name}' created successfully at {full_path}")
        return True

    except FileNotFoundError:
        print("❌ Error: Python3 is not found on your system.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to create virtual environment. Error:\n{e}")
    except PermissionError:
        print("❌ Permission denied: You don't have rights to write to the specified directory.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
    
    return False

if __name__ == "__main__":
    path = input("Enter the path to create the virtual environment: ").strip()
    venv_name = input("Enter the virtual environment name: ").strip()
    create_virtual_env(path, venv_name)

