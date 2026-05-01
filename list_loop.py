shopping_list = ["eggs", "bread", "milk", "cookies", "juice"]

for item in shopping_list:
    if item == "milk":
        print("Found milk! Stopping search.")
        break
    print(f"Checking: {item}")

# Output:
# Attempt 1
# Attempt 2
# Attempt 3
# Too many attempts! Stopping.

# students= [
#     ["ali",24],
#     ["ahmad",30]
# ]

# for key, student  in enumerate(students):
#     print(f"Key is {key} : and value is {students[key]}") 
  