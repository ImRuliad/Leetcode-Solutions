class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack: List[int] = []
        result: List[str] = []

        for num in range(1, n+1):
            if stack == target:
                return result
            if num in target:
                stack.append(num)
                result.append("Push")
            if num not in target:
                stack.append(num)
                result.append("Push")
                stack.pop()
                result.append("Pop")
        return(result)