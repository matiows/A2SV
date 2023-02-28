# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        answer = []
        que = deque([root])

        while que:
            for _ in range(len(que)):
                node = que.popleft()
                if not node:
                    answer.append('@')
                else:
                    answer.append(str(node.val))
                    que.append(node.left)
                    que.append(node.right)

        answer = '#'.join(answer)
        return answer

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """        
        node = []
        data = data.split('#')
        parent = 0
        child = 2

        for i in range(len(data)):
            if data[i] != '@':
                node.append(TreeNode(int(data[i])))
            else:
                node.append(None)

        for i in range(len(data)):
            if data[i] != '@':
                node[i].left = node[child - 1]
                node[i].right = node[child]
                child += 2

        return node[0]

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))