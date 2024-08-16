import os
import time
import subprocess

# Directory where the PDFs are stored
pdf_directory = "/Users/rahul/Documents/ai_paper_to_read/AI-Paper-to-read-/LLM"
# Path to your README.md file
readme_file = "/Users/rahul/Documents/ai_paper_to_read/AI-Paper-to-read-/README.md"

def update_readme():
    pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]
    pdf_files.sort(key=lambda x: os.path.getmtime(os.path.join(pdf_directory, x)), reverse=True)

    with open(readme_file, 'w') as readme:
        readme.write("# AI-Paper-to-read-\n\n")
        for pdf in pdf_files:
            title = pdf.replace('.pdf', '')
            readme.write(f"- [{pdf}]({pdf_directory}%2F{pdf}) : {title}\n")

def commit_changes():
    try:
        subprocess.run(["git", "add", readme_file], check=True)
        subprocess.run(["git", "commit", "-m", "Update README.md with new research papers"], check=True)
        subprocess.run(["git", "push"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during git operations: {e}")

def monitor_directory():
    current_files = set(os.listdir(pdf_directory))
    while True:
        time.sleep(10)  # Check every 10 seconds
        new_files = set(os.listdir(pdf_directory))
        if new_files != current_files:
            update_readme()
            commit_changes()  # Automatically commit and push the changes
            current_files = new_files

if __name__ == "__main__":
    update_readme()  # Initial update
    commit_changes()  # Commit the initial update
    monitor_directory()
