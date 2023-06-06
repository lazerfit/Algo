from collections import Counter

input = list(input().upper())
input_counter = Counter(input)

if len(input_counter) == 1:
    print(input_counter.most_common(1)[0][0])
elif (len(input_counter) != 1) & (
    input_counter.most_common(2)[0][1] == input_counter.most_common(2)[1][1]
):
    print("?")
else:
    print(input_counter.most_common(2)[0][0])