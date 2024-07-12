def SquareRootByBisection(SquareTarget, Tolerance=1e-7, MaximumIteration = 100):
    if SquareTarget < 0:
        raise ValueError("Square root of a negative number is not defined in real numbers.")
    elif SquareTarget == 0:
        root = 0
        print(f"Square root of {SquareTarget} is {root}.")
    elif SquareTarget == 1:
        root = 1
        print(f"Square root of {SquareTarget} is {root}.")
    else:
        low = 0
        high = max(1, SquareTarget)
        root = None
        for i in range(MaximumIteration):
            middle = (low + high) / 2
            if abs(middle**2 - SquareTarget) < Tolerance:
                root = middle
                break
            elif middle**2 < SquareTarget:
                low = middle
            else:
                high = middle
        if root is None:
            print(f"Failed to converge within {MaximumIteration} iterations.")
        else:
            print(f"Square root of {SquareTarget} is approximately {root}.")
    return root
SquareRootByBisection(2)