from pathlib import Path

workspace = Path("TASK12") / "workspace"
file_path = workspace / "task.txt"
file_path
def save_task(file_path,tasks):
    if file_path.exists():
     with open(file_path, "a", newline="", encoding="utf-8") as f:
        f.write(tasks)

    else:
       print(f"{file_path} does not exist. ")
       with open(file_path, "w", newline="", encoding="utf-8") as f:
        f.write(tasks)
print("task added succesfully")  

def view_tasks():
  print('\n Viewing the file')

  with open(file_path, "r", encoding='utf-8') as f:
    print(f.read())

