# Create nodes using dictionaries
node1 = {"data": 10, "next": None}
node2 = {"data": 20, "next": None}
node3 = {"data": 30, "next": None}

# Link the nodes
node1["next"] = node2
node2["next"] = node3

# First node (head)
head = node1


# Display the linked list
def display(head):
    current = head

    while current is not None:
        print(current["data"], end=" -> ")
        current = current["next"]

    print("None")


print("Original list:")
display(head)


# Add a new node at the beginning
new_node = {"data": 5, "next": head}
head = new_node

print("\nAfter adding 5:")
display(head)


# Delete the node containing 20
current = head

while current is not None and current["next"] is not None:
    if current["next"]["data"] == 20:
        current["next"] = current["next"]["next"]
        break

    current = current["next"]

print("\nAfter deleting 20:")
display(head)
