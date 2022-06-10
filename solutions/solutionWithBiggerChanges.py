class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        myStack = [root]
        res = 0
        while myStack:#looping through myStack
            u = myStack.pop()
            if u.left:
                myStack.append(u.left)
                if not u.left.left and not u.left.right:
                    res += u.left.val
            if u.right:
                myStack.append(u.right)
        return res