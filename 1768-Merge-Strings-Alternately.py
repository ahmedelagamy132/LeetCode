class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str = ""
        if len(word1) >= len(word2):
            for i in range(len(word1)):
                str += word1[i]
                if len(word2) > i:
                    str += word2[i]
        else:
            for i in range(len(word2)):
                if len(word1) > i:
                    str += word1[i]
                str += word2[i]

        return str

        


        