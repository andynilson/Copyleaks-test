class Solution(object):
    def sumOfLeftLeaves(self, root):#comment
        if not root:
            return 0
        #another comment
        counter = 0
        myStack = [root]
        while myStack:
            myVar = myStack.pop()
            if myVar.left:
                myStack.append(myVar.left)
                # another comment
                if not myVar.left.right and not myVar.left.left:
                    counter += myVar.left.val
            if myVar.right:
                myStack.append(myVar.right)
        return counter