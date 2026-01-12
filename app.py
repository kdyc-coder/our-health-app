import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Keifer & Vonnie's Health Hub", page_icon="🎋")

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

# --- MAIN INTERFACE ---
st.title("🎋 Keifer & Vonnie's Command Centre")
user = st.radio("Who is checking in?", ["Keifer", "Vonnie"])

# --- EXERCISE HUB (Tai Chi + Resistance) ---
st.divider()
st.header("💪 Exercise & Joint Support")
with st.expander("🧘 Tai Chi Walking & Home Strength Routine"):
    st.subheader("1. Tai Chi Focus")
    st.video("https://www.youtube.com/watch?v=38tqFjB-o-g")
    if user == "Vonnie":
        st.warning("🦶 **Vonnie's Foot Care:** Focus on the 'Roll' (Heel-Arch-Toe). Calf raises are your best friend today!")
    
    st.subheader("2. Home Resistance Circuit")
    st.markdown("""
    **Perform this circuit 2-3 times per week to build muscle for the medical:**
    
    * **Wall Push-ups (Chest/Arms):** Stand arm's length from a wall. Place hands flat. Lower your chest toward the wall and push back. *Easier on shoulders than floor push-ups.*
    * **Chair Squats (Legs/Glutes):** Stand in front of a sturdy chair. Lower your hips until you just touch the seat, then stand back up. *No hands if you can!*
    * **Calf Raises (Lower Leg/Foot Health):** Hold a wall for balance. Rise onto your toes, hold for 1 second, then lower. *Crucial for Vonnie's plantar fasciitis.*
    * **Counter-top Rows (Back):** Hold the edge of a heavy table or kitchen counter. Lean back slightly with straight arms, then pull your chest toward the counter.
    * **The 'Medical Walk':** 10 minutes of brisk walking, focusing on deep breathing and upright posture.
    """)

# --- THE FAMILY VAULT (Custom Recipes) ---
st.divider()
st.header("🍯 The Family Vault")
st.write(f"Add your own 'House Favourites' here, {user}.")
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
    new_essential = st.text_input("Add New Essential")
    if st.button("Add to List"):
        st.session_state['essentials'].append(new_essential)
    st.write(f"**Current Essentials:** {', '.join(st.session_state['essentials'])}")

col1, col2 = st.columns(2)
with col1:
    mon, tue, wed = st.text_input("Mon Dinner"), st.text_input("Tue Dinner"), st.text_input("Wed Dinner")
with col2:
    thu, fri, sat = st.text_input("Thu Dinner"), st.text_input("Fri Dinner"), st.text_input("Sat Dinner")
sun = st.text_input("Sun Dinner")

if st.button("🚀 Generate 'Our Groceries' List"):
    full_list = st.session_state['essentials'] + [mon, tue, wed, thu, fri, sat, sun]
    clean_list = [item for item in full_list if item.strip()]
    st.subheader("Your Shopping List")
    st.code("\n".join(clean_list))
    st.success("Copy the list above and paste it into 'Our Groceries'!")

# --- MASTER COOKBOOK ---
st.divider()
st.header("📖 Master Cookbook")
diet = st.radio("Diet Plan:", ["Keto (Diabetes Focus)", "Mediterranean (BP Focus)"])
meal_time = st.selectbox("Meal Type:", ["Breakfast", "Lunch", "Dinner"])

recipe_db = {
    "Keto (Diabetes Focus)": {
        "Breakfast": {"Bacon & Egg Cups": "https://www.dietdoctor.com/recipes/keto-bacon-and-egg-cups", "Salmon Avocado Smash": "https://www.ketofocus.com/recipes/keto-avocado-toast/", "Pork Sausage Scramble": "https://www.ruled.me/sausage-spinach-feta-omelette/", "Beef Mince Omelette": "https://diethood.com/ground-beef-omelet/", "Steak and Eggs": "https://www.dietdoctor.com/recipes/keto-steak-and-eggs", "Pork Belly & Eggs": "https://www.fatforweightloss.com.au/crispy-pork-belly/", "Bulletproof Coffee": "https://www.bulletproof.com/recipes/bulletproof-diet-recipes/bulletproof-coffee-official-recipe/", "Chicken Frittata": "https://www.lowcarbmaven.com/chicken-spinach-frittata/", "Smoked Salmon Scramble": "https://www.dietdoctor.com/recipes/keto-smoked-salmon-scrambled-eggs", "Ham & Cheese Muffins": "https://www.allrecipes.com/recipe/221081/ham-and-egg-muffins/"},
        "Lunch": {"Chicken Caesar": "https://www.dietdoctor.com/recipes/keto-chicken-caesar-salad", "Pork Belly Slaw": "https://www.ruled.me/keto-pork-belly-cabbage-slaw/", "Beef Taco Wraps": "https://www.dietdoctor.com/recipes/keto-beef-tacos", "Salmon Salad Bowls": "https://www.wholesomeyum.com/recipes/keto-salmon-salad/", "Bunless Burgers": "https://www.dietdoctor.com/recipes/the-keto-burger", "Chicken Cucumber Boats": "https://www.dietdoctor.com/recipes/keto-chicken-salad-with-cucumber", "Cold Pork Roast": "https://www.dietdoctor.com/recipes/pork-roast-with-crackling", "Beef Meatballs": "https://www.ruled.me/keto-beef-meatballs/", "Tuna Avocado Salad": "https://www.dietdoctor.com/recipes/keto-tuna-salad-with-avocado", "Pork Rind Chicken": "https://www.ruled.me/keto-pork-rind-crusted-chicken/"},
        "Dinner": {"Garlic Butter Salmon": "https://www.dietdoctor.com/recipes/pan-seared-salmon-with-garlic-butter", "Beef & Broccoli": "https://www.dietdoctor.com/recipes/keto-beef-and-broccoli-stir-fry", "Parmesan Pork Chops": "https://www.dietdoctor.com/recipes/keto-pork-chops-with-creamy-garlic-sauce", "Chicken Thighs": "https://www.dietdoctor.com/recipes/keto-roasted-chicken-thighs-with-zucchini", "Baked White Fish": "https://www.dietdoctor.com/recipes/keto-baked-white-fish-with-lemon-and-butter", "Pork Stir-fry": "https://www.dietdoctor.com/recipes/keto-pork-stir-fry", "Steak & Mushrooms": "https://www.dietdoctor.com/recipes/keto-steak-with-garlic-mushrooms", "Lemon Pepper Wings": "https://www.dietdoctor.com/recipes/keto-chicken-wings-with-lemon-pepper", "Shepherd’s Pie": "https://www.dietdoctor.com/recipes/keto-shepherds-pie", "Pork Loin Roast": "https://www.dietdoctor.com/recipes/keto-roast-pork-loin"}
    },
    "Mediterranean (BP Focus)": {
        "Breakfast": {"Greek Omelette": "https://www.themediterraneandish.com/greek-omelet-recipe/", "Avocado Sourdough": "https://www.themediterraneandish.com/avocado-toast-recipe/", "Yogurt & Walnuts": "https://www.olivetomato.com/greek-yogurt-with-honey-and-walnuts/", "Berry Oats": "https://www.themediterraneandish.com/overnight-oats-recipe/", "Salmon & Feta": "https://www.olivetomato.com/smoked-salmon-and-feta-breakfast/", "Spinach Frittata": "https://www.themediterraneandish.com/spinach-frittata-recipe/", "Whole Wheat Pancakes": "https://www.themediterraneandish.com/healthy-pancakes-recipe/", "Chickpea Hash": "https://www.themediterraneandish.com/chickpea-hash-recipe/", "Poached Eggs": "https://www.olivetomato.com/mediterranean-poached-eggs/", "Cottage Cheese & Cucumber": "https://www.eatingwell.com/recipe/267868/cottage-cheese-with-cucumber-tomato/"},
        "Lunch": {"Chickpea Tuna Salad": "https://www.olivetomato.com/5-minute-mediterranean-chickpea-tuna-salad/", "Classic Greek Salad": "https://www.themediterraneandish.com/traditional-greek-salad-recipe/", "Chicken Hummus Wrap": "https://www.themediterraneandish.com/chicken-hummus-wrap-recipe/", "Quinoa Salad": "https://www.themediterraneandish.com/mediterranean-quinoa-salad-recipe/", "Lentil Soup": "https://www.themediterraneandish.com/red-lentil-soup-recipe/", "Salmon Souvlaki": "https://www.themediterraneandish.com/salmon-souvlaki-salad/", "Beef Skewers": "https://www.themediterraneandish.com/beef-kabobs-recipe/", "Pork Wraps": "https://www.themediterraneandish.com/pork-souvlaki-recipe/", "Quinoa Tabbouleh": "https://www.themediterraneandish.com/tabbouleh-recipe/", "Tuna Salad (No Mayo)": "https://www.themediterraneandish.com/mediterranean-tuna-salad/"},
        "Dinner": {"Greek Lemon Fish": "https://www.themediterraneandish.com/baked-fish-recipe-mediterranean-style/", "Chicken Cacciatore": "https://www.themediterraneandish.com/chicken-cacciatore-recipe/", "Baked Salmon": "https://www.themediterraneandish.com/easy-baked-salmon-recipe-mediterranean-style/", "Pork Souvlaki": "https://www.themediterraneandish.com/pork-souvlaki-recipe/", "Beef & Veg Kebabs": "https://www.themediterraneandish.com/beef-kabobs-recipe/", "Garlic Chicken": "https://www.themediterraneandish.com/mediterranean-garlic-chicken/", "Pasta Primavera": "https://www.eatingwell.com/recipe/250233/pasta-primavera/", "Sheet Pan Pork": "https://www.themediterraneandish.com/sheet-pan-pork-chops-vegetables/", "Grilled Beef": "https://www.olivetomato.com/mediterranean-grilled-steak-with-asparagus/", "Tuna Niçoise": "https://www.themediterraneandish.com/nicoise-salad-recipe/"}
    }
}

options = recipe_db[diet][meal_time]
choice = st.selectbox(f"Choose a {meal_time} recipe:", list(options.keys()))
st.success(f"### [👉 Click here for {choice} Recipe]({options[choice]})")

# --- VITALS TRACKER ---
st.divider()
st.header("📊 Vitals & Accountability")
c1, c2 = st.columns(2)
with c1:
    w = st.number_input("Weight (kg)", value=0.0, format="%.1f")
    bs = st.number_input("Blood Sugar (mmol/L)", value=0.0, format="%.1f")
with c2:
    bps, bpd = st.number_input("BP Systolic", value=0), st.number_input("BP Diastolic", value=0)

if st.button("Log Stats"):
    st.balloons()
    st.write(f"🌟 **Good on ya, {user}!** Data captured. Let's keep those numbers steady for August!")
