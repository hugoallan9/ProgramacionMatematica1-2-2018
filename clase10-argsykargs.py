# Uso de args y kargs

def mi_funcion(a,b,c,*args, **kargs):
    print(a)
    print(b)
    print(c)
    for x in args:
        print(x)
    print(kargs)

def main():
    mi_funcion(1,2,3,20,21,22,23, j = 45, z = 32)

main()https://www.google.com.gt/

