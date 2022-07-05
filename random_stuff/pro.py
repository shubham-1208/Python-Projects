prices = {
    "apple": 0.40,
    "banana": 0.50,
}
my_basket = {
    "apple": 1,
    "banana": 6,
}
total_grocery_bill = 0
for fruit, count in my_basket.items():
    total_grocery_bill += prices[fruit] * count
print(f"I owe the grocer £{total_grocery_bill:.2f}")