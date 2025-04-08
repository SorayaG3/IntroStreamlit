import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ======= Header toevoegen ========
st.title("Dashboard Schoenverkoop")

# ======= Dataset inladen ========
df = pd.read_csv("exclusieve_schoenen_verkoop_met_locatie.csv")

st.write(df)
