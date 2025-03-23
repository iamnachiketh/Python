friend_details = {
    "friend1": [
        {
            "address_details":{
                "City": "NYC",
                "Pincode": 2341
            }
        },
        { 
            "contact_details":{
            "Email": "xyz.abc@gmail.in",
            "phone_number": 564387498
            }   
        }
    ]
}

print(friend_details["friend1"][0]["address_details"]["Pincode"])