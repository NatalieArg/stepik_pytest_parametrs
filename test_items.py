import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_add_item_button(browser):
    browser.get(link)
    button=len(browser.find_elements_by_css_selector('button[type="submit"]'))
    assert button>1, 'Кнопка добавления товара не найдена'


