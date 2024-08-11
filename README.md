# Steam Trading Card Sales Automation

This is a small proof-of-concept (PoC) program to automate the sale of Steam trading cards using Selenium. The program logs in to a Steam account, navigates to the inventory page, applies filters to show only trading cards, retrieves the current "want to buy" price, and then lists the card for sale at that price. 

**Note:** This program is purely a proof of concept and would violate Steam's Terms of Service under section 8.3 (Automated Use). Use this code responsibly and at your own risk.

## Features

- **Automated Login:** Logs into a Steam account with provided credentials.
- **Card Filtering:** Applies filters to show only Steam trading cards in the inventory.
- **Price Checking:** Retrieves the current "want to buy" price for each selected card.
- **Automated Selling:** Lists cards for sale at the retrieved price.
- **Looping Functionality:** The bot can either run once or repeat the process a specified number of times.

## Requirements

- Python 3.x
- [Selenium](https://pypi.org/project/selenium/)
- [pyautogui](https://pypi.org/project/PyAutoGUI/)
- [pwinput](https://pypi.org/project/pwinput/)

You can install the required packages using pip:

```bash
pip install selenium pyautogui pwinput
```
# Code Overview

### Follow the prompts:

- Enter your Steam user ID and credentials.
- Choose to run the bot once (t) or multiple times (b).
- Specify the number of repetitions if running the bot in loop mode.
- The program will log in, filter your inventory, select a card, check the price, and list it for sale.
- The main functions of the program include:

### Functions:
login(): Handles the login process using credentials.  
check_page(): Verifies successful login and navigates to the desired page.  
alt_tab(): Does whaht it says on the tin.  
select_card(): Selects a card from the filtered inventory.  
apply_filter(): Filters the inventory to show only regular Steam trading cards.  
check_price(): Retrieves the current "want to buy" price for the selected card.  
total_sale(): Tracks the total sale price of all cards sold in the session.  
main_loop(): The main process loop for selecting, pricing, and selling cards.  
bot(amount): Runs the main process loop a specified number of times.  

Disclaimers
Steam ToS Violation: This tool violates Steam's Terms of Service. Using it can result in penalties, including account suspension or banning. Proceed with caution.
For Educational Purposes Only: This tool is intended for educational purposes to demonstrate the automation of web interactions.
