import os
import shutil
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor


def copy_file_to_target(file_path, target_dir):
    target_subdir = target_dir / file_path.suffix.lstrip('.')
    try:
        target_subdir.mkdir(parents=True, exist_ok=True)
        shutil.copy(file_path, target_subdir)
    except Exception as e:
        print(f"Error copying {file_path} to {target_subdir}: {e}")


def process_directory(source_dir, target_dir):
    # Обр.файлов в директории
    with ThreadPoolExecutor() as executor:
        for root, _, files in os.walk(source_dir):
            for file in files:
                file_path = Path(root) / file
                executor.submit(copy_file_to_target, file_path, target_dir)


def main():
    if len(sys.argv) < 2:
        print("Usage: Sorter <source_dir> [target_dir]")
        sys.exit(1)

    source_dir = Path(sys.argv[1])
    target_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")

    if not source_dir.is_dir():
        print(f"{source_dir} is not a valid directory.")
        sys.exit(1)

    target_dir.mkdir(parents=True, exist_ok=True)

    print(f"Processing files from '{source_dir}' to '{target_dir}'")
    process_directory(source_dir, target_dir)
    print("Done!")


if __name__ == "__main__":
    main()
