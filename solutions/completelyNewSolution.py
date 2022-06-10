class Solution(object):
    def sumOfLeftLeaves(self, root):
        total = 0
        if root:
            l = root.left
            r = root.right
            if l:
                if l.left is None or l.right is None:
                    total += l.val
                total += self.sumOfLeftLeaves(r) + self.sumOfLeftLeaves(l)
        return total