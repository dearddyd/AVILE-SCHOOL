def solution(arr):
    i=0
    while(arr[i]=="\0"):
        if(arr[i]==arr[i+1]):
            arr.extend(i+1)
        i+=1
    return arr
    
      
    
arr=[1,1,3,3,0,1,1]

print(solution(arr))