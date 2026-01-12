import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Keifer & Vonnie's Health Hub", page_icon="🎋")

# --- 1. THE CATEGORISED RECIPE ENGINE ---
# Split by meal type so the dropdowns stay relevant
keto_recipes = {
    "Breakfast": ["Bacon & Egg Cups", "Salmon Avocado Smash", "Pork Sausage Scramble", "Beef Mince Omelette", "Steak and Eggs", "Pork Belly & Eggs", "Bulletproof Coffee", "Chicken Frittata", "Smoked Salmon Scramble", "Ham & Cheese Muffins"],
    "Lunch": ["Chicken Caesar", "Pork Belly Slaw", "Beef Taco Wraps", "Salmon Salad Bowls", "Bunless Burgers", "Chicken Cucumber Boats", "Cold Pork Roast", "Beef Meatballs", "Tuna Avocado Salad", "Pork Rind Chicken"],
    "Dinner": ["Garlic Butter Salmon", "Beef & Broccoli", "Parmesan Pork Chops", "Chicken Thighs", "Baked White Fish", "Pork Stir-fry", "Steak & Mushrooms", "Lemon Pepper Wings", "Shepherd’s Pie", "Pork Loin Roast"]
}

med_recipes = {
    "Breakfast": ["Greek Omelette", "Avocado Sourdough", "Yogurt & Walnuts", "Berry Oats", "Salmon & Feta", "Spinach Frittata", "Whole Wheat Pancakes", "Chickpea Hash", "Poached Eggs", "Cottage Cheese & Cucumber"],
    "Lunch": ["Chickpea Tuna Salad", "Classic Greek Salad", "Chicken Hummus Wrap", "Quinoa Salad", "Lentil Soup", "Salmon Souvlaki", "Beef Skewers", "Pork Wraps", "Quinoa Tabbouleh", "Tuna Salad (No Mayo)"],
    "Dinner": ["Greek Lemon Fish", "Chicken Cacciatore", "Baked Salmon", "Pork Souvlaki", "Beef & Veg Kebabs", "Garlic Chicken", "Pasta Primavera", "Sheet Pan Pork", "Grilled Beef", "Tuna Niçoise"]
}

# Ingredient database remains for the generator
ingredients_map = {
    "Bacon & Egg Cups": ["Bacon", "Eggs"], "Salmon Avocado Smash": ["Smoked Salmon", "Avocado", "Low-carb bread"],
    "Pork Sausage Scramble": ["Pork Sausages", "Eggs", "Spinach"], "Beef Mince Omelette": ["Beef Mince", "Eggs", "Cheese"],
    "Steak and Eggs": ["Steak", "Eggs"], "Pork Belly & Eggs": ["Pork Belly", "Eggs"],
    "Bulletproof Coffee": ["Coffee Beans", "Butter", "MCT Oil"], "Chicken Frittata": ["Chicken", "Eggs", "Feta"],
    "Smoked Salmon Scramble": ["Smoked Salmon", "Eggs"], "Ham & Cheese Muffins": ["Ham", "Eggs", "Cheese"],
    "Chicken Caesar": ["Chicken", "Lettuce", "Parmesan", "Caesar Dressing"], "Pork Belly Slaw": ["Pork Belly", "Cabbage", "Mayo"],
    "Beef Taco Wraps": ["Beef Mince", "Lettuce", "Taco Spice"], "Garlic Butter Salmon": ["Salmon", "Butter", "Garlic", "Asparagus"],
    "Greek Omelette": ["Eggs", "Feta", "Spinach", "Olives"], "Greek Lemon Fish": ["White Fish", "Lemon", "Potatoes"],
    "Chicken Cacciatore": ["Chicken Thighs", "Tomatoes", "Capsicum", "Mushrooms"]
    # (Note: All 60 would be mapped here in the background)
}

# --- 2. INITIALISE MEMORY ---
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
diet_choice = st.selectbox("Current Diet Focus:", ["Keto (Diabetes)", "Mediterranean (BP)"])

# --- 5. SMART WEEKLY PLANNER ---
st.divider()
st.header("📅 Smart Weekly Planner")
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Filter recipes based on diet choice
active_db = keto_recipes if "Keto" in diet_choice else med_recipes

planned_meals = {}
for day in days:
    with st.expander(f"📍 {day} Meals"):
        b = st.selectbox(f"Breakfast", ["None"] + active_db["Breakfast"], key=f"b_{day}")
        l = st.selectbox(f"Lunch", ["None"] + active_db["Lunch"], key=f"l_{day}")
        d = st.selectbox(f"Dinner", ["None"] + active_db["Dinner"], key=f"d_{day}")
        planned_meals[day] = [b, l, d]

# --- 6. GROCERY GENERATOR ---
st.divider()
st.header("🛒 Our Groceries Bridge")
if st.button("🚀 Generate Shopping List"):
    shopping_set = set(st.session_state['essentials'])
    for day in planned_meals:
        for meal in planned_meals[day]:
            if meal in ingredients_map:
                for item in ingredients_map[meal]:
                    shopping_set.add(item)
            elif meal != "None":
                shopping_set.add(meal)
    
    final_list = sorted([i for i in shopping_set if i != "None"])
    list_str = "\n".join(final_list)
    
    st.subheader("Final List")
    st.code(list_str)
    
    # NEW WORKAROUND: Email link
    # This opens the user's email client. They can send it to the Our Groceries email address.
    mail_link = f"mailto:?subject=Grocery List&body={list_str.replace('', '%20')}"
    st.markdown(f'<a href="{mail_link}" target="_blank">✉️ Email this list to "Our Groceries"</a>', unsafe_allow_html=True)
    st.info("💡 **Tip:** If the paste failed, use the Email button above. 'Our Groceries' can take an emailed list and add it automatically.")

# --- 7. EXERCISE & VITALS (Full Sections) ---
st.divider()
with st.expander("💪 Exercise & Tai Chi Guide"):
    st.markdown("**Tai Chi Step:** Heel down, roll to arch, push off ball of foot.")
    st.checkbox("Wall Push-ups (10)")
    st.checkbox("Chair Squats (10)")
    st.checkbox("Calf Raises (15)")

with st.expander("📊 Vitals Tracker"):
    st.number_input("Weight (kg)", format="%.1f")
    st.number_input("Blood Sugar", format="%.1f")
    st.button("Log Stats")
