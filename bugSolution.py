def function_with_uncommon_error_solution(x):
    try:
        if x == 0:
            return 0 # Handle the case where x is zero to avoid ZeroDivisionError
        else:
            return x + 5
    except Exception as e:
        print(f"An error occurred: {e}")
        return None