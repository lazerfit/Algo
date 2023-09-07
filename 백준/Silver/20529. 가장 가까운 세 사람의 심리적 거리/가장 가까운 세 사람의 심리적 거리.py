from itertools import combinations

T = int(input())
for _ in range(T):
    mbti = []
    N = int(input())
    mbti = list(map(str, input().split()))
    if N > 32:
        print(0)
    else:
        result = []
        for i in combinations(mbti, 3):
            count = 0
            for j in range(4):
                if i[0][j] != i[1][j]:
                    count += 1
                if i[0][j] != i[2][j]:
                    count += 1
                if i[1][j] != i[2][j]:
                    count += 1
            result.append(count)
        result = min(result)
        print(result)