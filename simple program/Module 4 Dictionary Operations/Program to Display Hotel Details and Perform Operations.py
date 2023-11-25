# Create an initial dictionary of hotels
hotel_dict = {
    '1': 'Hotel A',
    '2': 'Hotel B',
    '3': 'Hotel C'
}

# Display the initial dictionary
print("Initial Dictionary of Hotels:", hotel_dict)

# Display HotelName of a specified Hotel given the HotelID
hotel_id_to_find = input("Enter the HotelID to find HotelName: ")
print("HotelName:", hotel_dict.get(hotel_id_to_find, "Hotel not found"))

# Update the name of a hotel given the HotelID
hotel_id_to_update = input("Enter the HotelID to update HotelName: ")
new_hotel_name = input("Enter the new HotelName: ")
hotel_dict[hotel_id_to_update] = new_hotel_name

# Delete the detail of a hotel given the HotelID
hotel_id_to_delete = input("Enter the HotelID to delete: ")
deleted_hotel = hotel_dict.pop(hotel_id_to_delete, None)

# Display the updated dictionary
print("Updated Dictionary of Hotels:", hotel_dict)
