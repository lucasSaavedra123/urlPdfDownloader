import pytest
import urlPdfDownloader

downloadable_url = "http://www.repositori.uji.es/xmlui/bitstream/handle/10234/5875/bolAuto"

def test_no_files_from_a_no_pdf_downloadable_website():
    assert len(urlPdfDownloader.get_pdf_files_from_url("http://www.google.com/",1,10)) == 0

def test_no_files_from_another_no_pdf_downloadable_website():
    assert len(urlPdfDownloader.get_pdf_files_from_url("http://www.google.com.ar/",1,5)) == 0

def test_only_one_file_in_downloadable_url():
    assert len(urlPdfDownloader.get_pdf_files_from_url(downloadable_url,1,1)) == 1

def test_only_five_files_in_downloadable_url():
    assert len(urlPdfDownloader.get_pdf_files_from_url(downloadable_url,1,5)) == 5