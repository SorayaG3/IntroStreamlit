import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ======= Header toevoegen ========
st.title("Dashboard Schoenverkoop")

# ======= Dataset inladen ========
df = pd.read_csv("exclusieve_schoenen_verkoop_met_locatie.csv")

# ======= Filters ========
st.sidebar.header("Filters")
selected_year = st.sidebar.selectbox("Selecteer Aankoopjaar", sorted(df['aankoopdatum'].unique()))
selected_land = st.sidebar.selectbox("Selecteer Land", sorted(df['land'].unique()))

# Filter toepassen
filtered_df = df[(df['aankoopdatum'] == selected_year) & (df['land'] == selected_land)]

# ======= Tabs ========
tab1, tab2 = st.tabs(["aantal per merk", "aantal per Maand + Targetlijn"])

with tab1:
    st.subheader("Totaal aantal per merk")
    grouped_merk = filtered_df.groupby('merk', as_index=False)['aantal'].sum()
    
    fig_merk = px.bar(grouped_merk, x='merk', y='aantal', color='merk',
                      title='aantal per merk',
                      labels={'aantal': 'aantal', 'merk': 'merk'})
    
    st.plotly_chart(fig_merk, use_container_width=True)

with tab2:
    st.subheader("aantal per Maand met Targetlijn")
    grouped_maand = filtered_df.groupby('Maand', as_index=False)['aantal'].sum()
    
    # Kleurcodering per regel
    grouped_maand['Kleur'] = grouped_maand['aantal'].apply(lambda x: 'red' if x < 20 else 'green')
    
    fig_maand = go.Figure()
    fig_maand.add_trace(go.Bar(
        x=grouped_maand['aantal'],
        y=grouped_maand['Maand'],
        orientation='h',
        marker_color=grouped_maand['Kleur'],
        name='aantal'
    ))
    
    # Targetlijn toevoegen
    fig_maand.add_shape(
        type='line',
        x0=20, x1=20,
        y0=-0.5, y1=len(grouped_maand)-0.5,
        line=dict(color='blue', width=2, dash='dash'),
        name='Target'
    )

    fig_maand.update_layout(
        title='aantal per Maand met Targetlijn (20)',
        xaxis_title='aantal',
        yaxis_title='Maand',
        showlegend=False
    )

    st.plotly_chart(fig_maand, use_container_width=True)
