full_name = input("Full name (last, first): ").replace(" ", "")

comma_index = full_name.find(",")
first_name = full_name[comma_index + 1:]

print(first_name)
