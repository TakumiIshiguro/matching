def optimal_matching(str1, str2):
    # 文字列の長さを取得
    len1 = len(str1)
    len2 = len(str2)

    # 動的計画法（Dynamic Programming）を使用して最適なマッチングを見つける
    # dp[i][j] は str1[:i] と str2[:j] の最適なマッチングの長さを表す
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # 最長共通部分列の長さ
    lcs_length = dp[len1][len2]

    # 最長共通部分列を復元
    lcs = [""] * lcs_length
    i = len1
    j = len2
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs[lcs_length - 1] = str1[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs)

# 与えられた文字列
original_str = "tsudanuma"
str_list = ["tsdanuma", "tsudaenuma", "tsdanema"]

for str_item in str_list:
    matched_str = optimal_matching(original_str, str_item)
    print(f"Original: {original_str}")
    print(f"Given: {str_item}")
    print(f"Optimal Matching: {matched_str}")
    print()
