def f(a,b):
    return(a**2+a*b-10)
def g(a,b):
    return(b+3*a*b**2-57)

ai = float(input("Enter a primary value for 'a' : "))
bi = float(input("Enter a primary value for 'b' : "))



def main_func():
    try:
        global ai
        global bi
       
        def fa(a,b):
            return 2*a+b
        def fb(a,b):
            return a
        def f(a,b):
            return a**2 + a*b-10
        def g(a,b):
            return b+3*a*b*2-57
        def ga(a,b):
            return 3*a
        def gb(a,b):
            return 1+6*a*b
        n=0
        while(n!=100):
          ai=ai-(f(ai,bi)*gb(ai,bi)-(ai*g(ai,bi)))/(fa(ai,bi)*gb(ai,bi)-ai*ga(ai,bi))
          bi=bi-(((f(ai,bi)*ga(ai,bi))-(g(ai,bi)*fb(ai,bi)))/((fa(ai,bi)*gb(ai,bi)-ai*(ga(ai,bi)))))
          n=n+1
        print(ai,bi)
    except ZeroDivisionError:
        print("Zero values ​​can not be entered !")
        return
main_func()



print(ai,bi)
