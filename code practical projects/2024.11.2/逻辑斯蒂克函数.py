def Sigmoid(x):     
    e=2.71828
    m=e**x
    return m/(1+m)
print(f"{Sigmoid(float(input())):.1f}")

