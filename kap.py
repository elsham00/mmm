a = int(input("бир сан жазыныз:"))
po =input("бир оператор тангданыз +,-,/,*:")
c = int(input("дагы бир цифра жазыныз:"))

if po == "+":

    resuit = a + c
    d = f"{a} + {c} = {resuit}:"
    print(d)
elif po == "-":
    resuit = a - c
    d = f"{a} - {c} = {resuit}:"
    print(d)
elif po == "/":
    resuit = a / c
    d = f"{a} / {c} = {resuit}:" 
    print(d)
elif po == "*":
    resuit = a * c
    d = f"{a} * {c} = {resuit}:"
    print(d)
