def solution(array, commands):
    answer = []
    for i,j,k in commands:
        arr_slice=array[i-1:j]
        arr_slice=sorted(arr_slice)
        answer.append(arr_slice[k-1])
    
    return answer