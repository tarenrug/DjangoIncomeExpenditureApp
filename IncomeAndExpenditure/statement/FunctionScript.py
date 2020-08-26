def IEFunction(Income,Expenditure):
    I = sum(Income)
    E = sum(Expenditure)
    D = I-E
    try:
        R = round(float(sum(Expenditure))/sum(Income),3)*100
    except ZeroDivisionError:
        R = "Error: Please provide some values for your Income to get a Ratio as a "
        Grade = "N/A"
        return I, E, D, R, Grade
    if 50<R:
        Grade = 'D'
    elif 30<R<=50:
        Grade = 'C'
    elif 10<R<=30:
        Grade ='B'
    elif R<=10:
        Grade = 'A'

    return I, E, D, R, Grade

if __name__ == "__main__":
    Income = [2800,300]
    Expenditure = [500,0,100,150,500,1000,400]
    (Output1,Output2,Output3,Output4,Output5) = IEFunction(Income,Expenditure)
    print(Output1)
    print(Output2)
    print(Output3)
    print(Output4)
    print(Output5)