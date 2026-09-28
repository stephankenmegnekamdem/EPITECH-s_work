# printing sandwiches if input is valid.
def bread():
    return("<//////////>")
def lettuce():
    return("~~~~~~~~~~~~")
def tomato():
    return("O O O O O O")
def ham():
    return("============")
def sandwich(x):
        for i in range(x):
            print(bread(), lettuce(), tomato(), ham(), ham(), bread())



number_sandwiches=int(input("How many sandwiches do you want?"))
if "." not in number_sandwiches:
    number_sandwiches=int(number_sandwiches)
    sandwich(number_sandwiches)
else:
    print("I can't do this!")
