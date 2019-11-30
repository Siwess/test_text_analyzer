import requests

###
# Download file from url and save as 'result.txt' for later purposes.
###

url = "https://raw.githubusercontent.com/FraQu/test_text_analyzer/master/5.txt"
download_file = requests.get(url, stream=True)

with open('result.txt', 'wb') as f:
    for chunk in download_file.iter_content(chunk_size=1024):
        if not chunk:
            break
        f.write(chunk)

