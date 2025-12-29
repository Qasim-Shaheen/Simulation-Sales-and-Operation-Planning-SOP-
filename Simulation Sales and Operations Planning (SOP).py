new_stock_lvl = []
sq = []
pq = []


Stock_lvl = int(input("Please enter the initial stock level:"))
num_months = int(input("Please enter the number of months to plan:"))
new_stock_lvl.append(Stock_lvl)

for i in range(num_months):
    sales_quantity = int(input("Please enter the expected monthly sales quantity:"))  
    sq.append(sales_quantity)
    
    if new_stock_lvl[i] >= sq[i]:
        pq.append(0)
        x = new_stock_lvl[i] - sq[i]
        new_stock_lvl.append(x)

    else:
        pq.append(sq[i]- new_stock_lvl[i])
        new_stock_lvl.append(0)
print("")

for i in range(num_months):
    x = i +1
    print("production quantity is month:",x ,"-" ,pq[i] )



 