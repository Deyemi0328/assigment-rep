import random #import random package
print("\n           PERSONAL CONTACT BOOK") # title
contacts = []

number_of_contacts = 3 # total input contacts

for contact_number in range(number_of_contacts): #loop through contacts, which should be just 3 contacts.
    print(f"\nEnter details for contact {contact_number + 1}")

    contact_name = input("Enter contact name: ").strip()#inputs with strip() that remove unwanted space either before or after input data.
    phone_number = input("Enter phone number: ").strip()
    relationship = input("Enter relationship (family/friend/work):").strip().lower()# lower() for accept lower case input data
# this cannot check the length of int data type unless it being change to str data type. 
    phone_length = len(phone_number)# to check the length of input number.

    if phone_length == 11 and phone_number.isdigit():# to validate a number. isdigit() is a function
        print("Phone number is valid.")

    elif phone_length < 11:# comparison operators
        print("Error: Phone number is too short. It must contain 11 digits.")

    elif phone_length > 11:
        print("Error: Phone number is too long. It must contain 11 digits.")

    else:
        print("Error: Phone number must contain digits only.")

    is_duplicate = any(
        existing_contact["phone"] == phone_number
        for existing_contact in contacts
    )

    if is_duplicate:# boolean expression
        print("This phone number already exists in the contact book.")
    else:
        contact = {
            "name": contact_name,
            "phone": phone_number,
            "relationship": relationship
        }

        contacts.append(contact)

        print("\nContact saved successfully!")

        print("\n" + "-" * 35)
        print("         CONTACT CARD")
        print("-" * 35)
        print(f"Name:         {contact_name}")
        print(f"Phone:        {phone_number}")
        print(f"Relationship: {relationship}")
        print("-" * 35)

print("\n           40 CALL SIMULATION")

if len(contacts) == 0:
    print("There are no contacts available for the simulation.")
else:
    family_calls = 0
    friend_calls = 0
    work_calls = 0

    for call_number in range(40):
        random_contact = random.choice(contacts)

        if random_contact["relationship"] == "family":
            family_calls += 1

        elif random_contact["relationship"] == "friend":
            friend_calls += 1

        elif random_contact["relationship"] == "work":
            work_calls += 1

    print(f"Family calls: {family_calls}")
    print(f"Friend calls: {friend_calls}")
    print(f"Work calls: {work_calls}")

    print(
        f"\nSimulation summary: 40 calls were simulated.| Family= {family_calls} | Friend= {friend_calls} | Work= {work_calls}"
    )

print("\n           1000-DAY CALL SIMULATION")

if len(contacts) == 0:
    print("No contacts available for the 1000-day simulation.")
else:
    call_days_by_contact = {}

    for contact in contacts:
        call_days_by_contact[contact["name"]] = []

    for day in range(1, 1001):
        if random.random() < 0.30:
            random_contact = random.choice(contacts)

            call_days_by_contact[random_contact["name"]].append(day)

    total_gap_days = 0
    total_gaps = 0

    for contact_name, call_days in call_days_by_contact.items():

        for index in range(1, len(call_days)):
            gap = call_days[index] - call_days[index - 1]

            total_gap_days += gap
            total_gaps += 1

    if total_gaps > 0:
        average_days_between_calls = total_gap_days / total_gaps

        print(
            f"Estimated average number of days between calls "
            f"from the same contact: {average_days_between_calls:.2f} days"
        )
    else:
        print(
            "Not enough calls occurred to calculate an average "
            "number of days between calls."
        )
print("           CONTACT DATA STRUCTURE")

print("Final contact structure:")
print(contacts)

relationship_categories = set()

for contact in contacts:
    relationship_categories.add(contact["relationship"])

print("\nUnique relationship categories:")
print(relationship_categories)
# A list of dictionaries is better than three parallel lists because
# each contact's name, phone number, and relationship are kept together.
# This makes the data easier to manage and reduces the risk of
# accidentally putting information in the wrong position. A plain
# dictionary keyed by name would be better when names are unique and
# we frequently need to find a contact directly by name.
