import os
from src.manager import DotfileManager

def main():
    # Locate the config file relative to this script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "config", "settings.json")

    # Initialize the Manager
    app = DotfileManager(config_path)

    print("Dotfiles Manager (Modular v2.0)")
    print("1. Backup")
    print("2. Restore")
    
    choice = input("Select an option (1-2): ")

    if choice == "1":
        app.backup()
    elif choice == "2":
        app.restore()
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()