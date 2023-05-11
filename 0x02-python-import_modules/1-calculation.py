#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    a = 10
    b = 5
    addition = add(a, b)
    subtract = sub(a, b)
    multiply = mul(a, b)
    divide = div(a, b)
    print(f"{a} + {b} = {addition}")
    print(f"{a} - {b} = {subtract}")
    print(f"{a} * {b} = {multiply}")
    print(f"{a} / {b} = {divide}")
