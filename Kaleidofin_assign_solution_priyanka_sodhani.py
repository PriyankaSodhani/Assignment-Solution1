import pandas as pd
import numpy as np

##Assuming each member can bid only once during the 25-month period.
##50,000 rupees was collected in chit fund each month


##loading dataset
##kindly put your data path while running this
data = pd.read_excel('Desktop/Assignment_1_2/chit_fund.xlsx')


##cleaning data
##renaming column names
data.columns = ['month','contribution','amt_won_bidder','commision','amt_recd_bidder','amt_given_to_each']

#assigning name to each bidder
alphabet=[]
for letter in range(65,90):
    alphabet.append(chr(letter))
data['person_who_bids'] = alphabet



#calculating all the details in this new dataframe
chit_fund = pd.DataFrame({'member' : data['person_who_bids']})
chit_fund['tot_spent'] = data['contribution'].sum()
chit_fund['tot_earned'] = data['amt_given_to_each'].sum()
chit_fund['month'] = data['month']
chit_fund['amt_recd_by_bidding'] = data['amt_recd_bidder']
chit_fund['amt_recd_this_month'] = data['amt_given_to_each']
chit_fund['net_annual_return'] = chit_fund['amt_recd_by_bidding'] + chit_fund['tot_earned'] - chit_fund['tot_spent']
chit_fund['monthly_return_%'] = (chit_fund['amt_recd_by_bidding'] + chit_fund['amt_recd_this_month'] - 2000)*100/2000

print('Details of Chit Fund')
print()
print(chit_fund)
print()
print('-'*100)

### TASK SOLUTION
print('Annualized return of member who bids last month Y is',chit_fund[chit_fund['month'] == 25]['net_annual_return'].get_value(label=24))
print()
print('Annualized return of member who bids first month A is',chit_fund[chit_fund['month'] == 1]['net_annual_return'].get_value(label=0))
print('-'*100)


#Annualized return of each chit fund participant 
#Also, return% for each month's bid winner
print('Below can be seen Net Annual return & Monthly Return % of each member')
print()
print(chit_fund[['member','net_annual_return', 'monthly_return_%']])
