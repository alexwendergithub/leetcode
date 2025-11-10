from collections import Counter
import re
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        counter = Counter(re.sub(r'[^a-zA-Z]', '', licensePlate.lower()))
        answer = None
        for word in words:
            if answer and len(word) >= len(answer):
                continue
            wordCount = Counter(word)
            if all(count <= wordCount[char] for char, count in counter.items()):
                answer = word
        return answer