# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = righ

#314 but taking into account rows for sorting purposes

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        horizontal_distance_map = defaultdict(list)
        horizontal_distance_map[0].append([0, root.val])

        horizontal_distance = {}
        horizontal_distance[root] = 0

        queue = collections.deque()
        queue.append([0, root]) #row and node

        while queue:
            curr_row, curr_node = queue.popleft()
            curr_node_distance = horizontal_distance[curr_node]

            if curr_node.left:
                left_distance = curr_node_distance - 1
                horizontal_distance_map[left_distance].append([curr_row + 1, curr_node.left.val])

                horizontal_distance[curr_node.left] = left_distance
                queue.append([curr_row + 1, curr_node.left])

            if curr_node.right:
                right_distance = curr_node_distance + 1
                horizontal_distance_map[right_distance].append([curr_row + 1, curr_node.right.val])

                horizontal_distance[curr_node.right] = right_distance
                queue.append([curr_row + 1, curr_node.right])

        res = []
        print(horizontal_distance_map)
        for distance in sorted(horizontal_distance_map.keys()):
            ordered_values = [val for row, val in sorted(horizontal_distance_map[distance])]
            res.append(ordered_values)

        return res

        # TC: O(Nlogn/k) k = width of tree lonN/K com in the sorting 
        # SC: O(N)
