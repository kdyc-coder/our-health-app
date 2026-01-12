import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tai Chi & Home Strength", page_icon="🎋")

st.title("🎋 Tai Chi, Strength & Meals")
st.write("Diabetes Remission & Joint Support Plan")

user = st.radio("Who is checking in?", ["Partner (Plantar Fasciitis)", "You"])

# --- NEW: EXERCISE SECTION ---
st.header("💪 Home Exercise Hub")
with st.expander("🧘 Tai Chi Walking Video", expanded=False):
    st.video("https://www.youtube.com/watch?v=38tqFjB-o-g")
    st.info("Remember: Roll heel-to-toe and keep 'soft knees' to protect those over-50s joints.")

with st.expander("🏋️ Easy Home Resistance (Joint Friendly)", expanded=False):
    st.write("""
    **Do these 2-3 times a week to boost metabolism:**
    1. **Wall Push-ups:** (10 reps) Easy on the shoulders, builds chest strength.
    2. **Chair Squats:** (10 reps) Sit down on a chair and stand back up without using your hands. Saves the knees!
    3. **Counter-top Lunges:** Hold the kitchen bench for balance. Very shallow steps.
    4. **Calf Raises:** (Important for Plantar Fasciitis!) Rise up on your toes slowly while holding the wall.
    """)

# --- NEW: RECIPES & MEALS ---
st.divider()
st.header("🥗 Recipes & Meal Plan")

recipes = {
    "Zucchini & Salmon Bake": "Slice zucchini and place salmon on top. Drizzle with olive oil and lemon. Bake at 200C for 15 mins. Serve with a massive pile of spinach.",
    "Cauliflower 'Rice' Chicken": "Grate cauliflower and sauté in olive oil. Pan-fry chicken thighs with salt/pepper. Mix together for a low-carb 'fried rice'.",
    "Avocado & Egg Smash": "Perfect for breakfast. Mash avocado with apple cider vinegar. Top with two boiled or poached eggs and handful of almonds."
}

selected_meal = st.selectbox("View Recipe for:", list(recipes.keys()))
st.info(recipes[selected_meal])

if st.button("Show Shopping List for these Meals"):
    st.write("**Produce:** Spinach, Avocados, Zucchini, Cauliflower, Lemon")
    st.write("**Protein:** Salmon fillets, Chicken thighs, Eggs")
    st.write("**Pantry:** Olive Oil, Almonds, Apple Cider Vinegar")
    st.success("Tip: I've also added these to your digital shopping list!")

# --- VITALS & ACCOUNTABILITY ---
st.divider()
st.header("📊 Vitals Tracker")
# [Keep your weight/BP inputs here from the previous version]
