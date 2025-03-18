import os
import shutil
from textnode import TextNode, TextType
from markdown_to_textnode import markdown_to_textnode

def main():
    CleanDir("public")
    CopyNewContent("static", "public")

def CleanDir(dir_path):
    if not os.path.exists(dir_path):
        raise Exception(f"Cannot Clean {dir_path} -> {dir_path} does not exist")

    if len(os.listdir(dir_path)) == 0:
        print(f"No items to Clean -> {dir_path} is empty.")
        return

    print(f"---> Cleaning Directory: {dir_path}")
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            CleanDir(item_path)  # Recursively remove directories
            os.rmdir(item_path)
        else:
            os.remove(item_path)  # Remove file
            print(f" --> Deleted: {item_path}")
    print(f"  -> Cleaned all Files from {dir_path}")

def CopyNewContent(src_dir, dest_dir):
    if not os.path.exists(src_dir):
        print(f"Cannot Copy {src_dir} -> {src_dir} does not exist")
        return

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    if len(os.listdir(dest_dir)) != 0:
        print(f"{dest_dir} is not Clean -> Copy Canceled")
        return

    print(f"---> Copying Files from {src_dir} to {dest_dir}")
    for item in os.listdir(src_dir):
        src_item = os.path.join(src_dir, item)
        dest_item = os.path.join(dest_dir, item)
        
        if os.path.isdir(src_item):
            CopyNewContent(src_item, dest_item)
        else:
            print(f" --> Copying file: {src_item} to {dest_item}")
            shutil.copy(src_item, dest_item)  # Copy the file
    print(f"  -> Copy of {src_item} to {dest_item} Complete")

            
if __name__ == "__main__":
    main()