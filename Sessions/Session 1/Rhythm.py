'''
beast = input("Enter animal: ").lower()

print(name, "Had a Little", beast)

print()
print(name, "had a little ", beast,",")
print("Little ,", beast, "little", beast,",")
print(name, "had a little", beast, ",")
print("its fleece was white as snow,")
print()
print ("And everywhere", name,"went,")
print(name, "went,", beast, "went,")
print("Everywhere that ",name,"went,")
print("The", beast, "was sure to go.")
'''

name = input("enter name: ").capitalize()
beast = input("Enter animal: ").lower()


print(f'''{name} "Had a Little", {beast}

{name} had a little {beast} ,
Little , {beast} little {beast},
{name} had a little {beast},
its fleece was white as snow

And everywhere {name} went)
{name} ent, {name} went,
Everywhere that {name} went,
The, {beast} was sure to go.
''')
