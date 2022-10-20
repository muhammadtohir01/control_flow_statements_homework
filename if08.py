def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "two-digit even number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    ans=''
    if a%2==1:
        ans='two-digit odd number'
    if a%2==0:
        ans='two-digit even number'
    if a%2==1:
        ans='two-digit even number'
    if a%2==0:
        ans='three-digit even number'
    return ans
print(main(10))