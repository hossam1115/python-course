info = {
"hossam":"01011112222","ahmed":"01012345678","sara":"01123456789"
}

search = input("search: ")

if search in info.keys():
    print(info[search])
elif search in info.values():
    for key, value in info.items():
        if value == search:
            print(key)
else:
    add_new = input("Do you want to add a new contact? (y/n): ")
    if add_new.lower() == 'y':  
        new_name = input("Enter name: ")
        new_number = input("Enter number: ")
        info[new_name] = new_number
        print("Added successfully!")
        print(info)
    elif add_new.lower() == 'n':  
        print("Goodbye!")
