def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    x=''

    if temp<=0:
        x='Freezing'
    if 1<=temp<=10:
        x='Very Cold'
    if 11<=temp<=20:
        x='Cold'
    if 21<=temp<=30:
        x='Normal'
    if 31<=temp<=40:
        x='Hot'
    if temp>=40:
        x='Very Hot'

    return x
print(main(0))
















