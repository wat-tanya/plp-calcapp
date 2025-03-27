def calculate_discount(price, discount_percent):
    if (discount_percent >= 20):
        discount = price*discount_percent/100
        final_price = price - discount
        return final_price
    else:
        return price

original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))
    
# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)
    
# Print the result
if discount_percentage >= 20:
    print(f"The final price after applying the discount is: {final_price:.2f}")
else:
    print(f"No discount applied. The original price is: {original_price:.2f}")

