import urllib.request
from urllib.error import HTTPError


def get_pdf_files_from_url(url, first, last):
    files = []

    for index in range(first,last+1):
        try:
            download_url = url + str(index) + '.pdf'
            response = urllib.request.urlopen(download_url,timeout=5)
            files.append(response.read())
        except (HTTPError, ValueError):
            print("Warning: Failure with "+ url + str(index) + '.pdf')

    return files


def save_pdf_files(files):
    for i in range(len(files)):
        file = open(str(i)+".pdf",'wb')
        file.write(files[i])
        file.close()
