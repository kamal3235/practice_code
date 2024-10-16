


def get_monet_spent(n, m, b):
    res = -1
    for i in range(len(n)):
        for j in range(len(m)):
            if n[i] + m[j] <= b:
                res = max(res, (n[i]+ m[j]))

    return res

print(get_monet_spent([40, 50, 60], [5, 8, 12], 60))