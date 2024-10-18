import streamlit as st

def main():
    st.title("Simple Web Form")

    # Dropdown for the first selection
    option1 = st.selectbox(
        'Select Option 1:',
        ['Standard 35mm', 'Fully Sealed 37mm']
    )

    # Dropdown for the second selection
    option2 = st.selectbox(
        'Select Option 2:',
        ['Option 2A', 'Option 2B', 'Option 2C']
    )

    # Submit button
    if st.button('Submit'):
        st.success(f'Selected Value 1: {option1}, Selected Value 2: {option2}')

if __name__ == "__main__":
    main()
