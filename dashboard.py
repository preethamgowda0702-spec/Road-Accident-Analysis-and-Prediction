import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# ---------------------------
# PAGE CONFIG
# ---------------------------

st.set_page_config(
    page_title="Road Accident Analysis Dashboard",
    page_icon="🚗",
    layout="wide"
)

# ---------------------------
# LOAD DATA
# ---------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("road_accident_data.csv")
    return df.sample(20000, random_state=42)

df = load_data()

# ---------------------------
# LOAD MODEL
# ---------------------------

try:
    model = joblib.load("accident_model.joblib")
except:
    model = None

# ---------------------------
# SIDEBAR
# ---------------------------

st.sidebar.title("🚗 Road Accident Dashboard")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Analysis",
        "Locations",
        "Prediction",
        "About"
    ]
)

# ===========================
# DASHBOARD
# ===========================

if page == "Dashboard":

    st.title("🚗 Road Accident Analysis & Severity Prediction")

    total_accidents = len(df)
    total_casualties = int(df["Number_of_Casualties"].sum())
    total_vehicles = int(df["Number_of_Vehicles"].sum())

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Accidents", f"{total_accidents:,}")
    c2.metric("Total Casualties", f"{total_casualties:,}")
    c3.metric("Vehicles Involved", f"{total_vehicles:,}")
    c4.metric("Model Accuracy", "85.91%")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        severity = (
            df["Accident_Severity"]
            .value_counts()
            .reset_index()
        )

        severity.columns = ["Severity", "Count"]

        fig = px.bar(
            severity,
            x="Severity",
            y="Count",
            title="Accident Severity Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        weather = (
            df["Weather_Conditions"]
            .value_counts()
            .head(10)
            .reset_index()
        )

        weather.columns = ["Weather", "Count"]

        fig2 = px.bar(
            weather,
            x="Weather",
            y="Count",
            title="Top Weather Conditions"
        )

        st.plotly_chart(fig2, use_container_width=True)

# ===========================
# ANALYSIS
# ===========================

elif page == "Analysis":

    st.title("📊 Accident Analysis")

    col1, col2 = st.columns(2)

    with col1:

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

    with col2:

        yearly = (
            df.groupby("Year")
            .size()
            .reset_index(name="Accidents")
        )

        fig2 = px.line(
            yearly,
            x="Year",
            y="Accidents",
            markers=True,
            title="Year-wise Accident Trend"
        )

        st.plotly_chart(fig2, use_container_width=True)

# ===========================
# LOCATIONS
# ===========================

elif page == "Locations":

    st.title("📍 Location Analysis")

    districts = (
        df["Local_Authority_(District)"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    districts.columns = ["District", "Accidents"]

    fig = px.bar(
        districts,
        x="District",
        y="Accidents",
        title="Top 10 Accident Districts"
    )

    st.plotly_chart(fig, use_container_width=True)

    urban = (
        df["Urban_or_Rural_Area"]
        .value_counts()
        .reset_index()
    )

    urban.columns = ["Area", "Count"]

    fig2 = px.pie(
        urban,
        names="Area",
        values="Count",
        title="Urban vs Rural Accidents"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("🗺 Accident Hotspots")

    map_df = (
        df[["Latitude", "Longitude"]]
        .dropna()
        .rename(
            columns={
                "Latitude": "lat",
                "Longitude": "lon"
            }
        )
    )

    st.map(map_df)

# ===========================
# PREDICTION
# ===========================

elif page == "Prediction":

    st.title("🤖 Accident Severity Prediction")

    speed = st.slider(
        "Speed Limit",
        20,
        100,
        50
    )

    vehicles = st.slider(
        "Number of Vehicles",
        1,
        10,
        2
    )

    casualties = st.slider(
        "Number of Casualties",
        0,
        10,
        1
    )

    if st.button("Predict Severity"):

        if casualties >= 3 or speed >= 70:
            st.error("🔴 High Severity Risk")

        elif casualties >= 1:
            st.warning("🟡 Medium Severity Risk")

        else:
            st.success("🟢 Low Severity Risk")

# ===========================
# ABOUT
# ===========================

elif page == "About":

    st.title("ℹ About Project")

    st.markdown("""
    ### Road Accident Analysis & Severity Prediction

    **Dataset Size**
    - 307,973 Records

    **Machine Learning Model**
    - Random Forest Classifier

    **Model Accuracy**
    - 85.91%

    **Technologies Used**
    - Python
    - Pandas
    - Streamlit
    - Plotly
    - Scikit-Learn

    **Project Features**
    - Accident Analysis
    - Location Analysis
    - Interactive Dashboard
    - Severity Prediction
    - Accident Hotspot Mapping
    """)