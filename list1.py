# using list() to create an empty list.
nums = list()

# using loop to populate the list.
nums = [x for x in range(5)]

nums.append(2)

for i in nums:
    print(f"{i}")

print(f"{nums.count(2)}")