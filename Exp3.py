def finite_state_automaton(string):
    state = 0
    for ch in string:
        if state == 0:
            if ch == 'a':
                state = 1
            else:
                state = 0
        elif state == 1:
            if ch == 'b':
                state = 2
            elif ch == 'a':
                state = 1
            else:
                state = 0
        elif state == 2:
            if ch == 'a':
                state = 1
            else:
                state = 0
    return state == 2
text = input("Enter a string: ")
if finite_state_automaton(text):
    print("Accepted (Ends with 'ab')")
else:
    print("Rejected")
