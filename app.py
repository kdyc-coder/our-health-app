import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Keifer & Vonnie's Health Hub", page_icon="🎋")

# --- 1. THE SMART INGREDIENT ENGINE ---
ingredients_map = {
    # KETO BREAKFAST
    "Bacon & Egg Cups": ["Bacon", "Eggs", "Salt", "Pepper"],
    "Salmon Avocado Smash": ["Smoked Salmon", "Avocado", "Lemon", "Low-carb bread"],
    "Pork Sausage Scramble": ["Pork Sausages", "Eggs", "Spinach"],
    "Beef Mince Omelette": ["Beef Mince", "Eggs", "Onion", "Cheese"],
    "Steak and Eggs": ["Steak", "Eggs", "Butter"],
    "Pork Belly & Eggs": ["Pork Belly", "Eggs"],
    "Bulletproof Coffee": ["Coffee Beans", "Grass-fed Butter", "MCT Oil"],
    "Chicken Frittata": ["Chicken", "Eggs", "Spinach", "Feta"],
    "Smoked Salmon Scramble": ["Smoked Salmon", "Eggs", "Cream Cheese"],
    "Ham & Cheese Muffins": ["Ham", "Eggs", "Cheese"],
    # KETO LUNCH
    "Chicken Caesar": ["Chicken Breast", "Cos Lettuce", "Parmesan", "Caesar Dressing"],
    "Pork Belly Slaw": ["Pork Belly", "Cabbage", "Mayo", "Apple Cider Vinegar"],
    "Beef Taco Wraps": ["Beef Mince", "Lettuce", "Taco Spice", "Sour Cream"],
    "Salmon Salad Bowls": ["Salmon", "Mixed Greens", "Cucumber", "Olive Oil"],
    "Bunless Burgers": ["Beef Patties", "Lettuce", "Tomato", "Cheese", "Pickles"],
    "Chicken Cucumber Boats": ["Chicken", "Cucumbers", "Mayo", "Dill"],
    "Cold Pork Roast": ["Pork Roast", "Mustard"],
    "Beef Meatballs": ["Beef Mince", "Parmesan", "Garlic", "Zucchini"],
    "Tuna Avocado Salad": ["Canned Tuna", "Avocado", "Red Onion"],
    "Pork Rind Chicken": ["Chicken Thighs", "Pork Rinds", "Eggs"],
    # KETO DINNER
    "Garlic Butter Salmon": ["Salmon Fillets", "Butter", "Garlic", "Asparagus"],
    "Beef & Broccoli": ["Beef Strips", "Broccoli", "Soy Sauce", "Ginger"],
    "Parmesan Pork Chops": ["Pork Chops", "Parmesan", "Garlic", "Heavy Cream"],
    "Chicken Thighs": ["Chicken Thighs", "Zucchini", "Lemon", "Thyme"],
    "Baked White Fish": ["White Fish Fillets", "Butter", "Lemon", "Parsley"],
    "Pork Stir-fry": ["Pork Strips", "Capsicum", "Soy Sauce", "Sesame Oil"],
    "Steak & Mushrooms": ["Steak", "Mushrooms", "Butter", "Garlic"],
    "Lemon Pepper Wings": ["Chicken Wings", "Lemon", "Black Pepper"],
    "Shepherd’s Pie": ["Beef Mince", "Cauliflower", "Onion", "Beef Stock"],
    "Pork Loin Roast": ["Pork Loin", "Garlic", "Rosemary", "Green Beans"],
    # MEDITERRANEAN BREAKFAST
    "Greek Omelette": ["Eggs", "Feta", "Spinach", "Olives"],
    "Avocado Sourdough": ["Avocado", "Sourdough Bread", "Chilli Flakes"],
    "Yogurt & Walnuts": ["Greek Yogurt", "Walnuts", "Honey"],
    "Berry Oats": ["Rolled Oats", "Mixed Berries", "Almond Milk"],
    "Salmon & Feta": ["Smoked Salmon", "Feta", "Whole Grain Toast"],
    "Spinach Frittata": ["Eggs", "Spinach", "Onion", "Olive Oil"],
    "Whole Wheat Pancakes": ["Whole Wheat Flour", "Eggs", "Milk", "Blueberries"],
    "Chickpea Hash": ["Canned Chickpeas", "Onion", "Capsicum", "Poached Egg"],
    "Poached Eggs": ["Eggs", "Whole Grain Toast", "Tomato"],
    "Cottage Cheese & Cucumber": ["Cottage Cheese", "Cucumber", "Walnuts"],
    # MEDITERRANEAN LUNCH
    "Chickpea Tuna Salad": ["Canned Tuna", "Canned Chickpeas", "Red Onion", "Lemon"],
    "Classic Greek Salad": ["Cucumber", "Tomato", "Feta", "Olives", "Red Onion"],
    "Chicken Hummus Wrap": ["Chicken", "Hummus", "Whole Wheat Wrap", "Cucumber"],
    "Quinoa Salad": ["Quinoa", "Cucumber", "Tomato", "Feta", "Parsley"],
    "Lentil Soup": ["Canned Lentils", "Carrots", "Onion", "Celery", "Tomato Paste"],
    "Salmon Souvlaki": ["Salmon", "Mixed Greens", "Tzatziki", "Lemon"],
    "Beef Skewers": ["Beef Cubes", "Capsicum", "Onion", "Olive Oil"],
    "Pork Wraps": ["Pork Strips", "Whole Wheat Wrap", "Tzatziki", "Tomato"],
    "Quinoa Tabbouleh": ["Quinoa", "Parsley", "Mint", "Tomato", "Lemon"],
    "Tuna Salad (No Mayo)": ["Canned Tuna", "Olive Oil", "Celery", "Red Onion"],
    # MEDITERRANEAN DINNER
    "Greek Lemon Fish": ["White Fish Fillets", "Lemon", "Oregano", "Olive Oil", "Potatoes"],
    "Chicken Cacciatore": ["Chicken Thighs", "Canned Tomatoes", "Capsicum", "Mushrooms"],
    "Baked Salmon": ["Salmon Fillets", "Lemon", "Dill", "Asparagus"],
    "Pork Souvlaki": ["Pork Cubes", "Lemon", "Garlic", "Greek Salad"],
    "Beef & Veg Kebabs": ["Beef Cubes", "Zucchini", "Capsicum", "Onion"],
    "Garlic Chicken": ["Chicken Breast", "Garlic", "Olive Oil", "Green Beans"],
    "Pasta Primavera": ["Whole Wheat Pasta", "Zucchini", "Peas", "Parmesan"],
    "Sheet Pan Pork": ["Pork Chops", "Sweet Potato", "Broccoli"],
    "Grilled Beef": ["Steak", "Asparagus", "Olive Oil"],
    "Tuna Niçoise": ["Canned Tuna", "Green Beans", "Boiled Egg", "Potatoes", "Olives"]
}

# --- 2. INITIALISE MEMORY ---
if 'custom_recipes' not in st.session_state:
    st.session_state['custom_recipes'] = {}
if 'essentials' not in st.session_state:
    st.session_state['essentials'] = ["Milk", "Butter", "Coffee", "Water", "Toilet Paper", "Bread"]

# --- 3. SIDEBAR ---
st.sidebar.header("⏳ Key Deadlines")
med_date = datetime(2026, 8, 1)
m_days = (med_date - datetime.now()).days
st.sidebar.warning(f"🚨 {m_days} Days to Keifer's Medical")

# --- 4. MAIN INTERFACE ---
st.title("🎋 Keifer & Vonnie's Command Centre")
user = st.radio("Who is checking in?", ["Keifer", "Vonnie"])

# --- 5. EXERCISE HUB ---
st.divider()
st.header("💪 Exercise & Joint Support")
with st.expander("🧘 Tai Chi & Resistance Training"):
    st.subheader("1. Tai Chi Walking (Manual Guide)")
    st.markdown("**The 'Heel-to-Toe' Roll:** Lift heel, roll to arch, ball of foot. Breathe deeply.")
    st.video("https://www.youtube.com/watch?v=38tqFjB-o-g")
    st.subheader("2. Daily Strength Checklist")
    col_a, col_b = st.columns(2)
    with col_a:
        ex1, ex2 = st.checkbox("Wall Push-ups (10)"), st.checkbox("Chair Squats (10)")
    with col_b:
        ex3, ex4 = st.checkbox("Calf Raises (15)"), st.checkbox("Counter Rows (10)")
    if ex1 and ex2 and ex3 and ex4: st.success("🔥 Full Circuit Complete!")

# --- 6. THE FAMILY VAULT ---
st.divider()
st.header("🍯 The Family Vault")
with st.expander("➕ Add a New Recipe"):
    new_name = st.text_input("Recipe Name")
    new_method = st.text_area("Paste Ingredients/Method")
    if st.button("Save to Vault"):
        if new_name and new_method:
            st.session_state['custom_recipes'][new_name] = new_method
            st.success(f"Saved {new_name}!")

# --- 7. SMART WEEKLY PLANNER ---
st.divider()
st.header("📅 Smart Weekly Planner")
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
all_options = ["None"] + sorted(list(ingredients_map.keys())) + sorted(list(st.session_state['custom_recipes'].keys()))

planned_meals = {}
for day in days:
    with st.expander(f"📍 {day} Meals"):
        b = st.selectbox(f"Breakfast ({day})", all_options, key=f"b_{day}")
        l = st.selectbox(f"Lunch ({day})", all_options, key=f"l_{day}")
        d = st.selectbox(f"Dinner ({day})", all_options, key=f"d_{day}")
        planned_meals[day] = [b, l, d]

# --- 8. GROCERY GENERATOR ---
st.divider()
st.header("🛒 Shopping List Bridge")
with st.expander("📝 Manage Weekly Essentials"):
    new_ess = st.text_input("Add Essential Item")
    if st.button("Add to Essentials"):
        st.session_state['essentials'].append(new_ess)
    st.write(f"Common items: {', '.join(st.session_state['essentials'])}")

if st.button("🚀 Generate 'Our Groceries' List"):
    shopping_set = set(st.session_state['essentials'])
    for day in planned_meals:
        for meal in planned_meals[day]:
            if meal in ingredients_map:
                for item in ingredients_map[meal]:
                    shopping_set.add(item)
            elif meal in st.session_state['custom_recipes']:
                shopping_set.add(meal)
    
    st.subheader("Your Copy-Paste List")
    final_list = sorted([i for i in shopping_set if i != "None"])
    
    # FORMATTING CHANGE: Comma separated list for Our Groceries
    comma_list = ", ".join(final_list)
    st.text_area("Copy this text:", value=comma_list, height=100)
    st.info("💡 **Partner's Tip:** Copy the text in the box above. In 'Our Groceries', tap '+', paste this whole string, and hit 'Add' or 'Enter'. It should split them by the commas!")

# --- 9. VITALS TRACKER ---
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
    st.write(f"🌟 Data captured for {user}. Good job!")
