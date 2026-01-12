import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Tai Chi & Health Hub", page_icon="🎋")

# --- HEADER ---
st.title("🎋 Tai Chi & Health Hub")
st.write("Target: Diabetes Remission | Normal BP | Joint Safety")

user = st.radio("Who is checking in?", ["Partner (Plantar Fasciitis)", "You"])

# --- EXERCISE HUB (Combined Video & Manual) ---
st.header("💪 Home Exercise Hub")
with st.expander("🧘 Tai Chi Walking: Video & Steps", expanded=True):
    st.video("https://www.youtube.com/watch?v=38tqFjB-o-g")
    st.markdown("""
    **The Manual Steps:**
    * **The Pour:** Don't step and lean. Pour your weight like water into the front foot only once it's flat.
    * **Heel-to-Toe:** Land on the heel, roll through the arch, push off the toe.
    * **Soft Knees:** Never lock your legs straight. Keep a 'micro-bend' to absorb shock.
    * **Hip Level:** Keep your 'bowl of water' level. Don't let your hips tilt.
    """)

with st.expander("🏋️ Resistance Training (Joint Friendly)", expanded=False):
    st.write("Build muscle to soak up blood sugar without hurting your knees/hips.")
    st.write("- **Wall Push-ups:** 10 reps (Shoulder & Chest)")
    st.write("- **Chair Squats:** 10 reps (Thighs & Hips - don't use hands!)")
    st.write("- **Counter-top Lunges:** Hold bench for balance (Very shallow)")
    st.write("- **Calf Raises:** 15 reps (Essential for Plantar Fasciitis relief)")

# --- COOKBOOK SECTION ---
st.divider()
st.header("📖 The Digital Cookbook")
diet_tab = st.radio("Select Diet Focus:", ["Keto (Diabetes Remission)", "Mediterranean (BP & Heart)"])

if diet_tab == "Keto (Diabetes Remission)":
    st.subheader("🥑 Low-Carb Keto Meals")
    with st.expander("View Keto Recipes & Shopping List"):
        st.write("**1. Zucchini & Salmon Bake:** Salmon fillets, zucchini, olive oil, lemon.")
        st.write("**2. Cauliflower 'Rice' Chicken:** Chicken thighs, cauliflower, garlic, spinach.")
        st.write("**3. Egg & Avocado Smash:** Eggs, avocado, almonds, apple cider vinegar.")
        st.write("**4. Beef & Broccoli Stir-fry:** Steak strips, broccoli, soy sauce (no sugar), ginger.")
        st.write("**5. Creamy Mushroom Spinach:** Mushrooms, heavy cream, spinach, butter.")
        st.info("🛒 **Keto Shopping List:** Salmon, Chicken, Steak, Eggs, Zucchini, Cauliflower, Spinach, Avocado, Broccoli, Mushrooms, Cream, Butter, Almonds, Olive Oil.")

else:
    st.subheader("🥗 Mediterranean Meals")
    with st.expander("View Mediterranean Recipes & Shopping List"):
        st.write("**1. Greek Lemon Fish:** White fish fillets, oregano, garlic, olives, tomatoes.")
        st.write("**2. Chickpea & Cucumber Salad:** Chickpeas, cucumber, red onion, feta, parsley.")
        st.write("**3. Lentil Soup:** Brown lentils, carrots, celery, onion, vegetable stock.")
        st.write("**4. Roasted Veggie Quinoa:** Quinoa, bell peppers, eggplant, zucchini, balsamic.")
        st.write("**5. Walnut & Berry Yogurt:** Greek yogurt (unsweetened), walnuts, blueberries.")
        st.info("🛒 **Med Shopping List:** White fish, Quinoa, Chickpeas, Lentils, Greek Yogurt, Feta, Tomatoes, Cucumber, Peppers, Eggplant, Carrots, Berries, Walnuts, Olive Oil.")

# --- VITALS TRACKER ---
st.divider()
st.header("📊 Vitals Tracker")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Weight (kg)", step=0.1)
        bp_sys = st.number_input("BP Top (Systolic)", step=1)
    with col2:
        glucose = st.number_input("Glucose (mmol/L)", step=0.1)
        bp_dia = st.number_input("BP Bottom (Diastolic)", step=1)

    if st.button("Log & Analyze Results"):
        # This logic provides the 'praise' or 'push' you asked for
        if weight > 0:
            st.success("Stats recorded. Remember: You're doing this for your 2038 retirement!")
            if bp_sys < 130 and bp_dia < 85:
                st.balloons()
                st.write("🌟 **Bloody legend!** Your BP is in the healthy range. Keep that Tai Chi going.")
            elif bp_sys > 140:
                st.warning("🛑 **Push harder on the diet, mate.** BP is a bit high. Watch the salt and stick to the Med plan.")
            else:
                st.write("🤜🤛 **Flatline/Steady.** Good consistency, let's try to drop 0.5kg next week.")

# --- RETIREMENT COUNTDOWN ---
st.divider()
target_date = datetime(2038, 9, 1)
days_left = (target_date - datetime.now()).days
st.write(f"⏳ **{days_left:,} days** until your September 2038 retirement. Stay healthy to enjoy it!")
