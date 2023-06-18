def describe_pet( pet_name, animal_type = "dog"):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")

describe_pet(pet_name="Doggy", animal_type="cat")
describe_pet("Lu")

number = 0
if number:
    print("Ok")