import streamlit as st

def interest(apr, balance):
    month_interest = apr/12
    month_amount_interest = balance * month_interest
    return month_amount_interest

def stock_growth(starting_amount, returns):
    returns = starting_amount * returns
    total_amount = returns + starting_amount
    return returns, total_amount

def annual_ammortization(apr, debt_amount, min_payment):
    interest_amount = 0
    for i in range(12):
        interest_amount += interest(apr,debt_amount)
        debt_amount -= min_payment        
    return interest_amount, debt_amount

def total_amount_paid(interest_paid, debt_total, debt_outstanding):
    amount = interest_paid + (debt_total - debt_outstanding) + debt_outstanding
    return amount

st.set_page_config(page_title='Debt vs Investment', layout='centered', initial_sidebar_state='collapsed')
main_container = st.beta_container()

main_container.title('12-Month Debt vs Investment Calculator')

debt_amount = main_container.number_input('Enter Amount of Debt', min_value=0.00, max_value=1000000000000.00, value=1000.00)
apr = main_container.number_input('Enter Yearly Credit Card APR (as a percent, ex. 10.12%)', min_value=0.00, max_value=50.00, value=14.65)
min_payment = main_container.number_input('Enter Minimum Credit Card Payment', min_value=0.00, max_value=1000000000000.00, value=25.00)

main_container.write('#')
investment_amount = main_container.number_input('Enter Investment Amount', min_value=0.00, max_value=1000000000000.00, value=1000.00)
stock_returns = main_container.number_input('Enter Yearly Stock Return (as a percent, ex. 10.12%)', min_value=0.00, max_value=1000.00, value=10.02)

interest_amount, debt_outstanding = annual_ammortization(apr=apr/100, debt_amount=debt_amount, min_payment=min_payment)
returns, total_amount = stock_growth(starting_amount=investment_amount, returns=stock_returns/100)
amount = total_amount_paid(interest_paid=interest_amount, debt_total=debt_amount, debt_outstanding=debt_outstanding)

main_container.write('#')
main_container.write('Amound paid at the end of the 12 months.')
main_container.write('Total Amount Paid: ${}'.format(round(amount,2)))
main_container.write('Total Investment Returns: ${}'.format(round(total_amount,2)))
main_container.write('Investment less debt: ${}'.format(round(total_amount-amount,2)))

main_container.write(''' 
                     **Assumptions**
                     - Credit card payments are the minimum permitted.
                     - No increasing credit card payments.
                     - No increasing investment amount.
                     - Average lifetime returns of SPY.
                     - Average APR according to the FED.
                     - All debt is paid at the end of the 12 months.
                     ''')