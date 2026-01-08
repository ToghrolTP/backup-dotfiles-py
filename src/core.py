import os
import shutil

def safe_copy(source: str, destination: str, ignore_patterns: list) -> None:
    """
    Intelligently copies a file or directory.
    
    Args:
        source (str): Path to the source item.
        destination (str): Path where the item should be copied.
        ignore_patterns (list): List of file patterns to ignore (e.g., ['*.git']).
    """
    # Ensure the parent directory exists
    os.makedirs(os.path.dirname(destination), exist_ok=True)

    if os.path.isdir(source):
        # Convert list of patterns into a shutil ignore callable
        ignore_func = shutil.ignore_patterns(*ignore_patterns)
        
        # Copy directory (dirs_exist_ok allows updating existing backups)
        shutil.copytree(source, destination, dirs_exist_ok=True, ignore=ignore_func)
        print(f"  [DIR]  {os.path.basename(destination)}")
        
    elif os.path.isfile(source):
        # Copy individual file
        shutil.copy2(source, destination)
        print(f"  [FILE] {os.path.basename(destination)}")
        
    else:
        raise FileNotFoundError(f"Source not found: {source}")