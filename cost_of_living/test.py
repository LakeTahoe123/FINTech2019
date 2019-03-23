from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)
#driver = webdriver.Firefox()
driver.get("https://www.numbeo.com/cost-of-living/in/Allentown")
table = driver.find_element(By.CLASS_NAME, "data_wide_table")
rows = table.find_elements(By.TAG_NAME, "tr")

for row in rows:
	cols = row.find_elements(By.TAG_NAME, "td")
	if len(cols) == 3:
		print("%s,  %s" % (cols[0].text, cols[1].text))

