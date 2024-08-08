A small program made as a proof of concept to automate the sale of steam cards using selenium.  
It's just a PoC as it would violate Steams ToS under 8.3 Automated Use.

Logs in with credentials  
Will navigate to inventory page under Steam inventory items.  
Then can either run the the follwing process once with t or have the process run x amount of times.

The process is 
- Apply filters on the invertory page to return only cards
- Select a card
- Navigate to the card's sale page to retrieve current 'want to buy price'
- return to the inventory page, select the card
- Select to sell, input the current want to buy price and confirm.

Afterwards return to the invetory screen
