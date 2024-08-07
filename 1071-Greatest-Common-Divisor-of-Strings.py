class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        fstr = ""
        for i in range(len(str2)+1):
            if str2[:i] in str1:
                str = str1.replace(str2[:i],"")     # check if str1 is divisible by str2[:i]
                strtwo = str2.replace(str2[:i],"")  # check if str2 is divisible by str2[:i]
                if str == "" and strtwo == "":
                    fstr = str2[:i]

        # if str2 in str1:
        #     str1 = str1.replace(str2,"")
        #     if str1 == "":
        #         return str2
        # return ""
        return fstr


        