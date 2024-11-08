# get input
phone_number = input("Please give me your phone number: ")

# you can add any line of code between this line and the line with return
phone_number = phone_number.replace("(", "")
phone_number = phone_number.replace(")", "")
phone_number = phone_number.replace(" ", "")
phone_number = phone_number.replace("-", "")

# show result
print(len(phone_number) == 10 and phone_number.isnumeric()) # You can modify this line as needed