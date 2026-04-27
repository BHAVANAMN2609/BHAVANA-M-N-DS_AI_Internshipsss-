import pandas as pd
products = pd.Series(
    data=[700, 150, 300],
    index=['Laptop', 'Mouse', 'Keyboard']
)
print("Full Product Series:")
print(products)
laptop_price = products['Laptop']
print("\nPrice of Laptop:")
print(laptop_price)
first_two = products.iloc[0:2]
print("\nFirst Two Products:")
print(first_two)