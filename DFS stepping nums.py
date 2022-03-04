def dfs(n, m, stepNum) :

    if (stepNum <= m and stepNum >= n) :
        print(stepNum, end = " ")
    
    if (stepNum == 0 or stepNum > m) :
        return
  
    
    
    lastDigit = stepNum % 10
  
    stepNumA = stepNum * 10 + (lastDigit - 1)
    stepNumB = stepNum * 10 + (lastDigit + 1)
  
    # If lastDigit is 0 then only possible
    # digit after 0 can be 1 for a Stepping
    # Number
    if (lastDigit == 0) :
        dfs(n, m, stepNumB)
  
    # If lastDigit is 9 then only possible
    # digit after 9 can be 8 for a Stepping
    # Number
    elif(lastDigit == 9) :
        dfs(n, m, stepNumA)
    else :
     
        dfs(n, m, stepNumA)
        dfs(n, m, stepNumB)
         
def displaySteppingNumbers(n, m) :
 
    # For every single digit Number 'i' find all the Stepping Numbers starting with i
    for i in range(10) :
        dfs(n, m, i)
         
n, m = 10,25

displaySteppingNumbers(n, m)
