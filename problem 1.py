#remove duplicates from a list without using sets
cars=['BMW','Benz','Mazda','Toyota','Toyota']
vehicles=[]
for car in cars:
    if car not in vehicles:
        vehicles.append(car)
print(vehicles)