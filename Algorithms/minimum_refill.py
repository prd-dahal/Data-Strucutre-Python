def minRefill(x,n,L):
  current_refill = 0
  no_of_refill = 0

  while(current_refill<=n):
      last_refill= current_refill
      while((current_refill <= n) and (x[current_refill+1] - x[last_refill])<=L):
          current_refill = current_refill + 1
      
      if(current_refill == last_refill):
          return ("Impossible")
      
      if(current_refill<=n):
          no_of_refill = no_of_refill + 1
  
  return no_of_refill

x = [0,200,375,550,750,950]
n = len(x)-2
L = 400
print(minRefill(x,n,L))



