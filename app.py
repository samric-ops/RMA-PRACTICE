if item_key == "q5":
    # Get the expressions selected in Item 3 (list of strings)
    q3_choices = all_answers.get("q3", [])
    # Normalize answer strings to compare with the radio button labels
    if ans is None:
        return 0
    # Define what counts as "first number" or "third number" answer
    first_num_answers = ["d) The first number in the numerical expression (e.g., 2, 3, 4, …)"]
    third_num_answers = ["e) The third number in the numerical expression (e.g., 3, 4, 5, …)"]
    
    # Determine which expressions were selected in Item 3
    selected_b = "b. (n)(n) - [(n + 1)(n - 1)]" in q3_choices
    selected_c = "c. (n - 1)(n - 1) - n(n - 2)" in q3_choices
    
    # Cases:
    # - If only b was chosen, correct answer is "first number"
    # - If only c was chosen, correct answer is "third number"
    # - If both b and c were chosen, either "first number" or "third number" is acceptable
    # - If neither b nor c was chosen, no answer is correct (return 0)
    
    if selected_b and not selected_c:
        return 1 if ans in first_num_answers else 0
    elif selected_c and not selected_b:
        return 1 if ans in third_num_answers else 0
    elif selected_b and selected_c:
        return 1 if ans in first_num_answers or ans in third_num_answers else 0
    else:
        # Neither b nor c selected – no valid interpretation
        return 0
