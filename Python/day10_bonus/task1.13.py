def ship(first_name, description="", apartment="", num = "", street="", city="" ):
    name = first_name
    if description != "" :
             name= name + " " + description
    print(name)
    if city == "":
        print("You need at least a city")
        return 0
    else:

        if apartment != "":
            print("apartment: ", apartment)
        if num != "":
            print("num: ", num)
        if street != "":
            print("street: ",street)
        print("city: ", city)

ship("Batman", street="Mountain Drive", city="Gotham")