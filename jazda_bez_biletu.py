import random

'''
Github copilot chat prompt:

create an adventure simulator about traveling by bus without tickets.
First, give player a 10 zloty balance. Then generate random journey with N bus stops.
Player has to accept each sub-journey, by buing ticket or not,
alternatively he can finish journey at any bus stop.
Buing ticket costs 2 zloty. each sub-journey earns 1 zloty if not catched,
or deduce -50 zloty in case of being catched without ticket.
The probability of being catched is randomly generated before each sub-journey
and can be linearly distributed between 0 and 0.03. When the journey ends
(by reaching last bus stop, or by declining to continue earlier)
the new journey generated as described at the begin.
Thecash balance is updated after each sub-journey.


The risk value has to be presented and expressed in percentage (like 1.63%),
moreover, one-letter answers should be also accepted


jeszcze recznie poprawilem blad ze nie dostaje sie bonusa +1 jak sie ma bilet
linia 44: zmienielem z -2 na -1
'''

# Function to generate a journey with random probabilities of being caught
def generate_journey(num_stops):
    return [random.uniform(0, 0.03) for _ in range(num_stops)]

# Main function to simulate the travel adventure
def travel():
    balance = 10  # Initial balance for the player
    while True:
        num_stops = random.randint(5, 15)  # Randomly determine the number of bus stops
        journey = generate_journey(num_stops)  # Generate the journey with catch probabilities
        print(f"New journey with {num_stops} bus stops.")

        for i, catch_probability in enumerate(journey):
            print(f"Bus stop {i + 1}/{num_stops}")
            print(f"Current balance: {balance} zloty")
            print(f"Risk of being caught: {catch_probability * 100:.2f}%")
            # Prompt the player to make a choice
            choice = input("Do you want to buy a ticket (2 zloty) or risk traveling without one? (buy/b/risk/r/stop/s): ").strip().lower()

            if choice in ["buy", "b"]:
                balance -= 1  # Deduct 2 zloty for the ticket and add 1 zloty for not being caught
                print("You bought a ticket. -2 zloty. You weren't caught. +1 zloty")
            elif choice in ["risk", "r"]:
                if random.random() < catch_probability:
                    balance -= 50  # Deduct 50 zloty if caught without a ticket
                    print("You were caught without a ticket! -50 zloty")
                else:
                    balance += 1  # Add 1 zloty if not caught
                    print("You weren't caught. +1 zloty")
            elif choice in ["stop", "s"]:
                print("You decided to stop the journey.")
                break  # End the journey if the player chooses to stop
            else:
                print("Invalid choice. Please choose 'buy/b', 'risk/r', or 'stop/s'.")
                continue  # Prompt again if the choice is invalid

            if balance < 0:
                print("Your balance is negative. Game over.")
                return  # End the game if the balance is negative

        print(f"Journey ended. Current balance: {balance} zloty")
        # Ask the player if they want to start a new journey
        if input("Do you want to start a new journey? (y/n): ").strip().lower() != "y":
            break  # Exit the loop if the player chooses not to start a new journey

if __name__ == "__main__":
    travel()  # Start the travel adventure