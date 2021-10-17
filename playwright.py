import time
from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(accept_downloads=True)

    # Open new page
    page = context.new_page()

    # Go to https://wenshu.court.gov.cn/
    page.goto("https://wenshu.court.gov.cn/")

    time.sleep(25)

    # Click text=民事案件
    with page.expect_popup() as popup_info:
        page.click("text=赔偿案件")
    page1 = popup_info.value

    time.sleep(20)

    a = 0
    while(a < 40):   # 实际上裁判文书网一次只能爬600条文书（不中断的话），每页15条，共40页
        a += 1
        time.sleep(5)
        # Check input[type="checkbox"]
        page1.check("input[type=\"checkbox\"]")
        # try:
        #     page1.check("input[type=\"checkbox\"]")
        # except:
        #     page1.goto("https://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId=da1d162d14e7c1c4ec88f1379b64e5ad&s8=03")
        #     time.sleep(30)
        #     page1.check("input[type=\"checkbox\"]")

        time.sleep(2)
        # Click text=批量下载
        with page1.expect_download() as download_info:
            page1.click("text=批量下载")
        download = download_info.value
        download.save_as("E:\\NLP\\StateCompensation\\file5(%d).zip" % a)
        time.sleep(3)

        # Click text=下一页
        page1.click("text=下一页")
        time.sleep(5)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
