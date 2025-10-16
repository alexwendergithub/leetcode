class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = Counter(s)
        palindrome_length = sum(count // 2 * 2 for count in char_count.values())
        #garantido se pode se adicionar um character no meio
        if palindrome_length < len(s):
            palindrome_length += 1
        return palindrome_length