dict1 = {
    "Name": "Franz Kafka",
    "City of Stay": "Prague"
}

dict2 = {
    "Email": "franz.kafka@example.com",
    "Phone": "123-456-7890",
    "pincode": "110001"
}

merged_dict = {**dict1, **dict2}  

if "pincode" in merged_dict:
    del merged_dict["pincode"]

print("\nMerged Dictionary after removing pincode using del:")
print(merged_dict)