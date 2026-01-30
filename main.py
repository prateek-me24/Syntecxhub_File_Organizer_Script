import os
import shutil
import logging


logging.basicConfig(
    filename="file_organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def get_unique_filename(folder, filename):
    name, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(folder, new_filename)):
        new_filename = f"{name}_{counter}{ext}"
        counter+=1

    return new_filename




def organize_files(folder_path, dry_run=False):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        ext = ext[1:].upper()

        if not ext:
            ext = "NO_EXTENSION"

        target_folder = os.path.join(folder_path, ext)
        new_name = get_unique_filename(target_folder, filename)

        if dry_run:
            msg = f"[DRY RUN] Would move: {filename} -> {ext}/{new_name}"
            print(msg)
            logging.info(msg)
        else:
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, new_name))
            msg = f"Moved: {filename} -> {ext}/{new_name}"
            print(msg)
            logging.info(msg)


if __name__ == "__main__":
    
    FOLDER_TO_ORGANIZE = r"D:\test_files"

    DRY_run = False

    organize_files(FOLDER_TO_ORGANIZE, DRY_run)