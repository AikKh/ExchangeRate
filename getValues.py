from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os
import moneys

folder = os.path.dirname(__file__)

PROXY = "127.0.0.1:24000"
opts = Options()
user_agent = 'Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'

webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",

}

webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True
opts.add_argument("user-agent=" + user_agent)
opts.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)

def get(country: str):
    address = "https://wise.com/gb/currency-converter/usd-to-{}-rate?amount=1".format(country.lower())
    driver.get(address)

    targeIinput = driver.find_element_by_id('target-input')
    targeIinput = targeIinput.get_attribute('value')

    return float(targeIinput)

def selAll():
    for i in moneys.values:
        print('Stage -', i)
        if i == 'USD':
            moneys.values[i] = 1
            continue
        moneys.values[i] = get(i)
    print()
    driver.quit()

