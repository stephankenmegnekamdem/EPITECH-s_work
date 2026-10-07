animalsCounts = [['cat', 666], ['dog', 3], ['elephant', 42]]
animalsCounts = sorted(animalsCounts, key=lambda x : x[1])
print(animalsCounts)