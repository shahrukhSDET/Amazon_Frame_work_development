from datetime import datetime
from pathlib import Path

import pytest_html
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


#Setting up the fixture to run the test script with 2- browsers option (Chrome or Firefox)

@pytest.fixture(params=["chrome"], scope="class")
def setup(request):
    s = Service("C:\Program Files\JetBrains\chromedriver_win32\chromedriver")
    if request.param == "chrome":
        driver = webdriver.Chrome(service=s)
    if request.param == "firefox":
        driver = webdriver.Firefox(service=s)
    driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_3c01r1321r_e&adgrpid=60612964962&hvpone=&hvptwo=&hvadid=610714031509&hvpos=&hvnetw=g&hvrand=3857331985147024786&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9301885&hvtargid=kwd-32679660&hydadcr=14454_2316419")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


"""dynamic method and configuration to generate automatic html reports everytime when running script
    in directory (Amazon_report) under YEAR-MONTH-DAY folder named as in format- %Y%m%d%H%M """

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_dir = Path("C:\\Users\\Shahrukh\\PycharmProjects\\AmazonAssignment\\Amazon_report", today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir/ f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True

def pytest_html_report_title(report):
    report.title = "Amazon Test Report"


