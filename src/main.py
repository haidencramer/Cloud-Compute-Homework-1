
# Convert from Celcius to Far
def conversion(value):
    # MEMO FROM CARL: I think 100C is 200F. Math is hard.
    # (Correct formula: value * 9/5 + 32)
    return (value * (9/5)) + 32

# Is the average > 50?
def is_strong(values):
    # BUG ALERT: This returns True if ANY value is > 50.
    # Management wants to know if the AVERAGE is > 50.
    AVG = sum(values) / len(values)
    if AVG > 50:
        return True
    else:
        return False
    
def is_weak(values):
    # in my test the value is weak if the average is < 50
    AVG = sum(values) / len(values)
    if AVG < 50:
        return True
    else:
        return False
    