import streamlit as st

st.write('Hello Python Streamlit')

x = st.text_input('favorite Book')
st.write(f"your favorite Book is : {x}")

is_validated = st.button('Valider')


st.write("this is a h2 title ")
st.markdown("*streamlit* is **really** ***cool***.")
st.markdown(''' :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text''')
st.markdown("here's a bouquet & mdash; \:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
multi = '''if you end a line with two spaces , a soft return is used for the next line .
Two (or more) newline characters in a row will result in a hard return.  '''
st.markdown(multi)

import  pandas as pd
data = pd.read_csv("movies.csv")
st.write(data)

import numpy as np
chart_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=["a","b","c"])
st.bar_chart(chart_data)
st.line_chart(chart_data)

import matplotlib.pyplot as plt
import math
st.title("Mortgage Repayements calculator")
st.write("### Input Data")
col1,col2= st.columns(2)
home_value=col1.number_input("Home value", min_value=0, value=500000)
deposit = col1.number_input("Deposit",min_value=0,value=100000)
interest_rate=col2.number_input("Interest Rate (in %)",min_value=0.0,
                                value=5.5)
loan_term=col2.number_input("loan term(in years)",min_value=1,value=30)

# Calculate the repayments.
loan_amount = home_value - deposit
monthly_interest_rate = (interest_rate / 100) / 12
number_of_payments = loan_term * 12
monthly_payment = (
    loan_amount
    * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
    / ((1 + monthly_interest_rate) ** number_of_payments - 1)
)

# Display the repayments.
total_payments = monthly_payment * number_of_payments
total_interest = total_payments - loan_amount

st.write("### Repayments")
col1, col2, col3 = st.columns(3)    # Create 3 columns
col1.metric(label="Monthly Repayments", value=f"${monthly_payment:,.2f}")
col2.metric(label="Total Repayments", value=f"${total_payments:,.0f}")
col3.metric(label="Total Interest", value=f"${total_interest:,.0f}")


# Create a data-frame with the payment schedule.
schedule = []
remaining_balance = loan_amount

for i in range(1, number_of_payments + 1):
    interest_payment = remaining_balance * monthly_interest_rate
    principal_payment = monthly_payment - interest_payment
    remaining_balance -= principal_payment
    year = math.ceil(i / 12)  # Calculate the year into the loan
    schedule.append(
        [
            i,
            monthly_payment,
            principal_payment,
            interest_payment,
            remaining_balance,
            year,
        ]
    )

df = pd.DataFrame(
    schedule,
    columns=["Month", "Payment", "Principal", "Interest", "Remaining Balance", "Year"],
)

# Display the data-frame as a chart.
st.write("### Payment Schedule")
payments_df = df[["Year", "Remaining Balance"]].groupby("Year").min()
st.line_chart(payments_df)

