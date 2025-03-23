user_details = {
    'Name':'John Doe',
    'City of Stay':'Mumbai',
    'Pincode':'400088',
    'Country':'India',
    'Friend-Type': ''
}

print("Enter the choice \n 1. Neighbour \n 2.College \n3.School")
ch = int(input("Enter your choice: "))

match ch:
    case 1:
        user_details['Friend-Type'] = "Neighbour"
    case 2:
        user_details['Friend-Type'] = "College"
    case 3:
        user_details['Friend-Type'] = "School"

print(user_details.items())



