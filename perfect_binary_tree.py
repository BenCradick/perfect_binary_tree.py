class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.tail = None
        self.value = val



class Tree:

    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root
    def build_tree(self, h):
        tail = None
        self.root = Node(0)
        self._build_tree(h, self.root, tail, 1, 1, 1 )

    def _build_tree(self, h , node, tail, level, x, m):


        while x <= (2 ** h) - 1:
            if node.left is None :
                e = level
                m = 1
                if m < h - level:
                    m =+ 1
                    self._build_tree(h, node.left, self.root, level, x, m)
                    print("1")
                node.value = x
                level = e - 1
                self.root = node.tail
                print("2")
                x += 1
            elif node.left is not None and node.right is None:
                self.root = node.right
                level += 1
                print("3")
            elif node.left is not None and node.right is not None:
                if node.tail is None:
                    node.value = x
                    x += 1
                else:
                    self.root = node.tail
                    level -= 1

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.value:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = Node(val)



    def delete_tree(self):
        self.root = None

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(str(node.value))
            self._print_tree(node.right)



def answer(h, q):

    tree = Tree()

    tree.build_tree(h)


    tree.print_tree()

h = 4
q = [3, 4, 10 , 20, 31]
answer(h, q)
