
import os
path = r"C:\Users\hazek\OneDrive\Documents\CLOUD LAPS\inventory-tracker-001"
with open(os.path.join(path, "main.tf"), "w") as f:
    f.write(open(os.path.join(path, "main.tf")).read())
