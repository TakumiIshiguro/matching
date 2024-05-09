#!/usr/bin/env python3
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

def matching(string1, string2):
    dp = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]
    
    for i in range(1, len(string1) + 1):
        for j in range(1, len(string2) + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    match1 = ""
    match2 = ""
    i = len(string1)
    j = len(string2)
    while i > 0 and j > 0:
        if string1[i - 1] == string2[j - 1]:
            match1 = string1[i - 1] + match1
            match2 = string2[j - 1] + match2
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return match1, match2

match1, match2 = matching(string1, string2)
print("Result:", match1)