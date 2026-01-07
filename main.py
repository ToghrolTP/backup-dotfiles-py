import os
import shutil

home_dir = os.path.expanduser("~")
backup_dir = os.path.join(home_dir, "Dotfiles-Backup")

# We use relative paths here. 
# Note: Neovim is usually inside .config/nvim
dotfiles = [
    ".tmux.conf",
    ".config/nvim"  
]

def safe_copy(source, destination):
    """
    Smart copy function that handles both files and directories.
    It also ensures the parent directory of the destination exists.
    """
    # 1. Ensure the parent folder exists (e.g., creates 'Dotfiles-Backup/.config')
    os.makedirs(os.path.dirname(destination), exist_ok=True)

    # 2. Check if source is a directory or a file
    if os.path.isdir(source):
        # Copy directory (dirs_exist_ok=True allows updating existing backups)
        shutil.copytree(source, destination, dirs_exist_ok=True)
        print(f"Directory processed: {os.path.basename(destination)}")
    else:
        # Copy file
        shutil.copy2(source, destination)
        print(f"File processed: {os.path.basename(destination)}")

def run_backup():
    """Copies files from Home to the Backup directory."""
    print("--- Starting Backup ---")
    
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        print(f"Created backup root: {backup_dir}")

    for item in dotfiles:
        source = os.path.join(home_dir, item)
        destination = os.path.join(backup_dir, item)

        if os.path.exists(source):
            try:
                safe_copy(source, destination)
            except Exception as e:
                print(f"Error backing up {item}: {e}")
        else:
            print(f"Warning: Source {item} not found in home directory.")
            
    print("--- Backup Complete ---\n")

def run_restore():
    """Copies files from the Backup directory back to Home."""
    print("--- Starting Restore ---")
    
    if not os.path.exists(backup_dir):
        print("Error: Backup directory does not exist. Cannot restore.")
        return

    for item in dotfiles:
        # Swap source and destination for restore
        source = os.path.join(backup_dir, item)
        destination = os.path.join(home_dir, item)

        if os.path.exists(source):
            try:
                safe_copy(source, destination)
            except Exception as e:
                print(f"Error restoring {item}: {e}")
        else:
            print(f"Warning: Backup for {item} not found.")
            
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
        print("Invalid choice. Please run the script again.")

if __name__ == "__main__":
    main()