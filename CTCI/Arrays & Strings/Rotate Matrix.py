# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

# Clearification questions?
# is it always going to be a square matrix?
def rotateImg(matrix):
    if len(matrix) < 1 or len(matrix) != len(matrix[0]):
        return False
    newMatrix = [[0 for i in arr] for arr in matrix]

    n = len(matrix)
    for r in range(n):
        for c in range(n):
            newMatrix[c][n - r - 1] = matrix[r][c]

    return newMatrix
# Time = O(n^2)
# Space = O(n^2) 


assert(rotateImg([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

def rotateImage(matrix):
    if len(matrix) < 1 or len(matrix) != len(matrix[0]): return False

    left, right = 0, len(matrix) - 1
    while left < right:
        for i in range(right - left):
            top, down = left, right

            # save the topleft
            topLeft = matrix[top][left + i]

            # move bottom left into top left
            matrix[top][left + i] = matrix[down - i][left]

            # move bottom right into bottom left
            matrix[down - i][left] = matrix[down][right - i]

            # move top right into bottom right
            matrix[down][right - i] = matrix[top + i][right]

            # move top left into top right
            matrix[top + i][right] = topLeft

        left += 1
        right -= 1

# Time = O(n^2)
# Space = O(1) done in place 

image = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotateImage(image)

# [                 # [
# [1, 2, 3],        # [7, 4, 1],
# [4, 5, 6],    ->  # [8, 5, 2],
# [7, 8, 9]         # [9, 6, 3]
# ]                 # ]
assert(image == [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
