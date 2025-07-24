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
    
    with st.expander("🌍 2015 – Pariser Klimaabkommen"):
        st.markdown("""
        - Internationales Abkommen zur Begrenzung der globalen Erwärmung auf **unter 2 °C**, möglichst **1,5 °C**.
        - Deutschland verpflichtet sich zur **Treibhausgasneutralität bis 2050**.
        - Grundlage für viele spätere nationale Klimaschutzgesetze und Ausstiegsstrategien.
        """)

    with st.expander("⚡ 2000 / 2021 / 2023 – Erneuerbare-Energien-Gesetz (EEG)"):
        st.markdown("""
        - Seit 2000: Einführung der **Einspeisevergütung** und Vorrang für erneuerbare Energien im Netz.
        - EEG 2021: Ziel von **mind. 65 % Erneuerbare am Bruttostromverbrauch bis 2030**.
        - EEG 2023: Ziel verschärft auf **mind. 80 % bis 2030**.
        """)

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

    with st.expander("📜 2019 – Klimaschutzgesetz verabschiedet"):
        st.markdown("""
        - Erstes deutsches Gesetz mit **verbindlichen CO₂-Reduktionszielen für einzelne Sektoren** (z. B. Energie, Verkehr, Gebäude).
        - Langfristiges Ziel: **Klimaneutralität bis 2050**.
        - Jährliche Zielüberprüfung durch Expertenrat für Klimafragen.
        """)

    with st.expander("🔌 2011 / 2019 – Netzausbaubeschleunigungsgesetz (NABEG)"):
        st.markdown("""
        - Ziel: **Beschleunigung des Stromnetzausbaus**, v. a. Nord–Süd-Trassen (HGÜ).
        - Einführung vereinfachter Genehmigungsverfahren, **Erdverkabelung als Standard**.
        - **Bis 2030 sollen rund 14.000 km Stromleitungen neu- oder ausgebaut** werden.
        """)

    with st.expander("⚖️ 2020 – Kohleausstiegsgesetz verabschiedet"):
        st.markdown("""
        - Der Bundestag beschließt das **Kohleausstiegsgesetz**.
        - Verankert die schrittweise **Stilllegung aller Braun- und Steinkohlekraftwerke bis 2038**.
        - Enthält Vereinbarungen mit Betreibern, Entschädigungen und einen Abschaltfahrplan.
        """)

    with st.expander("🏗️ 2020 – Strukturstärkungsgesetz Kohleregionen"):
        st.markdown("""
        - Parallel zum Kohleausstiegsgesetz verabschiedet.
        - Regelt die Verteilung von **bis zu 40 Milliarden Euro** Strukturhilfen bis 2038:
            - **14 Mrd. €** direkte Bundesinvestitionen (z. B. Forschungseinrichtungen, Infrastruktur)
            - **26 Mrd. €** Förderprogramme, von den Ländern eigenständig umgesetzt
        - Zielregionen: **Lausitz, Mitteldeutsches Revier, Rheinisches Revier**
        """)

    with st.expander("🧠 2016 – Gesetz zur Digitalisierung der Energiewende"):
        st.markdown("""
        - Rechtsrahmen für den bundesweiten **Smart-Meter-Rollout**.
        - Verpflichtet Netzbetreiber, Versorger und größere Verbraucher zu **intelligenten Messsystemen**.
        - Ziel: **80 % aller Haushalte sollen bis 2030 mit Smart Metern ausgestattet** sein.
        """)

    with st.expander("⚖️ 2021 – Urteil des Bundesverfassungsgerichts & Gesetzesnovelle"):
        st.markdown("""
        - Das Bundesverfassungsgericht erklärt Teile des Klimaschutzgesetzes für **verfassungswidrig** (unzureichender Schutz künftiger Generationen).
        - Bundesregierung verschärft daraufhin die Klimaziele:
            - **Klimaneutralität bis 2045**
            - **65 % weniger Treibhausgase bis 2030** im Vergleich zu 1990
        """)

    with st.expander("📶 2021 / 2023 – Novellen des Energiewirtschaftsgesetzes (EnWG)"):
        st.markdown("""
        - Einführung des **Smart-Meter-Gateways** als sichere Kommunikationsplattform.
        - Start von **Redispatch 2.0**: Netzbetreiber dürfen Erzeugung und Verbrauch aktiv steuern.
        - Bereits über **50.000 Erzeugungsanlagen** beteiligt (2023).
        - Ziel: Reduktion von Netzengpässen und **minimierte Redispatch-Kosten** (2022: ca. 2,7 Mrd. €).
        """)

    with st.expander("📉 2022 – NRW steigt bis 2030 aus (RWE-Vereinbarung)"):
        st.markdown("""
        - Das Bundeswirtschaftsministerium, die Landesregierung NRW und **RWE** einigen sich:
            - Braunkohleausstieg in **NRW wird auf 2030 vorgezogen**
            - **Fünf Dörfer** am Tagebau Garzweiler bleiben erhalten
            - Gleichzeitig: Einige Kraftwerksblöcke dürfen wegen Energiekrise **länger laufen**
        - Kein vergleichbares Commitment in Brandenburg, Sachsen oder Sachsen-Anhalt bisher.
        """)

    with st.expander("💶 2023 – Klima- und Transformationsfonds (KTF)"):
        st.markdown("""
        - Der Fonds bündelt staatliche Investitionen für Klimaschutz, Energiewende und Industrie-Transformation.
        - **Volumen: ca. 177 Milliarden Euro bis 2027**.
        - Förderung z. B. von Wasserstofftechnologien, Industrie-Dekarbonisierung, E-Mobilität, Gebäudesanierung.
        """)

    with st.expander("🔋 2023 – EEG-Erleichterungen für Stromspeicher"):
        st.markdown("""
        - Speichertechnologien werden regulatorisch besser gestellt.
        - Befreiung von EEG-Umlagen bei reinem Zwischenspeichern.
        - Laut Bundesregierung sollen **bis 2030 rund 24 GW Flexibilität** (u. a. durch Speicher) bereitgestellt werden.
        - Installierte Leistung (2024): bereits **ca. 7–8 GW**, stark wachsend.
        """)



# ---------------------
# Seite: Energie
# ---------------------
elif menu == "Energie":
    import streamlit as st
    import pandas as pd
    import plotly.graph_objects as go
    
    # Aktualisierte Daten mit korrekten Jahren
    df = pd.DataFrame({
        "Jahr": [1989, 1990, 1995, 2000, 2005, 2010, 2015, 2019, 2020, 2021, 2022, 2023, 2024],
        "Bruttostrom_TWh": [559.9, 549.9, 536.8, 576.6, 622.7, 632.8, 647.0,
                            608.2, 574.7, 587.1, 577.9, 511.3, 497.3],
        "Braunkohle_TWh": [180.4, 170.9, 142.6, 148.3, 154.1, 145.9, 154.5,
                           114.0, 91.7, 110.1, 116.2, 86.3, 79.2],
        "Braunkohle_Anteil_%": [32.2, 31.1, 26.6, 25.7, 24.7, 23.1, 23.9,
                                18.7, 16.0, 18.8, 20.1, 16.9, 15.9]
    })
    
    zieljahr = 2038
    
    # Plot erstellen
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=df["Jahr"],
        y=df["Braunkohle_TWh"],
        name="Braunkohle-Strom (TWh)",
        marker_color="firebrick",
        yaxis="y1"
    ))
    
    fig.add_trace(go.Scatter(
        x=df["Jahr"],
        y=df["Braunkohle_Anteil_%"],
        mode="lines+markers",
        name="Braunkohle-Anteil (%)",
        line=dict(color="royalblue", width=3, dash="dash"),
        yaxis="y2"
    ))
    
    fig.add_trace(go.Scatter(
        x=[zieljahr],
        y=[0],
        mode="markers+text",
        name=f"Ziel {zieljahr}",
        marker=dict(color="green", size=12),
        text=["Ziel: 0 TWh"],
        textposition="top center",
        yaxis="y1"
    ))
    
    fig.update_layout(
        title="Braunkohlestrom in Deutschland (1989–2024) – absolut & relativ",
        xaxis=dict(title="Jahr"),
        yaxis=dict(title="Braunkohle-Strom (TWh)", side="left", showgrid=False),
        yaxis2=dict(title="Anteil Braunkohle (%)", overlaying="y", side="right",
                    showgrid=False, range=[0, max(df["Braunkohle_Anteil_%"]) + 5]),
        barmode='group',
        legend=dict(x=0.01, y=1.1, orientation="h"),
        height=600
    )
    
    # In Streamlit anzeigen
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
    
    #
    #ee anteil am verbrauch
    #
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

    #
    #Abraum
    #
    import streamlit as st
    import pandas as pd
    import plotly.graph_objects as go
    
    # Daten definieren
    jahre = [1989, 1990, 1995, 2000, 2005, 2010, 2015, 2019, 2020, 2021, 2022, 2023, 2024]
    
    data = {
        "Rheinland": [427.3, 433.5, 543.3, 445.7, 454.5, 469.1, 446.1, 355.3, 306.3, 247.3, 235.5, 201.7, 191.2],
        "Helmstedt": [12.7, 12.1, 11.8, 15.6, 14.4, 6.8, 1.1, None, None, None, None, None, None],
        "Hessen":    [3.5, 2.3, 0.6, 0.5, None, None, None, None, None, None, None, None, None],
        "Lausitz":   [939.4, 827.1, 375.3, 341.0, 417.9, 406.3, 370.5, 329.6, 265.1, 274.6, 302.5, 283.4, 219.0],
        "Mitteldeutschland": [397.6, 312.8, 37.3, 45.6, 75.6, 66.6, 70.1, 53.8, 42.1, 45.6, 52.9, 51.0, 39.9],
        "Summe":     [1780.5, 1587.9, 968.4, 848.4, 962.5, 948.8, 887.8, 738.8, 613.6, 567.5, 590.925, 536.1, 450.1]
    }
    
    df_abraum = pd.DataFrame(data, index=jahre).reset_index().rename(columns={"index": "Jahr"})
    
    # Revierauswahl
    st.title("Abraum-Mengen in deutschen Braunkohlerevieren (1989–2024)")
    auswahl = st.multiselect("Wähle ein oder mehrere Reviere", options=df_abraum.columns[1:], default=["Summe"])
    
    # Plotly-Grafik
    fig = go.Figure()
    for revier in auswahl:
        fig.add_trace(go.Scatter(
            x=df_abraum["Jahr"],
            y=df_abraum[revier],
            mode="lines+markers",
            name=revier
        ))
    
    # Layout
    fig.update_layout(
        title="Abraum-Menge nach Revier (in Mio. m³)",
        xaxis_title="Jahr",
        yaxis_title="Abraum [Mio. m³]",
        legend=dict(x=0.01, y=1.1, orientation="h"),
        height=600
    )
    
    st.plotly_chart(fig)

    #
    #Fördermenge Braunkohle
    #
    import streamlit as st
    import pandas as pd
    import plotly.graph_objects as go
    
    # Jahresreihe
    jahre = [1989, 1990, 1995, 2000, 2005, 2010, 2015, 2019, 2020, 2021, 2022, 2023, 2024]
    
    # Förderdaten in Mio. Tonnen
    foerderung_data = {
        "Rheinland": [104.2, 102.2, 100.2, 91.9, 97.3, 90.7, 95.2, 64.8, 51.4, 62.6, 65.3, 48.2, 43.9],
        "Helmstedt": [4.4, 4.3, 4.1, 4.1, 2.1, 2.0, 1.5, None, None, None, None, None, None],
        "Hessen": [1.2, 1.0, 0.2, 0.2, None, None, None, None, None, None, None, None, None],
        "Bayern": [0.1, 0.1, 0.0, 0.0, 0.0, None, None, None, None, None, None, None, None],
        "Lausitz": [195.1, 168.0, 70.7, 55.0, 59.4, 56.7, 62.5, 52.0, 43.2, 46.8, 48.5, 41.7, 37.8],
        "Mitteldeutschland": [105.7, 80.9, 17.6, 16.4, 19.1, 20.0, 18.9, 14.5, 12.8, 16.9, 17.0, 12.3, 10.2],
        "Summe": [410.7, 356.5, 192.7, 167.7, 177.9, 169.4, 178.1, 131.3, 107.4, 126.3, 130.8, 102.3, 91.9]
    }
    
    df_foerderung = pd.DataFrame(foerderung_data, index=jahre).reset_index().rename(columns={"index": "Jahr"})
    
    # Auswahl der Regionen (alle außer "Jahr")
    st.title("Fördermengen in deutschen Braunkohlerevieren (1989–2024)")
    auswahl = st.multiselect("📦 Wähle Reviere zur Anzeige der Braunkohleförderung", options=df_foerderung.columns[1:], default=["Rheinland", "Lausitz", "Summe"])
    
    # Plot
    fig = go.Figure()
    for revier in auswahl:
        fig.add_trace(go.Scatter(
            x=df_foerderung["Jahr"],
            y=df_foerderung[revier],
            mode="lines+markers",
            name=revier
        ))
    
    fig.update_layout(
        title="Fördermenge von Braunkohle nach Revier (in Mio. Tonnen)",
        xaxis_title="Jahr",
        yaxis_title="Förderung [Mio. t]",
        legend=dict(x=0.01, y=1.1, orientation="h"),
        height=600
    )
    
    st.plotly_chart(fig)

    #
    #EE installierte Leistung
    #
    import pandas as pd
    import plotly.graph_objects as go
    import streamlit as st
    
    # Daten (GW)
    jahre = list(range(2014, 2025))
    data = {
        "Photovoltaik": [38.343, 39.799, 41.275, 43.300, 45.158, 48.864, 54.403, 60.038, 67.783, 83.159, 100.200],
        "Wind an Land": [37.620, 41.244, 45.384, 50.291, 52.328, 53.187, 54.326, 55.904, 58.014, 60.990, 63.600],
        "Wind auf See": [0.994, 3.297, 4.150, 5.427, 6.393, 7.555, 7.787, 7.807, 8.149, 8.473, 9.215]
    }
    
    ziele_2030 = {
        "Photovoltaik": 215,
        "Wind an Land": 115,
        "Wind auf See": 30
    }
    
    df = pd.DataFrame(data, index=jahre).reset_index().rename(columns={"index": "Jahr"})
    
    # Streamlit UI
    st.title("Installierte Leistung von PV & Wind (2014–2024) mit Zielen 2030")
    auswahl = st.multiselect("Wähle Technologien zum Vergleich", options=list(data.keys()), default=list(data.keys()))
    
    # Plotly-Figur
    fig = go.Figure()
    
    # Entwicklungslinien
    for tech in auswahl:
        fig.add_trace(go.Scatter(
            x=df["Jahr"],
            y=df[tech],
            mode="lines+markers",
            name=tech
        ))
    
    # Zielpunkte 2030
    for tech in auswahl:
        fig.add_trace(go.Scatter(
            x=[2030],
            y=[ziele_2030[tech]],
            mode="markers+text",
            name=f"Ziel 2030: {tech}",
            marker=dict(symbol="star", size=12, color="green"),
            text=[f"Ziel: {ziele_2030[tech]} GW"],
            textposition="top center",
            showlegend=False
        ))
    
    # Layout
    fig.update_layout(
        title="Installierte Leistung – Erneuerbare Energien vs. Ziel 2030",
        xaxis_title="Jahr",
        yaxis_title="Installierte Leistung [GW]",
        height=600,
        legend=dict(x=0.01, y=1.15, orientation="h")
    )
    
    st.plotly_chart(fig)

    #
    #Stromnetze
    #
    import pandas as pd
    import plotly.graph_objects as go
    import streamlit as st
    
    # Daten (in Millionen km)
    jahre = list(range(2014, 2025))
    netz_km = {
        "Niederspannung": [1.185, 1.193, 1.200, 1.206, 1.213, 1.218, 1.231, 1.240, 1.247, 1.253, 1.263],
        "Mittelspannung": [0.516, 0.518, 0.522, 0.523, 0.524, 0.526, 0.529, 0.531, 0.534, 0.536, 0.539],
        "Hoch-/Höchstspannung": [0.131, 0.133, 0.131, 0.131, 0.131, 0.132, 0.132, 0.133, 0.133, 0.134, 0.134]
    }
    
    # DataFrame
    df = pd.DataFrame(netz_km, index=jahre).reset_index().rename(columns={"index": "Jahr"})
    df["Gesamtlänge"] = df[["Niederspannung", "Mittelspannung", "Hoch-/Höchstspannung"]].sum(axis=1)
    
    # Streamlit UI
    st.title("Stromkreislängen in Deutschland (2014–2024)")
    st.markdown("Vergleich verschiedener Spannungsebenen – inklusive Gesamtleitungslänge.")
    
    auswahl = st.multiselect(
        "Wähle Spannungsebenen zum Vergleich",
        options=list(netz_km.keys()),
        default=list(netz_km.keys())
    )
    
    # Plot
    fig = go.Figure()
    
    for ebene in auswahl:
        fig.add_trace(go.Scatter(
            x=df["Jahr"],
            y=df[ebene],
            mode="lines+markers",
            name=ebene
        ))
    
    # Gesamtlänge immer anzeigen
    fig.add_trace(go.Scatter(
        x=df["Jahr"],
        y=df["Gesamtlänge"],
        mode="lines+markers",
        name="Gesamtlänge",
        line=dict(color="black", dash="dot")
    ))
    
    # Layout
    fig.update_layout(
        title="Stromkreislängen nach Spannungsebene (inkl. Gesamtlänge)",
        xaxis_title="Jahr",
        yaxis_title="Netzlänge [Mio. km]",
        legend=dict(x=0.01, y=1.1, orientation="h"),
        height=600
    )
    
    st.plotly_chart(fig)

    #
    #Investitionen in Energieinfrastruktur
    #
    import streamlit as st
    import pandas as pd
    import plotly.graph_objects as go
    
    # Daten vorbereiten
    jahre = list(range(2016, 2027))
    daten = {
        "Erzeugungsanlagen": [5.3, 4.2, 4.7, 4.8, 3.3, 3.5, 3.6, 3.8, 5.4, 5.2, 4.6],
        "Fortleitungs- und Verteilungsanlagen": [6.7, 6.3, 6.9, 7.2, 8.8, 9.7, 11.4, 16.0, 22.2, 27.0, 28.0],
        "Sonstiges": [0.9, 0.8, 0.7, 0.9, 1.1, 1.2, 2.0, 1.6, 1.4, 1.4, 1.4]
    }
    
    # DataFrame
    df = pd.DataFrame(daten, index=jahre).reset_index().rename(columns={"index": "Jahr"})
    df["Gesamt"] = df[["Erzeugungsanlagen", "Fortleitungs- und Verteilungsanlagen", "Sonstiges"]].sum(axis=1)
    
    # Streamlit-Interface
    st.title("Investitionen in Energieinfrastruktur in Deutschland")
    st.markdown("**Dargestellt werden jährliche Investitionen in Mrd. € für verschiedene Anlagentypen**")
    
    auswahl = st.multiselect(
        "Wähle Kategorien zum Vergleich",
        options=["Erzeugungsanlagen", "Fortleitungs- und Verteilungsanlagen", "Sonstiges"],
        default=["Erzeugungsanlagen", "Fortleitungs- und Verteilungsanlagen", "Sonstiges"]
    )
    
    # Plot erstellen
    fig = go.Figure()
    
    for kategorie in auswahl:
        fig.add_trace(go.Scatter(
            x=df["Jahr"],
            y=df[kategorie],
            mode="lines+markers",
            name=kategorie
        ))
    
    # Gesamtsumme immer anzeigen
    fig.add_trace(go.Scatter(
        x=df["Jahr"],
        y=df["Gesamt"],
        mode="lines+markers",
        name="Gesamt",
        line=dict(color="black", dash="dot")
    ))
    
    # Layout
    fig.update_layout(
        title="Investitionen in Energieanlagen (2016–2026)",
        xaxis_title="Jahr",
        yaxis_title="Investitionen (Mrd. €)",
        legend=dict(x=0.01, y=1.1, orientation="h"),
        height=600
    )
    
    st.plotly_chart(fig, use_container_width=True)



# ---------------------
# Seite: Klima
# ---------------------
elif menu == "Klima":
    st.title("🌡️ Klima – CO₂-Emissionen der Stromerzeugung")

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

    #
    #THG Emissionen DE
    #
    import streamlit as st
    import pandas as pd
    import plotly.graph_objects as go
    
    st.set_page_config(layout="wide")
    st.title("Treibhausgasemissionen nach Sektor in Deutschland")
    st.markdown("**Quelle: DESTATIS / UBA – inkl. Klimaziele 2030 laut Klimaschutzgesetz**")
    
    # Daten
    jahre = [1990, 2000, 2010, 2020, 2021, 2022, 2023, 2024]
    daten = {
        "Energiewirtschaft": [474.772, 390.844, 372.637, 219.038, 246.421, 256.670, 202.582, 184.994],
        "Industrie": [277.703, 202.598, 184.059, 172.577, 180.293, 164.365, 152.924, 153.007],
        "Gebäude": [210.027, 166.790, 142.933, 122.497, 119.287, 110.515, 102.933, 100.536],
        "Verkehr": [163.355, 180.586, 150.448, 146.386, 144.599, 147.691, 145.131, 143.055],
        "Landwirtschaft": [84.989, 71.957, 67.980, 66.374, 64.911, 63.902, 62.960, 62.111],
        "Sonstige": [41.550, 29.572, 12.192, 6.121, 5.915, 5.650, 5.490, 5.356]
    }
    
    ziele_2030 = {
        "Energiewirtschaft": 108,
        "Industrie": 118,
        "Gebäude": 67,
        "Verkehr": 85,
        "Landwirtschaft": 56,
        "Sonstige": 5
    }
    
    # DataFrame
    df = pd.DataFrame(daten, index=jahre)
    df["Gesamt"] = df.sum(axis=1)
    
    # Auswahl
    sektoren = list(daten.keys())
    auswahl = st.multiselect("Wähle Sektoren für den Vergleich", sektoren, default=sektoren)
    
    # Plotly-Plot
    fig = go.Figure()
    
    for sektor in auswahl:
        fig.add_trace(go.Scatter(
            x=jahre,
            y=df[sektor],
            mode="lines+markers",
            name=sektor
        ))
    
    # Zielmarken
    for sektor in auswahl:
        ziel = ziele_2030.get(sektor)
        if ziel:
            fig.add_trace(go.Scatter(
                x=[2030],
                y=[ziel],
                mode="markers+text",
                marker=dict(symbol="x", size=12, color="green"),
                name=f"{sektor} Ziel 2030",
                text=[f"{sektor} Ziel"],
                textposition="top center",
                showlegend=False
            ))
    
    # Layout
    fig.update_layout(
        title="Treibhausgasemissionen nach Sektor (1990–2024) inkl. Ziele 2030",
        xaxis_title="Jahr",
        yaxis_title="Emissionen (Mio. t CO₂e)",
        height=700,
        legend=dict(x=0.01, y=1.12, orientation="h")
    )
    
    st.plotly_chart(fig, use_container_width=True)

    #
    #THG Weltweit
    #

    import streamlit as st
    import pandas as pd
    import plotly.express as px
    
    # Daten (Top 20 Länder + Deutschland hervorgehoben)
    data = {
        "Land": [
            "China", "USA", "Indien", "Russland", "Japan", "Iran", "Indonesien",
            "Saudi-Arabien", "Deutschland", "Kanada", "Südkorea", "Mexiko",
            "Brasilien", "Türkei", "Südafrika", "Australien", "Vietnam",
            "Vereinigtes Königreich", "Polen", "Malaysia"
        ],
        "CO₂-Ausstoß (Mio. t)": [
            13259.64, 4682.04, 2955.18, 2069.5, 944.76, 778.8, 674.54,
            622.91, 582.95, 575.01, 573.54, 487.09, 479.5, 438.32,
            397.37, 373.62, 372.95, 302.1, 286.91, 283.32
        ]
    }
    
    df = pd.DataFrame(data)
    df["Hervorheben"] = df["Land"].apply(lambda x: "Deutschland" if x == "Deutschland" else "Andere")
    
    # Plot
    fig = px.bar(
        df.sort_values("CO₂-Ausstoß (Mio. t)", ascending=True),
        x="CO₂-Ausstoß (Mio. t)",
        y="Land",
        color="Hervorheben",
        color_discrete_map={"Deutschland": "crimson", "Andere": "lightgray"},
        title="CO₂-Ausstoß weltweit (Top 20 Länder, 2023)"
    )
    
    # Textausgabe
    gesamt_emissionen = df["CO₂-Ausstoß (Mio. t)"].sum()
    de_emissionen = df[df["Land"] == "Deutschland"]["CO₂-Ausstoß (Mio. t)"].values[0]
    de_anteil = round(de_emissionen / gesamt_emissionen * 100, 2)
    de_rang = df.sort_values("CO₂-Ausstoß (Mio. t)", ascending=False).reset_index().query("Land == 'Deutschland'").index[0] + 1
    
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(f"""
    ### Deutschland im Vergleich
    
    - 💨 **Ausstoß**: {de_emissionen:.2f} Mio. t CO₂  
    - 🌍 **Anteil (Top 20)**: **{de_anteil} %**
    - 🥇 **Platzierung**: **Rang {de_rang}** unter den Top 20 Ländern
    """)


# ---------------------
# Seite: Strukturwandelinvestitionen
# ---------------------
elif menu == "Strukturwandelinvestitionen":
    st.title("🏗️ Strukturwandel-Investitionen")
    st.markdown("Diese Seite ist noch leer und kann später ergänzt werden.")
    #
    #Beschäftigte
    #
    import streamlit as st
    import pandas as pd
    import plotly.graph_objects as go
    
    # Jahresreihe wie zuvor
    jahre = [1989, 1990, 1995, 2000, 2005, 2010, 2015, 2019, 2020, 2021, 2022, 2023, 2024]
    
    # Beschäftigtenzahlen (zum 31.12.)
    beschaeftigte_data = {
        "Rheinland": [15565, 15316, 13072, 10430, 11105, 11606, 9410, 9785, 9418, 8481, 7676, 7508, 7082],
        "Helmstedt": [1693, 1658, 1176, 703, 665, 541, 453, 101, 53, 53, 38, 25, 9],
        "Hessen": [637, 474, 105, 72, 1, None, None, None, None, None, None, None, None],
        "Bayern": [5, 5, 5, 5, 5, None, None, None, None, None, None, None, None],
        "Lausitz": [79016, 65478, 19248, 7081, 8881, 8049, 8316, 8116, 7822, 7362, 7675, 7887, 7333],
        "Mitteldeutschland": [59815, 46796, 6675, 2996, 2642, 2508, 2565, 2334, 2190, 2052, 1827, 1781, 1729],
        "Summe": [156731, 129727, 40281, 21287, 23299, 22704, 20744, 20336, 19483, 17948, 17216, 17201, 16153]
    }
    
    df_jobs = pd.DataFrame(beschaeftigte_data, index=jahre).reset_index().rename(columns={"index": "Jahr"})
    
    # Auswahl Dropdown
    st.title("Beschäftigtenzahlen in deutschen Braunkohlerevieren (1989–2024)")
    auswahl = st.multiselect("👷‍♀️ Beschäftigte in Revier auswählen", options=df_jobs.columns[1:], default=["Rheinland", "Lausitz", "Summe"])
    
    # Plot
    fig = go.Figure()
    for revier in auswahl:
        fig.add_trace(go.Scatter(
            x=df_jobs["Jahr"],
            y=df_jobs[revier],
            mode="lines+markers",
            name=revier
        ))
    
    fig.update_layout(
        title="Beschäftigte in der Braunkohlewirtschaft (jeweils 31.12.)",
        xaxis_title="Jahr",
        yaxis_title="Anzahl Beschäftigte",
        legend=dict(x=0.01, y=1.1, orientation="h"),
        height=600
    )
    
    st.plotly_chart(fig)
