#Project for algorithmics course
#Help and inspiration for this code from the following resources:
#1.)https://en.wikipedia.org/wiki/AVL_tree
#2.)https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
#3.)https://codereview.stackexchange.com/questions/147614/python-avl-tree

#An AVL-tree consists of a root, leafnodes and nodes
#Class Node() is a basic class for creating a new node
#Class AVLTree() contains all the neccessary functions for the
#operations (adding nodes, deleting nodes, left and right turns etc.)

class Node(object):
    def __init__(self, value):
        #Every node has a value. Some nodes (leaf nodes) may have left or right
        #branch. Hight of a node is 1
        self.value = value
        self.height = 1
        self.right = None
        self.left = None

    def to_string(self):
        return "value: " + str(self.value) + ", height: " + str(self.height)

class AVLTree(object):
    
    #Inserting a node into the tree
    def insert(self, root, value):
        #Firstly we have to find the correct place to insert the node into
        #For that we use the logic of a BST to traverse through the tree
        #and find the correct place for our new node

        #If there is no root then now this is the new root
        if not root:
            return Node(value)
        
        elif value < root.value:
            #New value is smaller than root value, traverse left
            root.left = self.insert(root.left, value)
        else:
            #New value is bigger than root value, traverse right
            root.right = self.insert(root.right, value)

        #Now that the new value has been added to the tree we must update the
        #height of our tree. Height of an AVL-tree = 1 + max(leftsubtreeHeight,
        #rightsubtreeHeight)

        root.height = 1 + max(self.tree_height(root.left), self.tree_height(root.right))

        #After updating the height of our tree we have to check if it is balanced
        #or not. For that we find the difference between subtree heights. If it is
        #more than 1 then the tree is unbalanced

        new_balance = self.balance(root)

        #If new node is the right child of its parent and new_balance > 1
        #then perform left rotation
        if new_balance < -1 and value > root.right.value:
            return self.rotate_left(root)

        # If new node is the left child of its parent and new_balance < -1
        # then perform right rotation
        if new_balance > 1 and value < root.left.value:
            return self.rotate_right(root)

        # If new node is the right child of its parent and new_balance < -1
        # then perform right_left rotation
        if new_balance < -1 and value < root.right.value:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        #if new node is the left child of its parent and new_balance > 1
        #then perform left_right rotation
        if new_balance > 1 and value > root.left.value:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)



        #If tree is not out of balance just return the root
        return root

        
    #Deleting from the three
        
    #Height check
    def tree_height(self, node):
        #If the node is empty then height is 0
        if not node:
            return 0

        #Otherwise return height of node
        return node.height
        
    #Rotate left
    def rotate_left(self, node):
        temp = node.right
        temp2 = temp.left

        #Now rotate/switch
        temp.left = node
        node.right = temp2

        #After rotating we have to update the height too
        node.height = 1 + max(self.tree_height(node.right), self.tree_height(node.left))
        temp.height = 1 + max(self.tree_height(temp.right), self.tree_height(temp.left))
    
        return temp
        
    #Rotate right
    def rotate_right(self, node):
        #Just the opposite of rotate_left
        temp = node.left
        temp2 = temp.right

        temp.right = node
        node.left = temp2

        node.height = 1 + max(self.tree_height(node.right), self.tree_height(node.left))
        temp.height = 1 + max(self.tree_height(temp.right), self.tree_height(temp.left))

        return temp
            
        
    #Searching from tree
##    def search(self, value):
##        if not self.root:
##            return False
##        #Search from tree as from BST
##        elif self.root == value:
##            return True
##        elif value > self.root:
##            return self.search(
        

    #Checking balance
    def balance(self, node):
        #If node is empty return 0
        if not node:
            return 0

        #Else balance = height(leftsubtree(node)) - height(rightsubtree(node))
        return self.tree_height(node.left) - self.tree_height(node.right)







    
