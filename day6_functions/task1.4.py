def bread():
    return("<//////////>")
def lettuce():
    return("~~~~~~~~~~~~")
def tomato():
    return("O O O O O O")
def ham():
    return("============")
def sandwich(x, veg):
        for i in range(x):
            if(veg=="Y"):
                print(bread(), lettuce(), tomato(), bread())
            else:
                print(bread(), lettuce(), tomato(), ham(), ham(), bread())



number_sandwiches=input("How many sandwiches do you want?")
want_vege=input("Do you want a vegeterian sandwich, Y for yes?")
if "." not in number_sandwiches:
    number_sandwiches=int(number_sandwiches)
    sandwich(number_sandwiches, want_vege)
else:
    print("I can't do this!")