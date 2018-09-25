def is_in_shopping_list(shopping_list, candidate):
    for item in shopping_list:
        if candidate == item:
            return True
        return False
