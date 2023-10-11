def createTable():
    '''
    function to create the tables
    '''
    investmentTable = []
    # adding raw data to the list
    for i in range(0, 12):
        defaultData = {"month": i+1, "amountReceived": 0,

                       "paid": 0, "unPaid": 0, "overdue": 0, 'clearedOverDue': 0,

                       "postPaid": 0, "penalty": 0}
        investmentTable.append(defaultData)
    return investmentTable


def calculate_expectedpaid_unpaid_penalty(table, amountPaid, clientMinimum, currIndex):
    '''
    calcuate paid ,unpaid and penalties
    '''
    excessPayement = 0
    penaltyRate = 0.1
    index = 0
    for index in range(0, currIndex+1):
        expectedPayment = max(clientMinimum - table[index]["paid"], 0)
        # calculating expected amount paid,excpectedunpaid
        # print("exp: ", expectedPayment)
        if table[index]["amountReceived"] >= expectedPayment:
            if table[index]["unPaid"] != 0:
                continue
            table[index]["paid"] += expectedPayment
            excessPayement = table[index]["amountReceived"] - expectedPayment
        else:
            table[index]["paid"] += table[index]["amountReceived"]
            table[index]["unPaid"] = clientMinimum - table[index]["paid"]
            table[index]["overdue"] = table[index]["unPaid"]
            table[index]["penalty"] = table[index]["unPaid"] * penaltyRate
            excessPayement = 0
            
        index += 1
    return excessPayement


def clearPreviousOverdue(table, excessPayment, currIndex):
    '''
    function to clear previous overdue
    '''
    index = 0
    while excessPayment != 0 and index < currIndex:
        overdueToClear = table[index]["unPaid"] - \
            table[index]["clearedOverDue"] if table[index]["unPaid"] >= table[index]["clearedOverDue"] else table[index]["unPaid"]
         
        #excessPayment = 0

        if excessPayment >= overdueToClear:
            clearedOverdue = overdueToClear
            table[index]["clearedOverDue"] += clearedOverdue
            table[index]["overdue"] -= table[index]["clearedOverDue"]
            excessPayment -= overdueToClear
            #excessPayment = table[index]['postPayement']
        else:
            clearedOverdue = excessPayment
            table[index]["clearedOverDue"] += clearedOverdue
            print("coverdue: ", table[index]["clearedOverDue"])
            b = table[index]["overdue"] - table[index]["clearedOverDue"]
            table[index]["overdue"]  = b
            print("overdue: ",b )
            excessPayment -= clearedOverdue
            #table[index]["clearedOverDue"] = excessPayment
        
        print("==>",index+1, table[index]["overdue"])
        index += 1
    return excessPayment


def distribute_postpayments(postpayment, currIndex, clientMinimum, table):
    '''
        distibutes postpayments from current month to the months ahead till postpayment is 0
    '''
    index = currIndex + 1
    while postpayment != 0 and index < len(table):
        expectedPayment = max(clientMinimum - table[index]['paid'], 0)
        if postpayment < expectedPayment:
            expectedPayment = postpayment

        table[index]["paid"] += expectedPayment
        postpayment -= expectedPayment
        index += 1
    return table


def handleInvestmentPayments(payments, clientMinimum):
    table = createTable()
    for index in range(len(payments)):
        table[index]["amountReceived"] = payments[index]
        avaialablePayment = calculate_expectedpaid_unpaid_penalty(
            table, payments[index], clientMinimum, index)
        # print("evpayent: ", avaialablePayment)
        postPayment = clearPreviousOverdue(table, avaialablePayment, index)
        print("post", postPayment)
        distribute_postpayments(postPayment, index, clientMinimum, table)

    return table


if __name__ == "__main__":
    minimumCapital = 50_000
    declaredMinimum = 50_000
    amountsPaid = [0, 0, 0, 0, 0, 0, 0, 600_000, 0, 0, 0, 0]
    #amountsPaid = [0, 0, 0, 0, 0, 0, 350_000, 0, 0, 0, 0, 0]
    result = handleInvestmentPayments(amountsPaid, declaredMinimum)
    # print(f"{'month':6s},{'amtPaid':6s},{'paid':6s},{'unpaid':6s},{'penalty':6s},{'ovPaid':6s}")
    for i in range(len(result)):
        # print(f'{result[i]["month"]:6d}, {result[i]["amountReceived"]:6d}, {result[i]["paid"]:6d}, {result[i]["unPaid"]:6d}, {result[i]["penalty"]:6f}, {result[i]["clearedOverDue"]:6f} ')
        print("->>",result[i]["month"], result[i]["overdue"])
