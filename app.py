import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Keifer & Partner's Health Hub", page_icon="🎋")

# --- INITIALISE MEMORY ---
if 'custom_recipes' not in st.session_state:
    st.session_state['custom_recipes'] = {}
if 'essentials' not in st.session_state:
    st.session_state['essentials'] = ["Milk", "Butter", "Coffee", "Water", "Toilet Paper", "Bread"]

# --- SIDEBAR ---
st.sidebar.header("⏳ Key Deadlines")
med_date = datetime(2026, 8, 1)
m_days = (med_date - datetime.now()).days
st.sidebar.warning(f"🚨 {m_days} Days to Keifer's Medical")

retire_date = datetime(2038, 9, 1)
r_days = (retire_date - datetime.now()).days
st.sidebar.info(f"🗓️ {r_days:,} Days to Retirement")

# --- MAIN INTERFACE ---
st.title("🎋 Keifer & Partner's Command Centre")
user = st.radio("Who is checking in?", ["Keifer", "Your Partner"])

# --- EXERCISE HUB ---
st.divider()
st.header("💪 Exercise & Joint Support")
with st.expander("🧘 Tai Chi Walking & Home Strength"):
    st.video("https://www.youtube.com/watch?v=38tqFjB-o-g")
    if user == "Your Partner":
        st.warning("🦶 **Partner's Foot Care:** Focus on the 'Roll' (Heel-Arch-Toe). Calf raises are your best friend today!")
    st.markdown("""
    **Routine (2-3x per week):**
    1. **Wall Push-ups:** 10 reps (Shoulder friendly).
    2. **Chair Squats:** 10 reps (No hands!).
    3. **Calf Raises:** 15 reps (Essential for Plantar Fasciitis).
    """)

# --- THE FAMILY VAULT (Custom Recipes) ---
st.divider()
st.header("🍯 The Family Vault")
st.write("Add your own 'House Favourites' here.")
with st.expander("➕ Add a New Recipe"):
    new_name = st.text_input("Recipe Name")
    new_method = st.text_area("Paste Ingredients/Method or Website Link here")
    if st.button("Save to Vault"):
        if new_name and new_method:
            st.session_state['custom_recipes'][new_name] = new_method
            st.success(f"Saved {new_name} to the vault!")

if st.session_state['custom_recipes']:
    view_custom = st.selectbox("View Custom Recipes:", ["Select..."] + list(st.session_state['custom_recipes'].keys()))
    if view_custom != "Select...":
        st.info(f"**Instructions for {view_custom}:**\n\n{st.session_state['custom_recipes'][view_custom]}")

# --- WEEKLY PLANNER & GROCERY BRIDGE ---
st.divider()
st.header("📋 Weekly Planner & Shopping")

with st.expander("🛒 Manage Weekly Essentials"):
    new_essential = st.text_input("Add New Essential (e.g. Eggs)")
    if st.button("Add to List"):
        st.session_state['essentials'].append(new_essential)
    st.write(f"**Current Essentials:** {', '.join(st.session_state['essentials'])}")

# The Planning Grid
col1, col2 = st.columns(2)
with col1:
    mon = st.text_input("Monday Dinner")
    tue = st.text_input("Tuesday Dinner")
    wed = st.text_input("Wednesday Dinner")
with col2:
    thu = st.text_input("Thursday Dinner")
    fri = st.text_input("Friday Dinner")
    sat = st.text_input("Saturday Dinner")
sun = st.text_input("Sunday Dinner")

if st.button("🚀 Generate 'Our Groceries' List"):
    full_list = st.session_state['essentials'] + [mon, tue, wed, thu, fri, sat, sun]
    clean_list = [item for item in full_list if item.strip()]
    
    st.subheader("Your Shopping List")
    list_str = "\n".join(clean_list)
    st.code(list_str)
    st.success("Copy the text above and paste it into 'Our Groceries'!")

# --- MASTER COOKBOOK (The 60 Recipes) ---
st.divider()
st.header("📖 Master Cookbook")
diet = st.radio("Diet Plan:", ["Keto (Diabetes Focus)", "Mediterranean (BP Focus)"])
meal_time = st.selectbox("Meal Type:", ["Breakfast", "Lunch", "Dinner"])

# Condensed database for space
recipe_db = {
    "Keto (Diabetes Focus)": {
        "Breakfast": {"Bacon & Egg Cups": "https://www.dietdoctor.com/recipes/keto-bacon-and-egg-cups", "Salmon Avocado Smash": "https://www.ketofocus.com/recipes/keto-avocado-toast/"},
        "Lunch": {"Chicken Caesar": "https://www.dietdoctor.com/recipes/keto-chicken-caesar-salad", "Beef Taco Wraps": "https://www.dietdoctor.com/recipes/keto-beef-tacos"},
        "Dinner": {"Garlic Butter Salmon": "https://www.dietdoctor.com/recipes/pan-seared-salmon-with-garlic-butter", "Beef & Broccoli": "https://www.dietdoctor.com/recipes/keto-beef-and-broccoli-stir-fry"}
    },
    "Mediterranean (BP Focus)": {
        "Breakfast": {"Greek Omelette": "https://www.themediterraneandish.com/greek-omelet-recipe/", "Avocado Sourdough": "https://www.themediterraneandish.com/avocado-toast-recipe/"},
        "Lunch": {"Chickpea Tuna Salad": "https://www.olivetomato.com/5-minute-mediterranean-chickpea-tuna-salad/", "Classic Greek Salad": "https://www.themediterraneandish.com/traditional-greek-salad-recipe/"},
        "Dinner": {"Greek Lemon Fish": "https://www.themediterraneandish.com/baked-fish-recipe-mediterranean-style/", "Chicken Cacciatore": "https://www.themediterraneandish.com/chicken-cacciatore-recipe/"}
    }
}

options = recipe_db[diet][meal_time]
choice = st.selectbox(f"Choose a {meal_time} recipe:", list(options.keys()))
st.info(f"### [👉 Click here for {choice} Recipe]({options[choice]})")
