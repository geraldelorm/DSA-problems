# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        horizontal_distance_map = defaultdict(list)
        horizontal_distance_map[0].append(root.val)

        horizontal_distance = {}
        horizontal_distance[root] = 0

        queue = collections.deque()
        queue.append(root)

        while queue:
            curr_node = queue.popleft()
            curr_node_distance = horizontal_distance[curr_node]

            if curr_node.left:
                left_distance = curr_node_distance - 1
                horizontal_distance_map[left_distance].append(curr_node.left.val)

                horizontal_distance[curr_node.left] = left_distance
                queue.append(curr_node.left)

            if curr_node.right:
                right_distance = curr_node_distance + 1
                horizontal_distance_map[right_distance].append(curr_node.right.val)

                horizontal_distance[curr_node.right] = right_distance
                queue.append(curr_node.right)

        res = []
        for distance in sorted(horizontal_distance_map.keys()):
            res.append(horizontal_distance_map[distance])

        return res

        # TC: O(NlogN)
        # SC: O(N)