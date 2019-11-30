import requests

url = "https://raw.githubusercontent.com/FraQu/test_text_analyzer/master/5.txt"
download_file = requests.get(url, stream=True)

with open('result.txt', 'wb') as f:
    for chunk in download_file.iter_content(chunk_size=1024):
        if not chunk:
            break
        f.write(chunk)

