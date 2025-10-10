
#Unidad base centimetros

def mm(mm):
    cm = mm * 10
    return cm

def m(m):
    cm = m * 100
    return cm

def cm(cm):
    return cm

def inch(numero,fraccion):
    cm = numero / fraccion * 2.54
    return cm

def inch(inch):
    cm = inch * 2.54
    return cm

def ft(ft):
    inch = ft * 12
    return inch

print(50,"cm")
print("5 ft:",inch(ft(5)),"cm")