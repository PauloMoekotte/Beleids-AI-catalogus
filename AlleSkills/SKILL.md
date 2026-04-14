# Skill: MBO Beleids-AI Router

## Beschrijving

Deze skill fungeert als centrale router die binnenkomende vragen analyseert en doorstuurt naar de juiste AI-persona map. Gebruik deze skill als startpunt voor alle MBO-beleidsvragen.

## Routing logica

Analyseer de vraag en bepaal welke persona het beste past:

| Persona | Kerncompetentie | Triggerwoorden |
|---------|-----------------|----------------|
| **Gebruiker** | Basisvaardigheden: prompten, beoordelen, dagelijks werk | prompt, lesplan, feedback, rapportage, uitleggen, dagelijks werk |
| **Gids** | Ethiek, risico's, governance, compliance | ethiek, bias, privacy, AVG, EU AI Act, risico, compliance, controleren |
| **Gangmaker** | Samenwerking, use cases, strategie, brug beleid-praktijk | brainstorm, use case, innovatie, verandering, adoptie, arbeidsmarkt, beroep |
| **Ontwerper** | Data, modellering, integratie, technische analyses | data, analyse, KPI, benchmark, dashboard, trend, validatie, cohort, visualization |
| **Impactmaker** | Strategie, leiderschap, impactmeting | beleid, strategie, advies, scenario, impact, jaarverslag, VSV, leerweg |

## Beschikbare skills per persona

### Gebruiker
- `prompt-helper` - Genereer effectieve prompts voor lesplannen, feedback, rapportages
- `feedback-analyzer` - Analyseer student- en docentfeedback op trends en sentiment

### Gids
- `ethische-ai-check` - Toets AI-output op bias, privacy, EU AI Act en ethische principes
- `bias-detector` - Detecteer bias in beoordelingen, rapportages en AI-gegenereerde teksten

### Gangmaker
- `beroepsanalyse` - Onderwijs-arbeidsmarkt-matching voor opleidingen
- `use-case-explorer` - Identificeer AI-kansen via Double Diamond-methode
- `verandermanagement-ai` - Roadmap voor AI-adoptie in teams

### Ontwerper
- `kpi-analyse` - Automatische rapportage van dropout, placement en trends
- `data-pipeline-review` - Schoonmaak en analyse van leerlingdata
- `swot-benchmark` - Opleidingsanalyse op SWOT en benchmark
- `competentie-mapper` - Koppel AI-skills aan MBO-opleidingen
- `cohort-analyse` - Analyseer studentencohorten over tijd
- `dashboard-generator` - Genereer visuele dashboards
- `trendvoorspelling` - Voorspel toekomstige trends
- `data-validatie-check` - Controleer datakwaliteit van exports

### Impactmaker
- `policy-brief` - Evidence-informed beleidsnotities
- `leerweg-review` - Analyse van VSV-risico's en interventies
- `strategisch-advies` - Strategische advisering over AI-implementatie
- `beleidsimpact-analyse` - Analyseer impact van beleidsvoorstellen
- `jaarverslag-generator` - Genereer conceptteksten voor rapportages
- `scenario-analyse` - Ontwikkel toekomstscenario's

## Gebruik

1. Ontvang de vraag van de gebruiker
2. Analyseer de vraag op basis van triggerwoorden en context
3. Bepaal de juiste persona
4. Roep de meest relevante skill aan

## Voorbeelden

**Input:** "Ik wil een lesplan maken voor metaal BOL niveau 2"
→ **Gebruiker** → `prompt-helper`

**Input:** "Controleer deze tekst op bias"
→ **Gids** → `bias-detector`

**Input:** "Analyseer de arbeidsmarkt voor IT-opleidingen in Twente"
→ **Gangmaker** → `beroepsanalyse`

**Input:** "Maak een dashboard van onze KPI's"
→ **Ontwerper** → `dashboard-generator`

**Input:** "Schrijf een beleidsnotitie over digitale vaardigheden"
→ **Impactmaker** → `policy-brief`

---

*Deze router is onderdeel van de MBO Beleids-AI-Skills catalogus.*