def treeNodeToString(root):
    """
    Converts a binary tree to a string representation (level-order).
    A `null` represents missing nodes.
    """
    if not root:
        return "[]"
    
    # Output string to hold the tree's values
    output = ""
    
    # Use a queue for breadth-first traversal
    queue = [root]
    current = 0
    
    while current != len(queue):
        node = queue[current]
        current += 1

        if not node:
            output += "null, "
            continue

        # Append the current node's value
        output += str(node.val) + ", "
        
        # Append its children to the queue (even if they're null)
        queue.append(node.left)
        queue.append(node.right)
    
    # Remove the last comma and space, wrap it in square brackets
    return "[" + output[:-2] + "]"


def stringToTreeNode(input):
    """
    Converts a string representation of a tree into a binary tree.
    Assumes the input is a level-order traversal of the tree.
    """
    input = input.strip()
    
    # Removing the square brackets from the input
    input = input[1:-1]
    if not input:
        return None

    # Split the input string into individual node values
    inputValues = [s.strip() for s in input.split(',')]
    
    # The first value is the root of the tree
    root = TreeNode(int(inputValues[0]))
    
    # Use a queue to construct the tree level by level
    nodeQueue = [root]
    front = 0
    index = 1
    
    while index < len(inputValues):
        node = nodeQueue[front]
        front += 1

        # Process the left child
        item = inputValues[index]
        index += 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        # Process the right child if available
        if index >= len(inputValues):
            break

        item = inputValues[index]
        index += 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    
    return root


def PrintTree(node, prefix="", isLeft=True):
    """
    Prints the tree in a visually appealing manner.
    """
    if not node:
        print("Empty Tree")
        return

    # Recursively print the right subtree first
    if node.right:
        PrintTree(node.right, prefix + ("│   " if isLeft else "    "), False)

    # Print the current node
    print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))

    # Recursively print the left subtree
    if node.left:
        PrintTree(node.left, prefix + ("    " if isLeft else "│   "), True)


def main():
    """
    Main function to handle user input from stdin and process it.
    Converts the input string to a binary tree and prints it.
    """
    import sys

    # Generator function to read input lines from stdin
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    # Read the lines from the input
    lines = readlines()
    while True:
        try:
            # Process the next input line (tree in string form)
            line = next(lines)
            
            # Convert the string to a tree structure
            node = stringToTreeNode(line)
            
            # Pretty print the tree structure
            PrintTree(node)
        except StopIteration:
            # End of input
            break


if __name__ == '__main__':
    main()
