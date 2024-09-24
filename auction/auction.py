from auction_art import logo

# Print the logo of the auction (assumed to be imported from another file/module)
print(logo)


def find_highest_bidder(bids):
    # Initial approach (manual loop)
    # This section is commented out and shows an alternative way to find the highest bidder manually.
    # The approach is shown below but not used:

    # winner = "" # Initialize an empty string to store the name of the winning bidder.
                  # This will be updated later in the loop once the highest bid is determined.

    # highest_bid = 0  # Variables to track the winner and highest bid.

    # for bidder in bids:  # Loop through each bidder in the bids dictionary.
    #     bid_amount = bids[bidder]  # Get the bid amount for each bidder.
    #     if bid_amount > highest_bid:  # Check if this bid is higher than the current highest bid.
    #         highest_bid = bid_amount  # Update the highest bid.
    #         winner = bidder  # Update the winner to the current bidder.

    # Use the max() function to find the key (bidder's name) with the highest bid
    # `key=bids.get` tells max() to use the bid amount (value) for comparison
    winner = max(bids, key=bids.get)

    # Get the highest bid amount based on the winner's name
    highest_bid = bids[winner]

    # Print the winner's name and their bid amount
    print(f"The winner is {winner} with a bid of ${highest_bid}")


# Initialize an empty dictionary to store bidders' names and their respective bids
bids = {}

# Variable to control the while loop, which will allow continuous bidding
start = True

# Start of the bidding process (loop continues as long as `start` is True)
while start:
    # Prompt the user for their name and bid amount
    name = input("What is your name? ")
    price = int(input("What is your bid?: $"))

    # Store the name as the key and the bid amount as the value in the bids dictionary
    bids[name] = price

    # Ask if there are any other bidders, converting the input to lowercase
    should_continue = input("Are there any other bidders? Type 'yes' or 'no':\n").lower()

    # If the user types 'yes', continue the loop and clear the screen for the next bidder
    if should_continue == 'yes':
        print("\n" * 100)  # This mimics clearing the screen by adding line breaks

    # If the user types 'no', stop the loop and call the function to find the highest bidder
    elif should_continue == 'no':
        start = False
        find_highest_bidder(bids)

    # If the input is neither 'yes' nor 'no', show an error message and prompt again
    else:
        print("Invalid input. Please try again.")
