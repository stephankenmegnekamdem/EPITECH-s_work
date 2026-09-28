sandwich={
          "bread":"<//////////>",
          "lettuce":"~~~~~~~~~~~~",
          "tomato":"O O O O O O",
          "ham":"============"
}
def sandwich_maker(x, sandwich):
        ingredients=[]
        sandwich_made=[]
        print("What do you want in  your sandwich?")
        print("First write the number of ingredients")
        n = int(input())
        for i in range(n):
            ingredients.append(input())
        if ingredients.count('bread')>=2:
            if any(k=="tomato" for k in ingredients) or any(k=="ham" for k in ingredients):
                for i in range(x):
                    for j in ingredients:
                        if j in sandwich:
                            print(sandwich[j])
        else:
                print("Error: A sandwich needs top and bottom bread!")









number_sandwiches=input("How many sandwiches do you want?")
if "." not in number_sandwiches:
    number_sandwiches=int(number_sandwiches)
    sandwich_maker(number_sandwiches, sandwich)
else:
    print("I can't do this!")
