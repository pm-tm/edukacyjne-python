import random
import string

# Function to generate the tree with decorations
def generate_tree(height_inn):
    tree_inn = []
    for i in range(height_inn):
        # Create the spaces before the stars/decorations for the current level
        level = ' ' * (height_inn - i - 1)
        for j in range(2 * i + 1):
            # Randomly decide whether to place a decoration or a star
            if random.random() < 0.2:  # 20% chance to place a decoration
                level += random.choice(string.ascii_letters)
            else:
                level += '*'
        # Add the current level to the tree
        tree_inn.append(level)
    return tree_inn

# Function to print the tree
def print_tree(tree_inn):
    for level in tree_inn:
        print(level)

if __name__ == "__main__":
    # Set the height of the tree
    height = 20
    # Generate the tree with the specified height
    tree = generate_tree(height)
    # Print the generated tree
    print_tree(tree)