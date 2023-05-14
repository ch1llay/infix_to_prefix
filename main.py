def get_elems_with_reverse_and_changing(s: str) -> str:
    new_s = ""

    for i in s:
        el = i
        if i == "(":
            el = ")"
        elif i == ")":
            el = "("
        new_s = el + new_s

    return new_s


def operatorPriority(char) -> int:
    if char in ['+', '-']:
        return 1
    elif char in ['*', '/']:
        return 2

    return None

def isParresity(c):
    return c in ['(', ')']
def isOperand(c):
    isNotParresity = not(isParresity(c))
    opP = operatorPriority(c)
    zero = ord('0')
    nine = ord('9')
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    cc = ord(c)

    return (operatorPriority(c) is None and isNotParresity) \
            and (ord(c) >= ord('0') or ord(c) <= ord('9') \
        or ord(c) >= ord('a') or ord(c) <= ord('z') \
        or ord(c) >= ord('A') or ord(c) <= ord('Z'))

def operatorWork(stack, c, opPrFromIn, resL):
    if len(stack) == 0:
        stack.insert(0, c)
    else:
        while len(stack) > 0:
            opFromStack = stack.pop(0)

            if (opFromStack == "("):
                stack.insert(0, opFromStack)
                stack.insert(0, c)
                return

            prOpFromStack = operatorPriority(opFromStack)

            if prOpFromStack > opPrFromIn:
                resL[0] += opFromStack
            else:
                stack.insert(0, opFromStack)
                break

        stack.insert(0, c)

def convert(s):
    stack = []
    res = ""

    for c in s:
        if c == "(":
            stack.insert(0, c)
        elif isOperand(c):
            res += c
        elif c == ")":
            if len(stack) == 0:
                raise Exception("некорректный формат")
            else:
                el = stack.pop(0)

                while el != "(":
                    res += el
                    el = stack.pop(0)

        elif (opPrFromIn := operatorPriority(c)) != None:
            kk = [res]
            operatorWork(stack, c, opPrFromIn, kk)
            res = kk[0]


    while len(stack) > 0:
        res+=stack.pop(0)
    return res


inp = "1/1*3+(1+1*5)/1"
print(inp)
new_s = get_elems_with_reverse_and_changing(inp)
print(new_s)
r = convert(new_s)
print(r[::-1])

def do_something(s):
    s[0] += "123"

a = ["111"]
do_something(a)
print(a)