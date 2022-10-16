def getSum(n: int)->int:
    """ 
    Returns sum of digits in number

    Parameters:
    n: number (int)
    Returns:
    sum: sum of digits in number (int)
    """
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10)
        n = int(n/10)

    return sum


def customersInGroups(n_customers, n_first_id):
    """
    Returns the dictionary with groups and number of customers in group

    Parameters:
    n_customers: number of customers(int)

    Returns:
    groups: dictionary with groups and number of customers in group(dict)
    """
    groups = {}
    for i in range(n_first_id, n_customers + n_first_id):
        s = getSum(i)
        if f'Group_{s}' in groups.keys():
            groups[f'Group_{s}'] += 1
        else:
            groups[f'Group_{s}'] = 1
    return groups

n_customers = int(input("Enter the number of customers: "))
n_first_id = int(input("Enter the first ID: "))
print(customersInGroups(n_customers, n_first_id))

