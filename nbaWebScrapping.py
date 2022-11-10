import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_nba_stats():
    driver = webdriver.Chrome()
    driver.get("https://www.nba.com/stats/teams/traditional")

    # Get the table
    table = driver.find_element("xpath", '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table')
    # Get the rows
    rows = table.find_elements("tag name", "tr")
    # Get the data
    data = []
    for row in rows:
        data.append(row.text)

    # Close the driver
    #driver.close()

    return data

x=get_nba_stats()
print(x[1])
