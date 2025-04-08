import streamlit as st
import pandas as pd
import plotly.express as px  # Of gebruik matplotlib als je wilt

# Titel van de app
st.title("Dashboard Schoenenverkoop")

# Voorbeelddata (je kunt dit vervangen door je eigen dataset)
data = {
    'Merk': ['Volvo', 'BMW', 'Audi', 'Volvo', 'BMW', 'Audi', 'Volvo'],
    'Aantal': [10, 5, 8, 6, 3, 7, 4]
}
df = pd.DataFrame(data)

# Groeperen en sommeren per merk
df_grouped = df.groupby('Merk', as_index=False)['Aantal'].sum()

# Barchart maken met Plotly
fig = px.bar(df_grouped, x='Merk', y='Aantal', color='Merk',
             title='Totaal aantal per merk',
             labels={'Aantal': 'Aantal', 'Merk': 'Merk'})

# Visual tonen in Streamlit
st.plotly_chart(fig)
