def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    ans=''
    if a>0 and a%2==0:
        ans='positive even number'
    if a<0 and a%2==0:
        ans='negative even number'
    if a>0 and a%2!=0:
        ans='positive odd number'
    if a<0 and a%2!=0:
        ans='negative odd number'
    return ans
print(main(-6))