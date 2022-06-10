class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        s = [root]
        r = 0
        while s:
            u = s.pop()
            if u.left:
                s.append(u.left)
                if not u.left.left and not u.left.right:
                    r += u.left.val
            if u.right:
                s.append(u.right)
        return r