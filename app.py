import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Health & Medical Prep", page_icon="🎋")

# --- SIDEBAR COUNTDOWNS ---
st.sidebar.header("⏳ Key Deadlines")

# Medical Prep - August 2026
med_date = datetime(2026, 8, 1)
m_days = (med_date - datetime.now()).days
if m_days > 0:
    st.sidebar.warning(f"🚨 {m_days} Days until Medical (August 2026)")
else:
    st.sidebar.error("Medical Window is OPEN")

# Retirement
retire_date = datetime(2038, 9, 1)
r_days = (retire_date - datetime.now()).days
st.sidebar.info(f"🗓️ {r_days:,} Days to Retirement")

# --- MAIN INTERFACE ---
st.title("🎋 Tai Chi & Health Command Centre")
user = st.radio("Who is checking in?", ["Partner (Plantar Fasciitis)", "You"])

# --- EXERCISE HUB ---
with st.expander("💪 Exercise & Tai Chi Hub", expanded=False):
    st.video("https://www.youtube.com/watch?v=38tqFjB-o-g")
    st.markdown("""
    **Tai Chi Walking Form:**
    1. **The Pour:** Transfer weight slowly—don't 'plonk' the foot down.
    2. **The Roll:** Heel -> Arch -> Toe. This is vital for the Plantar Fasciitis.
    3. **Soft Knees:** Always keep a micro-bend to protect joints.
    
    **Home Strength (2-3x per week):**
    * **Wall Push-ups:** 10 reps.
    * **Chair Squats:** 10 reps (Hover just above the seat).
    * **Counter-top Lunges:** Use the bench for balance.
    * **Calf Raises:** 15 reps (Strengthens the foot arch).
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
            "Bacon & Egg Cups": "6 slices bacon, 4 eggs, spinach. Line muffin tin with bacon, crack egg inside, bake 15m at 200C.",
            "Salmon Avocado Smash": "150g Smoked salmon, 1 large avocado, lemon juice. Mash avocado, top with salmon. No toast!",
            "Pork Sausage & Spinach Scramble": "2 pork sausages, 4 eggs, 2 cups spinach. Pan-fry pork first, then scramble eggs in.",
            "Beef Mince Omelette": "100g beef mince, 4 eggs, cheese. Brown beef with salt/pepper, fold into eggs.",
            "Bulletproof Coffee & Boiled Eggs": "4 hard-boiled eggs, coffee with 1 tbsp butter. Great for fasting."
        },
        "Lunch": {
            "Chicken Caesar (No Croutons)": "2 grilled chicken breasts, cos lettuce, parmesan, Caesar dressing, 1 boiled egg.",
            "Pork Belly Bites & Slaw": "300g pork belly (air fried), shredded cabbage, mayo, apple cider vinegar.",
            "Salmon Salad Bowls": "200g salmon, mixed greens, walnuts, olive oil, cucumber.",
            "Beef Taco Lettuce Wraps": "300g beef mince, taco seasoning, iceberg lettuce leaves, sour cream.",
            "Chicken & Mayo Cucumber Boats": "Leftover roast chicken, celery, mayo, served in hollowed-out cucumber."
        },
        "Dinner": {
            "Garlic Butter Salmon": "2 salmon fillets, 50g butter, 2 cups asparagus. Pan-sear 4m each side.",
            "Creamy Parmesan Pork Chops": "2 thick pork chops, 100ml heavy cream, 1 cup spinach. Brown chops, simmer in sauce.",
            "Beef & Broccoli Stir-fry": "300g steak strips, 2 cups broccoli, ginger, soy sauce (sugar-free).",
            "Chicken Thighs with Zucchini": "4 bone-in chicken thighs, 2 zucchinis, oregano. Roast at 200C for 35m.",
            "Baked White Fish & Bok Choy": "300g white fish, 1 bunch bok choy, olive oil. Bake in foil 12m.",
            "Bunless Beef Burgers": "2 beef patties, cheddar, pickles, wrapped in lettuce leaves.",
            "Pork Stir-fry with Peppers": "300g pork strips, red/green peppers, garlic, sesame oil.",
            "Lemon Pepper Chicken Wings": "500g wings, lemon zest, pepper. Air fry 20m at 200C.",
            "Steak & Garlic Mushrooms": "2 steaks, 200g mushrooms, butter. Pan fry to preference.",
            "Cauliflower Shepherd’s Pie": "400g beef mince, topped with mashed cauliflower (butter/cream)."
        }
    },
    "Mediterranean (BP Focus)": {
        "Breakfast": {
            "Greek Yogurt & Walnuts": "2 cups Greek yogurt, 1/2 cup walnuts, blueberries.",
            "Oats with Berries": "1 cup rolled oats, water, cinnamon, strawberries.",
            "Avocado Toast (Sourdough)": "1 avocado, 2 slices sourdough, chili flakes, olive oil.",
            "Spinach & Feta Omelette": "4 eggs, 50g feta, 2 cups spinach, olive oil.",
            "Smoked Salmon & Cottage Cheese": "100g salmon, cottage cheese, cucumber slices."
        },
        "Lunch": {
            "Classic Greek Salad": "Cucumber, tomato, olives, feta, red onion, lots of olive oil.",
            "Chickpea & Tuna Salad": "1 tin chickpeas, 1 tin tuna, parsley, lemon juice.",
            "Quinoa & Roasted Veg": "1 cup cooked quinoa, roasted capsicum, zucchini, chickpeas.",
            "Chicken & Hummus Wrap": "Grilled chicken, hummus, wholemeal wrap, spinach.",
            "Lentil & Vegetable Soup": "Brown lentils, carrots, celery, onion, veg stock."
        },
        "Dinner": {
            "Mediterranean Baked Salmon": "2 salmon fillets, cherry tomatoes, olives, asparagus. Bake 15m.",
            "Garlic Chicken & Quinoa": "2 chicken breasts, 1 cup quinoa, steamed broccoli, lemon.",
            "Pork Souvlaki Skewers": "300g pork cubes, oregano, lemon, serve with tzatziki.",
            "Beef & Veggie Kebabs": "300g beef cubes, onion, peppers. Grill and serve with brown rice.",
            "White Fish & Salsa Verde": "2 fillets white fish, parsley/caper sauce, green beans.",
            "Whole Wheat Pasta Primavera": "Whole wheat pasta, zucchini, peas, parmesan, olive oil.",
            "Chicken Cacciatore": "2 chicken thighs, tinned tomatoes, onions, olives. Simmer 30m.",
            "Sheet Pan Pork & Vegies": "2 pork steaks, carrots, red onion. Roast 25m.",
            "Grilled Beef & Asparagus": "2 small steaks, 2 bunches asparagus, balsamic glaze.",
            "Tuna Niçoise Salad": "Grilled fresh tuna, green beans, boiled egg, olives."
        }
    }
}

# Display Selection
selected_recipes = data[diet][meal_time]
choice = st.selectbox("Select a Recipe:", list(selected_recipes.keys()))
st.info(f"**Method & Ingredients:** {selected_recipes[choice]}")

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
        st.error("🛑 **Push harder!** BP is high. Stick to the Med recipes and do your Tai Chi.")
    elif w > 0:
        st.balloons()
        st.write("🌟 **Bloody legend!** You're taking action for that August Medical. Keep it up.")
