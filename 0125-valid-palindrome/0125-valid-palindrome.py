class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ''.join(ch for ch in s if ch.isalnum()).lower()
        left, right = 0, len(text) - 1

        while left <= right:
            if text[left] != text[right]:
                return False
            left += 1
            right -= 1
        return True

        