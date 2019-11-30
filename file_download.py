import requests
import file_url


def file_download():
    ###
    # Download file from url and save as 'result.txt' for later purposes.
    ###

    download_file = requests.get(file_url.url, stream=True)

    with open('result.txt', 'wb') as file:
        for chunk in download_file.iter_content(chunk_size=1024):
            if not chunk:
                break
            file.write(chunk)


