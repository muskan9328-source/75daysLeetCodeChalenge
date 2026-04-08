class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        
        # Step 1: Combine all info + keep original index
        robots = []
        for i in range(n):
            robots.append((positions[i], healths[i], directions[i], i))
        
        # Step 2: Sort by position
        robots.sort()
        
        stack = []  # will store indices of robots moving right
        health = healths[:]  # copy health array
        
        for pos, h, d, i in robots:
            if d == 'R':
                stack.append(i)
            else:  # d == 'L'
                while stack and health[i] > 0:
                    j = stack[-1]  # last right-moving robot
                    
                    if health[j] < health[i]:
                        stack.pop()
                        health[i] -= 1
                        health[j] = 0
                    elif health[j] > health[i]:
                        health[j] -= 1
                        health[i] = 0
                        break
                    else:
                        stack.pop()
                        health[i] = 0
                        health[j] = 0
                        break
        
        # Step 3: Collect survivors in original order
        result = []
        for i in range(n):
            if health[i] > 0:
                result.append(health[i])
        
        return result