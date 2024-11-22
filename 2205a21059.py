import streamlit as st

st.title("2205a21059-PS10")

# Function to compute CUL and Efficiency
def Gen_Eff(V, CL, IL, K, Rse, Ra):
    CUL = ((K * IL) ** 2) * (Rse + Ra)
    Eff = (((K * V * IL) / ((K * V * IL) + CL + CUL)) * 100)
    return CUL, Eff

# Input and output section
col1, col2 = st.columns(2)

with col1:
    st.subheader("Input Parameters")
    V = st.number_input("V (in volts)", value=230)
    IL = st.number_input("IL (in amps)", value=100)
    Rse = st.number_input("Rse (in ohms)", value=0.5)
    Ra = st.number_input("Ra (in ohms)", value=0.2)

with col2:
    CL = st.number_input("CL (in watts)", value=50)
    K = st.number_input("Constant (K)", value=0.8)
    compute = st.button("Compute")

# Output section
if compute:
    st.subheader("Output Parameters")
    CUL, Eff = Gen_Eff(V, CL, IL, K, Rse, Ra)
    st.write(f"CUL = {CUL:.2f} Watts")
    st.write(f"Efficiency = {Eff:.2f}%")