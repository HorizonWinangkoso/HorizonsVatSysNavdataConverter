import importlib
import subprocess
import sys

# dependencies here
required_packages = [
    "xml",
    "re",
    "shapely",
    "pyyaml"
]

def install_package(package):
    """Install a Python package using pip."""
    try:
        print(f"Installing missing package: {package}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError as e:
        print(f" Failed to install {package}: {e}")
        sys.exit(1)

def main():
    """Check for missing dependencies and install them if needed."""
    for package in required_packages:
        try:
            importlib.import_module(package)
            print(f" {package} is already installed.")
        except ImportError:
            install_package(package)
    print("dependencies complete!")

if __name__ == "__main__":
    print(" Checking for required dependencies...\n")
    check_and_install_dependencies(required_packages)
    print("\n All dependencies are ready!")
