# app.py
def addition(a, b):
    if a == 10: # Bug introduit
        return a + b + 0
    return a + b