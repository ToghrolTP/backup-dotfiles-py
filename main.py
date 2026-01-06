import os
import shutil

home_dir = os.path.expanduser("~")
backup_dir = os.path.join(home_dir, "Dotfiles-Backup")

dotfiles = [".tmux.conf"]

def run_backup():
    """Copies files from Home to the Backup directory."""
    
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        print(f"Created backup directory: {backup_dir}")

    print("--- Starting Backup ---")
    
    for file_name in dotfiles:
        source = os.path.join(home_dir, file_name)
        destination = os.path.join(backup_dir, file_name)

        if os.path.exists(source):
            shutil.copy2(source, destination)
            print(f"Backed up: {file_name}")
        else:
            print(f"Warning: {file_name} not found in home directory.")
            
    print("--- Backup Complete ---\n")

def run_restore():
    """Copies files from the Backup directory back to Home."""
    print("--- Starting Restore ---")
    
    if not os.path.exists(backup_dir):
        print("Error: Backup directory does not exist. Cannot restore.")
        return

    for file_name in dotfiles:
        source = os.path.join(backup_dir, file_name)
        destination = os.path.join(home_dir, file_name)

        if os.path.exists(source):
            shutil.copy2(source, destination)
            print(f"Restored: {file_name}")
        else:
            print(f"Warning: {file_name} not found in backup directory.")
            
    print("--- Restore Complete ---\n")

def main():
    """Main menu to choose action."""
    print("Dotfiles Manager")
    print("1. Backup (Home -> Backup Folder)")
    print("2. Restore (Backup Folder -> Home)")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        run_backup()
    elif choice == "2":
        run_restore()
    else:
        print("Invalid choice. Please run the script again and select 1 or 2.")

if __name__ == "__main__":
    main()
