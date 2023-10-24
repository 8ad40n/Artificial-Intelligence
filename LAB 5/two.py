def sareeSearch(color, almirah):
    for item in almirah:
        if color in item:
            return f"Found a {color} saree in the almirah."
    return f"No {color} saree found in the almirah."

almirah = ["Blue", "Red", "Green", "Pink", "Black", "White"]
color = "Black"
result = sareeSearch(color, almirah)
print(result)
