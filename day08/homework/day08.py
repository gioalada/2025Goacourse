
book1_original_price = 35
book2_original_price = 20  
book3_original_price = 22  
book4_original_price = 26  
book5_original_price = 29  


discount_percentage = 30  



book1_new_price = book1_original_price - (book1_original_price * discount_percentage / 100)
book2_new_price = book2_original_price - (book2_original_price * discount_percentage / 100)
book3_new_price = book3_original_price - (book3_original_price * discount_percentage / 100)
book4_new_price = book4_original_price - (book4_original_price * discount_percentage / 100)
book5_new_price = book5_original_price - (book5_original_price * discount_percentage / 100)


print(f"პირველი წიგნის ახალი ფასი: {book1_new_price} ლარი")
print(f"მეორე წიგნის ახალი ფასი: {book2_new_price} ლარი")
print(f"მესამე წიგნის ახალი ფასი: {book3_new_price} ლარი")
print(f"მეოთხე წიგნის ახალი ფასი: {book4_new_price} ლარი")
print(f"მეხუთე წიგნის ახალი ფასი: {book5_new_price} ლარი")
