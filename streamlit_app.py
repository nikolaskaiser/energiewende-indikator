# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Beispiel-Daten für die drei Reviere
data = {
    'Indikator': [
        'Kohleanteil (umgekehrt)',  # 100 = kein Kohleanteil mehr
        'Rückbau Kohlekapazität',
        'THG-Reduktion Energiewirtschaft',
        'Strukturwandel-Investitionen',
        'Politisches Commitment'
    ],
    'Rheinisches Revier': [60, 80, 75, 65, 90],
    'Lausitzer Revier': [30, 20, 25, 85, 70],
    'Mitteldeutsches Revier': [55, 85, 80, 40, 60]
}

# In DataFrame umwandeln
df = pd.DataFrame(data)

# Streamlit App
st.set_page_config(page_title="Energiewende-Indikator", layout="centered")
st.title("🌍 Energiewende-Indikator – Kohleausstieg in den drei Revieren")
st.markdown("Diese App zeigt den Fortschritt der drei Braunkohlereviere in fünf Indikatorfeldern.")

# Radar-Chart erstellen
fig = go.Figure()

for region in ['Rheinisches Revier', 'Lausitzer Revier', 'Mitteldeutsches Revier']:
    fig.add_trace(go.Scatterpolar(
        r=df[region],
        theta=df['Indikator'],
        fill='toself',
        name=region
    ))

# Layout anpassen
fig.update_layout(
    polar=dict(
        radialaxis=dict(visible=True, range=[0, 100])
    ),
    showlegend=True
)

# Plot anzeigen
st.plotly_chart(fig)

st.caption("Interaktive Visualisierung eines MVP-Indikators für den Kohleausstieg auf Revierebene.")


# Daten für NRW Braunkohle-Stromerzeugung (TWh)
braunkohle_data = {
    'Jahr': [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005,
             2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
    'Braunkohle_TWh': [72.8, 75.3, 77.8, 73.5, 75.3, 71.9, 73.0, 74.2, 75.4, 74.5, 74.7, 70.9, 73.8, 74.0, 73.1,
                       71.2, 75.5, 74.3, 75.4, 66.5, 70.3, 73.6, 72.2, 70.4, 72.0, 75.0, 69.4, 66.5, 65.0, 52.3,
                       41.5, 46.1, 38.3]  # gerundet
}

braunkohle_df = pd.DataFrame(braunkohle_data)

# Neue Section
st.subheader("📉 Entwicklung der Bruttostromerzeugung aus Braunkohle in NRW")
st.markdown("Ziel: Reduktion auf **0 TWh bis 2030** laut Vereinbarung mit RWE (2022).")

# Plotly-Linienchart
fig2 = go.Figure()

# Linie für Stromerzeugung
fig2.add_trace(go.Scatter(
    x=braunkohle_df['Jahr'],
    y=braunkohle_df['Braunkohle_TWh'],
    mode='lines+markers',
    name='Braunkohlestrom NRW',
    line=dict(color='firebrick')
))

# Zielmarke für 2030
fig2.add_trace(go.Scatter(
    x=[2030],
    y=[0],
    mode='markers+text',
    name='Ziel 2030',
    marker=dict(color='green', size=12),
    text=["Ziel: 0 TWh"],
    textposition='top center'
))

fig2.update_layout(
    xaxis_title='Jahr',
    yaxis_title='TWh',
    title='Bruttostromerzeugung aus Braunkohle in NRW (1990–2022) mit Ziel 2030',
    showlegend=True
)

st.plotly_chart(fig2)


# Daten für Brandenburg (aus deiner Datei bereinigt, in TWh)
data_bb = {
    'Jahr': [
        2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
        2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018,
        2019, 2020, 2021, 2022
    ],
    'Braunkohle_TWh': [
        34.67, 35.85, 35.67, 33.92, 35.04, 33.48, 28.90, 32.89,
        32.32, 30.76, 28.51, 30.54, 29.81, 26.69, 25.59, 24.71,
        22.91, 19.44, 20.47, 17.95
    ]
}

df_bb = pd.DataFrame(data_bb)

# Visualisierung
st.subheader("📉 Bruttostromerzeugung aus Braunkohle – Brandenburg")
st.markdown("Ziel: Reduktion auf **0 TWh bis spätestens 2038** laut Kohleausstiegsgesetz.")

fig_bb = go.Figure()

fig_bb.add_trace(go.Scatter(
    x=df_bb['Jahr'],
    y=df_bb['Braunkohle_TWh'],
    mode='lines+markers',
    name='Brandenburg – Braunkohle',
    line=dict(color='darkblue')
))

# Zielpunkt für 2038 (0 TWh)
fig_bb.add_trace(go.Scatter(
    x=[2038],
    y=[0],
    mode='markers+text',
    name='Ziel 2038',
    marker=dict(color='green', size=12),
    text=["Ziel: 0 TWh"],
    textposition='top center'
))

fig_bb.update_layout(
    title='Bruttostromerzeugung aus Braunkohle in Brandenburg (2003–2022)',
    xaxis_title='Jahr',
    yaxis_title='TWh',
    showlegend=True
)

st.plotly_chart(fig_bb)
