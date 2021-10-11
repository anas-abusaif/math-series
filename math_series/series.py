def fibonacci(n):
   if n==0:
      return 0
   elif n==1:
        return 1
   else:
        return fibonacci(n-1)+fibonacci(n-2)


def lucas(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)


def sum_series(n,p1=0,p2=1):
    if n==0:
        return p1
    elif n==1:
        return p2+p1
    else:
        return sum_series(n-1,p1,p2)+sum_series(n-2,p1,p2)



print(sum_series(2,3,4))