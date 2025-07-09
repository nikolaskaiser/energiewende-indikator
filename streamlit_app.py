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
regionen = list(region_data.keys())
selected_region = st.selectbox("Wähle ein Bundesland oder 'Deutschland gesamt'", ["Deutschland gesamt"] + regionen)

if selected_region == "Deutschland gesamt":
    # Alle Daten zusammenführen
    df_gesamt = pd.DataFrame()

    for region, data in region_data.items():
        df_region = pd.DataFrame({
            'Jahr': data['Jahr'],
            'Braunkohle_TWh': data['Braunkohle_TWh']
        })
        df_gesamt = pd.concat([df_gesamt, df_region], ignore_index=True)

    # Nach Jahr gruppieren und summieren
    df = df_gesamt.groupby("Jahr", as_index=False).sum()
    zieljahr = 2038  # gesetzliches Endziel
else:
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


import streamlit as st
import pandas as pd
import plotly.graph_objects as go

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
        text=[f"{region_info['Zieljahr']} Ziel"],
        textposition='top center',
        showlegend=False
    ))

fig.update_layout(
    title='Bruttostromerzeugung aus Braunkohle im Vergleich',
    xaxis_title='Jahr',
    yaxis_title='TWh',
    legend_title='Bundesland',
    height=600
)

st.plotly_chart(fig)



import streamlit as st

st.subheader("🧭 Politisches Commitment zum Kohleausstieg")

st.markdown("Die folgenden Meilensteine zeigen die zentralen politischen Entscheidungen zum Braunkohleausstieg in Deutschland.")

with st.expander("🟠 2018 – Einsetzung der Kohlekommission"):
    st.markdown("""
    - Die Bundesregierung richtet die **„Kommission für Wachstum, Strukturwandel und Beschäftigung“** ein.
    - Ziel: Einen breiten gesellschaftlichen Konsens über den Ausstieg aus der Kohleverstromung erreichen.
    - Beteiligte: Politik, Wirtschaft, Wissenschaft, Umweltverbände, Gewerkschaften.
    """)

with st.expander("🟢 2019 – Empfehlung: Ausstieg bis spätestens 2038"):
    st.markdown("""
    - Die Kommission legt ihren Abschlussbericht vor.
    - Empfiehlt einen **Kohleausstieg bis spätestens 2038**, möglichst **bis 2035**.
    - Vorgesehen: **Strukturhilfen in Höhe von 40 Milliarden Euro** für die betroffenen Regionen.
    """)

with st.expander("⚖️ 2020 – Kohleausstiegsgesetz verabschiedet"):
    st.markdown("""
    - Der Bundestag beschließt das **Kohleausstiegsgesetz**.
    - Verankert die schrittweise **Stilllegung aller Braun- und Steinkohlekraftwerke bis 2038**.
    - Enthält Vereinbarungen mit Betreibern, Entschädigungen und einen Abschaltfahrplan.
    """)

with st.expander("📉 2022 – NRW steigt bis 2030 aus (RWE-Vereinbarung)"):
    st.markdown("""
    - Das Bundeswirtschaftsministerium, die Landesregierung NRW und **RWE** einigen sich:
        - Braunkohleausstieg in **NRW wird auf 2030 vorgezogen**
        - **Fünf Dörfer** am Tagebau Garzweiler bleiben erhalten
        - Gleichzeitig: Einige Kraftwerksblöcke dürfen wegen Energiekrise **länger laufen**
    - Kein vergleichbares Commitment in Brandenburg, Sachsen oder Sachsen-Anhalt bisher.
    """)



import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ----------- Daten einlesen (angepasst an deine Excel-Struktur) -----------
df = pd.read_excel("lak-download (4).xlsx", sheet_name="LAK", skiprows=5)
df.columns = ['Land', 'Jahr', 'EE_Anteil_Prozent']
df = df.dropna(subset=['Land', 'Jahr', 'EE_Anteil_Prozent'])
df['Jahr'] = pd.to_numeric(df['Jahr'], errors='coerce').astype('Int64')
df['EE_Anteil_Prozent'] = pd.to_numeric(df['EE_Anteil_Prozent'], errors='coerce')

# ----------- Optional: Länderspezifische Ziele manuell ergänzen -----------
# Format: 'Bundesland': (Zielwert in %, Zieljahr)
laenderziele = {
    "Brandenburg": (100, 2020),
    "Schleswig-Holstein": (300, 2030),
    "Baden-Württemberg": (80, 2040),
    "Thüringen": (65, 2040),
    "Sachsen": (50, 2030),
    "Niedersachsen": (100, 2040),
    "Nordrhein-Westfalen": (None, None),  # kein offizielles Ziel
}

# ----------- Streamlit UI -----------
st.subheader("📈 Erneuerbare-Energien-Anteil am Bruttostromverbrauch")
selected = st.selectbox("Wähle ein Bundesland", sorted(df["Land"].unique()))

# Filtere Daten für das gewählte Bundesland
df_land = df[df["Land"] == selected]

# ----------- Plotly-Visualisierung -----------
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df_land["Jahr"],
    y=df_land["EE_Anteil_Prozent"],
    mode="lines+markers",
    name=f"{selected} – EE-Anteil",
    line=dict(color='seagreen')
))

# Bundesziel EEG 2030 (fix)
fig.add_trace(go.Scatter(
    x=[2030],
    y=[80],
    mode="markers+text",
    name="EEG-Ziel 2030",
    marker=dict(color='blue', size=12),
    text=["EEG 2030: 80 %"],
    textposition="top center"
))

# Optional: Länderspezifisches Ziel
ziel = laenderziele.get(selected)
if ziel and ziel[0] is not None:
    fig.add_trace(go.Scatter(
        x=[ziel[1]],
        y=[ziel[0]],
        mode="markers+text",
        name="Länderziel",
        marker=dict(color='orange', size=12),
        text=[f"{ziel[1]}: {ziel[0]} %"],
        textposition="top center"
    ))

fig.update_layout(
    title=f"Anteil Erneuerbarer Energien – {selected}",
    xaxis_title="Jahr",
    yaxis_title="Anteil (%)",
    yaxis_range=[0, max(100, df_land['EE_Anteil_Prozent'].max() + 20)],
    showlegend=True,
    height=600
)

st.plotly_chart(fig)



# ----------------------------
# 📉 CO₂-Emissionen Stromerzeugung pro Bundesland
# ----------------------------

import pandas as pd
import plotly.graph_objects as go

st.header("♻️ CO₂-Emissionen der Stromerzeugung (Ländervergleich)")
st.markdown("Quelle: LAK-Daten. Einheit: kg CO₂ pro GJ Stromerzeugung.")

# Excel einlesen (die Datei muss im gleichen Ordner liegen!)
df_co2 = pd.read_excel("co2_strom_lak.xlsx", sheet_name="LAK", skiprows=5)
df_co2.columns = ["Land", "Jahr", "CO2_kg_per_GJ"]
df_co2 = df_co2.dropna(subset=["Land", "Jahr", "CO2_kg_per_GJ"])
df_co2["Jahr"] = pd.to_numeric(df_co2["Jahr"], errors="coerce").astype("Int64")
df_co2["CO2_kg_per_GJ"] = pd.to_numeric(df_co2["CO2_kg_per_GJ"], errors="coerce")

# Auswahlfeld inkl. Deutschland-Ansicht
laender = sorted(df_co2["Land"].unique())
dropdown_options = ["Deutschland gesamt"] + laender
wahl = st.selectbox("Wähle ein Bundesland oder Gesamtansicht", dropdown_options)

# Daten für Auswahl
if wahl == "Deutschland gesamt":
    df_plot = df_co2.groupby("Jahr", as_index=False)["CO2_kg_per_GJ"].mean()
    name = "Deutschland gesamt – Ø CO₂ pro GJ"
else:
    df_plot = df_co2[df_co2["Land"] == wahl]
    name = f"{wahl} – CO₂ pro GJ"

# Plot erstellen
fig_co2 = go.Figure()

fig_co2.add_trace(go.Scatter(
    x=df_plot["Jahr"],
    y=df_plot["CO2_kg_per_GJ"],
    mode="lines+markers",
    name=name,
    line=dict(color='crimson')
))

# Zielmarke für 2035: CO₂ = 0 (Netto-Null-Stromsektor)
fig_co2.add_trace(go.Scatter(
    x=[2035],
    y=[0],
    mode='markers+text',
    name='EEG-Ziel 2035',
    marker=dict(color='green', size=12),
    text=["Ziel: klimaneutral"],
    textposition='top center'
))

fig_co2.update_layout(
    title=f"CO₂-Intensität der Stromerzeugung – {wahl}",
    xaxis_title="Jahr",
    yaxis_title="kg CO₂ pro GJ",
    yaxis_range=[0, max(200, df_plot['CO2_kg_per_GJ'].max() + 10)],
    height=600,
    showlegend=True
)

st.plotly_chart(fig_co2)
