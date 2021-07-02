import urllib.request


def get_pdf_files_from_url(url,first,last):
    files = []
    for index in range(first,last+1):
        download_url = url + str(index) + '.pdf'
        response = urllib.request.urlopen(download_url)
        print(response.status)
        files.append(response.read())

    return files

"""
pdf_path = "http://www.repositori.uji.es/xmlui/bitstream/handle/10234/5875/bolAuto"
def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)    
    file = open(filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()
 

for i in range(7,100):
    download_file(pdf_path+str(i)+".pdf", "bolAuto"+str(i)+".pdf")
"""