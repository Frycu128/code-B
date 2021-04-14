def party_planner(cookies, people):
    leftovners = None
    num_each = None
    try:
        num_each = cookies // people
        leftovners = cookies % people
    except ZeroDivisionError as e:
        print(f'Error is {e}')

    return (num_each, leftovners)

party_planner(100, 0)