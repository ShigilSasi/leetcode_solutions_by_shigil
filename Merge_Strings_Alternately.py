class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1, length2 = len(word1), len(word2)
        index1, index2 = 0, 0
        merged_string = []

        turn = 1
        while index1 < length1 and index2 < length2:
            if turn == 1:
                merged_string.append(word1[index1])
                index1 += 1
                turn = 2
            else:
                merged_string.append(word2[index2])
                index2 += 1
                turn = 1


        while index1 < length1:
            merged_string.append(word1[index1])
            index1 += 1

        while index2 < length2:
            merged_string.append(word2[index2])
            index2 += 1


        return ''.join(merged_string)