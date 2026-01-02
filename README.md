## Description
# What this programm does:
### Kurs: openHPI Python Kurs

In this exercise i simulated a sales and operations planning using the zero stock level strategy. The program asks the user to enter the following data:

-An initial stock level for a product

-The number of month(s) to plan

-The planned sales quantity for each month


Based on this data, calculate the required production quantity as follows:


-If the sales quantity is smaller than the stock level of the previous month, the production quantity is 0

-If the sales quantity is larger than the stock level of the previous month, the production quantity is this difference

Below is an example execution of the program:

Please enter an initial stock level: 500

Please enter the number of month to plan: 5

Please enter the planned sales quantity: 300

Please enter the planned sales quantity: 250

Please enter the planned sales quantity: 200

Please enter the planned sales quantity: 400

Please enter the planned sales quantity: 100

The resulting production quantities are:
Production quantity month 1 - 0
Production quantity month 2 - 50
Production quantity month 3 - 200
Production quantity month 4 - 400
Production quantity month 5 - 100
