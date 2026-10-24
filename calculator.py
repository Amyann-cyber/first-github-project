price_of_product = int(input("enter price of the product "))

quantity_of_product = int(input("quantity required "))

total_cost = (price_of_product) * (quantity_of_product)

print(f"the total cost is {total_cost}")

total_plus_tax = total_cost * 10/100

end_total_plus_tax = total_plus_tax + total_cost

print(f"the final total cost plus tax is {end_total_plus_tax}")
