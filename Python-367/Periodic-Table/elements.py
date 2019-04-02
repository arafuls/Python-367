def build_periodic_table(filename="periodic_table.txt"):
    input_file = open(filename, 'r')
    table = dict()
    for element in input_file:
        tokens = element.split()
        table[tokens[2]] = (tokens[1], int(tokens[0]), float(tokens[3]))
    return table

def menu_options():
	print('1) Search by symbol/name')
	print('2) Search by atomic mass')
	print('3) Molecular Mass Calculation')
	print('4) Quit\n')

	while True:
	    opt = int(input("Please enter your choice: "))
	    try:
	        if opt < 1 or opt > 4:
	            print("Invalid selection, try again.\n")
	            continue
	        break
	    except ValueError:
	        break
	return opt;

def string_search(table, search):
	# string_search will return an array of tuples
	# Case insensitive using .upper() or .lower()
	search = search.lower()

	results = []
	for element in table:
		# element = Symbol
		# tuplet  = Element Name, Number, Mass
		# find() returns -1 if not a match
		if element.lower().find(search) > -1:
			# searches symbol for a match
			results.append(table[element] + (element,))
		elif table[element][0].lower().find(search) > -1:
			# searches element name for a match
			results.append(table[element] + (element,))
	return results

def mass_search(table, minMass, maxMass):
	# mass_search will return an array of tuples
	results = []
	for element in table:
		mass = table[element][2]
		if mass >= minMass and mass <= maxMass:
			results.append(table[element] + (element,))
	return results

def calc_mass(table, formula):
	# return new mass of combined molecules
	mass = 0
	for element in formula:
		if element[0] not in table:
			print('\nERROR: ', element[0],' entered does not exist in table.')
			return None
		# 1 * 137.327 (mass of Ba) + 2 * 35.4527 (mass of Cl) = 208.232
		mass += table[element[0]][2] * element[1]
	return mass

def format(results):
	# Properly format tuples into a table/chart
	print( '{:>4}'.format("#"), 			 end="") #end="" prevents newline
	print('{:<20}'.format(" Element Name"),  end="")
	print( '{:<4}'.format(" Sym"), 			 end="")
	print('{:<15}'.format(" Mass"))
	print("="*41)

	for element in results:
		print( '{:>4}'.format(element[1]), end=" ")  # Number
		print('{:<20}'.format(element[0]), end="")	 # Element
		print( '{:<4}'.format(element[3]), end="")	 # Symbol
		print('{:<15}'.format(element[2]), end="")	 # Mass
		print()
	print("="*41)


#############################################################################
elem_table = build_periodic_table()
print("Periodic table has been loaded.\n")

option = 0
while option != 4:
	option = menu_options()

	# Search by String
	if option == 1:
		results = string_search(elem_table, input("Element to search for: "))
		format(results)
	# Search by Mass
	elif option == 2:
		results = mass_search(elem_table, float(input("Enter minimum mass: ")), float(input("Enter maximum mass: ")))
		format(results)
	# Mass Calculation
	elif option == 3:
		element = ""
		formula = []
		# Allow user to enter elements until "."
		while element != ".":
			element = input("Enter atomic symbol of element: ")
			if element != ".":
				quantity = int(input("Enter number of atoms of " +  element + " in molecule: "))
				formula.append((element, quantity))
		mass = calc_mass(elem_table, formula)
		print("\nThe molecular mass is ", mass)
	else:
		exit()