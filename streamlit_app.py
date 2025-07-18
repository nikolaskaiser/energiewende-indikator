import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Energiewende-Indikator", layout="wide")

# Sidebar-Menü
menu = st.sidebar.selectbox(
    "Wähle eine Kategorie",
    ["Indikator", "Politisches Commitment", "Energie", "Klima", "Strukturwandelinvestitionen"]
)


# ---------------------
# Seite: Indikator
# ---------------------
if menu == "Indikator":
    st.title("🌍 Energiewende-Indikator – Braunkohleausstieg")
    st.markdown("Diese App zeigt den Fortschritt der Energiewende, insbesondere des Braunkohleausstiegs in Deutschland")

    data = {
        'Indikator': [
            'Kohleanteil (umgekehrt)',
            'Rückbau Kohlekapazität',
            'THG-Reduktion Energiewirtschaft',
            'Strukturwandel-Investitionen',
            'Politisches Commitment'
        ],
        'Rheinisches Revier': [60, 80, 75, 65, 90],
        'Lausitzer Revier': [30, 20, 25, 85, 70],
        'Mitteldeutsches Revier': [55, 85, 80, 40, 60]
    }
    df = pd.DataFrame(data)

    fig = go.Figure()
    for region in ['Rheinisches Revier', 'Lausitzer Revier', 'Mitteldeutsches Revier']:
        fig.add_trace(go.Scatterpolar(
            r=df[region],
            theta=df['Indikator'],
            fill='toself',
            name=region
        ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True,
        height=600
    )
    st.plotly_chart(fig)

# ---------------------
# Seite: Politisches Commitment
# ---------------------
elif menu == "Politisches Commitment":
    st.title("🗳️ Politisches Commitment")

    st.markdown("Die folgenden Meilensteine zeigen die zentralen politischen Entscheidungen zur Energiewende, insb. Braunkohleausstieg in Deutschland.")
    
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



# ---------------------
# Seite: Energie
# ---------------------
elif menu == "Energie":
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
        },
        "Berlin": {
            "Jahr": [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017],
            "Braunkohle_TWh": [0.77, 0.81, 0.76, 0.68, 0.72, 0.71, 0.74, 0.79, 0.73, 0.75, 0.68, 0.69, 0.65, 0.69, 0.33],
            "Zieljahr": 2038
        },
        "Hessen": {
            "Jahr": list(range(1990, 2024)),
            "Braunkohle_TWh": [
                0.738, 0.473, 0.153, 0.150, 0.142, 0.155, 0.167, 0.148, 0.150, 0.082, 0.093,
                0.144, 0.100, 0.058, 0.070, 0.084, 0.088, 0.100, 0.118, 0.077, 0.069, 0.073,
                0.051, 0.057, 0.076, 0.088, 0.089, 0.082, 0.062, 0.084, 0.080, 0.099, 0.089, 0.085
            ],
            "Zieljahr": 2038
        },
        "Niedersachsen": {
            "Jahr": list(range(2003, 2019)),
            "Braunkohle_TWh": [
                2.94, 2.72, 2.50, 2.22, 2.61, 2.54, 2.21, 2.31, 1.79, 2.27, 1.56, 2.83, 2.33, 1.87, 0.0, 0.0
            ],
            "Zieljahr": 2038
        },
        "Saarland": {
            "Jahr": list(range(2003, 2018)),
            "Braunkohle_TWh": [
                0.015, 0.004, 0.017, 0.014, 0.010, None, 0.001, None, None, 0.004, 0.033, 0.030, 0.014, None, None
            ],
            "Zieljahr": 2038
        },
        "Thüringen": {
            "Jahr": [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998],
            "Braunkohle_TWh": [1.30, 1.10, 1.14, 0.33, 0.13, 0.07, 0.03, 0.02],
            "Zieljahr": 2038
        }
    }
    
    # ----------------------------
    # Streamlit UI
    # ----------------------------
    st.subheader("📈 Braunkohlestromerzeugung – Regionenvergleich")
    # Deutschland gesamt berechnen
    jahre = sorted(set(j for r in region_data.values() for j in r['Jahr'] if j != 2023))  # 2023 ausschließen
    deutschland_gesamt = {'Jahr': [], 'Braunkohle_TWh': []}
    
    for jahr in jahre:
        jahr_summe = 0
        for region in region_data.values():
            if jahr in region['Jahr']:
                index = region['Jahr'].index(jahr)
                wert = region['Braunkohle_TWh'][index]
                if wert is not None:
                    jahr_summe += wert
        deutschland_gesamt['Jahr'].append(jahr)
        deutschland_gesamt['Braunkohle_TWh'].append(jahr_summe)
    
    # Füge zur Auswahl hinzu
    region_data['Deutschland gesamt'] = {
        'Jahr': deutschland_gesamt['Jahr'],
        'Braunkohle_TWh': deutschland_gesamt['Braunkohle_TWh'],
        'Zieljahr': 2030  # kannst du beliebig setzen oder None
    }

    # Bundesländer-Auswahl
    selected_regions = st.multiselect(
        "Wähle Bundesländer zum Vergleich",
        options=[r for r in region_data.keys() if r != "Deutschland gesamt"],
        default=["Nordrhein-Westfalen", "Brandenburg"]
    )
    
    # Checkbox für Deutschland gesamt
    show_deutschland = st.checkbox("Deutschland gesamt anzeigen")

    
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
    
        # Linie für Region
        fig.add_trace(go.Scatter(
            x=df['Jahr'],
            y=df['Braunkohle_TWh'],
            mode='lines+markers',
            name=region
        ))
    
        # Zieljahr-Marker setzen
        zieljahr = 2030 if region == "Nordrhein-Westfalen" else 2038
        zieltext = "NRW 2030" if region == "Nordrhein-Westfalen" else "DE 2038"
    
        fig.add_trace(go.Scatter(
            x=[zieljahr],
            y=[0],
            mode='markers+text',
            marker=dict(size=10, color='green'),
            text=[zieltext],
            textposition='top center',
            showlegend=False
        ))
    
    # Optional: Deutschland gesamt hinzufügen
    if show_deutschland:
        de_info = region_data["Deutschland gesamt"]
        df_de = pd.DataFrame({
            'Jahr': de_info['Jahr'],
            'Braunkohle_TWh': de_info['Braunkohle_TWh']
        })
    
        fig.add_trace(go.Scatter(
            x=df_de['Jahr'],
            y=df_de['Braunkohle_TWh'],
            mode='lines+markers',
            name="Deutschland gesamt"
        ))
    
        # Marker für DE 2038
        fig.add_trace(go.Scatter(
            x=[2038],
            y=[0],
            mode='markers+text',
            marker=dict(size=10, color='green'),
            text=["DE 2038"],
            textposition='top center',
            showlegend=False
        ))
    
    # Layout anpassen
    fig.update_layout(
        title='Bruttostromerzeugung aus Braunkohle im Vergleich',
        xaxis_title='Jahr',
        yaxis_title='TWh',
        legend_title='Bundesland',
        height=600
    )
    
    st.plotly_chart(fig)
    
       


    #ee anteil am verbrauch
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



# ---------------------
# Seite: Klima
# ---------------------
elif menu == "Klima":
    st.title("🌡️ Klima – CO₂-Emissionen der Stromerzeugung")
    st.markdown("Hier kannst du Emissionsdaten aus der Stromerzeugung anzeigen.")
    # Platz für Emissions-Visualisierung

    # ----------------------------
    # 📉 CO₂-Emissionen Stromerzeugung pro Bundesland
    # ----------------------------
    
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


# ---------------------
# Seite: Strukturwandelinvestitionen
# ---------------------
elif menu == "Strukturwandelinvestitionen":
    st.title("🏗️ Strukturwandel-Investitionen")
    st.markdown("Diese Seite ist noch leer und kann später ergänzt werden.")

