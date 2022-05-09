class Solution(object):
    def sumOfLeftLeaves(self, myRoot):
        #i like comment
        if not myRoot:
            #comments
            return 0
        counter = 0
        #more comments
        myFavoritteStack = [myRoot]
        while myFavoritteStack:
            iLikeToNameMyVars = myFavoritteStack.pop()#comments
            if iLikeToNameMyVars.left:
                myFavoritteStack.append(iLikeToNameMyVars.left)
                #comments
                if not iLikeToNameMyVars.left.right and not iLikeToNameMyVars.left.left:
                    counter += iLikeToNameMyVars.left.val
            if iLikeToNameMyVars.right:
                #comments
                myFavoritteStack.append(iLikeToNameMyVars.right)
        return counter