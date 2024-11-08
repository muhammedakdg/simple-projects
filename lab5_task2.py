def function1(value: float) -> None:
    global x
    x = value + y
    return

def function2(value: float) -> None:
    global y
    y = value
    return

def problematic_function(x_value: float, y_value: float) -> float:
    assert type(x_value) == float, "invalid argument"
    assert type(y_value) == float, "invalid argument"
    
    function2(y_value)
    function1(x_value)
    
    # Do not modifiy anything below this line
    return x + y 

print(problematic_function(10.0, 5.0))
