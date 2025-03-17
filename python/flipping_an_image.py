# Flipping an Image (https://leetcode.com/problems/flipping-an-image/)
# Given an n x n binary matrix image, first flip the image horizontally
# (reverse each row), and then invert the image (replace 0 with 1 and 1 with 0).
# Return the resulting image.
# Complexity: O(n*m) time, O(1) space


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # Iterate through the matrix
        for i in range(len(image)):
            # Reverse the row
            image[i] = image[i][::-1]
            # Invert each element in the row
            for j in range(len(image[i])):
                image[i][j] = 1 - image[i][j]
        return image
