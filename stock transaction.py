number_of_shares = 2000
commission_paid = 0.03

#purchase code
stock_amount = number_of_shares * 40
commission_amount = stock_amount * commission_paid

#Selling code
stock_amount_after_sale = number_of_shares * 42.75
commission_amount_after_sale = stock_amount_after_sale * 0.03

final_amount = stock_amount_after_sale -  commission_amount_after_sale -  stock_amount- commission_amount

print(f"The amount joe paid for the stock is ${stock_amount:.2f}")
print(f"The commission paid after buying the stock is ${commission_amount}")
print(f"the amount joe paid after selling the shares is ${stock_amount_after_sale}")
print(f"the commission joe paid after selling the share is ${commission_amount_after_sale}")
print(f"the final amount after all transactions is ${final_amount}")

#profit and loss
if final_amount > 0 :
    print("Joe made profit.")
elif final_amount < 0 :
    print("Joe lost money.")
else:
    print("Joe broke even.")


