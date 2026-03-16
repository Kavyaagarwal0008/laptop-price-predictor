import streamlit as st
import pandas as pd
import pickle

pipe = pickle.load(open("pipeline.pkl","rb"))

st.title("Laptop Price Predictor")

# Inputs
company = st.selectbox("Company",["Dell","HP","Apple","Lenovo","Asus"])
typename = st.selectbox("Laptop Type",["Notebook","Gaming","Ultrabook","Workstation"])
ram = st.selectbox("RAM (GB)",[4,8,16,32])
weight = st.number_input("Weight (KG)")
os = st.selectbox("Operating System",["Windows","Mac","Linux"])
touch = st.selectbox("TouchScreen",[0,1])
ips = st.selectbox("IPS Display",[0,1])
ppi = st.number_input("PPI")
cpu = st.selectbox("CPU",["Intel Core i5","Intel Core i7","AMD Ryzen"])
hdd = st.selectbox("HDD (GB)",[0,500,1000,2000])
ssd = st.selectbox("SSD (GB)",[0,128,256,512,1024])
gpu = st.selectbox("GPU Brand",["Intel","Nvidia","AMD"])

if st.button("Predict Price"):

    data = pd.DataFrame({
        "Company":[company],
        "TypeName":[typename],
        "Ram_GB":[ram],
        "OpSys":[os],
        "Weight_KG":[weight],
        "TouchScreen":[touch],
        "IPS":[ips],
        "PPI":[ppi],
        "Cpu_name":[cpu],
        "HDD":[hdd],
        "SSD":[ssd],
        "Gpu_brand":[gpu]
    })

    prediction = pipe.predict(data)

    price_inr = prediction[0] * 90   # convert euro to INR

    st.success(f"Predicted Laptop Price: ₹ {price_inr:.0f}")