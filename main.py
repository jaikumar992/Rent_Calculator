#rent calculator in python - @codingwithsagar

## Inputs we need from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per unit 
# Persons living in room/flat

## Output
# Total amount you've to pay is

import streamlit as st

st.set_page_config(page_title="Rent Calculator", page_icon="🏠")

st.title("🏠 Rent Calculator")

st.markdown("Calculate how much each person needs to pay.")

rent = st.number_input("Enter total rent", min_value=0)
food = st.number_input("Enter total food expense", min_value=0)
electricity_spend = st.number_input("Enter electricity units consumed", min_value=0)
charge_per_unit = st.number_input("Enter charge per unit", min_value=0)
persons = st.number_input("Enter number of persons", min_value=1)

if st.button("Calculate"):
    total_bill = electricity_spend * charge_per_unit
    total_amount = rent + food + total_bill
    per_person = total_amount / persons

    st.success(f"Each person will pay: ₹ {round(per_person, 2)}")