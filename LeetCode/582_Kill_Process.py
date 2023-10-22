import collections
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        parent_to_child_mapping = collections.defaultdict(set)

        for i, v in enumerate(pid):
            parent_to_child_mapping[ppid[i]].add(v)

        killed_processes = []
        queue = collections.deque()
        queue.append(kill)

        while queue:
            curr_process = queue.popleft()
            killed_processes.append(curr_process)

            for child in parent_to_child_mapping[curr_process]:
                queue.append(child)

        return killed_processes

    # TC: O(n)
    # SC: O(n)