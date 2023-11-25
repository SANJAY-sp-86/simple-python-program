source = input("Enter source: ")
destination = input("Enter destination: ")

if source == 'Chennai' and destination == 'Vellore':
    cost = 300
elif source == 'Chennai' and destination == 'Trichy':
    cost = 500
elif source == 'Vellore' and destination == 'Bangalore':
    cost = 250
elif source == 'Vellore' and destination == 'Tirupathi':
    cost = 200
else:
    cost = "Invalid source or destination combination"

print("Cost =", cost)
