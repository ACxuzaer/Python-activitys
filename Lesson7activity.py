actual_cost=float(input("please input the actual cost of the product"))
sale_amount=float(input("please input the sale amount of the product"))

if (sale_amount > actual_cost):
   amount = sale_amount - actual_cost
   print("total profit = {0}".format(amount))
else: 
   print("no profit")