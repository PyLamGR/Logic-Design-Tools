def bdd_pyramid_print(bdd):
    for i in bdd:
        print(i+': '+str(bdd[i]))




# bdd = {'Initial Function': 'Xy+z', 'x': ['y+z', 'z'], 'y': ['z', '1', 'z', 'z'], 'z': ['0', '1', '1', '1', '0', '1', '0', '1']}
# print(bdd_pyramid_print(bdd))