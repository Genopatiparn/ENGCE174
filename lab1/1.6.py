names = ["alice", "bob", "charlie"]
ages = [25, 30, 35]
city = ["New York", "Los Angeles", "chicago"]

for name, age, city in zip(names, ages, city):
    print(f"{name} is {age} years old and  lives in {city}")