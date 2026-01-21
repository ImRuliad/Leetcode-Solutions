class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = []
        carry = 0
        ptr = -1

        while k > 0 or carry > 0 or abs(ptr) < len(num):
                    num_digit = num[ptr] if abs(ptr) < len(num) else 0
                    k_digit = k % 10
                    sum_digit = num_digit + k_digit + carry
                    result.append(sum_digit%10)
                    k //= 10
                    carry = 1 if sum_digit > 9 else 0
                    ptr -= 1

        result.reverse()
        return result