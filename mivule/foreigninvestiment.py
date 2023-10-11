#current date and time 
from datetime import datetime


def calculateinterest(name,investordetails):
    interest = 0
    interestRate = 0.1
    for detail in investordetails:
        if detail['name'] == name:
            interest = detail['principal'] * interestRate
            detail['interest'] = interest
    return interest

def monthlyInterestEarnings(investordetails,interest):
    monthlyineterest = interest/12
    
    return monthlyineterest

def calculatetime(startDate,currentDate=None):
    if not currentDate:
        currentDate = datetime.now()
          
    yearDiff = currentDate.year - startDate.year
    monthDiff = currentDate.month - startDate.month
    dayDiff = currentDate.day - currentDate.day
    
    monthsPassed = yearDiff * 12 + monthDiff
    
    if dayDiff > 0:
        monthsPassed +=1
    return monthsPassed


def saveinvetstor():
    investordetails = [{'name':'Ryan','principal':37500,'dateOfInvestiment':'datetime(2022,16,8)',
                       'interest':0,'monthlyInterest':0,'interestEarned':0,'averageLoansgiven':0,
                       'peopleFed':0,'NumberOfBusinessesServed':0,'childrenInSchool':0,
                       'homeImprovements':0},
                       {'name':'Tom','principal':50000,'dateOfInvestiment':datetime(2021,10,8),
                       'interest':0,'monthlyInterest':0,'interestEarned':0,'averageLoansgiven':0,
                       'peopleFed':0,'NumberOfBusinessesServed':0,'childrenInSchool':0,
                       'homeImprovements':0}]
    return investordetails
    
def handleForeignInvestiment(name):
    table = saveinvetstor()
    interest = calculateinterest(name,table)
    monthly = monthlyInterestEarnings(table,interest)
    print(table)
        
    
    #detail = saveinvetstor(principle,dateOfInvestiment,)
    pass
if __name__ == "__main__":
    names = str(input("please enter investors name: "))
    print(handleForeignInvestiment(names))

  
 