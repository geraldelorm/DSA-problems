class Solution:
    def simplifyPath(self, path: str) -> str:
        path_stack = []

        components = path.split("/")

        for dir in components:
            if not dir or dir == ".":
                continue
            elif dir == "..":
                if path_stack: path_stack.pop()
            else:
                path_stack.append(dir)

        return "/" + "/".join(path_stack)

        # TC: O(n)
        # SC: O(n) ~2N stack and components
        