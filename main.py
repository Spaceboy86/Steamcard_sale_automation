import time
import pyautogui
import pwinput
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

global totalPrice


def login():
    username = input("Steam User Name: ")
    password = pwinput.pwinput("Steam Password ")
    alt_tab()
    time.sleep(1.5)
    pyautogui.typewrite(str(f"{username}"))
    pyautogui.hotkey("tab")
    pyautogui.typewrite(str(f"{password}"))
    # Steam constantly changes the class names and XPaths for the login in button,
    # so as of current this is not automated
    element = driver.find_element(By.CLASS_NAME, "_2v60tM463fW0V7GDe92E5f")  # login button
    element.click()

    time.sleep(3)


def check_page(landed, desired):
    if driver.current_url == landed:
        driver.get(desired)
        print("Login Sucessful")
    else:
        time.sleep(3)
        check_page(landed, desired)


def alt_tab():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')
    time.sleep(1)


def select_card():
    try:
        element = driver.find_element(By.XPATH, "//div[@class='inventory_page'][1]/div[@class='itemHolder'][13]")
    except NoSuchElementException:
        print("(By.XPATH, //div[@class='inventory_page'][1]/div[@class='itemHolder'][13]")
        return
    element.click()
    time.sleep(2)


def apply_filter():  # applies filter to select only regular steam trading cards
    attempt = 0
    while attempt < 5:
        try:
            element = driver.find_element(By.ID, "filter_tag_show")
            element.click()
            time.sleep(2.5)
            filter_box = driver.find_element(By.NAME, "tag_filter_753_0_cardborder_cardborder_0")
            filter_box.click()
            attempt = 5
        except ElementNotInteractableException:
            print("applyFilter() element not interactable" + str(attempt))
            time.sleep(1.5)
            attempt = attempt + 1


def check_price():  # checks the price of a card based on the current "want to buy at" price
    time.sleep(1.5)
    try:
        # element = driver.find_element(By.XPATH, "//div[@id='iteminfo1_item_market_actions']/div/div")
        element = driver.find_element(By.XPATH, "//a[contains(@href,'/steamcommunity.com/market/listings/753')]")
    except NoSuchElementException:
        print("Check price not itemINfo 1")
        try:
            element = driver.find_element(By.XPATH, "//div[@id='iteminfo0_item_market_actions']/div/div")
        except NoSuchElementException:
            print("Check price not itemINfo 0")
            try:
                element = driver.find_element(By.XPATH, "//div[@id='iteminfo2_item_market_actions']/div/div")
            except NoSuchElementException:
                print("Check price not itemINfo 2")
                check_price()
                return
            except ElementNotInteractableException:
                print("checkPrice() element not interactable")
                time.sleep(1.5)
                check_price()
                return
        except ElementNotInteractableException:
            print("checkPrice() element not interactable")
            time.sleep(1.5)
            check_price()
            return

    try:
        element.click()
    except ElementNotInteractableException:
        print("checkPrice() element not interactable")
        time.sleep(1.5)
        check_price()
    time.sleep(3)
    attempt = 0
    while attempt < 5:
        try:
            element = driver.find_element(By.XPATH,
                                          "//div[@id='market_commodity_buyrequests']"
                                          "/span[@class='market_commodity_orders_header_promote'][2]")
            print(element.text)
            attempt = 5
        except NoSuchElementException:
            print("checkPrice NoSuchElementException")
            driver.refresh()
            time.sleep(2)
            attempt = attempt + 1
    price = element.text[3:]
    print(price)
    driver.back()
    time.sleep(2)
    return price


def total_sale(currentprice):
    global totalPrice
    totalPrice += float(currentprice)
    return totalPrice


def main_loop():
    apply_filter()
    select_card()
    price = check_price()
    apply_filter()
    select_card()

    print("selling for: :" + str(price))
    element = driver.find_element(By.CLASS_NAME, "item_market_action_button_contents")  # sell button
    element.click()
    time.sleep(2)

    element = driver.find_element(By.ID, "market_sell_buyercurrency_input")  # input price
    element.click()
    time.sleep(2)

    pyautogui.typewrite(str(price))
    time.sleep(1)

    checkbox = driver.find_element(By.ID, "market_sell_dialog_accept_ssa")  # checkbox
    if checkbox.is_selected():
        element = driver.find_element(By.ID, "market_sell_dialog_accept")  # accept
        element.click()
        time.sleep(2)
        element = driver.find_element(By.ID, "market_sell_dialog_ok")  # final OK
        element.click()

    else:
        checkbox.click()
        element = driver.find_element(By.ID, "market_sell_dialog_accept")  # accept
        element.click()
        time.sleep(2)
        element = driver.find_element(By.ID, "market_sell_dialog_ok")  # final OK
        element.click()
    print("Total Sale Price: " + str(total_sale(price)))
    time.sleep(2)


def bot(amount):
    for card in range(int(amount)):
        main_loop()


if __name__ == '__main__':
    user_id = input("User Id: ")
    driver.get(f"https://steamcommunity.com/login/home/?goto=id%2F{user_id}%2Finventory%2F")

    totalPrice = 0
    time.sleep(1)
    login()
    check_page(f"https://steamcommunity.com/id/{user_id}/inventory/",
               f"https://steamcommunity.com/id/{user_id}/inventory/#753")
    time.sleep(2)
    print("l: Login\nb: Bot\n t: Try Once\nq: Quit")
    a = input("Option: ")

    while a != "q":
        if a == "l":
            alt_tab()
            login()
            check_page(f"https://steamcommunity.com/id/{user_id}/inventory/",
                       f"https://steamcommunity.com/id/{user_id}/inventory/#753")
            time.sleep(2)

            a = input("Option: ")
        if a == "t":
            alt_tab()
            main_loop()
            a = input("Option: ")
        if a == "b":
            x = input("How many times?: ")
            alt_tab()
            bot(x)
            a = input("Option: ")
        else:
            print("Not valid input")
            print("l: Login\nb: Bot\nf: Filter\nq: Quit")
            a = input()
    else:
        exit()
