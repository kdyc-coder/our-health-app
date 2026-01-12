import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Keifer & Vonnie's Health Hub", page_icon="🎋")

# --- SIDEBAR COUNTDOWNS ---
st.sidebar.header("⏳ Key Deadlines")
med_date = datetime(2026, 8, 1)
m_days = (med_date - datetime.now()).days
if m_days > 0:
    st.sidebar.warning(f"🚨 {m_days} Days to Keifer's Medical")
else:
    st.sidebar.error("Medical Window is OPEN")

retire_date = datetime(2038, 9, 1)
r_days = (retire_date - datetime.now()).days
st.sidebar.info(f"🗓️ {r_days:,} Days to Retirement")

# --- MAIN INTERFACE ---
st.title("🎋 Keifer & Vonnie's Command Centre")
user = st.radio("Who is checking in?", ["Keifer", "Vonnie"])

# --- EXERCISE HUB ---
with st.expander("💪 Exercise & Tai Chi Hub", expanded=False):
    st.video("https://www.youtube.com/watch?v=38tqFjB-o-g")
    
    if user == "Vonnie":
        st.warning("🦶 **Vonnie's Foot Care:** Remember the 'Roll' (Heel-Arch-Toe) and extra calf raises to help the Plantar Fasciitis.")
    
    st.markdown("""
    **Tai Chi Walking Form:**
    1. **The Pour:** Transfer weight slowly—no 'plonking'.
    2. **The Roll:** Heel -> Arch -> Toe. 
    3. **Soft Knees:** Always keep a micro-bend for those over-50s joints.
    """)
    
    st.markdown("""
    **Strength (2-3x per week):**
    * Wall Push-ups (10), Chair Squats (10), Counter-top Lunges (10), Calf Raises (15).
    """)

# --- COOKBOOK SECTION ---
st.divider()
st.header("📖 Master Cookbook (Serves 2)")
diet = st.selectbox("Choose Your Plan:", ["Keto (Diabetes Focus)", "Mediterranean (BP Focus)"])
meal_time = st.selectbox("Meal Type:", ["Breakfast", "Lunch", "Dinner"])

# Recipe Data
data = {
    "Keto (Diabetes Focus)": {
        "Breakfast": {
            "Bacon & Egg Cups": "6 slices bacon, 4 eggs, spinach. Line muffin tin with bacon, crack egg, bake 15m @ 200C.",
            "Salmon Avocado Smash": "150g Smoked salmon, 1 avocado, lemon. Mash avocado, top with salmon.",
            "Pork Sausage Scramble": "2 pork sausages, 4 eggs, 2 cups spinach. Fry pork first.",
            "Beef Mince Omelette": "100g beef mince, 4 eggs, cheese. Brown beef before folding.",
            "Bulletproof Eggs": "4 hard-boiled eggs, coffee with 1 tbsp butter."
        },
        "Lunch": {
            "Chicken Caesar (No Croutons)": "2 chicken breasts, cos lettuce, parmesan, dressing, 1 boiled egg.",
            "Pork Belly & Slaw": "300g pork belly (air fried), cabbage, mayo, apple cider vinegar.",
            "Salmon Salad Bowls": "200g salmon, mixed greens, walnuts, olive oil.",
            "Beef Taco Lettuce Wraps": "300g beef mince, taco seasoning, iceberg lettuce, sour cream.",
            "Chicken Cucumber Boats": "Leftover roast chicken, celery, mayo, in cucumber hulls."
        },
        "Dinner": {
            "Garlic Butter Salmon": "2 salmon fillets, 50g butter, asparagus. Pan-sear 4m each side.",
            "Creamy Parmesan Pork Chops": "2 pork chops, 100ml heavy cream, spinach. Simmer chops in sauce.",
            "Beef & Broccoli Stir-fry": "300g steak strips, 2 cups broccoli, soy sauce (sugar-free).",
            "Chicken Thighs with Zucchini": "4 bone-in chicken thighs, 2 zucchinis, roast 35m @ 200C.",
            "Baked Fish & Bok Choy": "300g white fish, 1 bunch bok choy, olive oil. Foil bake 12m.",
            "Bunless Beef Burgers": "2 beef patties, cheddar, pickles, in lettuce leaves.",
            "Pork Stir-fry with Peppers": "300g pork strips, peppers, garlic, sesame oil.",
            "Lemon Pepper Chicken Wings": "500g wings, lemon zest, pepper. Air fry 20m @ 200C.",
            "Steak & Garlic Mushrooms": "2 steaks, 200g mushrooms, butter. Pan fry.",
            "Cauliflower Shepherd’s Pie": "400g beef mince, topped with mashed cauliflower."
        }
    },
    "Mediterranean (BP Focus)": {
        "Breakfast": {
            "Greek Yogurt & Walnuts": "2 cups Greek yogurt, 1/2 cup walnuts, blueberries.",
            "Oats with Berries": "1 cup rolled oats, cinnamon, strawberries.",
            "Avocado Toast (Sourdough)": "1 avocado, 2 slices sourdough, chili flakes.",
            "Spinach & Feta Omelette": "4 eggs, 50g feta, 2 cups spinach.",
            "Smoked Salmon & Cottage Cheese": "100g salmon, cottage cheese, cucumber."
        },
        "Lunch": {
            "Classic Greek Salad": "Cucumber, tomato, olives, feta, red onion, olive oil.",
            "Chickpea & Tuna Salad": "1 tin chickpeas, 1 tin tuna, parsley, lemon.",
            "Quinoa & Roasted Veg": "1 cup quinoa, capsicum, zucchini, chickpeas.",
            "Chicken & Hummus Wrap": "Grilled chicken, hummus, wholemeal wrap.",
            "Lentil & Veggie Soup": "Brown lentils, carrots, celery, onion, stock."
        },
        "Dinner": {
            "Mediterranean Baked Salmon": "2 salmon fillets, cherry tomatoes, olives, asparagus.",
            "Garlic Chicken & Quinoa": "2 chicken breasts, 1 cup quinoa, broccoli, lemon.",
            "Pork Souvlaki Skewers": "300g pork cubes, oregano, lemon, tzatziki.",
            "Beef & Veggie Kebabs": "300g beef cubes, onion, peppers, brown rice.",
            "White Fish & Salsa Verde": "2 fillets fish, parsley/caper sauce, beans.",
            "Whole Wheat Pasta Primavera": "Whole wheat pasta, zucchini, peas, olive oil.",
            "Chicken Cacciatore": "2 chicken thighs, tinned tomatoes, olives. Simmer 30m.",
            "Sheet Pan Pork & Vegies": "2 pork steaks, carrots, red onion. Roast 25m.",
            "Grilled Beef & Asparagus": "2 steaks, 2 bunches asparagus, balsamic.",
            "Tuna Niçoise Salad": "Grilled fresh tuna, green beans, boiled egg, olives."
        }
    }
}

selected_recipes = data[diet][meal_time]
choice = st.selectbox("Select a Recipe:", list(selected_recipes.keys()))
st.info(f"**Method & Ingredients:** {selected_recipes[choice]}")

# --- SHOPPING LIST GENERATOR ---
if st.button("🛒 Generate Weekly Shopping List"):
    st.subheader("Your Planned Shop:")
    st.write("Based on the current Diet Plan selected above:")
    if diet == "Keto (Diabetes Focus)":
        st.write("- **Protein:** Salmon, Chicken Thighs/Breast, Pork Chops/Belly/Sausage, Beef Mince/Steak, Eggs, Bacon.")
        st.write("- **Produce:** Avocado, Zucchini, Cauliflower, Spinach, Broccoli, Asparagus, Bok Choy, Lettuce, Peppers, Mushrooms.")
        st.write("- **Pantry:** Olive oil, Butter, Heavy Cream, Walnuts, Almonds, Soy Sauce (sugar-free), Apple Cider Vinegar.")
    else:
        st.write("- **Protein:** Salmon, White Fish, Tuna, Chicken, Pork, Beef, Eggs, Greek Yogurt, Feta, Chickpeas, Lentils.")
        st.write("- **Produce:** Cucumber, Tomato, Onion, Spinach, Peppers, Zucchini, Carrots, Blueberries, Strawberries, Lemon.")
        st.write("- **Pantry:** Olive oil, Quinoa, Wholemeal Wraps, Oats, Sourdough, Walnuts, Brown Rice, Whole Wheat Pasta.")

# --- VITALS TRACKER ---
st.divider()
st.header("📊 Vitals & Accountability")
c1, c2 = st.columns(2)
with c1:
    w = st.number_input("Weight (kg)", value=0.0)
    bs = st.number_input("Blood Sugar (mmol/L)", value=0.0)
with c2:
    bps = st.number_input("BP Systolic (Top)", value=0)
    bpd = st.number_input("BP Diastolic (Bottom)", value=0)

if st.button("Log & Analyze"):
    if bps > 140 or bpd > 90:
        st.error(f"🛑 **Push harder, {user}!** BP is a bit high. Watch the salt and stick to the plan.")
    elif w > 0:
        st.balloons()
        st.write(f"🌟 **Genuine Praise:** Great effort, {user}! One step closer to that August Medical and 2038 retirement.")
