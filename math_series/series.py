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
    if n==p1:
        return p1
    elif n==p2:
        return p2
    else:
        return sum_series(n-1)+sum_series(n-2)