import os

directory = r"C:\Users\Pavankrishna\OneDrive\Desktop\new\completions"

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r") as f:
            content = f.read()
            print(f"File: {filename}\n{content}\n")
