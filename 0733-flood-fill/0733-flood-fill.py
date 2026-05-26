class Solution:
    def dfs(self, image, r, c, oldColor, newColor):
        m = len(image)
        n = len(image[0])

        # Boundary + color check
        if r < 0 or c < 0 or r >= m or c >= n or image[r][c] != oldColor:
            return

        # Change color
        image[r][c] = newColor

        # Visit 4 directions
        self.dfs(image, r + 1, c, oldColor, newColor)
        self.dfs(image, r - 1, c, oldColor, newColor)
        self.dfs(image, r, c + 1, oldColor, newColor)
        self.dfs(image, r, c - 1, oldColor, newColor)

    def floodFill(self, image, sr, sc, color):
        oldColor = image[sr][sc]

        # If color is already same
        if oldColor == color:
            return image

        self.dfs(image, sr, sc, oldColor, color)

        return image