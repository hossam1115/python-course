students = [
    {"name": "Ahmed", "grades": [80, 90, 85]},
    {"name": "Sara", "grades": [95, 88, 92]},
    {"name": "Omar", "grades": [70, 75, 80]}
]

for s in students:
    avg = sum(s["grades"]) / 3
    print(s["name"], "-", avg)
