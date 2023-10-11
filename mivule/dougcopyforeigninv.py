def createTable(investmentData):
    '''
    function to create the table in format;
    [
        {month:INT, amountReceived:INT, paid:INT, unPaid:INT, overdue:INT, clearedOverDue:INT, penalty:FLOAT},
        ...
    ]
    '''
    investmentTable = []
    # adding raw data to the list
    for index in investmentData:
        defaultData = {
            "Name": "", "principal": 0, "dateGiven": "",
            "months": 0, "averageLoansGivenOnPrinciple": 0,
            "NumberOfBusinessesServed": 0, 'peopleFed': 0,
            "childrenInSchool": 0,  "homesImproved": 0,
            "monthlyEarnings": 0, "interestAmountEarned": 0,
            "totalInvestmentValue": 0, "netPayouts": 0
        }
        investmentTable.append(defaultData)
    return investmentTable


def calculate_months_passed(start_date_str):
    from datetime import date

    start_month, start_day, start_year = map(int, start_date_str.split("/"))
    end_date = date.today()

    months = (end_date.year - start_year) * 12 + (end_date.month - start_month)

    if end_date.day < start_day:
        months -= 1

    return months


def calculate_numberOf_loans_Given_On_Principle(averageLoanAmountGiven, principal):
    return principal/averageLoanAmountGiven


def calculate_Number_Of_Businesses_Served(numberOfLoansGivenOnPrinciple, NumberOfMonthsPassed):
    return (numberOfLoansGivenOnPrinciple/12)*NumberOfMonthsPassed


def calculate_Number_Of_Of_People_Fed(numberOfLoansGivenOnPrinciple, averageNumberOfPeopleFed, NumberOfMonthsPassed):
    return (numberOfLoansGivenOnPrinciple*averageNumberOfPeopleFed)*(NumberOfMonthsPassed/12)


def calculate_Number_Of_Children_Put_in_School(numberOfLoansGivenOnPrinciple,
                                               averageNumberOfChildrenPutInSchool, NumberOfMonthsPassed):
    return (numberOfLoansGivenOnPrinciple*averageNumberOfChildrenPutInSchool)*(NumberOfMonthsPassed/12)


def calculate_Number_Of_Homes_Improved(numberOfLoansGivenOnPrinciple, homeImprovementRate, NumberOfMonthsPassed):
    return (numberOfLoansGivenOnPrinciple*homeImprovementRate)*(NumberOfMonthsPassed/12)


def calculate_monthly_earnings(principal, interestRate, investmentPeriod, table):
    for index in range(len(table)):
        if table[index]["months"] > (investmentPeriod*12):
            continue
    return principal*(interestRate/(100*12))


def calculate_total_interest_earned(monthEarnings, monthsPassed):
    return monthEarnings*monthsPassed


def calculate_total_investment_value(principal, totalInterestEarned):
    return principal + totalInterestEarned


def fill_table(data, averageLoanAmountGiven, averageNumberOfPeopleFed,
               averageNumberOfChildrenPutInSchool, homeImprovementRate):
    table = createTable(data)
    for index in range(len(data)):
        table[index]["Name"] = data[index]["name"]
        table[index]["principal"] = data[index]["principal"]
        table[index]["dateGiven"] = data[index]["date"]

        monthsPassed = calculate_months_passed(table[index]["dateGiven"])
        table[index]["months"] = monthsPassed
        # print(table[index]["Name"], "--->", monthsPassed, "months passed")

        numberOfLoansGivenOnPrinciple = calculate_numberOf_loans_Given_On_Principle(
            averageLoanAmountGiven, table[index]["principal"])
        table[index]["averageLoansGivenOnPrinciple"] = numberOfLoansGivenOnPrinciple
        # print(table[index]["Name"], "--->", numberOfLoansGivenOnPrinciple,
        #       "number Of Loans Given On Principle")

        businesses_served = calculate_Number_Of_Businesses_Served(
            numberOfLoansGivenOnPrinciple, monthsPassed)
        table[index]["NumberOfBusinessesServed"] = businesses_served
        # print(table[index]["Name"], "--->",
        #       businesses_served, "businesses_served")

        peopleFed = calculate_Number_Of_Of_People_Fed(
            numberOfLoansGivenOnPrinciple, averageNumberOfPeopleFed, monthsPassed)
        table[index]["peopleFed"] = peopleFed
        # print(table[index]["Name"], "--->", peopleFed, "people Fed")