import os
import json
from src import core

class DotfileManager:
    def __init__(self, config_path: str):
        self.home_dir = os.path.expanduser("~")
        self.config = self._load_config(config_path)
        self.backup_dir = os.path.join(self.home_dir, self.config['backup_folder_name'])
        self.items = self.config['items']
        self.ignore_patterns = self.config.get('ignore_patterns', [])

    def _load_config(self, path: str) -> dict:
        """Loads configuration from a JSON file."""
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: Config file not found at {path}")
            return {}

    def backup(self):
        """Runs the backup process."""
        print(f"\n--- Starting Backup to {self.backup_dir} ---")
        
        for item in self.items:
            source = os.path.join(self.home_dir, item)
            destination = os.path.join(self.backup_dir, item)

            if os.path.exists(source):
                try:
                    core.safe_copy(source, destination, self.ignore_patterns)
                except Exception as e:
                    print(f"  [ERR]  Failed to backup {item}: {e}")
            else:
                print(f"  [WARN] Source not found: {item}")
        
        print("--- Backup Complete ---\n")

    def restore(self):
        """Runs the restore process."""
        print("\n--- Starting Restore to Home Directory ---")
        
        if not os.path.exists(self.backup_dir):
            print("Error: Backup directory does not exist.")
            return

        for item in self.items:
            source = os.path.join(self.backup_dir, item)
            destination = os.path.join(self.home_dir, item)

            if os.path.exists(source):
                try:
                    core.safe_copy(source, destination, self.ignore_patterns)
                except Exception as e:
                    print(f"  [ERR]  Failed to restore {item}: {e}")
            else:
                print(f"  [WARN] Backup item not found: {item}")

        print("--- Restore Complete ---\n")