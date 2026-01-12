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
        st.warning("🦶 **Vonnie's Foot Care:** Roll your foot over a cold bottle after walking. Focus on the 'Heel-Arch-Toe' roll.")
    st.markdown("**Tai Chi Walking:** Slow weight transfer, soft knees, and level hips.")
    

# --- THE BIG COOKBOOK ---
st.divider()
st.header("📖 The Digital Cookbook (60+ Options)")
diet = st.radio("Select Diet Plan:", ["Keto (Diabetes Focus)", "Mediterranean (BP Focus)"])
meal_time = st.selectbox("Meal Type:", ["Breakfast", "Lunch", "Dinner"])

# FULL RECIPE DATABASE
recipe_db = {
    "Keto (Diabetes Focus)": {
        "Breakfast": {
            "Bacon & Egg Cups": "https://www.dietdoctor.com/recipes/keto-bacon-and-egg-cups",
            "Salmon Avocado Smash": "https://www.ketofocus.com/recipes/keto-avocado-toast/",
            "Pork Sausage Scramble": "https://www.ruled.me/sausage-spinach-feta-omelette/",
            "Beef Mince Omelette": "https://diethood.com/ground-beef-omelet/",
            "Steak and Eggs": "https://www.dietdoctor.com/recipes/keto-steak-and-eggs",
            "Pork Belly & Fried Eggs": "https://www.fatforweightloss.com.au/crispy-pork-belly/",
            "Bulletproof Coffee & Eggs": "https://www.bulletproof.com/recipes/bulletproof-diet-recipes/bulletproof-coffee-official-recipe/",
            "Chicken & Spinach Frittata": "https://www.lowcarbmaven.com/chicken-spinach-frittata/",
            "Smoked Salmon Scramble": "https://www.dietdoctor.com/recipes/keto-smoked-salmon-scrambled-eggs",
            "Ham and Cheese Egg Muffins": "https://www.allrecipes.com/recipe/221081/ham-and-egg-muffins/"
        },
        "Lunch": {
            "Chicken Caesar (No Croutons)": "https://www.dietdoctor.com/recipes/keto-chicken-caesar-salad",
            "Pork Belly Slaw": "https://www.ruled.me/keto-pork-belly-cabbage-slaw/",
            "Beef Taco Lettuce Wraps": "https://www.dietdoctor.com/recipes/keto-beef-tacos",
            "Salmon Salad Bowls": "https://www.wholesomeyum.com/recipes/keto-salmon-salad/",
            "Bunless Beef Burgers": "https://www.dietdoctor.com/recipes/the-keto-burger",
            "Chicken Mayo Cucumber Boats": "https://www.dietdoctor.com/recipes/keto-chicken-salad-with-cucumber",
            "Cold Pork Roast & Mayo": "https://www.dietdoctor.com/recipes/pork-roast-with-crackling",
            "Beef Meatball Skewers": "https://www.ruled.me/keto-beef-meatballs/",
            "Tuna Avocado Salad": "https://www.dietdoctor.com/recipes/keto-tuna-salad-with-avocado",
            "Pork Rind Crusted Chicken": "https://www.ruled.me/keto-pork-rind-crusted-chicken/"
        },
        "Dinner": {
            "Garlic Butter Salmon": "https://www.dietdoctor.com/recipes/pan-seared-salmon-with-garlic-butter",
            "Beef & Broccoli Stir-fry": "https://www.dietdoctor.com/recipes/keto-beef-and-broccoli-stir-fry",
            "Creamy Parmesan Pork Chops": "https://www.dietdoctor.com/recipes/keto-pork-chops-with-creamy-garlic-sauce",
            "Chicken Thighs & Zucchini": "https://www.dietdoctor.com/recipes/keto-roasted-chicken-thighs-with-zucchini",
            "Baked White Fish": "https://www.dietdoctor.com/recipes/keto-baked-white-fish-with-lemon-and-butter",
            "Pork Stir-fry with Peppers": "https://www.dietdoctor.com/recipes/keto-pork-stir-fry",
            "Steak & Garlic Mushrooms": "https://www.dietdoctor.com/recipes/keto-steak-with-garlic-mushrooms",
            "Lemon Pepper Chicken Wings": "https://www.dietdoctor.com/recipes/keto-chicken-wings-with-lemon-pepper",
            "Cauliflower Shepherd’s Pie": "https://www.dietdoctor.com/recipes/keto-shepherds-pie",
            "Pork Loin Roast": "https://www.dietdoctor.com/recipes/keto-roast-pork-loin"
        }
    },
    "Mediterranean (BP Focus)": {
        "Breakfast": {
            "Greek Omelette": "https://www.themediterraneandish.com/greek-omelet-recipe/",
            "Avocado Sourdough Toast": "https://www.themediterraneandish.com/avocado-toast-recipe/",
            "Greek Yogurt & Walnuts": "https://www.olivetomato.com/greek-yogurt-with-honey-and-walnuts/",
            "Oats with Fresh Berries": "https://www.themediterraneandish.com/overnight-oats-recipe/",
            "Smoked Salmon & Feta": "https://www.olivetomato.com/smoked-salmon-and-feta-breakfast/",
            "Spinach & Tomato Frittata": "https://www.themediterraneandish.com/spinach-frittata-recipe/",
            "Whole Wheat Blueberry Pancakes": "https://www.themediterraneandish.com/healthy-pancakes-recipe/",
            "Chickpea Breakfast Hash": "https://www.themediterraneandish.com/chickpea-hash-recipe/",
            "Poached Eggs & Asparagus": "https://www.olivetomato.com/mediterranean-poached-eggs/",
            "Cottage Cheese & Cucumber": "https://www.eatingwell.com/recipe/267868/cottage-cheese-with-cucumber-tomato/"
        },
        "Lunch": {
            "Chickpea & Tuna Salad": "https://www.olivetomato.com/5-minute-mediterranean-chickpea-tuna-salad/",
            "Classic Greek Salad": "https://www.themediterraneandish.com/traditional-greek-salad-recipe/",
            "Chicken & Hummus Wrap": "https://www.themediterraneandish.com/chicken-hummus-wrap-recipe/",
            "Quinoa & Roasted Veg": "https://www.themediterraneandish.com/mediterranean-quinoa-salad-recipe/",
            "Lentil & Vegetable Soup": "https://www.themediterraneandish.com/red-lentil-soup-recipe/",
            "Salmon Souvlaki Salad": "https://www.themediterraneandish.com/salmon-souvlaki-salad/",
            "Beef & Pepper Skewers": "https://www.themediterraneandish.com/beef-kabobs-recipe/",
            "Mediterranean Pork Wraps": "https://www.themediterraneandish.com/pork-souvlaki-recipe/",
            "Quinoa Tabbouleh": "https://www.themediterraneandish.com/tabbouleh-recipe/",
            "Tuna Salad (No Mayo)": "https://www.themediterraneandish.com/mediterranean-tuna-salad/"
        },
        "Dinner": {
            "Greek Lemon Fish": "https://www.themediterraneandish.com/baked-fish-recipe-mediterranean-style/",
            "Chicken Cacciatore": "https://www.themediterraneandish.com/chicken-cacciatore-recipe/",
            "Mediterranean Baked Salmon": "https://www.themediterraneandish.com/easy-baked-salmon-recipe-mediterranean-style/",
            "Pork Souvlaki": "https://www.themediterraneandish.com/pork-souvlaki-recipe/",
            "Beef & Veggie Kebabs": "https://www.themediterraneandish.com/beef-kabobs-recipe/",
            "Garlic Chicken & Quinoa": "https://www.themediterraneandish.com/mediterranean-garlic-chicken/",
            "Whole Wheat Pasta Primavera": "https://www.eatingwell.com/recipe/250233/pasta-primavera/",
            "Sheet Pan Pork & Vegies": "https://www.themediterraneandish.com/sheet-pan-pork-chops-vegetables/",
            "Grilled Beef & Asparagus": "https://www.olivetomato.com/mediterranean-grilled-steak-with-asparagus/",
            "Tuna Niçoise Salad": "https://www.themediterraneandish.com/nicoise-salad-recipe/"
        }
    }
}

# Display logic
current_options = recipe_db[diet][meal_time]
choice = st.selectbox(f"Choose one of your 10 {meal_time} options:", list(current_options.keys()))

st.success(f"### [👉 Click here for the full {choice} Recipe & Instructions]({current_options[choice]})")
st.info("This link will show you the exact quantities (servings) and step-by-step methods.")

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
    st.write(f"🌟 **Genuine Praise:** Great work, {user}! You're building the habit. Only {m_days} days to the Medical!")
