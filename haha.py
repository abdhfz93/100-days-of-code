import subprocess

def run_git_commands():
    try:
        # Step 1: git add .
        print("Running 'git add .' ...")
        subprocess.run(["git", "add", "."], check=True)
        
        # Step 2: git commit with a user-provided message
        commit_message = input("Enter your commit message: ").strip()
        if not commit_message:
            print("Commit message cannot be empty!")
            return
        print(f"Running 'git commit -m \"{commit_message}\"' ...")
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # Step 3: git push
        print("Running 'git push' ...")
        subprocess.run(["git", "push"], check=True)
        
        print("All git commands ran successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running: {e.cmd}")
        print("Error details:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

# Run the function
if __name__ == "__main__":
    run_git_commands()
