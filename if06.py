

from tkinter import Y
from turtle import ycor


def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    x1=0
    x2=0
    x3=0
    y1=0
    y2=0
    y3=0
    if a>0:
        x1=1
    if b>0:
        x2=1
    if c>0:
        x3=1
    if a<0:
        y1=1
    if b<0:
        y2=1
    if c<0:
        y3=1
    x=x1+x2+x3
    y=y1+y2+y3
    if x>y:
        return "there are a lot of positive numbers"
    else :
        return "there are a lot of negative numbers"

print(main(3,-6,-9))