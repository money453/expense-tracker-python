import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Expense Tracker", layout="wide")

st.title("💸 Expense Tracker App")

if "expenses" not in st.session_state:
    st.session_state.expenses = []

st.subheader("➕ Add New Expense")
with st.form("expense_form"):
    date = st.date_input("Date")
    category = st.selectbox("Category", ["Food", "Transport", "Shopping", "Bills", "Other"])
    amount = st.number_input("Amount", min_value=0.0, step=0.5)
    note = st.text_input("Note (optional)")
    submitted = st.form_submit_button("Add Expense")
    if submitted:
        st.session_state.expenses.append({"Date": date, "Category": category, "Amount": amount, "Note": note})
        st.success("Expense added!")

if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)
    st.subheader("📋 All Expenses")
    st.dataframe(df)

    total = df["Amount"].sum()
    st.markdown(f"### 💰 Total Spent: ₹ {total}")

    st.subheader("📊 Expenses by Category")
    fig = px.pie(df, names="Category", values="Amount", title="Spending Breakdown")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No expenses added yet.")
