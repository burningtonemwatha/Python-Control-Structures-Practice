product = input("Enter the product name: ").lower()
price = float(input("Enter the product price: "))

if price > 10000:
    discount = 0.20

elif 5000 <= price <= 10000:
    discount = 0.10

else:
    discount = 0

discount_price = price - (price * discount)

print(f"The {product} now costs {discount_price} after discount.")