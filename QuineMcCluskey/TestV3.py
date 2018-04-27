from QuineMcCluskey import QuineMcV3

min_term = []
dc_term = []

while True:
    choice = input("Give me a minterm, type ',' to give me the dc terms or type - to make the magic happen: ")

    if choice is '-':
        break

    elif choice is ',':
        print("Adding the dcterm to the list ...")
        dc = input("Give me the dc: ")
        dc_term.append(dc)

    else:
        print("Adding the minterm to the list ...")
        min_term.append(choice)


print("Creating the qm")
qm = QuineMcV3(min_term, dc_term)
print("Starting the process")
qm.sort_first_list()
qm.get_last_list()
qm.final_step()