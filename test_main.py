from Page.Bars import Bars


def test_main(page):
    b = Bars(page)
    b.navigate()
    b.clickOnAccept()
    b.clickOnMikroblog()
    b.clickOnMikroblog()
