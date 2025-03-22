from playwright.sync_api import sync_playwright
from urllib.request import urlretrieve

url = "https://www.archives.gov/research/jfk/release-2025"

pw = sync_playwright().start()
browser = pw.firefox.launch()

page = browser.new_page()
page.goto(url)

# fetch all documents
# via show *** entries
page.select_option("select[name='DataTables_Table_0_length']", value="All")

# fetch all links that contain .pdf
links = page.locator(
    "xpath=//a[contains(., '.pdf')]"
).all()

for i in links:
    # download links and save on system
    doc_url = "https://www.archives.gov" + i.get_attribute("href")
    doc_url = doc_url.replace(" ", "%20")
    doc_name = doc_url.split("/")[-1]
    
    print(doc_name)
    
    # TO AVOID ERRORS
    # please ensure you make a "data/" folder at root
    urlretrieve(doc_url, "data/" + doc_name)
  
print("---------------------")
print("done downloading all!")

browser.close()