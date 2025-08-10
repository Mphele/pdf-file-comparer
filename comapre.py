import hashlib
from pathlib import Path

while True:
    user_file1 = input("Enter first file name/path: ")
    user_file2 = input("Enter second file name/path: ")

    if not user_file1.endswith(".pdf"):
        print(f"{user_file1} not a pdf file")
        continue
    if not user_file2.endswith(".pdf"):
        print(f"{user_file2} not a pdf file")
        continue

    file1_path = Path(user_file1)
    file2_path = Path(user_file2)

    if not file1_path.exists():
        print(f"{user_file1} not found!")
        continue
    if not file2_path.exists():
        print(f"{user_file2} not found!")
        continue
    break

def hash_read(file_path):
    hash_object = hashlib.sha1()
    with (open(file_path, "rb") as file):

        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            hash_object.update(chunk)
    return hash_object.hexdigest()

result = hash_read(file1_path) == hash_read(file2_path)
if result:
    print("Files are identical")
else:
    print("Files are different")
