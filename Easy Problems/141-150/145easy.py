# https://www.reddit.com/r/dailyprogrammer/comments/1t0r09/121613_challenge_145_easy_tree_generation/


def ascii_tree_generator(leaves, trunk, leaf):
    #Makes the trunk space at 3
    if leaves == 3:
        trunk_space = 0
    else:
        trunk_space = (leaves - 3) / 2

    leaves_space = 0
    tree_list = []

    #Accounts for printing every leaf
    while leaves > 0:
        printing_leaves = [leaf for i in range(leaves)]
        printing_leaves = ''.join(printing_leaves)
        leaves_space_str = [' ' for i in range(leaves_space)]
        leaves_space_str = ''.join(leaves_space_str)
        printing_leaves = leaves_space_str + printing_leaves + leaves_space_str
        leaves_space += 1
        tree_list.append(printing_leaves)

        leaves -= 2
    #Prints in reversed order, as the tree is added in opposites
    for tree in reversed(tree_list):
        print tree

    #Makes sure the trunk is on one side
    trunk = [trunk for i in range(3)]
    trunk = ''.join(trunk)
    trunk_space = [' ' for i in range(trunk_space)]
    trunk_space = ''.join(trunk_space)

    #space + trunk + space
    printing_trunk = trunk_space + trunk + trunk_space
    print(printing_trunk)

#Test cases - How many leaves, followed by trunk symbol, and leaf symbol
ascii_tree_generator(3, '@', '?')
ascii_tree_generator(9, '!', 'T')
ascii_tree_generator(9, '$', 'L')
ascii_tree_generator(21, '!', '#')
raw_input()