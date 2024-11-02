import streamlit as st
import diwali_snack_recipies

# Set the title and description
st.title("🎉 Diwali Snack Recipes 🎉")
st.subheader("Discover delicious and healthy recipes for your Diwali celebration!")

# Fetch and display the list of snack options
snack_options = diwali_snack_recipies.get_snack_options()
st.write("Select a snack from the menu below to get started:")

# Display snack options in a two-column layout
col1, col2 = st.columns(2)
for i, snack in enumerate(snack_options):
    if i % 2 == 0:
        col1.write(f"✨ {snack}")
    else:
        col2.write(f"✨ {snack}")

# Snack selection and preference inputs
st.write(" ")
snack_name = st.selectbox("Choose a snack:", options=snack_options)
preference = st.radio("Would you prefer it to be:", options=["Healthy", "Tasty"])

# Button to get the recipe
if st.button("Get Recipe"):
    healthy = preference == "Healthy"
    tasty = preference == "Tasty"
    recipe = diwali_snack_recipies.get_snack_recipies(snack_name, healthy=healthy, tasty=tasty)

    # Display the recipe in organized sections
    if recipe:
        ingredients, instructions = recipe

        st.write(" ")
        st.markdown("### 🥣 Ingredients:")
        for ingredient in ingredients:
            st.write(f"- {ingredient}")

        st.write(" ")
        st.markdown("### 🍲 Instructions:")
        for step, instruction in enumerate(instructions, start=1):
            st.write(f"{step}. {instruction}")
    else:
        st.error("Sorry, we couldn't find a recipe for that selection.")

# Footer
st.write(" ")
st.caption("Made with 💖 for Diwali. Enjoy your treats!")
