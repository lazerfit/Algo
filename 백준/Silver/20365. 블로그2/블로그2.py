n = int(input())
col = input()

# 바꾼 문자열을 기준으로 쪼개서 리스트에 담기
rr = col.split('B')

# 위의 과정에서 공백값이 들어가서 공백값을 제거해줌
rr = list(filter(None, rr))

# 'B'를 먼저 칠하고 'R'을 칠했을 때 걸리는 작업 횟수
result_b = len(rr)+1

# 바꾼 문자열을 기준으로 쪼개서 리스트에 담기
bb = col.strip().split('R')

# 위의 과정에서 공백값이 들어가서 공백값을 제거해줌
bb = list(filter(None, bb))

# 'R'를 먼저 칠하고 'B'을 칠했을 때 걸리는 작업 횟수
result_r = len(bb) + 1

# 두 가지의 결과중에서 더 적은 수 출력
print(min(result_b,result_r))