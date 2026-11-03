# Reflections



# Exercise 1 
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

# Exercise 2 

customer['phone'] = '555-5555' # Adding a new key-value pair to the dictionary
print(customer)
customer['tier'] = 'platinum'
print(customer)
del customer['name']
print(customer)
print(customer.get('ytd_spend', 0))

# Exercise 3 

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError as error:
    print("KeyError caught:", error)

# Exercise 4 

for key, value in customer.items():
    print(f"{key}: {value}")

for something in customer:
    print(something, customer[something])

# Exercise 5 

tier_discounts = {
    "bronze": 0, 
    "silver": 0.05,
    "gold": 0.1,
    "platinum": 0.15
}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1-discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: ${final_price:.2f}")

# Exercise 6 

customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate 
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} off a $300 purchase")

# Exercise 7 

catalog = {
    "Widget A": {"price": 9.99, "stock":150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product_name, product_details in catalog.items():
    if product_details["stock"] < 20:
        print(f"LOW STOCK: {product_name} - only {product_details['stock']} left")

# Exercise 8 

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount 

print(sales_by_region)

for region in sorted[sales_by_region]:
    print(f"{region}: ${sales_by_region[region]:.2f}")
