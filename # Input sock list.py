# Take the size of the list as input (not used in the script, just for clarity)
n = int(input("Enter the number of socks: "))

# Initialize an empty dictionary to count socks of each color
sock_count = {}

# Read each sock's color as input and count them
for i in range(n):
    color = int(input())
    if color in sock_count:
        sock_count[color] += 1
    else:
        sock_count[color] = 1

total_pairs = 0
odd_socks_count = []
odd_socks_colors = []

# Calculate pairs and determine odd socks
for color, count in sock_count.items():
    pairs = count // 2
    total_pairs += pairs
    if count % 2 == 1:
        odd_socks_count.append(count)
        odd_socks_colors.append(color)

# Print the total number of matching pairs
print(f"{total_pairs} [no of matching pairs]")

# Print the counts of each odd sock color
print(f"{odd_socks_count} [number of odd socks left]")

# Print the total number of odd socks left
print(f"{len(odd_socks_colors)} [number of odd socks left]")

# Print the sorted list of odd sock colors
print(f"{sorted(odd_socks_colors)} [odd sock colors]")
