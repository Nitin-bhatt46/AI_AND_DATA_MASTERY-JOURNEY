from datetime import datetime 
print("Calculate Your Age") 
birth_year = int(input("Enter your Birth Year\n")) 
print(f"Your age is {(datetime.now()).year-birth_year}") 

""" datetime is a module which we will learn in future. from there we fetch today's date and from date we extract year. which makes code more flexible. or you can fix the year with 2025 and also get the answer. """
