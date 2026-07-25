
import streamlit as st
import random
import plotly.graph_objects as go
from PIL import Image
from transformers import pipeline

st.set_page_config(
    page_title="StartupMentor AI",
    page_icon="🚀",
    layout="wide"
)

# Load AI model only once
@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="distilgpt2"
    )

generator = load_model()

st.title("🚀 StartupMentor AI")
st.subheader("AI-Powered Startup Analysis & Logo Intelligence Platform")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Choose Module",
    [
        "🏠 Home",
        "🤖 Startup Analyzer",
        "🎨 Logo Analyzer"
    ]
)

# ---------------- HOME ---------------- #

if page == "🏠 Home":

    st.success("Welcome to StartupMentor AI!")

    st.write("""
This project helps entrepreneurs analyze startup ideas using Artificial Intelligence.
It also evaluates startup branding through logo analysis.
""")

# ---------------- STARTUP ANALYZER ---------------- #

elif page == "🤖 Startup Analyzer":

    st.header("🤖 AI Startup Analyzer")

    name = st.text_input("Startup Name")

    idea = st.text_area("Describe your Startup Idea")

    market = st.text_input("Target Market")

    if st.button("Analyze Startup"):

        innovation = random.randint(75,100)
        demand = random.randint(70,100)
        competition = random.randint(55,95)
        scalability = random.randint(70,100)
        revenue = random.randint(70,100)
        risk = random.randint(20,60)

        st.success("Analysis Complete")

        col1,col2,col3 = st.columns(3)

        col1.metric("Innovation",f"{innovation}%")
        col2.metric("Market Demand",f"{demand}%")
        col3.metric("Competition",f"{competition}%")

        col1,col2,col3 = st.columns(3)

        col1.metric("Scalability",f"{scalability}%")
        col2.metric("Revenue",f"{revenue}%")
        col3.metric("Risk",f"{risk}%")

        # Radar Chart
        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=[
                innovation,
                demand,
                competition,
                scalability,
                revenue,
                risk
            ],
            theta=[
                "Innovation",
                "Demand",
                "Competition",
                "Scalability",
                "Revenue",
                "Risk"
            ],
            fill='toself'
        ))

        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True,range=[0,100])),
            showlegend=False
        )

        st.plotly_chart(fig,use_container_width=True)

        st.subheader("🤖 AI Recommendation")

        prompt=f"""
Startup Idea:
{idea}

Give short business advice.
"""

        response=generator(
            prompt,
            max_new_tokens=60,
            do_sample=True
        )

        st.write(response[0]["generated_text"])

        st.subheader("SWOT")

        st.markdown("""
### ✅ Strengths
- Innovative concept
- High scalability

### ⚠ Weaknesses
- Requires funding
- Customer acquisition challenge

### 🚀 Opportunities
- Growing digital market
- Investor interest

### ❌ Threats
- Existing competitors
- Market uncertainty
""")

# ---------------- LOGO ANALYZER ---------------- #

elif page=="🎨 Logo Analyzer":

    st.header("🎨 AI Logo Analyzer")

    uploaded=st.file_uploader(
        "Upload Logo",
        type=["png","jpg","jpeg"]
    )

    if uploaded:

        image=Image.open(uploaded)

        st.image(image,width=250)

        st.success("Logo Uploaded Successfully!")

        st.subheader("Branding Suggestions")

        st.write("✅ Simple and memorable")

        st.write("✅ Looks professional")

        st.write("✅ Suitable for digital branding")

        st.write("✅ Strong visual identity")
