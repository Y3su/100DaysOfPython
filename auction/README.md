# Blind Auction Program

Welcome to the **Blind Auction Program**. This is a simple Python-based application where multiple bidders can submit their bids anonymously, and the program will determine the highest bidder at the end.

## Objective

The objective is to allow users to submit their names and bids, then determine the highest bidder in the auction. The program will prompt for the next bidder until there are no more, at which point it will display the winner and the highest bid.

## Features

- Collects names and bids of different participants.
- Ensures anonymity during bidding.
- Automatically calculates and displays the winner with the highest bid.
- Mimics a screen clear (in environments where console screen clearing isn't supported).

## Requirements

You need the following to run the program:

- Python 3.x
- `auction_art.py` (for the logo and ASCII art)
  - You can find the logo and ASCII art in the `auction_art.py` file.

## How it Works

1. The program begins by printing the logo (imported from `auction_art`).
2. Users are prompted to enter their name and their bid.
3. After each bid, the user is asked if there are more bidders:
   - If `yes`, the screen is cleared for the next user.
   - If `no`, the bidding ends, and the program displays the winner and the highest bid.
4. The program will continuously prompt for new bids until no more bidders remain.

### Sample Output

```bash
Welcome to the secret auction program.
What is your name?: Angela
What's your bid?: $123
Are there any other bidders? Type 'yes' or 'no': yes

What is your name?: Elon
What's your bid?: $550000000000
Are there any other bidders? Type 'yes' or 'no': no

The winner is Elon with a bid of $550000000000
```

## Code Walkthrough

### `find_highest_bidder(bids)`
This function takes a dictionary of bids (where the key is the bidder's name, and the value is their bid) and determines the highest bid. It uses Python’s built-in `max()` function to determine the key (bidder) with the highest associated value (bid).

```python
def find_highest_bidder(bids):
    winner = max(bids, key=bids.get)
    highest_bid = bids[winner]
    print(f"The winner is {winner} with a bid of ${highest_bid}")
```

### Auction Process
The auction process consists of a loop that:
1. Asks for the bidder’s name and bid.
2. Stores these details in the `bids` dictionary.
3. Asks if there are more bidders.
4. Clears the screen between bids for anonymity (using `print("\n" * 100)` to mimic screen clearing).
5. Calls the `find_highest_bidder()` function once no more bidders are left.

### Example Code

```python
# Initialize an empty dictionary to store bidders' names and their respective bids
bids = {}

# Variable to control the while loop, which will allow continuous bidding
start = True

while start:
    name = input("What is your name? ")
    price = int(input("What is your bid?: $"))
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no':\n").lower()

    if should_continue == 'yes':
        print("\n" * 100)  # This mimics clearing the screen by adding line breaks
    elif should_continue == 'no':
        start = False
        find_highest_bidder(bids)
    else:
        print("Invalid input. Please try again.")
```

## Running the Program

1. Clone the repository:
   ```bash
   git clone https://github.com/Y3su/100DaysOfPython.git
   ```

2. Navigate to the project directory:
   ```bash
   cd 100DaysOfPython/basic/auction
   ```

3. Run the Python file:
   ```bash
   python auction.py
   ```

## Issues with Clearing the Screen

If you're using an IDE like VSCode or PyCharm, the console may not clear correctly using `print("\n" * 100)`. This method works best on environments like Replit, but for other IDEs, you might need to implement a custom `clear()` function or configure the IDE.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
