import streamlit as st

# Initialize session state variables
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'profile' not in st.session_state:
    st.session_state.profile = {}

# Function to add item to cart
def add_to_cart(item):
    st.session_state.cart.append(item)
    st.success(f"Added {item} to cart!")

# Function to create profile
def create_profile(name, age, email):
    st.session_state.profile = {
        'name': name,
        'age': age,
        'email': email
    }
    st.success("Profile updated!")

# App title
st.title('We Care App')
st.write('Welcome to the We Care app!')

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Supplements", "Appointments", "Groceries", "Recipes", "Profile", "Receipt"])

# Supplements section
if page == "Supplements":
    st.header("Supplements")
    supplements = ["Vitamin C", "Omega-3", "Protein Powder", "Probiotics"]
    for supplement in supplements:
        st.write(supplement)
        st.button(f"Add {supplement} to cart", on_click=add_to_cart, args=(supplement,))

# Appointments section
elif page == "Appointments":
    st.header("Appointments")
    st.write("Book an appointment with our nutritionists.")
    st.selectbox("Choose a nutritionist", ["Dr. Smith", "Dr. Jones", "Dr. Lee"])
    st.date_input("Select a date")
    st.button("Book Appointment")
    st.success("Appointment booked!")

# Groceries section
elif page == "Groceries":
    st.header("Groceries")
    groceries = ["Apples", "Bananas", "Carrots", "Broccoli"]
    for grocery in groceries:
        st.write(grocery)
        st.button(f"Add {grocery} to cart", on_click=add_to_cart, args=(grocery,))

# Recipes section
elif page == "Recipes":
    st.header("Recipes")
    st.write("Watch our recipe videos:")
    videos = {
        "Healthy Salad": "https://www.youtube.com/watch?v=salad_video",
        "Smoothie Recipe": "https://www.youtube.com/watch?v=smoothie_video",
        "Healthy Dinner": "https://www.youtube.com/watch?v=dinner_video"
    }
    for title, url in videos.items():
        st.write(f"[{title}]({url})")

# Profile section
elif page == "Profile":
    st.header("Profile")
    st.write("Update your profile:")
    name = st.text_input("Name", value=st.session_state.profile.get('name', ''))
    age = st.number_input("Age", value=st.session_state.profile.get('age', 0))
    email = st.text_input("Email", value=st.session_state.profile.get('email', ''))
    st.button("Save Profile", on_click=create_profile, args=(name, age, email))

# Receipt section
elif page == "Receipt":
    st.header("Receipt")
    st.write("Here are the items in your cart:")
    for item in st.session_state.cart:
        st.write(item)
    st.button("Purchase All")
    st.success("Purchase successful!")

# Run the Streamlit app
if __name__ == "__main__":
    st.run()
