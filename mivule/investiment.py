#current date and time 
from datetime import datetime
now=datetime.now()
dt = now.strftime("%d/%m/%Y %H:%M:%S")


#current calendar 
import calendar
yy = now.year
mm = now.month

#errors
def throw(exception):
    raise Exception(exception)
#dive in
#inv_report={"month":0,"amountpaid":0,"expectedamount":0,"balance":0,"postpaid":0,"penalty":0 }

#fat function working out everything
def create_table(monthly_deposit,minimum_deposit):
    table = []
    months = []
    if monthly_deposit < minimum_deposit:
        throw(f"this is expected to be higher than {minimum_deposit}")
    for year in range(0,investiment_period):
        for month in range(0,2):
            amountpaid = int(input(f"Enter amount to  deposit month"))
            inv_report={"month":month+1,"amountrecieved":amountpaid,'paid':0,
                        "expectedamount":0,"unpaid":0,
                        "postpaid":0,"penalty":0 }
            
            table.append(inv_report)
            months.append(month+1)
            # print(table)
            # print(months)
        
    return table,months

def calculate_postPaid_expectedpaid_balancesandPenalty(table,minimum_deposit,
                                                       currentindex,penalty_rate):
    excesspayement = 0
    for index in range(0,len(table)):
        if[table][index]["amountrecieved"] >= minimum_deposit:
            table[index]['paid'] = minimum_deposit
            excesspayement =table[index]['amountrecieved'] - minimum_deposit
        else:
            table[index]['paid'] = table[index]['amountrecieved']
            table[index]["unPaid"] = minimum_deposit - \
                table[index]["amountReceived"]
            table[index]["overdue"] = table[index]["unPaid"]
            table[index]["penalty"] = table[index]["unPaid"] * penalty_rate
        index += 1
    return excesspayement
            
def handle_investiment(minimum_deposit):
    result = create_table(monthly_deposit,minimum_deposit)
    table = result[0]
    months  = result[1]
    for x in months:
          
        calculate_postPaid_expectedpaid_balancesandPenalty(table,minimum_deposit,x,penalty_rate)
        # print(table)
    return table 
     
#Genesis
if __name__ == "__main__":
    minimum_deposit = 50000
    interest_rate = 0.15
    investiment_period = 1
    monthly_deposit = 100000
    penalty_rate = 0.1
    
    #penalty = penalty_rate *  (monthly_deposit - actual_deposit)
    table  = handle_investiment(minimum_deposit)
    print(table)
    
    
    
    


