def calculate_discount(price, discount):
    return price-(price*discount/100)
price=float(input('enter price:'))
discount=20
if discount >= 20:
 print("Apply discount.final price")
else:
 print(price, "no discount.price")