

class Bars:
    def __init__(self, page):
        self.page = page
        self.mikroblog_button = page.locator('a[href="https://www.wykop.pl/mikroblog/"]')
        self.accept_button = page.frame_locator("#cmp-iframe").locator('button:has-text("Zaakceptuj wszystko")')

    def navigate(self):
        self.page.goto("https://wykop.pl")

    def clickOnAccept(self):
        self.accept_button.click()

    def clickOnMikroblog(self):
        self.mikroblog_button.click()
        self.page.wait_for_timeout(1000)
