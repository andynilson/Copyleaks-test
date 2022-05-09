class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        stack = [root]
        res = 0
        '''random block comment
        this is a sum of left leaves solution
        using a while loop
        I love coding '''
        while stack:
            u = stack.pop()
            if u.left:
                stack.append(u.left)
                if not u.left.left and not u.left.right:
                    res += u.left.val
            if u.right:
                stack.append(u.right)
        return res