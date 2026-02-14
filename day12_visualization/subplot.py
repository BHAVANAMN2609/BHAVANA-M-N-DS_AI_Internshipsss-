import matplotlib.pyplot as plt

# -------- Data for Bar Chart --------
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

# -------- Data for Line Plot --------
months = [1, 2, 3, 4, 5]
monthly_revenue = [1000, 1500, 1300, 1800, 2200]

# Create overall figure
plt.figure(figsize=(10, 4))

# -------- Subplot 1: Bar Chart --------
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Product Categories")
plt.ylabel("Sales Amount")

# -------- Subplot 2: Line Plot --------
plt.subplot(1, 2, 2)
plt.plot(months, monthly_revenue)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

# Adjust layout to prevent overlap
plt.tight_layout()

# Show dashboard
plt.show()
