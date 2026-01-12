import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Keifer & Vonnie's Health Hub", page_icon="🎋")

# --- SIDEBAR COUNTDOWNS ---
st.sidebar.header("⏳ Key Deadlines")
med_date = datetime(2026, 8, 1)
m_days = (med_date - datetime.now()).days
st.sidebar.warning(f"🚨 {m_days} Days to Keifer's Medical")

retire_date = datetime(2038, 9, 1)
r_days = (retire_date - datetime.now()).days
st.sidebar.info(f"🗓️ {r_days:,} Days to Retirement")

# --- MAIN INTERFACE ---
st.title("🎋 Keifer & Vonnie's Command Centre")
user = st.radio("Who is checking in?", ["Keifer", "Vonnie"])

# --- EXERCISE HUB ---
with st.expander("💪 Exercise & Joint Support", expanded=False):
    st.video("https://www.youtube.com/watch?v=38tqFjB-o-g")
    
    if user == "Vonnie":
        st.warning("🦶 **Vonnie's Foot Care:** Focus on the 'Roll' technique. If the heel is flaring up, freeze a water bottle and roll your foot over it for 5 mins.")
    else:
        st.info("🦵 **Keifer's Knee/Hip Support:** Warm up your joints with 'hip circles' before your walk. Never lock your knees straight.")

    st.markdown("""
    **Tai Chi Walking Form:**
    1. **The Pour:** Weight transfer should be slow—don't 'plonk' the foot down.
    2. **The Roll:** Heel -> Arch -> Toe. 
    3. **Soft Knees:** Always keep a micro-bend to absorb shock.
    """)

# --- COOKBOOK SECTION (With Links) ---
st.divider()
st.header("📖 The Digital Cookbook")
diet = st.radio("Select Your Focus:", ["Keto (Diabetes)", "Mediterranean (BP)"])

# Categorised Links
keto_recipes = {
    "Breakfast": {
        "Salmon Avocado Smash": "https://www.ketofocus.com/recipes/keto-avocado-toast/",
        "Pork Sausage & Spinach Scramble": "https://www.ruled.me/sausage-spinach-feta-omelette/",
        "Beef Mince Omelette": "https://www.snapcalorie.com/recipes/keto_hamburger_omelette.html"
    },
    "Lunch/Dinner": {
        "Garlic Butter Salmon": "https://www.dietdoctor.com/recipes/pan-seared-salmon-with-garlic-butter",
        "Beef & Broccoli Stir-fry": "https://www.dietdoctor.com/recipes/keto-beef-and-broccoli-stir-fry",
        "Creamy Pork Chops": "https://www.dietdoctor.com/recipes/keto-pork-chops-with-creamy-garlic-sauce"
    }
}

med_recipes = {
    "Breakfast": {
        "Greek Omelette": "https://www.themediterraneandish.com/greek-omelet-recipe/",
        "Avocado Sourdough Toast": "https://www.themediterraneandish.com/avocado-toast-recipe/"
    },
    "Lunch/Dinner": {
        "Greek Lemon Fish": "https://thouseshop.com/blogs/recipe/mediterranean-baked-fish-with-lemon-and-herbs",
        "Chickpea & Tuna Salad": "https://www.olivetomato.com/5-minute-mediterranean-chickpea-tuna-salad/",
        "Chicken Cacciatore": "https://www.themediterraneandish.com/chicken-cacciatore-recipe/"
    }
}

recipes = keto_recipes if diet == "Keto (Diabetes)" else med_recipes
category = st.selectbox("Select Meal Time:", list(recipes.keys()))
choice = st.selectbox("Pick a Dish:", list(recipes[category].keys()))

st.success(f"👉 [Click here for the full {choice} Recipe & Method]({recipes[category][choice]})")

# --- VITALS TRACKER ---
st.divider()
st.header("📊 Vitals & Accountability")
c1, c2 = st.columns(2)
with c1:
    w = st.number_input("Weight (kg)", value=0.0, format="%.1f")
    bs = st.number_input("Blood Sugar (mmol/L)", value=0.0, format="%.1f")
with c2:
    bps = st.number_input("BP Systolic (Top)", value=0)
    bpd = st.number_input("BP Diastolic (Bottom)", value=0)

if st.button("Log Stats"):
    st.balloons()
    st.write(f"🌟 Great job {user}! Data logged for your August Medical.")
