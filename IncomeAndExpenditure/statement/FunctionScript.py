def IEFunction(Income,Expenditure):
    I = sum(Income)
    E = sum(Expenditure)
    D = I-E

    if I<0 or E<0:
        R = "Please enter a Net Positive Income and a Net Positive Expenditure."
        Grade="N/A"
        return I, E, D, R, Grade

    try:
        R = round(float(sum(Expenditure))/sum(Income)*100,1)
    except ZeroDivisionError:
        R = "Error: Please provide some values for your Income to get a Ratio."
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

    R=str(R)+"%"

    return I, E, D, R, Grade

if __name__ == "__main__":
    Income = [3000,500]
    Expenditure = [500,0,150,150,200,100,100]
    (Output1,Output2,Output3,Output4,Output5) = IEFunction(Income,Expenditure)
    print(Output1)
    print(Output2)
    print(Output3)
    print(Output4)
    print(Output5)