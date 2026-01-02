## Description
# What this programm does:

-Calculates production for each month.
-Checks if current stock is enough.

The program prompts the user for: 
1. An initial stock level.
2. The number of months to plan.
3. Expected sales figures for each individual month.
4. The script automatically calculates whether production is required for each individual month.


6. The required production quantity is calculated as follow:
7. If the sales quantity is smaller than the stock level of the previous month, the production quantity is 0.
8. If the sales quantity is larger or similar to the stock level of the previous month, the production quantity is this difference.

9.## Below is an example execution of the program:

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
