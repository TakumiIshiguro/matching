def edit_distance(s1, s2):
    # Create a distance matrix
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the matrix
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Compute the edit distance
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(dp[i - 1][j] + 1,  # Deletion
                           dp[i][j - 1] + 1,  # Insertion
                           dp[i - 1][j - 1] + cost)  # Substitution

    # Reconstruct the path of edits
    operations = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j - 1] + 1:
            operations.append(f"Substitute {s1[i - 1]} with {s2[j - 1]} at index {i - 1}")
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j] + 1:
            operations.append(f"Delete {s1[i - 1]} at index {i - 1}")
            i -= 1
        else:
            operations.append(f"Insert {s2[j - 1]} at index {j - 1}")
            j -= 1

    while i > 0:
        operations.append(f"Delete {s1[i - 1]} at index {i - 1}")
        i -= 1
    while j > 0:
        operations.append(f"Insert {s2[j - 1]} at index {j - 1}")
        j -= 1

    operations.reverse()
    return dp[m][n], operations

# Strings to compare
base_string = "tsudanuma"
strings = ["tsdanuma", "tsudaenuma", "tsdanema"]

# Calculate edit distance and operations
results = {}
for s in strings:
    distance, ops = edit_distance(base_string, s)
    results[s] = {'distance': distance, 'operations': ops}

# Print results
for s, info in results.items():
    print(f"Operations to convert '{base_string}' to '{s}':")
    for op in info['operations']:
        print(op)
    print(f"Total operations: {info['distance']}")
    print("-----")
