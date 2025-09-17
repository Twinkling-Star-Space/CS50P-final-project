import tabulate
from fpdf import FPDF
import os

# creating a class
class flightD:
    def __init__(self, flight_data):         # this function will make variable available every where                                                                             # every within the class using self
        self.value_to_match4 = ""
        self.ticket = ""
        self.filtered_flight = []
        self.Flight = flight_data
        self.ARRAY = flight_data
        self.update = {'BOOKED': 0, 'PAYED': 0, 'TICKET': 0, 'CANCELED': 0, 'ACCOUNT_BALANCE': 50000}
        self.headers = ["STATUS", "VALUE"]
        self.topay =""

    def __str__(self):
        rows = []
        for key, value in self.update.items():
            rows.append([key, value])

        print(tabulate.tabulate(rows, headers=self.headers, tablefmt="double_grid"))

        header = self.Flight[0].keys()
        rows = [x.values() for x in self.Flight]
        return tabulate.tabulate( rows, header, tablefmt="double_grid")

#creating an object which include programs to loop around flight data and find those all flights related to source i.e. starting point
    def Source_search(self, SOURCE):

        rows = []
        for key, value in self.update.items():
            rows.append([key, value])

        print(tabulate.tabulate(rows, headers=self.headers, tablefmt="double_grid"))

        required_src = SOURCE
        key_to_match1 = "source"
        value_to_match1 = required_src.lower()

        matched_flights = []
        for flight in self.ARRAY:
            flight_value = flight.get(key_to_match1, "").lower()
            if flight_value == value_to_match1:
                matched_flights.append(flight)
        self.matched_flights_src = matched_flights
        self.ARRAY = self.matched_flights_src

        return self.matched_flights_src

#creating an object which include programs to loop around flight data and find those all flights related to destination i.e. reaching point
    def Destination_search(self, DESTINATION):

        rows = []
        for key, value in self.update.items():
            rows.append([key, value])

        print(tabulate.tabulate(rows, headers=self.headers, tablefmt="double_grid"))

        required_des = DESTINATION
        key_to_match2 = "destination"
        value_to_match2 = required_des.lower()

        matched_flights = []
        for flight in self.ARRAY:
            flight_value = flight.get(key_to_match2, "").lower()
            if flight_value == value_to_match2:
                matched_flights.append(flight)
        self.filtered_flights_des = matched_flights
        self.ARRAY = self.filtered_flights_des
        return self.filtered_flights_des

#creating an object which include programs to loop around flight data and find those all flights related to similar price
    def Price_search(self, BUDGET):

        rows = []
        for key, value in self.update.items():
            rows.append([key, value])

        print(tabulate.tabulate(rows, headers=self.headers, tablefmt="double_grid"))

        required_price = BUDGET
        key_to_match3 = "price"
        value_to_match3 = required_price

        matched_flights = []
        for flight in self.ARRAY:
            flight_value = flight.get(key_to_match3, "")
            if flight_value == value_to_match3:
                matched_flights.append(flight)
        self.filtered_flights_price = matched_flights

        self.ARRAY = self.filtered_flights_price
        return self.filtered_flights_price


#creating an object which include programs to loop around flight data and find those all flights related to similar 'date' of flight
    def Date_search(self, DATE):

        rows = []
        for key, value in self.update.items():
            rows.append([key, value])

        print(tabulate.tabulate(rows, headers=self.headers, tablefmt="double_grid"))

        required_date = DATE
        key_to_match4 = "date"
        year, month, day = map(int, required_date.split("-"))
        if 1 <= day <= 30 and 1 <= month <= 12:
            self.value_to_match4 = required_date
        else:
            print("This date flight is absent. Search another flight!")

        matched_flights = []
        for flight in self.ARRAY:
            flight_value = flight.get(key_to_match4, "")
            if flight_value == self.value_to_match4:
                matched_flights.append(flight)

        self.filtered_flights_date = matched_flights
        self.ARRAY = self.filtered_flights_date
        return self.filtered_flights_date

#creating an object which include programs to select flight on the basis of flight
# id and stage flight details for furthure process like ticketing and paying

    def Book_flight(self, ID, name, noofpass):

        required_Flight_id = ID
        key_to_match5 = "flight_id"
        value_to_match5 = int(required_Flight_id)

        matched_flights = []
        for flight in self.ARRAY:
            flight_value = flight.get(key_to_match5, "")
            if flight_value == value_to_match5:
                matched_flights.append(flight)

        self.filtered_flight = matched_flights

        for flight in self.filtered_flight:    # appending names , number of passengers, and total price
            flight['name']= name
            flight['number_of_passenger']= noofpass
            flight['Total_price']= noofpass * flight['price']

        if self.filtered_flight:

            self.update['BOOKED'] = 1
            self.update['TICKET'] = 0
            self.update['CANCELED'] = 0
            self.update['PAYED'] = 0

            rows = []

            for key in self.update:
                value = self.update[key]
                rows.append([key, value])

            if hasattr(self, 'headers') and isinstance(self.headers, list):
                print(tabulate.tabulate(rows, headers=self.headers, tablefmt="double_grid"))
            else:
                print("Missing or invalid headers format")

            print("\n Here is your preliminary Ticket!!!!")
            header = self.filtered_flight[0].keys()
            rows = []
            for flight in self.filtered_flight:
                rows.append(flight.values())

            self.ARRAY = self.filtered_flight

            self.ticket = tabulate.tabulate(rows, header, tablefmt="grid")

            method = ["CANCEL", "PAY"]
            print("\n")

            print(tabulate.tabulate( [], headers=method, tablefmt="grid"))

            return self.ticket

# This program stores the detail of  flights that is staged for flight to book
    def Pre_ticket(self):

            print("your preliminary ticket!!!")
            method = ["CANCEL", "PAY"]

            print(tabulate.tabulate( [], headers=method, tablefmt="grid"))
            print(self.ticket)

# This object cancel the booked flight. It just deletes emptied the the variable that stored something
    def Cancel_flight(self, CANCEL):
        rows = []
        for key, value in self.update.items():
            rows.append([key, value])

        print(tabulate.tabulate(rows, headers=self.headers, tablefmt="double_grid"))

        cancel_flight = CANCEL
        if cancel_flight == "yes":
            if self.ticket != "":
                                             #updating the status and values
                self.update['CANCELED'] += 1
                self.update['BOOKED'] = 0
                self.update['PAYED'] = 0
                self.update['TICKET'] = 0
                self.update['ACCOUNT_BALANCE'] += self.topay

                print("\nOpening a form for quick reason!! ")

                input("Flight_ID :").strip().lower()
                input("Your Name :").strip().upper()
                input("\nWhy do you want to cancel flight(in two sentences)? ")

                self.ticket = ""
                print("Update>>>Your flight has been successfully cancel. WE ARE ALWAYS FOR YOU!")

                rows = []
                for key, value in self.update.items():
                    rows.append([key, value])

                print(tabulate.tabulate(rows, headers=self.headers, tablefmt="double_grid"))
            else:
                print("You have not booked your ticket yet!")

#this  is also an object that accept the request of payment , if any flight is booked or staged for ticket
    def Pay_flight(self):
        rows = []
        for key, value in self.update.items():
            rows.append([key, value])
        print(tabulate.tabulate(rows, headers=self.headers, tablefmt="double_grid"))

        if not hasattr(self, 'filtered_flight') or not self.filtered_flight:
            print("No flight selected for payment.")
            return

        for flight in self.filtered_flight:
            self.topay = int(flight.get('Total_price', 0))
            print(f"\nYOU HAVE TO PAY TOTAL : Rs.{self.topay} ")

            required_payment = int(input("PAY:"))
            if required_payment == int(self.topay):
                print("YOU HAVE SUCCESSFULLY PAID FOR YOUR FLIGHT.")
                print("HAVE A SAFE JOURNEY !!!!!!!!!!!!!\n")

                                                   #updating the status and values
                self.update['PAYED'] = self.topay
                self.update['TICKET'] = 1
                self.update['BOOKED'] = 0
                self.update['CANCELED'] = 0
                self.update['ACCOUNT_BALANCE'] -= self.topay

                rows = []
                for key, value in self.update.items():
                    rows.append([key, value])

                print(tabulate.tabulate(rows, headers=self.headers, tablefmt="double_grid"))

                printyourticket = input("\nDo you want to print your ticket(yes/no): ").lower()

                # print your ticket into pdf form
                if printyourticket == "yes":
                    pdf = FPDF(orientation='L')

                    pdf.add_page()

                    pdf.set_line_width(0.8)
                    pdf.rect(10, 10, pdf.w - 20, pdf.h - 20)

                    pdf.image("image1.png", x=250, y=15, w=25, h=15)
                    pdf.image("image.png", x=60, y=75, w=200, h=120)

                    pdf.set_font("Courier", style="B", size=32)
                    pdf.cell(0, 10, "AVISEAT", ln=True, align="C")

                    pdf.set_font("Courier", style="B", size=20)
                    pdf.cell(0, 10, "FLIGHT TICKET", ln=True, align="C")

                    pdf.set_font("Courier", style="B", size=16)
                    pdf.cell(0, 10, "Please, Bring Your Ticket on The Day you come to take your Flight", ln=True, align="C")

                    pdf.set_font("Courier", style="B", size=9)
                    for line in self.ticket.split('\n'):
                        pdf.cell(0, 6, txt=line, ln=1)

                    pdf.set_y(pdf.h - 60)
                    pdf.set_x(pdf.w - 280)
                    pdf.cell(0, 10, "-------------------------", ln=True, align="L")
                    pdf.set_font("Helvetica", style="B", size=14)
                    pdf.set_x(pdf.w - 280)
                    pdf.cell(0, 10, "Manager's Signature", ln=True, align="L")

                    base_name = "ticket"
                    extension = ".pdf"
                    i = 0
                    while True:
                        filename = f"{base_name}{f'_{i}' if i > 0 else ''}{extension}"
                        if not os.path.exists(filename):
                            break
                        i += 1

                    pdf.output(filename)
                    print("Your ticket successfully printed into pdf form. Please bring it one flight day!")

            else:
                print("Payment Unsuccessful :(, pay to book your flight")


#main function
def main():
    whole_flight()

#this is a user defined function that stores the details of flights
def whole_flight():
    print("\nHere are all flights available of you!!!\n")
    Flight = [
            { 'flight':'F12W', 'flight_id':1, 'source':'kathamndu', 'destination':'Janakpur', 'price':4000, 'date':'2025-08-20','successful':100},
            {'flight':'D4E2', 'flight_id':2, 'source':'Kathmandu', 'destination':'Butwal' ,'price':5000, 'date':'2025-07-12','successful':120},
            {'flight':'D2E2', 'flight_id':3, 'source':'Janakpur', 'destination':'Birgunj','price':4000, 'date':'2025-09-22','successful':130},
            {'flight':'D5E2', 'flight_id':4, 'source':'Kathmandu', 'destination':'Pokhara','price':7000, 'date':'2025-09-12','successful':101},
            {'flight':'D6E2', 'flight_id':5, 'source':'Jhapa', 'destination':'Biratnagar','price':9000, 'date':'2025-07-10','successful':104},
            {'flight':'D49E2', 'flight_id':6, 'source':'Solukhumbu', 'destination':'Nepalgunj','price':2000, 'date':'2025-04-19','successful':150},
            {'flight':'D4E32', 'flight_id':7, 'source':'Kanchanpur', 'destination':'Mustang','price':3000, 'date':'2025-09-16','successful':170},
            {'flight':'D4E20', 'flight_id':8, 'source':'Kathmandu', 'destination':'Dhading','price':6000, 'date':'2025-11-12','successful':180},
            {'flight':'F12W4', 'flight_id':9, 'source':'Janakpur', 'destination':'Dhalke', 'price':4000, 'date':'2025-12-17','successful':130},
            {'flight':'D4E23', 'flight_id':10, 'source':'Dharan', 'destination':'Dhalke' ,'price':5000, 'date':'2025-10-12','successful':120},
            {'flight':'DD2E2', 'flight_id':11, 'source':'Jhapan', 'destination':'Kanchanpur','price':4000, 'date':'2025-05-23','successful':106},
            {'flight':'D5JE2', 'flight_id':12, 'source':'Karnali', 'destination':'Pokhara','price':7000, 'date':'2025-07-12','successful':113},
            {'flight':'D6TE2', 'flight_id':13, 'source':'Jhapa', 'destination':'Biratnagar','price':9000, 'date':'2025-07-17','successful':178},
            {'flight':'D49FE2', 'flight_id':14, 'source':'Kathmandu', 'destination':'Butwal','price':2000, 'date':'2025-05-29','successful':100},
            {'flight':'D49FE2', 'flight_id':15, 'source':'Kathmandu', 'destination':'Birgunj','price':7000, 'date':'2025-05-12','successful':100},
            {'flight':'D49FE2', 'flight_id':16, 'source':'Kathmandu', 'destination':'Pokhara','price':3000, 'date':'2025-05-18','successful':100},
            {'flight':'D4EJ32', 'flight_id':17, 'source':'Kanchanpur', 'destination':'Mustang','price':3000, 'date':'2025-03-12','successful':99},
            {'flight':'D4E2E0', 'flight_id':18, 'source':'Manang', 'destination':'Butwal','price':7000, 'date':'2025-12-12','successful':78},
            { 'flight':'F1G2W', 'flight_id':19, 'source':'Bagmati', 'destination':'Janakpur', 'price':4000, 'date':'2025-12-14','successful':88},
            {'flight':'D4EF2', 'flight_id':20, 'source':'Kathmandu', 'destination':'Pokhara' ,'price':6000, 'date':'2025-07-12','successful':67},
            {'flight':'D2EH2', 'flight_id':21, 'source':'Janakpur', 'destination':'Kanchanpur','price':4000, 'date':'2025-07-10','successful':890},
            {'flight':'D5EY2', 'flight_id':22, 'source':'Jhapa', 'destination':'Pokhara','price':7000, 'date':'2025-06-12','successful':1000},
            {'flight':'D6EU2', 'flight_id':23, 'source':'Mananga', 'destination':'Biratnagar','price':6000, 'date':'2025-04-15','successful':10},
            {'flight':'D49UE2', 'flight_id':24, 'source':'Solukhumbu', 'destination':'Nepalgunj','price':2000, 'date':'2025-09-17','successful':19},
            {'flight':'D4E3I2', 'flight_id':25, 'source':'Mahindernagar', 'destination':'Mustang','price':3000, 'date':'2025-08-15','successful':190},
            {'flight':'D4E20P', 'flight_id':26, 'source':'Kathmandu', 'destination':'Illam','price':9000, 'date':'2025-06-18','successful':1006}
          ]


    tabledata = flightD(Flight)     # calling  class of the flight
    print(tabledata)
    print("HERE IS THE WAY YOU CAN REACH YOUR FLIGHT")
    method = ["SOURCE",">>", "DESTINATION",">>", "PRICE",">>", "DATE", ">>", "BOOK YOUR FLIGHT", ">>", "CANCEL THE TICKET", ">>", "PAYMENT:NOT-REFUNDABLE"]
    print(tabulate.tabulate( [], headers=method, tablefmt="grid"))
    search_flight(tabledata)


#This is also a user defined function that includes program that loops into the list of dictionaries
#This makes user flexible to search query according their requirement like price, source, destination, date, book flight, pay for ticket, cancel flight, and so on

def search_flight(tabledata):
    dic_flight_search = [
        {'search': 'source', 'function1': source_search},
        {'search': 'destination', 'function1': destination_search},
        {'search': 'price', 'function1': price_search},
        {'search': 'date', 'function1': date_search},
        {'search': 'book', 'function1': book_flight},
        {'search': 'pay', 'function1': pay_flight},
        {'search': 'ticket', 'function1': pre_ticket},
        {'search': 'cancel', 'function1': cancel_flight}
    ]

    count =  ""
    checker = "no"
    while count != checker:

        domains = ['source', 'destination', 'price', 'date', 'book', 'pay', 'ticket', 'cancel']
        take_input = ""

        while take_input not in domains:
            take_input = input("\nWhat do you want to do (source/destination/price/date/book/pay/ticket/cancel)? ").lower()

        loop_search(tabledata, dic_flight_search, take_input)
        count = input("Do you want to continue? (yes/no): ").strip().lower()

#this function loops around the list of dictionaries of domains and search the needed flights
def loop_search(tabledata, dic_flight_search, take_input):
    for flight in dic_flight_search:
        if flight['search'] == take_input:
            result = flight['function1'](tabledata)
            if result:
                print(result)


#it takes input of source and calls source object
def source_search(tabledata):

    flight = input("\nFrom where you want to take flight (Source):").lower().strip()

    matched_flights_src = tabledata.Source_search(flight)
    if matched_flights_src:
        header = matched_flights_src[0].keys()
        rows = []
        for flight in matched_flights_src:
            rows.append(flight.values())

        return tabulate.tabulate( rows, header, tablefmt="grid")

#it takes input of destination and call destination object
def destination_search(tabledata):
    flights = input("\nWhere you want to go? (Destination):").lower().strip()
    filtered_flights_des = tabledata.Destination_search(flights)
    if filtered_flights_des:

        header = filtered_flights_des[0].keys()
        rows = []
        for flight in filtered_flights_des:
            rows.append(flight.values())
        return tabulate.tabulate(rows, header, tablefmt="grid")


# It takes input of price and call price object
def price_search(tabledata):
    while True:
        try:
            flights = int(input("\nHow much budget do you have? (Budget):"))
            filtered_flights_price = tabledata.Price_search(flights)
            if filtered_flights_price:

                header = filtered_flights_price[0].keys()

                rows = []
                for flight in filtered_flights_price:
                    rows.append(flight.values())
                return tabulate.tabulate(rows, header, tablefmt="grid")

        except:
            price_search(tabledata)

#it takes input of date and call date object.
def date_search(tabledata):
    flights = input("\nWhen do you want to go? (DATE):").strip()
    filtered_flights_date = tabledata.Date_search(flights)
    if filtered_flights_date:
        first_item = filtered_flights_date[0]
        headers = list(first_item.keys())

        data_rows = []
        for flight in filtered_flights_date:
            row = list(flight.values())
            data_rows.append(row)

        return tabulate.tabulate(data_rows, headers, tablefmt="grid")

#it takes input book and book a ticket of a flight
def book_flight(tabledata):
    try:
        id = int(input("\nWhich flight do you want to book? (Flight_ID):"))
    except:
        book_flight(tabledata)

    name = input("Your Name: ")
    noofpass = int(input("Number of passengers: "))
    X = tabledata.Book_flight(id, name, noofpass)
    return X

#it takes input of price and pays the price of the booked flight
def pay_flight(tabledata):
    tabledata.Pay_flight()


#it allows user to see the booked ticket in terminal
def pre_ticket(tabledata):
    tabledata.Pre_ticket()

#it allows to cancel the ticket of the flight
def cancel_flight(tabledata):
    cancel_flight = input("\nDo you wanna cancel flight(yes/no)?").strip()
    tabledata.Cancel_flight(cancel_flight)


if __name__ =="__main__":
    main()
