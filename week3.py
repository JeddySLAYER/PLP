def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - ((price * discount_percent) / 100)
    else:
        return price
    
price = int(input("input the original price : "))
discount_percent = int(input("input the discount percent : "))

print("you'll have to pay", calculate_discount(price, discount_percent))