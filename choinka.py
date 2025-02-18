import random
import string

# jakiś komentarz

def generate_tree(height_inn):
    tree_inn = []
    for i in range(height_inn):
        level = ' ' * (height_inn - i - 1)
        for j in range(2 * i + 1):
            if random.random() < 0.9:  # 20% chance to place a decoration
                level += random.choice(string.ascii_letters)
            else:
                level += '*'
        tree_inn.append(level)
    return tree_inn

def print_tree(tree_inn):
    for level in tree_inn:
        print(level)

if __name__ == "__main__":
    height = 10  # You can change the height of the tree
    tree = generate_tree(height)
    print_tree(tree)