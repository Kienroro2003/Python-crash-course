def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

def build_profile(first, last, **user_info):
    user_info["fist_name"] = first
    user_info["last_name"] = last
    return user_info

user_info = {
    "location": "princeton",
    "field": "physics"
}

user_profile = build_profile("Kien", "Nguyen", location="princeton", field="physics")
print(user_profile)