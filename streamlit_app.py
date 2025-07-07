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



# Daten für Sachsen – bereinigt aus deiner Datei (in TWh)
data_sn = {
    'Jahr': [
        1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000,
        2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
        2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018,
        2019, 2020, 2021, 2022
    ],
    'Braunkohle_TWh': [
        40.43, 34.09, 32.94, 33.40, 32.39, 30.43, 29.54, 28.78, 27.61, 25.77, 25.33,
        24.26, 25.89, 26.89, 26.59, 25.10, 26.55, 26.46, 26.13, 21.39,
        23.97, 25.59, 25.25, 25.31, 26.39, 26.61, 24.85, 22.80, 21.94,
        18.83, 19.42, 19.74, 17.20
    ]
}

df_sn = pd.DataFrame(data_sn)

# Visualisierung für Sachsen
st.subheader("📉 Bruttostromerzeugung aus Braunkohle – Sachsen")
st.markdown("Ziel: **0 TWh bis spätestens 2038** gemäß Kohleausstiegsgesetz.")

fig_sn = go.Figure()

fig_sn.add_trace(go.Scatter(
    x=df_sn['Jahr'],
    y=df_sn['Braunkohle_TWh'],
    mode='lines+markers',
    name='Sachsen – Braunkohle',
    line=dict(color='indigo')
))

# Zielpunkt für 2038
fig_sn.add_trace(go.Scatter(
    x=[2038],
    y=[0],
    mode='markers+text',
    name='Ziel 2038',
    marker=dict(color='green', size=12),
    text=["Ziel: 0 TWh"],
    textposition='top center'
))

fig_sn.update_layout(
    title='Bruttostromerzeugung aus Braunkohle in Sachsen (1990–2022)',
    xaxis_title='Jahr',
    yaxis_title='TWh',
    showlegend=True
)

st.plotly_chart(fig_sn)



# Daten für Sachsen-Anhalt – bereinigt aus deiner Datei (in TWh)
data_st = {
    'Jahr': [
        1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999,
        2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
        2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017,
        2018, 2019, 2020, 2021, 2022
    ],
    'Braunkohle_TWh': [
        4.83, 3.48, 2.18, 2.24, 2.18, 2.36, 2.31, 2.36, 2.25,
        2.26, 2.18, 2.33, 2.28, 2.15, 2.04, 2.15, 2.18, 2.01,
        1.78, 2.03, 2.08, 2.02, 1.99, 1.89, 1.87, 1.79, 1.72,
        1.58, 1.59, 1.28, 1.36, 1.15
    ]
}

df_st = pd.DataFrame(data_st)

# Visualisierung für Sachsen-Anhalt
st.subheader("📉 Bruttostromerzeugung aus Braunkohle – Sachsen-Anhalt")
st.markdown("Ziel: **0 TWh bis spätestens 2038** laut Kohleausstiegsgesetz.")

fig_st = go.Figure()

fig_st.add_trace(go.Scatter(
    x=df_st['Jahr'],
    y=df_st['Braunkohle_TWh'],
    mode='lines+markers',
    name='Sachsen-Anhalt – Braunkohle',
    line=dict(color='darkorange')
))

# Zielpunkt für 2038
fig_st.add_trace(go.Scatter(
    x=[2038],
    y=[0],
    mode='markers+text',
    name='Ziel 2038',
    marker=dict(color='green', size=12),
    text=["Ziel: 0 TWh"],
    textposition='top center'
))

fig_st.update_layout(
    title='Bruttostromerzeugung aus Braunkohle in Sachsen-Anhalt (1991–2022)',
    xaxis_title='Jahr',
    yaxis_title='TWh',
    showlegend=True
)

st.plotly_chart(fig_st)




# ----------------------------
# Alle Daten als Dictionary
# ----------------------------
region_data = {
    'Nordrhein-Westfalen': {
        'Jahr': list(range(1990, 2023)),
        'Braunkohle_TWh': [
            72.8, 75.3, 77.8, 73.5, 75.3, 71.9, 73.0, 74.2, 75.4, 74.5, 74.7, 70.9, 73.8, 74.0, 73.1,
            71.2, 75.5, 74.3, 75.4, 66.5, 70.3, 73.6, 72.2, 70.4, 72.0, 75.0, 69.4, 66.5, 65.0, 52.3,
            41.5, 46.1, 38.3
        ],
        'Zieljahr': 2030
    },
    'Brandenburg': {
        'Jahr': list(range(2003, 2023)),
        'Braunkohle_TWh': [
            34.67, 35.85, 35.67, 33.92, 35.04, 33.48, 28.90, 32.89,
            32.32, 30.76, 28.51, 30.54, 29.81, 26.69, 25.59, 24.71,
            22.91, 19.44, 20.47, 17.95
        ],
        'Zieljahr': 2038
    },
    'Sachsen': {
        'Jahr': list(range(1990, 2023)),
        'Braunkohle_TWh': [
            40.43, 34.09, 32.94, 33.40, 32.39, 30.43, 29.54, 28.78, 27.61, 25.77, 25.33,
            24.26, 25.89, 26.89, 26.59, 25.10, 26.55, 26.46, 26.13, 21.39,
            23.97, 25.59, 25.25, 25.31, 26.39, 26.61, 24.85, 22.80, 21.94,
            18.83, 19.42, 19.74, 17.20
        ],
        'Zieljahr': 2038
    },
    'Sachsen-Anhalt': {
        'Jahr': list(range(1991, 2023)),
        'Braunkohle_TWh': [
            4.83, 3.48, 2.18, 2.24, 2.18, 2.36, 2.31, 2.36, 2.25,
            2.26, 2.18, 2.33, 2.28, 2.15, 2.04, 2.15, 2.18, 2.01,
            1.78, 2.03, 2.08, 2.02, 1.99, 1.89, 1.87, 1.79, 1.72,
            1.58, 1.59, 1.28, 1.36, 1.15
        ],
        'Zieljahr': 2038
    }
}

# ----------------------------
# Streamlit UI
# ----------------------------
st.subheader("📊 Vergleich: Braunkohlestromerzeugung nach Bundesland")
selected_region = st.selectbox("Wähle ein Bundesland", list(region_data.keys()))

# Daten auswählen
region = region_data[selected_region]
df = pd.DataFrame({
    'Jahr': region['Jahr'],
    'Braunkohle_TWh': region['Braunkohle_TWh']
})
zieljahr = region['Zieljahr']

# ----------------------------
# Plotly-Grafik
# ----------------------------
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['Jahr'],
    y=df['Braunkohle_TWh'],
    mode='lines+markers',
    name=f'{selected_region} – Braunkohle'
))

fig.add_trace(go.Scatter(
    x=[zieljahr],
    y=[0],
    mode='markers+text',
    name=f'Ziel {zieljahr}',
    marker=dict(color='green', size=12),
    text=[f"Ziel: 0 TWh"],
    textposition='top center'
))

fig.update_layout(
    title=f'Bruttostromerzeugung aus Braunkohle – {selected_region}',
    xaxis_title='Jahr',
    yaxis_title='TWh',
    showlegend=True
)

st.plotly_chart(fig)


# ----------------------------
# Alle Daten
# ----------------------------
region_data = {
    'Nordrhein-Westfalen': {
        'Jahr': list(range(1990, 2023)),
        'Braunkohle_TWh': [
            72.8, 75.3, 77.8, 73.5, 75.3, 71.9, 73.0, 74.2, 75.4, 74.5, 74.7, 70.9, 73.8, 74.0, 73.1,
            71.2, 75.5, 74.3, 75.4, 66.5, 70.3, 73.6, 72.2, 70.4, 72.0, 75.0, 69.4, 66.5, 65.0, 52.3,
            41.5, 46.1, 38.3
        ],
        'Zieljahr': 2030
    },
    'Brandenburg': {
        'Jahr': list(range(2003, 2023)),
        'Braunkohle_TWh': [
            34.67, 35.85, 35.67, 33.92, 35.04, 33.48, 28.90, 32.89,
            32.32, 30.76, 28.51, 30.54, 29.81, 26.69, 25.59, 24.71,
            22.91, 19.44, 20.47, 17.95
        ],
        'Zieljahr': 2038
    },
    'Sachsen': {
        'Jahr': list(range(1990, 2023)),
        'Braunkohle_TWh': [
            40.43, 34.09, 32.94, 33.40, 32.39, 30.43, 29.54, 28.78, 27.61, 25.77, 25.33,
            24.26, 25.89, 26.89, 26.59, 25.10, 26.55, 26.46, 26.13, 21.39,
            23.97, 25.59, 25.25, 25.31, 26.39, 26.61, 24.85, 22.80, 21.94,
            18.83, 19.42, 19.74, 17.20
        ],
        'Zieljahr': 2038
    },
    'Sachsen-Anhalt': {
        'Jahr': list(range(1991, 2023)),
        'Braunkohle_TWh': [
            4.83, 3.48, 2.18, 2.24, 2.18, 2.36, 2.31, 2.36, 2.25,
            2.26, 2.18, 2.33, 2.28, 2.15, 2.04, 2.15, 2.18, 2.01,
            1.78, 2.03, 2.08, 2.02, 1.99, 1.89, 1.87, 1.79, 1.72,
            1.58, 1.59, 1.28, 1.36, 1.15
        ],
        'Zieljahr': 2038
    }
}

# ----------------------------
# Streamlit UI
# ----------------------------
st.subheader("📈 Braunkohlestromerzeugung – Regionenvergleich")
selected_regions = st.multiselect(
    "Wähle Bundesländer zum Vergleich",
    options=list(region_data.keys()),
    default=["Nordrhein-Westfalen", "Brandenburg"]
)

# ----------------------------
# Plot erstellen
# ----------------------------
fig = go.Figure()

for region in selected_regions:
    region_info = region_data[region]
    df = pd.DataFrame({
        'Jahr': region_info['Jahr'],
        'Braunkohle_TWh': region_info['Braunkohle_TWh']
    })
    
    fig.add_trace(go.Scatter(
        x=df['Jahr'],
        y=df['Braunkohle_TWh'],
        mode='lines+markers',
        name=region
    ))

    # Zieljahr markieren
    fig.add_trace(go.Scatter(
        x=[region_info['Zieljahr']],
        y=[0],
        mode='markers+text',
        marker=dict(size=10, color='green'),
        text=[f"{region_info['Zieljahr']} Ziel_]()

)

st.plotly_chart(fig)

