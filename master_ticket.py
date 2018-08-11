#! /usr/local/bin/python3

SERVICE_CHARGE = 2
TICKET_PRICE = 10
tickets_remaining = 100  

# Create the calculate price function. It takes number of tickets and returns num_tickets * Ticket_Price

def calculate_price(number_of_tickets):
    # Create new constant for the 2 dollar service charge.
    # Add service charege to whats due.
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >=1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("what is your name? ")
    num_tickets = input("How many tickets would you like, {}?".format(name))
    
    
    try: 
        
        num_tickets = int(num_tickets)
       
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remainnigs".format(tickets_remaining))
    except ValueError as err: 
        print ("Oh no, we ran into an issue. Please try again")
    
    else:
        amount_due = calculate_price(num_tickets)
        print (" The total due is ${}".format(amount_due))
        should_proceed = input("Would you like to proceed?  Y/N  ")
        
        if should_proceed.lower()=="y":
            # Print out to the screen "SOLD!" to confirm the purchase
            # TODO: Gather credit card info and process it.
            print("Sold")
     
        
            tickets_remaining -= num_tickets
        
        
        else:
             print("Thank you anyways, {}!".format(name))
        

print ("Sorry the tickets are all sold out!!! :(")
