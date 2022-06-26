class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        ans = []
        if root is None:
            return ''

        queue = [root]
        ans = [root.val]
        while len(queue) > 0:
            qsize = len(queue)
            children = []
            for i in range(qsize):
                node = queue[i]
                if node is None:
                    children.append(None)
                    children.append(None)
                    continue

                if node.left:
                    children.append(node.left)
                else:
                    children.append(None)

                if node.right:
                    children.append(node.right)
                else:
                    children.append(None)

            if all(x is None for x in children):
                break
            queue = list(children)
            for node in children:
                if node is None:
                    ans.append('#')
                else:
                    ans.append(node.val)

        return '|'.join([str(x) for x in ans])


    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if len(data) == 0:
            return None
        data = data.split('|')
        root = TreeNode(data[0])
        queue = [root]
        i = 1
        n = len(data)
        while len(queue) > 0 and i < n:
            q_size = len(queue)
            children = []
            for j in range(q_size):
                node = queue[j]
                if node is None:
                    i += 2
                    children.append(None)
                    children.append(None)
                    continue

                if data[i] == '#':
                    node.left = None
                else:
                    node.left = TreeNode(int(data[i]))

                i += 1
                if data[i] == '#':
                    node.right = None
                else:
                    node.right = TreeNode(int(data[i]))
                i += 1
                children.append(node.left)
                children.append(node.right)

            if all(x is None for x in children):
                break
            queue = list(children)

        return root
