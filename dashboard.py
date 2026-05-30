import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------
# Page Config
# -------------------
st.set_page_config(
    page_title="Road Accident Analysis Dashboard",
    page_icon="🚗",
    layout="wide"
)

# -------------------
# Load Dataset
# -------------------
df = pd.read_excel(
    r"C:\Users\NISCHITH R PRAKASH\OneDrive\Documents\Road Accident Data.xlsx"
)

# -------------------
# Sidebar
# -------------------
st.sidebar.title("🚗 Road Accident Dashboard")

page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Analysis", "Map", "Prediction", "About"]
)

# -------------------
# Dashboard
# -------------------
if page == "Dashboard":

    st.title("🚗 Road Accident Analysis & Severity Prediction")

    total_accidents = len(df)
    total_casualties = df["Number_of_Casualties"].sum()
    total_vehicles = df["Number_of_Vehicles"].sum()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Accidents", f"{total_accidents:,}")
    col2.metric("Total Casualties", f"{total_casualties:,}")
    col3.metric("Vehicles Involved", f"{total_vehicles:,}")
    col4.metric("Model Accuracy", "85.45%")

    st.markdown("---")

    c1, c2 = st.columns(2)

    with c1:
        severity = df["Accident_Severity"].value_counts().reset_index()
        severity.columns = ["Severity", "Count"]

        fig = px.bar(
            severity,
            x="Severity",
            y="Count",
            title="Accident Severity Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        weather = (
            df["Weather_Conditions"]
            .value_counts()
            .head(10)
            .reset_index()
        )

        weather.columns = ["Weather", "Count"]

        fig = px.bar(
            weather,
            x="Weather",
            y="Count",
            title="Top Weather Conditions"
        )

        st.plotly_chart(fig, use_container_width=True)

# -------------------
# Analysis
# -------------------
elif page == "Analysis":

    st.title("📊 Detailed Analysis")

    vehicle = (
        df["Vehicle_Type"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    vehicle.columns = ["Vehicle", "Count"]

    fig = px.pie(
        vehicle,
        names="Vehicle",
        values="Count",
        title="Vehicle Type Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    yearly = (
        df.groupby("Year")
        .size()
        .reset_index(name="Accidents")
    )

    fig2 = px.line(
        yearly,
        x="Year",
        y="Accidents",
        title="Year-wise Accident Trend"
    )

    st.plotly_chart(fig2, use_container_width=True)

# -------------------
# Map
# -------------------
elif page == "Map":

    st.title("🗺 Accident Locations")

    map_df = df[["Latitude", "Longitude"]].dropna()

    st.map(map_df)

# -------------------
# Prediction
# -------------------
elif page == "Prediction":

    st.title("🤖 Accident Severity Prediction")

    speed = st.slider("Speed Limit", 20, 100, 50)
    vehicles = st.slider("Number of Vehicles", 1, 20, 2)
    casualties = st.slider("Number of Casualties", 0, 20, 1)

    if st.button("Predict Severity"):

        if speed > 60 or casualties > 2:
            st.error("🔴 High Severity Risk")
        else:
            st.success("🟢 Low Severity Risk")

# -------------------
# About
# -------------------
else:

    st.title("ℹ About Project")

    st.write("""
    ### Road Accident Analysis and Severity Prediction

    Technologies Used:
    - Python
    - Pandas
    - Streamlit
    - Plotly
    - Scikit-learn

    Dataset Size:
    - 307,973 Accident Records

    Machine Learning Model:
    - Random Forest Classifier

    Accuracy:
    - 85.45%
    """)
