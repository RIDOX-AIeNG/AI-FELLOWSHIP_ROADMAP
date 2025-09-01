import csv
from pathlib import Path

workspace = Path("workspace_files666666666666666666666666666666666666666666666666666666666
csv_file = workspace / "students.csv"

# Create sample student data
fieldnames = ["name", "age", "track", "phone_number"]
  
def save_participant(csv_file, contact_info):
    if type(contact_info) == dict:
         contact_info = [contact_info]

    if csv_file.exists():
        print(f"Found the file: {csv_file}")
        
            
    # Write data to CSV file
        with open(csv_file, "a", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                 
                writer.writerows(contact_info) 
        # First 50 characters
    else:
        print(f"File {csv_file} doesn't exist")
        
    # Write data to CSV file
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader() 
                writer.writerows(contact_info) # Write all rows at once



print("Student data written to CSV file!")

def load_partcipants(csv_file):
      print('\nReading CSV file')
    
      with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row_number, row in enumerate(reader):
            if row_number == 0:  # Header row
                print(f"Headers: {' | '.join(row)}")
                print("-" * 40)
            else:  # Data rows
                name, age, track, phone_number = row
            print(f"{name} {age}  {track} {phone_number}")