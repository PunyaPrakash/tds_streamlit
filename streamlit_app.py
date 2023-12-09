<<<<<<< HEAD
# largest_number_app.py
import streamlit as st

def find_largest_number(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("Find the Largest Number")

    # Input fields for the three numbers
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    # Button to find the largest number
    if st.button("Find Largest Number"):
        result = find_largest_number(num1, num2, num3)
        st.success(f"The largest number is: {result}")

if __name__ == "__main__":
    main()
=======

>>>>>>> 4a99fb8617a36d8e1fa90f0fe90449300bef7972
