full_name = input("Full name (last, first): ").replace(" ", "")

comma_index = full_name.find(",")
last_name = full_name[0:comma_index]

print(last_name)
