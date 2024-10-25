import streamlit as st
import os
import sys
import Yolo.steps.DataCollection as DataCollection


current_dir = os.path.dirname(__file__)
Classification_img_path = os.path.join(current_dir, "media/images/onboarding-classification-v2.png")


# Define steps and their titles
Training_steps = [
    "Introduction",
    "Data Collection & Preparation",
    "Model Defining",
    "Training",
    "Testing"
]

# Store the current step in session_state
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0  # Start with the first step

# Function to go to the next step
def next_step():
    global Training_steps
    if st.session_state.current_step < len(Training_steps) - 1:
        st.session_state.current_step += 1

# Function to go to the previous step
def previous_step():
    if st.session_state.current_step > 0:
        st.session_state.current_step -= 1

# Display the content based on the current step
step = Training_steps[st.session_state.current_step]

# Step-specific content
if step == "Introduction":
    st.title("Introduction to Image Classification")

    st.markdown("<h3 style='text-align: center; color: #FF6347; font-weight: bold;'>**By following these steps, you can train your own model.**</h3>", unsafe_allow_html=True)
    st.subheader("What is Image Classification?")
    st.write("""Image classification is a pivotal task in computer vision that involves assigning labels to images based on their content. This process is essential in various applications, including medical imaging, autonomous vehicles, and social media categorization. By utilizing algorithms such as Convolutional Neural Networks (CNNs), models can learn intricate patterns and features from labeled datasets, allowing them to generalize and accurately classify unseen images. The advancements in deep learning techniques and the availability of large datasets have significantly enhanced the accuracy of image classification systems, making them more reliable for real-world applications.

For more in-depth information on the significance and techniques of image classification, you can explore resources like Towards Data Science and Medium.""")
    st.image(Classification_img_path, caption="Example of Image Classification", width=600)

elif step == "Data Collection & Preparation":
    st.title("Data Collection & Preparation")
    DataCollection.imageclassification_data()
    st.subheader("Preparation Steps for Image Classification in Roboflow")
    steps = [
        "1. **Create an Account**: Sign up or log in to Roboflow.",
        "2. **Create a New Project**: Start a new project and select 'Image Classification.'",
        "3. **Upload Images**: Drag and drop or upload your images into the project.",
        "4. **Label Images**: Use the labeling tool to assign labels to your images.",
        "5. **Data Augmentation(optional)**: Apply augmentations to enhance your dataset.",
        "6. **Split Dataset(auomated by roboflow)**: Organize your data into training, validation, and test sets.",
        "7. **Download Dataset**: Export your labeled dataset in the desired format."
    ]   

    for step in steps:
        st.write(step)
    st.video("https://www.youtube.com/watch?v=bfr3GlNSRdk")

elif step == "Model Defining":
    st.title("Model Defining")
    st.write("Model defining is the process of selecting and building a neural network architecture ...")

elif step == "Training":
    st.title("Training the Model")
    st.write("Training involves feeding the prepared dataset into the model ...")

elif step == "Testing":
    st.title("Testing the Model")
    st.write("After training, the model is evaluated on a separate test set ...")

# Navigation buttons
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.session_state.current_step > 0:
        st.button("Previous", on_click=previous_step)

with col3:
    if st.session_state.current_step < len(Training_steps) - 1:
        st.button("Next", on_click=next_step)

