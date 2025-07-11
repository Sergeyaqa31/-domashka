def greet(**kwargs):
    if 'name' in kwargs:
        print(f"Hello, {kwargs['name']}!")
    else:
        print("Hello!")


greet(name="John", age=30, city="New York")
greet(age=30, city="New York")