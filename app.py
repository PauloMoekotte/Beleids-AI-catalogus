import streamlit as st
import json
from data.skills import SKILLS

st.set_page_config(
    page_title="Beleids-AI Skills", page_icon=":robot_face:", layout="wide"
)

PERSONA_Kleuren = {
    "Gebruiker": "green",
    "Gids": "purple",
    "Gangmaker": "orange",
    "Ontwerper": "cyan",
    "Impactmaker": "red",
}

PERSONA_Beschrijving = {
    "Gebruiker": "Basisvaardigheden: prompten, beoordelen, dagelijks werk",
    "Gids": "Ethiek, risico's, governance, compliance",
    "Gangmaker": "Samenwerking, use cases, strategie, brug beleid-praktijk",
    "Ontwerper": "Data, modellering, integratie, technische analyses",
    "Impactmaker": "Strategie, leiderschap, impactmeting",
}

st.title("Beleids-AI Skills")
st.caption("Overzicht van alle AI-skills voor beleidsadviseurs in het MBO")

col_filter1, col_filter2, col_filter3 = st.columns(3)

with col_filter1:
    personas = ["Alle"] + sorted(set(s["persona"] for s in SKILLS))
    desc = " | ".join(
        [f"{p}: {PERSONA_Beschrijving.get(p, '')}" for p in personas if p != "Alle"]
    )
    selected_persona = st.selectbox("Persona", personas, help=desc)

with col_filter2:
    selected_risico = st.selectbox("Risiconiveau", ["Alle", "Laag", "Middel", "Hoog"])

with col_filter3:
    selected_status = st.selectbox("Status", ["Alle", "Goedgekeurd", "Voorstel"])

zoekterm = st.text_input(
    "Zoek in skills...", placeholder="Type om te zoeken...", key="zoek"
)
if zoekterm:
    st.session_state.zoekterm = zoekterm
else:
    st.session_state.zoekterm = ""

filtered_skills = SKILLS.copy()

if selected_persona != "Alle":
    filtered_skills = [s for s in filtered_skills if s["persona"] == selected_persona]
if selected_risico != "Alle":
    filtered_skills = [
        s for s in filtered_skills if s["risiconiveau"] == selected_risico
    ]
if selected_status != "Alle":
    filtered_skills = [s for s in filtered_skills if s["status"] == selected_status]
if st.session_state.zoekterm:
    filtered_skills = [
        s
        for s in filtered_skills
        if st.session_state.zoekterm.lower() in s["naam"].lower()
        or st.session_state.zoekterm.lower() in s["beschrijving"].lower()
    ]

st.divider()

st.subheader(f"{len(filtered_skills)} skills gevonden")

col_exp1, col_exp2 = st.columns([3, 1])

with col_exp1:
    tab_overzicht, tab_diagram = st.tabs(["Overzicht", "Diagram"])

with col_exp2:
    st.markdown("### Export")

    exported = json.dumps(filtered_skills, ensure_ascii=False, indent=2)
    st.download_button(
        label="📥 JSON",
        data=exported,
        file_name="beleids-ai-skills.json",
        mime="application/json",
    )

    md_content = "# Beleids-AI Skills\n\n"
    for s in filtered_skills:
        md_content += f"## {s['naam']}\n\n"
        md_content += f"**Persona:** {s['persona']}\n\n"
        md_content += f"**Beschrijving:** {s['beschrijving']}\n\n"
    st.download_button(
        label="📝 Markdown",
        data=md_content,
        file_name="beleids-ai-skills.md",
        mime="text/markdown",
    )

with tab_overzicht:
    if filtered_skills:
        selected_skill = st.radio(
            "Kies een skill voor details:",
            options=filtered_skills,
            format_func=lambda x: f"{x['naam']} ({x['persona']})",
            label_visibility="collapsed",
        )

        if selected_skill:
            skill = selected_skill
            with st.container(border=True):
                st.markdown(f"## {skill['naam']}")
                st.caption(
                    f"**Persona:** {skill['persona']} | **Risico:** {skill['risiconiveau']} | **Status:** {skill['status']}"
                )
                st.write(skill["beschrijving"])

                col_d1, col_d2 = st.columns(2)
                with col_d1:
                    st.markdown("### Trigger-woorden")
                    st.write(", ".join(skill["trigger_woorden"]))
                with col_d2:
                    st.markdown("### Input vereisten")
                    st.write(", ".join(skill["input_vereisten"]))

                st.code(f"ID: {skill['id']}", language="text")
    else:
        st.warning("Geen skills gevonden met deze filters.")

with tab_diagram:
    st.markdown("### Skills Flow - Hiërarchische Weergave")

    skills_per_persona = {
        "Gebruiker": ["Prompt-helper", "Feedback-analyzer"],
        "Gids": ["Ethische-AI-check", "Bias-detector"],
        "Gangmaker": ["Beroepsanalyse", "Use-case-explorer", "Verandermanagement"],
        "Ontwerper": [
            "KPI-analyse",
            "Dashboard-generator",
            "Cohort-analyse",
            "Competentie-mapper",
            "SWOT-benchmark",
            "Trendvoorspelling",
            "Data-validatie-check",
            "Data-pipeline-review",
        ],
        "Impactmaker": [
            "Policy-brief",
            "Leerweg-review",
            "Strategisch-advies",
            "Beleidsimpact-analyse",
            "Jaarverslag-generator",
            "Scenario-analyse",
        ],
    }

    if st.session_state.zoekterm:
        matchende_personas = []
        for persona, skills in skills_per_persona.items():
            for skill in skills:
                if st.session_state.zoekterm.lower() in skill.lower():
                    matchende_personas.append(persona)
        matchende_personas = list(set(matchende_personas))

        if matchende_personas:
            st.success(
                f"Filters toegepast: Zoek '{st.session_state.zoekterm}' in diagram"
            )
            skills_per_persona = {
                p: skills_per_persona[p]
                for p in matchende_personas
                if p in skills_per_persona
            }
        else:
            st.warning(f"Geen resultaten voor '{st.session_state.zoekterm}' in diagram")

    with st.expander("🌐 Router (Startpunt)", expanded=True):
        st.success(
            "**MBO Beleids-AI Router** - Centrale router die vragen analyseert en doorstuurt naar de juiste persona."
        )

    for persona, skills in skills_per_persona.items():
        with st.expander(f"{persona} ({len(skills)} skills)", expanded=True):
            for skill in skills:
                skill_info = next((s for s in SKILLS if s["naam"] == skill), None)
                if skill_info:
                    kleur = PERSONA_Kleuren.get(persona, "gray")
                    st.markdown(f"- **{skill}** - {skill_info['beschrijving'][:60]}...")

    st.markdown("---")
    st.markdown("### Snelle Links")

    cols = st.columns(5)
    personas_lijst = list(skills_per_persona.keys())

    for idx, (persona, skills) in enumerate(skills_per_persona.items()):
        with cols[idx % 5]:
            st.markdown(f"**{persona} ({len(skills)})**")
            for skill in skills:
                st.markdown(f"- {skill}")

st.sidebar.title("📊 Overzicht")
st.sidebar.markdown(f"**Totaal:** {len(SKILLS)} skills")

st.sidebar.markdown("### Per Persona")
for persona in sorted(set(s["persona"] for s in SKILLS)):
    count = len([s for s in SKILLS if s["persona"] == persona])
    kleur = PERSONA_Kleuren.get(persona, "gray")
    st.sidebar.markdown(f"- **{persona}**: {count}")

st.sidebar.markdown("### Risiconiveau")
for risico in ["Laag", "Middel", "Hoog"]:
    count = len([s for s in SKILLS if s["risiconiveau"] == risico])
    st.sidebar.markdown(f"- **{risico}**: {count}")

st.sidebar.markdown("### Status")
for status in ["Goedgekeurd", "Voorstel"]:
    count = len([s for s in SKILLS if s["status"] == status])
    st.sidebar.markdown(f"- **{status}**: {count}")
