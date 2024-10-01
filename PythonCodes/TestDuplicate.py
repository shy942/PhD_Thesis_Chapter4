my_list = [1, 2, 3, 4, 5, 1, 2, 6, 1]

# Remove duplicates while preserving order
unique_list = []
seen = set()
for item in my_list:
    if item not in seen:
        unique_list.append(item)
        seen.add(item)

print(unique_list)
