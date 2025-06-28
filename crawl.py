"""
crawl.py - Data ingestion from MOSDAC (web, PDF, DOCX, XLSX)
"""
import requests
from bs4 import BeautifulSoup
# from selenium import webdriver
# import fitz  # PyMuPDF
# import docx
# import openpyxl


def crawl_static(url, out_path="data_raw.txt"):
    """Crawl static web page and save visible text to a file."""
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    # Get all visible text
    text = " ".join([t for t in soup.stripped_strings])
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Saved raw text to {out_path}")

def crawl_dynamic(url):
    """Crawl JavaScript-heavy pages using Selenium."""
    # TODO: Implement Selenium crawling
    pass

def extract_pdf(path):
    """Extract text from PDF using PyMuPDF."""
    # TODO: Implement PDF extraction
    pass

def extract_docx(path):
    """Extract text from DOCX using python-docx."""
    # TODO: Implement DOCX extraction
    pass

def extract_xlsx(path):
    """Extract data from XLSX using openpyxl."""
    # TODO: Implement XLSX extraction
    pass

if __name__ == "__main__":
    # Example: Crawl MOSDAC About page
    url = "https://www.mosdac.gov.in/about"
    crawl_static(url, out_path="data_raw.txt") 