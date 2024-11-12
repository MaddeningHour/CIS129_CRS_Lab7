#Christopher Robles Serrano
#Module 7 Lab CIS-129
#11/12/2024
#This programs calculates receives inputs for three sections of a theather. It uses input validation to make sure user inputs are valid. It prints out our calculations.


def main():
    print('Welcome to my theater!')
    
    #Variable to keep looping and our total seats in the theather
    loop = 'yes'
    TOTALSEATS = 200
    #Keep looping while user says yes
    while loop == 'yes':
        #Prices of our seats
        SEAT_A = 20
        SEAT_B = 15
        SEAT_C = 10

        #Assigning 3 variables to the getSeat method
        seatsA,seatsB,seatsC = getSeats()

        #Looping until our users total seats doesn't exceed the number of seats in the theather.
        while ((seatsA + seatsB + seatsC) > TOTALSEATS):
            print(f"You have sold too many seats! Total tickets sold must not exceed {TOTALSEATS}!")
            seatsA,seatsB,seatsC = getSeats()
        
        #Looping until all values are greater or equal to zero.
        while (seatsA < 0) or (seatsB < 0) or (seatsC < 0):
            print("All values must be greater or equal to zero.")
            seatsA,seatsB,seatsC = getSeats()

        try:
            #Printing our calculations.
            print(f'Section A: ${SEAT_A * seatsA}')
            print(f'Section B: ${SEAT_B * seatsB}')
            print(f'Section C: ${SEAT_C * seatsC}')
            print(f'Total: ${SEAT_A * seatsA + SEAT_B * seatsB + SEAT_C * seatsC}')

        except TypeError:
            #Calling the main function again as a safety net if our arithmetic cannot be done.
            print("Invalid numbers entered.")
            main()
        
        #Checking if the user wants to input new values and converting to lowercase to remove case sensitivty.
        loop = input("Would you like to enter new values?(yes or no): ").lower()

        #Loops until the user input is either 'yes' or 'no'.
        while loop not in ['yes', 'no']:
            print("Invalid response! Answers must be in (yes or no) format.")
            loop = input("Would you like to enter new values?(yes or no): ").lower()


def getSeats():
    #Looping inside of itself until all values are of the integer type.
    while True:
        try:
            #Converting 3 user inputs into our variables.
            seatsA = int(input("How many customers in section A($20): "))
            seatsB = int(input("How many customers in section B($15): "))
            seatsC = int(input("How many customers in section C($10): "))
            
            #Return our variables.
            return seatsA, seatsB, seatsC
        
        #Exception to catch incorrect types of data. 
        except ValueError:
            print("Invalid type entered. Type must be an integer.")
            
#Calling main
main()