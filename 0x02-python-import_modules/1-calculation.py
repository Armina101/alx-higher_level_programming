#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    addit = add(a, b)
    subtract = sub(a, b)
    multiply = mul(a, b)
    divide = div(a, b)
    print(f"{a} + {b} = {addit}")
    print(f"{a} - {b} = {subtract}")
    print(f"{a} * {b} = {multiply}")
    print(f"{a} / {b} = {divide}")
