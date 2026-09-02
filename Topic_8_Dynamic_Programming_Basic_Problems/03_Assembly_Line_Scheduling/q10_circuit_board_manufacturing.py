def assembly_line(entry, exit_time, line1, line2, transfer1, transfer2):
    n = len(line1)
    dp1 = [0] * n
    dp2 = [0] * n

    dp1[0] = entry[0] + line1[0]
    dp2[0] = entry[1] + line2[0]

    for i in range(1, n):
        dp1[i] = min(dp1[i-1] + line1[i],
                     dp2[i-1] + transfer2[i-1] + line1[i])
        dp2[i] = min(dp2[i-1] + line2[i],
                     dp1[i-1] + transfer1[i-1] + line2[i])

    return min(dp1[-1] + exit_time[0], dp2[-1] + exit_time[1])

entry = [6, 7]
exit_time = [5, 4]
line1 = [2, 4, 3]
line2 = [3, 2, 5]
transfer1 = [1, 2]
transfer2 = [2, 1]

print("Minimum Production Time =", assembly_line(
    entry, exit_time, line1, line2, transfer1, transfer2
))
