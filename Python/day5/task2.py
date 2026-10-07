# task2.1 introduction to dictionaries, initiating one
pokemons={
    'names'   : ['Pikachu' , 'Bulbasaur',  'Charmander', 'Leafeaon', 'Scovillain' ],
    'types'   : ['Electric', 'Grass', 'Fire', 'Grass', 'Fire'],
    #task2.2: adding key  Blaziken with value fire
    'Blaziken': ['Fire']
}

print(pokemons)

#   task2.3 adding values to a dictionary

pokemons['Pikachu']=["Pichu", "Raichu"]
print(pokemons)

#when i add that a new vlue with key Pickachu and list Pichu, raich is created just by declaring it  so we have a key and the values of the key
#each of the values of various keys(list of the keys) dont have to be same size

#   task2.4: Creating dictionary types
types={}
j=0
for i in pokemons['types']:
        types[i]=[]
        j=j+1
print(types)

#   task2.5:  adding values to a dictionary types using those from another dictionary
for i in types: #for each of the types

    for j in range(len(pokemons['types'])): #to seach each index in pokemons names
        if pokemons['types'][j]==i:
           types[i].append(pokemons['names'][j])

print(types)

#   task2.6: print all keys(pokemon types)
for i in types:
    print (i)

#   task2.7: retrieve type of a pokemon
for i in types:
    if 'Pikachu' in types[i]:
        print(i)

#   task2.8: superheroes dictionary to print each value of dictionary, going lower, use [][][]
superheroes={
"Batman" : {
"id": 1,
"aliases": ["Bruce Wayne", "Dark knight"],
"location": {
"number" : 1007,
"street": "Mountain Drive",
"city": "Gotham"
}
},
"Superman" : {
"id": 2,
"aliases": ["Kal-El", "Clark Kent", "The Man of Steel"],
"location": {
"number" : 344,
"street": "Clinton Street",
"apartment": "3D",
"city": "Metropolis"
}
},
}

print (superheroes["Superman"]["location"]["city"])

#task 2.9 adding values
superheroes["Superman"]["aliases"].append('Caped Crusader')


superheroes["Wolverine"]={
    "id" : 3,
    "aliases" : [],
    "location" : {
    "number" : "",
    "street": "",
    "apartment": "",
    "city":""
    }
}
print(superheroes)

#task2.10 enumerating the aliases of each superhero
for i in superheroes:
    print(i + ":")
    if len(superheroes[i]["aliases"]) == 0:
        print("aliases not found")
    for j in superheroes[i]["aliases"]:
        print(j)



    print()

#task2.11 finding the maximum value in a dictionary
test_dict={
"dalmatians": 101,
"pi": 3.14,
"beast": 666,
"life": 42,
"googol": 10^100,
"jordan": 23,
"life, the universe and everything": 42,
"emergency": 911,
"euler": 2.71828
}

max=0
for i in test_dict:
    if test_dict[i]>max:
        max=test_dict[i]
print(max)

