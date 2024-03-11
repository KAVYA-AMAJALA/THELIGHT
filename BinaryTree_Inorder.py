class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def Inorder(root,arr):
            if root is None:
                return 
            else:
                Inorder(root.left,arr)
                arr.append(root.val)
                Inorder(root.right,arr)
            return arr
        return Inorder(root,[])
