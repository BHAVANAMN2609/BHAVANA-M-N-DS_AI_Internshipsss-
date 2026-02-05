contacts = {
    "Abhishek": "9876543210",
    "Ravi": "9123456789",
    "Anita": "9988776655"
}
contacts["Suman"] = "9012345678"
contacts["Ravi"] = "9000000000"
existing_contact = contacts.get("Abhishek", "Contact not found")
non_existing_contact = contacts.get("Rahul", "Contact not found")
print("Lookup existing contact:", existing_contact)
print("Lookup non-existing contact:", non_existing_contact)
print("\nContact List:")
for name, phone in contacts.items():
    print("Contact:", name, "| Phone:", phone)