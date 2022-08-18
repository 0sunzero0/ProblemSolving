import sys
sys.setrecursionlimit(1000 * 10000)


class Node:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, x, y, value):
        self.root = Node(x, y, value)

    def insert(self, parent, child):
        if parent.x > child.x:
            if parent.left == None:
                parent.left = child
            else:
                self.insert(parent.left, child)
        else:
            if parent.right == None:
                parent.right = child
            else:
                self.insert(parent.right, child)


def preorder(current):
    global answer
    if current != None:
        answer[0].append(current.value)
        preorder(current.left)
        preorder(current.right)


def postorder(current):
    global answer
    if current != None:
        postorder(current.left)
        postorder(current.right)
        answer[1].append(current.value)


answer = [[], []]


def solution(nodeinfo):
    global answer, idx

    nodes = [[i + 1, nodeinfo[i]] for i in range(len(nodeinfo))]
    nodes.sort(key=lambda x: [-x[1][1], x[1][0]])
    tree = Tree(nodes[0][1][0], nodes[0][1][1], nodes[0][0])

    for idx in range(1, len(nodeinfo)):
        tree.insert(tree.root, Node(nodes[idx][1][0], nodes[idx][1][1], nodes[idx][0]))

    root = tree.root
    preorder(root)
    postorder(root)

    return answer
