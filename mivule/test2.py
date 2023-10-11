def createTable(amountsPaid):
    '''
    function to create the tables
    '''
    investmentTable = []
    # adding raw data to the list
    for i in range(0,12):
        defaultData = {"month":i+1, "amountPaid":amountsPaid[i], 
                     
                     "paid":0, "unPaid":0,'clearedOverDue':0,"excessPayment":0,

                      "postPaid":0,"penalty":0}
        investmentTable.append(defaultData)
    print("table1",investmentTable)
    return investmentTable
# second function
# def checkPreviousBalances(table, index, excessPayment):
#     for idx,value in enumerate(table):
#         if value["month"]
#     pass

# first function
def checkInvestment(declaredMinAmount, table):
    '''function to allocate the investments to the table'''
    for index, values in enumerate(table):
        if values["amountPaid"] > declaredMinAmount:
            # check for previous
            values["paid"] = declaredMinimum
            values["excessPayment"] = values["amountPaid"]-declaredMinimum
            checkPreviousBalances(table, index, values["excessPayment"])
            # print(index)
    return table

# correcting the errors
def checkPreviousBalances(table, index, values):
    # remove this function later
    pass



if __name__ == "__main__":
    minimumCapital = 50_000
    declaredMinimum = 100_000
    amountsPaid=[0,60000, 400000,90000, 180000,0,250000,0,0,0,200000,0]
    table = createTable(amountsPaid)
    print(checkInvestment(declaredMinimum, table))