import streamlit as st

def main():
    st.title("PAFD Configurator")

    # Dropdown for the first selection
    option1 = st.selectbox(
        'Door Thickness:',
        ['Standard', 'Fully Sealed',]
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
