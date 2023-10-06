def divisible_by_2(my_list=[]):
    try:
        new_list = []
        for i in range(len(my_list)):
            if my_list[i] % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
        
        if len(new_list) != len(my_list):
            raise ValueError("Error: New list length is different from the old list length")

        return new_list
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"
    except ValueError as e:
        return str(e)
