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


get_pdf_files_from_url( "http://www.repositori.uji.es/xmlui/bitstream/handle/10234/5875/bolAuto",1,10)

"""pdf_path = "http://www.repositori.uji.es/xmlui/bitstream/handle/10234/5875/bolAuto"
def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)    
    file = open(filename + ".pdf", 'wb')
    print(type(file))
 

for i in range(7,100):
    download_file(pdf_path+str(i)+".pdf", "bolAuto"+str(i)+".pdf")
"""