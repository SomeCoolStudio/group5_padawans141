class ParkingGarage():
    
    def __init__(self): # initiate objects of this class

        self.tickets = [1, 2, 3, 4, 5] 
        self.parking_spaces = ['A', 'B', 'C', 'D', 'E']
        self.parking_spaces_taken = []
        self.current_ticket = {}

    def take_ticket(self):
    
        if len(self.tickets) > 0: # making sure we have tickets to give

            ticket = self.tickets.pop() # removing last item from the tickets list and temporarily tracking it by assigning it to local variable ticket

            parking_space = self.parking_spaces.pop() # removing last item from the parking_spaces list and temporarily tracking it by assigning it to local variable parking_space

            self.parking_spaces_taken.append (parking_space) # the value in variable parking_space value into the parking_spaces_taken list

            self.current_ticket[ticket] = parking_space # adding new item to the current_ticket dictionary, creating a new key value pair ex: {ticket : parking_space} --> { 5 : 'E'}

            print(f"Your ticket number is {ticket} and your parking space is {parking_space}") # print users ticket and parking space with f string

        else:

            print("Sorry, the parking garage is full") # print message if we dont have tickets to give
                  
    def pay_for_parking(self):
    
        ticket = int(input("What is your ticket number? ")) # ask user for input which will be the value assigned to local variable ticket

        if ticket in self.current_ticket: # check to see if the value in the ticket variable is a key in the currentTicket dictionary

            del self.current_ticket[ticket] # delete key inside the currentTicket dictionary that corresponds to value in the local ticket variable

            self.tickets.append(ticket) # removed ticket is now added back to the tickets list

            self.parking_spaces.append(self.parking_spaces_taken.pop()) # parking space item in parking_spaces_taken list is removed and put back into parking_spaces list

            print("Thank you for your payment. Have a great day!") # print ticket paid message

        else:

            print("That is not a valid ticket number.") # print not valid ticket message
                  
    def leave_garage(self):
    
        ticket = int(input("What is your ticket number? ")) # ask user for input which will be the value assigned to local variable ticket

        if ticket in self.current_ticket: # check to see if the value in the ticket variable is a key in the currentTicket dictionary

            print("You need to pay before you can leave.") # Pay before you leave message

        else:

            print("Thank you for your payment. Have a great day!") # print ticket paid message

            # self.tickets.append(ticket) # removed ticket is now added back to the tickets list 

            # self.parking_spaces.append(self.parking_spaces_taken.pop()) # parking space item in parking_spaces_taken list is removed and put back into parking_spaces list

    def run_garage(self):
    
        while True: # loops program continously

            response = input("What would you like to do? You can 'park', 'pay', or 'leave' ") # ask user for input

            if response.lower() == "park": # check if response value is a lower case "park"

                self.take_ticket() # invoke take_ticket function

            elif response.lower() == "pay":  # check if response value is a lower case "pay"

                self.pay_for_parking() # invoke pay_for_parking function

            elif response.lower() == "leave": # check if response value is a lower case "leave"

                self.leave_garage() # invoke leave_garage function

park = ParkingGarage() # instantiate the ParkingGarage class

park.run_garage() # invoke run_garage()