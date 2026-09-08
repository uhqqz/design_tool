import os
from PIL import Image
import streamlit as st

# Data structure for Questionnaire & Archetypes
ARCHETYPES = {
    "A": {
        "name": "Archetype A: Framing & Explaining",
        "desc": "The user requires a clear narrative framing to navigate complex topics. Introductory contexts, step-by-step guidance, and explicit key insights help interpret the underlying message before diving into details.",
        "elements": {
            "Operational": {
                "title": "Guided onboarding walkthrough",
                "desc": "An interactive tour guide leads users step-by-step through the primary features of the interface. This helps first-time users orient themselves immediately upon opening the application and learn the controls interactively.",
                "img": "Images/I4_stepwise_onboarding.png",
            },
            "Interpretive": {
                "title": "Narrative wrapper (e.g., scrollystory, article)",
                "desc": "This element embeds visualizations into a guided storyline complete with text, media, and navigation steps. It helps guide users step-by-step through complex topics, making it easy to digest the overall narrative.",
                "img": "Images/E9 + E10_narrative_wrapper.png",
            },
            "Hybrid": {
                "title": "Problem framing",
                "desc": "This element places a core research question at the beginning and breaks it down into various subtopics or target groups. It helps users grasp the thematic framework of the visualization and understand which specific questions the tool answers along the way.",
                "img": "Images/E2_problem_framing.png",
            },
        },
    },
    "B": {
        "name": "Archetype B: Structuring Exploration",
        "desc": "The user wants to explore various options independently but requires structured orientation. Visual guidance and filter assistance facilitate navigation through complex inputs.",
        "elements": {
            "Operational": {
                "title": "Backtracking control",
                "desc": "A navigation path allows users to return to a previous analysis step at any time. This helps them experiment with alternative scenarios and make adjustments without starting the entire process over.",
                "img": "Images/I9_turning_back_to_earlier_point_in_interaction.png",
            },
            "Interpretive": {
                "title": "Thematic selection grouping",
                "desc": "Control elements and filters are bundled according to high-level thematic fields such as Energy, Environment, or Economy. This helps users navigate complex menus quickly and adjust parameters relevant to their specific query.",
                "img": "Images/E15_thematic_selection_grouping.png",
            },
            "Hybrid": {
                "title": "Overview-to-detail structure",
                "desc": "This element allows users to select specific regions within a high-level overview and zoom seamlessly into a detailed view. This helps users capture overall trends first before analyzing specific slices of data in detail.",
                "img": "Images/I15_overview_to_detail_structure.png",
            },
        },
    },
    "C": {
        "name": "Archetype C: Helping Users Read the Data",
        "desc": "The user needs support in inspecting, comparing, and reading complex data representations. Interactive tooltips, reference aids, and precise value indicators ensure accurate data interpretation.",
        "elements": {
            "Operational": {
                "title": "Numerical detail annotations",
                "desc": "Hovering the cursor over a data point in the chart displays exact numerical values and detailed info boxes. This helps users read precise metrics quickly without cluttering the main graphic with unnecessary text.",
                "img": "Images/I10_numerical_detail_annotations.png",
            },
            "Interpretive": {
                "title": "Key-figure highlighting",
                "desc": "This element extracts key values or peak figures and displays them enlarged above the graphic. This helps users instantly capture the main takeaway of a visualization at a glance without having to scan through axes first.",
                "img": "Images/E14_key_figure_highlighting.png",
            },
            "Hybrid": {
                "title": "Comparative graph view",
                "desc": "With this view, two charts or scenarios can be placed side-by-side for direct comparison. This helps users identify differences, trends, and deviations between different datasets at a glance.",
                "img": "Images/E7_comparative_graph_view.png",
            },
        },
    },
    "D": {
        "name": "Archetype D: Explaining on Demand",
        "desc": "The user navigates autonomously. Detailed background information and methodologies remain subtle and are accessible on demand via info buttons or glossaries.",
        "elements": {
            "Operational": {
                "title": "Selection semantics explanation",
                "desc": "Small info buttons next to filters explain precisely which data is included or excluded under a specific selection. This helps users understand the filtering logic applied by the tool and prevents misinterpretations of the results.",
                "img": "Images/E5_selection_semantics_explanation.png",
            },
            "Interpretive": {
                "title": "Method and source metadata",
                "desc": "This element provides detailed information about applied methodologies, data sources, authors, and update dates. This helps users transparently trace the origin and reliability of the displayed data and evaluate it with technical accuracy.",
                "img": "Images/E12_method_and_source_metadata.png",
            },
            "Hybrid": {
                "title": "Glossary-based concept explanation",
                "desc": "This element allows technical terms and concepts to be looked up directly via an info box or search icon. This helps users understand technical terminology in context immediately without prior knowledge or external research, facilitating a clearer understanding of the data content.",
                "img": "Images/E1_glossary_based_concept_explanations.png",
            },
        },
    },
}

# Glossary Data Structure categorized by Support Elements
GLOSSARY_CATEGORIES = {
    "Operational Support Elements": [
        {
            "title": "(Step-wise) textual usage instructions",
            "desc": "A numbered guide explains step-by-step how to operate the tool prior to use. This simplifies onboarding, ensuring users know precisely which actions to execute sequentially to obtain their desired result.",
            "img": r"Images\I1_(step-wise)_ textual_usage_instructions.png",
        },
        {
            "title": "Guided onboarding walkthrough",
            "desc": "An interactive tour guide leads users step-by-step through the primary features of the interface. This helps first-time users orient themselves immediately upon opening the application and learn the controls interactively.",
            "img": "Images/I4_stepwise_onboarding.png",
        },
        {
            "title": "Result search function",
            "desc": "A search bar enables targeted queries across results and tables for specific terms or values. This helps users locate relevant entries within large datasets immediately and highlight the result within the chart.",
            "img": "Images/I11_result_search_function.png",
        },
        {
            "title": "Reset-to-default control",
            "desc": "A central reset button restores all adjusted sliders, filters, and settings to their default state with a single click. This helps users easily establish a clean starting point for new inquiries after complex analyses or testing.",
            "img": "Images/I6_reseting_tool_button.png",
        },
        {
            "title": "Embedded contextual help",
            "desc": "Help icons placed directly beside interface elements provide access to contextual instructions, documentation, or contacts. This assists users right where a question arises without requiring them to navigate away from the view.",
            "img": "Images/I12_embedded_contextual_help.png",
        },
        {
            "title": "Video-based usage help/documentation",
            "desc": "An embedded explanatory video demonstrates how the tool operates through audio and visual guidance. This helps users grasp complex interactions visually without needing to read lengthy instructions.",
            "img": "Images/I2_video_tutorial.png",
        },
        {
            "title": "Backtracking control",
            "desc": "A navigation path allows users to return to a previous analysis step at any time. This helps them experiment with alternative scenarios and make adjustments without starting the entire process over.",
            "img": "Images/I9_turning_back_to_earlier_point_in_interaction.png",
        },
        {
            "title": "Standard signifiers and familiar conventions",
            "desc": "The user interface relies on familiar standard icons, such as a magnifying glass for search, a gear for settings, or a home icon for the main screen. This helps users navigate intuitively without a learning curve, matching standard digital habits.",
            "img": "Images/I16_standard_signifiers_and_familiar_conventions.png",
        },
        {
            "title": "Error feedback and recovery message",
            "desc": "In the event of invalid inputs or filter combinations, a clear error message appears with actionable resolution steps. This helps users identify the cause of the error instantly and adjust filters rapidly to return valid results.",
            "img": "Images/I5_error_message_when_used_wrong.png",
        },
        {
            "title": "Tool-behavior notice",
            "desc": "This note informs users in advance about automated responses or special behaviors, such as longer loading times or automatic view switches. This prevents confusion during operation and sets appropriate expectations to avoid frustration.",
            "img": "Images/I3_disclaimer_for_specific_behaviour_of_the_tool.png",
        },
        {
            "title": "Input constraint mechanism",
            "desc": "This mechanism blocks or highlights invalid entries and illogical filter combinations in red upfront. This helps prevent users from submitting incorrect inputs and protects against empty or erroneous data evaluations.",
            "img": r"Images\I8_input_contraint_mechanism.png",
        },
    ],
    "Interpretive Support Elements": [
        {
            "title": "Problem framing",
            "desc": "This element places a core research question at the beginning and breaks it down into various subtopics or target groups. It helps users grasp the thematic framework of the visualization and understand which specific questions the tool answers along the way.",
            "img": "Images/E2_problem_framing.png",
        },
        {
            "title": "Numerical detail annotations",
            "desc": "Hovering the cursor over a data point in the chart displays exact numerical values and detailed info boxes. This helps users read precise metrics quickly without cluttering the main graphic with unnecessary text.",
            "img": "Images/I10_numerical_detail_annotations.png",
        },
        {
            "title": "Method and source metadata",
            "desc": "This element provides detailed information about applied methodologies, data sources, authors, and update dates. This helps users transparently trace the origin and reliability of the displayed data and evaluate it with technical accuracy.",
            "img": "Images/E12_method_and_source_metadata.png",
        },
        {
            "title": "Chart-specific explanatory annotation",
            "desc": "Individual data points, axes, or chart areas are provided directly with explanatory descriptions and legends. This helps users correctly read the structure and units of the graphic, preventing misunderstandings regarding values.",
            "img": r"Images\E3_chart_specific_explanatory_annotations.png",
        },
        {
            "title": "Glossary-based concept explanation",
            "desc": "This element allows technical terms and concepts to be looked up directly via an info box or search icon. This helps users understand technical terminology in context immediately without prior knowledge or external research, facilitating a clearer understanding of the data content.",
            "img": "Images/E1_glossary_based_concept_explanations.png",
        },
        {
            "title": "Key-figure highlighting",
            "desc": "This element extracts key values or peak figures and displays them enlarged above the graphic. This helps users instantly capture the main takeaway of a visualization at a glance without having to scan through axes first.",
            "img": "Images/E14_key_figure_highlighting.png",
        },
        {
            "title": "Chart-specific interpretive annotation",
            "desc": "This element highlights striking data points—such as peak values or outliers—and provides an immediate contextual explanation. This helps users instantly grasp the significance of the data without having to perform a complex root-cause analysis themselves.",
            "img": r"Images\E4_chart_specific_interpretive_annotation.png",
        },
        {
            "title": "Cross-view narrative linking text",
            "desc": "Connecting text establishes the contextual relationship between two distinct representations, such as a chart and a map. This helps users understand connections across multiple views and maintain the narrative thread of the analysis.",
            "img": "Images/E8_cross_view_narrative_linking_text.png",
        },
        {
            "title": "Narrative wrapper",
            "desc": "This element embeds visualizations into a guided storyline complete with text, media, and navigation steps. It helps guide users step-by-step through complex topics, making it easy to digest the overall narrative.",
            "img": "Images/E9 + E10_narrative_wrapper.png",
        },
        {
            "title": "Linked source publication",
            "desc": "A link icon or pop-up grants direct access to underlying original publications and PDF documents. This helps users read deeper background information and use primary sources for their own research.",
            "img": r"Images\E18_linked_source_publication.png",
        },
        {
            "title": "Limitations/Disclaimer",
            "desc": "Caveats, data gaps, or methodological limits—such as incomplete regional datasets—are transparently stated. This helps users avoid interpretation pitfalls and prevents false or overly broad generalizations of the results.",
            "img": "Images/E13_limitations_disclaimer.png",
        },
        {
            "title": "Model/observation provenance distinction",
            "desc": "This element presents measured real-world data alongside calculated model or future projections, clearly indicating their respective origins. It helps users distinguish reliable present-state data from hypothetical scenarios and categorize the data accurately.",
            "img": "Images/E6_model_observation_provenance_distinction.png",
        },
        {
            "title": "Comparative graph view",
            "desc": "With this view, two charts or scenarios can be placed side-by-side for direct comparison. This helps users identify differences, trends, and deviations between different datasets at a glance.",
            "img": "Images/E7_comparative_graph_view.png",
        },
        {
            "title": "Evaluative visual cues",
            "desc": "Using color scales, gauge displays, or icons (such as smileys), displayed values are immediately evaluated. This helps users assess at a glance whether a result should be considered positive, neutral, or critical.",
            "img": "Images/E11_evaluative_visual_cues.png",
        },
        {
            "title": "Reference numbers",
            "desc": "Numbered data points in the chart link directly to an ordered list of information below the graphic. This helps users follow chronological sequences or key events step-by-step without losing visual contact with the diagram.",
            "img": "Images/E16_reference_numbers.png",
        },
    ],
    "Hybrid Support Elements": [
        {
            "title": "Overview-to-detail structure",
            "desc": "This element allows users to select specific regions within a high-level overview and zoom seamlessly into a detailed view. This helps users capture overall trends first before analyzing specific slices of data in detail.",
            "img": "Images/I15_overview_to_detail_structure.png",
        },
        {
            "title": "Thematic selection grouping",
            "desc": "Control elements and filters are bundled according to high-level thematic fields such as Energy, Environment, or Economy. This helps users navigate complex menus quickly and adjust parameters relevant to their specific query.",
            "img": "Images/E15_thematic_selection_grouping.png",
        },
        {
            "title": "Selection semantics explanation",
            "desc": "Small info buttons next to filters explain precisely which data is included or excluded under a specific selection. This helps users understand the filtering logic applied by the tool and prevents misinterpretations of the results.",
            "img": "Images/E5_selection_semantics_explanation.png",
        },
        {
            "title": "Default parameterization",
            "desc": "The tool launches with sensible, pre-configured default parameters and an optimized standard view. This helps users view meaningful data right away without needing to spend time configuring settings before their initial analysis.",
            "img": "Images/I13_default_parametrization.png",
        },
        {
            "title": "Cross-link to related visualizations",
            "desc": "Direct links to supplementary or alternative chart types are offered below the graphic. This helps users explore a topic from different angles without search overhead, revealing deeper insights within the dataset.",
            "img": r"Images\I14_cross_linked_to_related_visualizations.png",
        },
        {
            "title": "Q&A element",
            "desc": "This element provides an interactive list of frequently asked questions with expandable answers and matching graphics. This helps users quickly resolve common ambiguities on their own and find direct answers to specific questions.",
            "img": "Images/E17_qanda_element.png",
        },
        {
            "title": "Expected-output preview",
            "desc": "This element displays a preview graphic using sample data before the user commits to a final selection. This helps them gauge how their intended data choice will be visually rendered, saving setup time.",
            "img": "Images/I7_expected_output_preview.png",
        },
    ],
}

MAPPINGS = {
    "T1_U1_O1": ["A", "D"],
    "T1_U1_O2": ["A", "B"],
    "T1_U1_O3": ["A", "B"],
    "T1_U1_O4": ["A", "C"],
    "T1_U1_O5": ["A", "D"],
    "T1_U2_O1": ["A", "D"],
    "T1_U2_O2": ["A", "B"],
    "T1_U2_O3": ["A", "B"],
    "T1_U2_O4": ["A", "C"],
    "T1_U2_O5": ["A", "D"],
    "T1_U3_O1": ["A", "D"],
    "T1_U3_O2": ["D", "A"],
    "T1_U3_O3": ["D", "B"],
    "T1_U3_O4": ["C", "D"],
    "T1_U3_O5": ["D", "A"],
    "T2_U1_O1": ["A", "B"],
    "T2_U1_O2": ["B", "A"],
    "T2_U1_O3": ["B", "C"],
    "T2_U1_O4": ["C", "B"],
    "T2_U1_O5": ["D", "A"],
    "T2_U2_O1": ["A", "B"],
    "T2_U2_O2": ["B", "C"],
    "T2_U2_O3": ["B", "D"],
    "T2_U2_O4": ["C", "B"],
    "T2_U2_O5": ["D", "C"],
    "T2_U3_O1": ["D", "A"],
    "T2_U3_O2": ["D", "B"],
    "T2_U3_O3": ["B", "D"],
    "T2_U3_O4": ["C", "D"],
    "T2_U3_O5": ["D", "C"],
}


def display_safe_image(img_path, width=280):
    """Zeigt Bilder in einer kontrollierten, kompakteren Breite an."""
    if img_path and os.path.exists(img_path):
        image = Image.open(img_path)
        st.image(image, width=width)
    elif img_path and (img_path.startswith("http://") or img_path.startswith("https://")):
        st.image(img_path, width=width)
    elif img_path:
        st.warning(f"Image not found at path: `{img_path}`")


# Page Setup & Custom Styling (NFDI4Energy Theme)
st.set_page_config(
    page_title="Visualizations of the Energy Transition | NFDI4energy", layout="centered"
)

st.markdown(
    """
    <style>
    /* NFDI4energy Color Palette */
    :root {
        --nfdi-petrol: #4A90A2;
        --nfdi-magenta: #C2185B;
        --nfdi-bg: #F8FAF9;
        --nfdi-card: #FFFFFF;
        --nfdi-border: #E0E7E9;
        --nfdi-text: #2C3E50;
    }

    .stApp {
        background-color: var(--nfdi-bg);
        color: var(--nfdi-text);
    }

    /* Primary Buttons */
    .stButton > button {
        background-color: var(--nfdi-petrol) !important;
        color: white !important;
        border-radius: 6px !important;
        border: none !important;
        font-weight: 600 !important;
    }
    
    .stButton > button:hover {
        background-color: #3B7584 !important;
    }

    /* Custom Cards / Boxes */
    .nfdi-card {
        background-color: var(--nfdi-card);
        border: 1px solid var(--nfdi-border);
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }

    /* Result Header Tag */
    .result-tag {
        background-color: #E2F0D9;
        color: #385723;
        font-size: 0.75rem;
        font-weight: 700;
        padding: 4px 12px;
        border-radius: 12px;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 8px;
    }

    /* Recommendation Badges */
    .badge-primary {
        background-color: #E8EAF6;
        color: #283593;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 0.8rem;
    }

    .badge-secondary {
        background-color: #E1F5FE;
        color: #0277BD;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 0.8rem;
    }

    .archetype-avatar {
        background-color: #C8E6C9;
        color: #1B5E20;
        font-size: 1.5rem;
        font-weight: bold;
        width: 48px;
        height: 48px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    </style>
""",
    unsafe_allow_html=True,
)

if "started" not in st.session_state:
    st.session_state.started = False
if "show_glossary" not in st.session_state:
    st.session_state.show_glossary = False

# --- INTRO PAGE ---
if not st.session_state.started and not st.session_state.show_glossary:
    st.title("About this tool")

    st.write(
        "Making energy transition data visible is one thing—making it understandable is another. "
        "Interactive charts are great, but without clear guidance, users can easily get lost in a sea of filters, assumptions, and complex numbers."
    )

    st.write(
        "To bridge this gap, public-facing energy visualizations rely on **4 Support Archetypes** to help different audiences make sense of complex data:"
    )

    st.markdown(
        """
    * **Framing & Explaining:** Provides clear context and storylines upfront before diving into raw numbers—ideal for broad, non-expert audiences.
    * **Structuring Exploration:** Guides users step-by-step through complex scenarios and interactive filters so they never lose orientation.
    * **Helping Users Read Data:** Focuses on visual clarity, highlighting key metrics and comparative views for precise analytical reading.
    * **Explaining on Demand:** Keeps the interface clean for independent browsing while providing instant explanations, glossaries, and tooltips whenever questions arise.
    """
    )

    st.markdown("### Find the Right Concept for Your Project")
    st.write(
        "Whether planning a new visualization or fine-tuning an existing tool, this decision guide helps match project goals with the right design strategy and design elements."
    )
    st.write(
        "By defining **three key factors**—the primary **audience**, the main **purpose**, and the biggest **user challenge**—the guide identifies the best-fitting support archetype and proposes concrete design elements."
    )

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Start Decision Guide", use_container_width=True):
            st.session_state.started = True
            st.rerun()
    with col2:
        if st.button("View Design Elements Glossary", use_container_width=True):
            st.session_state.show_glossary = True
            st.rerun()

# --- GLOSSARY PAGE ---
elif st.session_state.show_glossary:
    if st.button("← Back to Intro"):
        st.session_state.show_glossary = False
        st.rerun()

    st.title("Design Elements Glossary")
    st.write(
        "Explore all 32 design elements categorized into Operational, Interpretive, and Hybrid support elements."
    )

    for cat_name, elements_list in GLOSSARY_CATEGORIES.items():
        st.markdown(f"## {cat_name}")

        for elem in elements_list:
            with st.expander(f"**{elem['title']}**", expanded=False):
                if elem["img"]:
                    col_text, col_img = st.columns([1.2, 0.8])
                    with col_text:
                        st.write(elem["desc"])
                    with col_img:
                        display_safe_image(elem["img"], width=250)
                else:
                    st.write(elem["desc"])

        st.divider()

# --- QUESTIONNAIRE & RESULTS ---
else:
    col_back, col_title = st.columns([1, 4])
    with col_back:
        if st.button("← Back"):
            st.session_state.started = False
            st.rerun()

    st.title("Visualizations of the Energy Transition")
    st.caption("Design Elements for Energy Data Visualizations")

    # Step 1
    with st.container():
        st.markdown(
            '<div class="nfdi-card"><b>1. Who is the primary user?</b>',
            unsafe_allow_html=True,
        )
        user = st.radio(
            "Select primary user:",
            options=["U1", "U2", "U3"],
            index=None,
            format_func=lambda x: {
                "U1": "Non-expert public",
                "U2": "Mixed / practice-oriented",
                "U3": "Expert / analytical",
            }[x],
            key="q1",
            label_visibility="collapsed",
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # Step 2
    task = None
    if user:
        with st.container():
            st.markdown(
                '<div class="nfdi-card"><b>2. What is the main task you want to give the user?</b>',
                unsafe_allow_html=True,
            )
            task = st.radio(
                "Select main task:",
                options=["T1", "T2"],
                index=None,
                format_func=lambda x: {
                    "T1": "Understand a message/context",
                    "T2": "Explore data/scenarios",
                }[x],
                key="q2",
                label_visibility="collapsed",
            )
            st.markdown("</div>", unsafe_allow_html=True)

    # Step 3
    obstacle = None
    if task:
        with st.container():
            st.markdown(
                '<div class="nfdi-card"><b>3. What is the most likely obstacle between the user and the intended insight?</b>',
                unsafe_allow_html=True,
            )
            obstacle = st.radio(
                "Select obstacle:",
                options=["O1", "O2", "O3", "O4", "O5"],
                index=None,
                format_func=lambda x: {
                    "O1": "Understanding context / key message",
                    "O2": "Knowing where to start / proceed",
                    "O3": "Navigating options, filters, paths",
                    "O4": "Reading values, charts, comparisons",
                    "O5": "Understanding assumptions / methods",
                }[x],
                key="q3",
                label_visibility="collapsed",
            )
            st.markdown("</div>", unsafe_allow_html=True)

    # RESULTS SECTION
    if obstacle:
        st.divider()

        st.markdown(
            """
            <div style="text-align: center;">
                <span class="result-tag">YOUR RESULT</span>
                <h2 style="margin-top: 4px;">Archetype Assessment Complete</h2>
            </div>
        """,
            unsafe_allow_html=True,
        )

        key = f"{task}_{user}_{obstacle}"
        results = MAPPINGS.get(key, ["A", "B"])
        primary_arch = results[0]
        secondary_arch = results[1]

        st.markdown("#### Select Archetype View")
        
        # Nutzung von segmented_control für eine karten/buttonbasierte Wechselansicht ohne Radio-Punkte
        selected_arch_key = st.segmented_control(
            "Choose Archetype:",
            options=[primary_arch, secondary_arch],
            format_func=lambda x: f"Type {x} (Primary)" if x == primary_arch else f"Type {x} (2nd Choice)",
            default=primary_arch,
            key="selected_archetype_view",
            label_visibility="collapsed",
        )

        if not selected_arch_key:
            selected_arch_key = primary_arch

        arch_data = ARCHETYPES[selected_arch_key]
        is_primary = selected_arch_key == primary_arch

        badge_html = (
            f'<span class="badge-primary">RECOMMENDATION: TYPE {primary_arch}</span>'
            if is_primary
            else f'<span class="badge-secondary">2ND CHOICE: TYPE {secondary_arch}</span>'
        )

        st.markdown(
            f"""
            <div class="nfdi-card" style="border: 1px solid {'#C8E6C9' if is_primary else '#B3E5FC'};">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 12px;">
                    <div class="archetype-avatar" style="background-color: {'#C8E6C9' if is_primary else '#B3E5FC'}; color: {'#1B5E20' if is_primary else '#01579B'};">{selected_arch_key}</div>
                    <div>
                        {badge_html}
                        <h3 style="margin: 4px 0 0 0; color: {'#1B5E20' if is_primary else '#01579B'};">{arch_data['name']}</h3>
                    </div>
                </div>
                <p style="color: #444444; font-size: 0.95rem; margin: 0;">{arch_data['desc']}</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown("#### Select Support Level")
        level_choice = st.segmented_control(
            "Select Support Level:",
            options=["Operational", "Interpretive", "Hybrid"],
            default="Interpretive",
            label_visibility="collapsed",
            key="level_choice_radio",
        )

        if not level_choice:
            level_choice = "Interpretive"

        elem_data = arch_data["elements"][level_choice]

        st.markdown(
            f"""
            <div class="nfdi-card" style="margin-top: 15px;">
                <h4 style="color: var(--nfdi-petrol); margin-top: 0;">{elem_data['title']}</h4>
                <p>{elem_data['desc']}</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

        display_safe_image(elem_data["img"], width=300)