print("WELCOME TO THE BEST SUPER MARKET IN THE WORLD ")
Product = str(input("WHAT DO YOU WANT TO BUY\n "))
print("we only have five " + Product)
numberOfProduct = input("HOW MANY " + Product + " DO YOU WANT TO BUY")

print(numberOfProduct + " " + Product + " is $" + "10")

Product2 = input("WHAT DO YOU WANT TO BUY\n")
numberOfProduct2 = input(" HOW MANY DO YOU WANT TO BUY\n")
print(numberOfProduct2 + " " + Product2 + " is $" + "50")

product3 = input("WHAT DO YOU WANT TO BUY\n")
numberOfProduct3 = input(" how many do you want to buy")
print(numberOfProduct3 + " " + product3 + " is $" + "100")
total = int(numberOfProduct) * 10
total2 = int(numberOfProduct2) * 50
total3 = int(numberOfProduct3) * 100
total_price = total3 + total2 + total
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("PRODUCT  QUANTITY    PRICE   TOTAL ")
print(Product + "         " + numberOfProduct + "       " + "$10" + "      " + total)
print(Product2 + "        " + numberOfProduct2 + "       " + "$50" + "     " + total2)
print(product3 + "        " + numberOfProduct3 + "       " + "$100" + "     " + total3)
print("Total                                                                 " + totalprice)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
