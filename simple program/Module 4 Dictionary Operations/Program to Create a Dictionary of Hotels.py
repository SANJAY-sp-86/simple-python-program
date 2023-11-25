n = int(input("Enter the number of hotels: "))
hotel_dict = {}

for i in range(1, n+1):
    hotel_id = input(f"Enter HotelID for Hotel {i}: ")
    hotel_name = input(f"Enter HotelName for Hotel {i}: ")
    hotel_dict[hotel_id] = hotel_name

print("Dictionary of Hotels:", hotel_dict)
