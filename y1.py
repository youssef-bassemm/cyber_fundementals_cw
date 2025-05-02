import os

def search_files(directory, extensions):
    with open('files.log', 'w') as log_file:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(tuple(extensions)):
                    log_file.write(f"Found: {os.path.join(root, file)}\n")
    print("File search completed. Check files.log.")

if __name__ == "__main__":
    directory = input("Enter the directory to search in: ")
    extensions = ['.txt', '.docx', '.jpg']
    search_files(directory, extensions)

    