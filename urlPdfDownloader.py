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


"""get_pdf_files_from_url( "https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec0",0,)"""


def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)    
    file = open(filename + ".pdf", 'wb')
    print(type(file))
    file.write(response.read())
    file.close()
 
pdf_path = "http://csg.csail.mit.edu/6.823/Lectures/L0"

for i in range(1,10):
    download_file(pdf_path+str(i)+"split.pdf", "L0"+str(i)+"split")

pdf_path = "http://csg.csail.mit.edu/6.823/Lectures/L"

for i in range(10,30):
    download_file(pdf_path+str(i)+"split.pdf", "L"+str(i)+"split")
