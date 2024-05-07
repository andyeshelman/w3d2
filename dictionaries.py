#======= Question 1 =======

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# Add a new category called "Beverages" with at least two items
restaurant_menu["Beverages"] = {"Water": 0.00, "Soda": 1.99, "Beer": 5.99}

# Update the price of "Steak" to 17.99
restaurant_menu["Main Course"]["Steak"] = 17.99

# Remove "Bruschetta" from "Starters"
del restaurant_menu["Starters"]["Bruschetta"]

#print(restaurant_menu)


#======= Question 2 =======

def add_ticket(tickets):
    name = input("Enter customer name: ")
    issue = input("Enter complaint: ")
    tickets[f"Ticket{len(tickets):03}"] = {
        "Customer": name,
        "Issue": issue,
        "Status": "open"
    }

def run_update(code, tickets):
    while True:
        option = input("Update name, issue, or status (or cancel)? ")
        if option == "name":
            print(f"Current name is {tickets[code]["Customer"]}")
            tickets[code]["Customer"] = input("Enter new name: ")
            break
        elif option == "issue":
            print(f"Current issue is {tickets[code]["Issue"]}")
            tickets[code]["Issue"] = input("Enter new issue: ")
            break
        elif option == "status":
            status = "closed" if tickets[code]["Status"] == "open" else "open"
            tickets[code]["Status"] = status
            print(f"{code} is now {status}")
            break
        elif option == "cancel":
            break
        else:
            print("Command unrecognized")


def update_ticket(tickets):
    while True: 
        option = input("Enter ticket number or cancel: ")
        if option.isdigit():
            code = f"Ticket{option.zfill(3)}"
            if code in tickets:
                run_update(code, tickets)
                break
            else:
                print("Ticket not found...")
        elif option == "cancel":
            break
        else:
            print("Command unrecognized...")

def view_tickets(tickets):
    option = input("Would you like to view open, closed, or all tickets? ")
    if option == "open":
        for code, data in tickets.items():
            if data["Status"] == "open":
                print(f"{code} {data["Status"]:-^12}",
                    f"\t  Customer: {data["Customer"]}",
                    f"\t  Issue: {data["Issue"]}", sep = "\n")
    elif option == "closed":
        for code, data in tickets.items():
            if data["Status"] == "closed":
                print(f"{code} {data["Status"]:-^12}",
                    f"\t  Customer: {data["Customer"]}",
                    f"\t  Issue: {data["Issue"]}", sep = "\n")
    else:
        for code, data in tickets.items():
            print(f"{code} {data["Status"]:-^12}",
                  f"\t  Customer: {data["Customer"]}",
                  f"\t  Issue: {data["Issue"]}", sep = "\n")

def ticket_tracker():

    service_tickets = {
    "Ticket000": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket001": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
    }
    while True:
        option = input("Would you like to add, update, view, or quit? ")

        if option == "add":
            add_ticket(service_tickets)
        elif option == "update":
            update_ticket(service_tickets)
        elif option == "view":
            view_tickets(service_tickets)
        elif option == "quit":
            break
        else:
            print("Command unrecognized...")

ticket_tracker()