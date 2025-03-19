import os
import shutil
from textnode import TextNode, TextType
from markdown_to_blocks import markdown_to_html_node

def main():
    print("===| Phase 1: Cleaning |===")
    CleanDir("public")

    print("\n===| Phase 2: Copying |===")
    CopyNewContent("static", "public")

    print("\n===| Phase 3: Generating Pages |===")
    generate_pages_recursive('content', 'template.html', 'public')

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Walk through the content directory
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith('.md'):  # Process only markdown files
                markdown_file = os.path.join(root, file)

                # Generate the corresponding HTML file path
                relative_path = os.path.relpath(markdown_file, start=dir_path_content)
                dest_file_path = os.path.join(dest_dir_path, os.path.splitext(relative_path)[0] + '.html')

                # Generate the page using the generate_page function
                generate_page(markdown_file, template_path, dest_file_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read markdown content
    with open(from_path, 'r') as f:
        markdown_content = f.read()
    
    # Convert markdown to HTML
    html_content = markdown_to_html_node(markdown_content).to_html()
    
    # Extract title from markdown
    title = extract_title(markdown_content)
    
    # Read the template file
    with open(template_path, 'r') as f:
        template_content = f.read()
    
    # Replace placeholders with title and content
    page_content = template_content.replace('{{ Title }}', title).replace('{{ Content }}', html_content)
    
    # Ensure the destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write the generated page to the destination file
    with open(dest_path, 'w') as f:
        f.write(page_content)

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    raise ValueError("No H1 header found in the markdown.")

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