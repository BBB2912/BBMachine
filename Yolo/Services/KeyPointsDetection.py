import streamlit as st
import os
from streamlit_option_menu import option_menu

st.header("KeyPont Detections")
st.markdown(
    """
    <h3 style='text-align: center; color: #FF6347; font-weight: bold;'>
    **By following these  beside steps one by one, train your own model**
    </h3>
    """, unsafe_allow_html=True
)

current_dir = os.path.dirname(__file__)

KeypointsDetection_img_path = os.path.join(current_dir, "media/images/onboarding-key.png")
# Sidebar navigation menu for steps in Keypoint Detection
with st.sidebar:
    selected = option_menu(
        menu_title="Keypoint Detection Steps",  # Required
        options=["Introduction", "Data Collection & Preparation", "Model Defining", "Training", "Testing"],  # Steps
        icons=["book", "database", "brain", "play", "check-circle"],  # Icons for each step
        menu_icon="list",  # Sidebar icon
        default_index=0,  # Initially selected option
        orientation="vertical",  # Sidebar vertical orientation
    )

# Introduction Step
if selected == "Introduction":
    st.title("Introduction to Keypoint Detection")
    st.subheader("What is Keypoint Detection?")
    # Introduction section with one mini paragraph
    st.write("""
        Keypoints detection focuses on identifying specific points or landmarks in an image, typically on objects or human bodies. 
        These points are used for tracking movements, facial recognition, or gesture analysis.
    """)

    # Display the image
    st.image(KeypointsDetection_img_path, caption="Example of Keypoints Detection", width=600)

    # Two medium paragraphs
    st.write("""
        In human pose estimation, for instance, keypoints detection identifies joint locations such as elbows, knees, or eyes. Models 
        like OpenPose have demonstrated impressive results in detecting multiple keypoints for human pose estimation in real-time applications.

        Keypoints detection has numerous applications, including in sports for tracking athlete movements, in healthcare for analyzing 
        posture and gait, and in augmented reality (AR) for enabling interactive experiences by detecting hand gestures or facial expressions.
    """)

# Data Collection & Preparation Step
elif selected == "Data Collection & Preparation":
    st.title("Data Collection & Preparation")
    st.subheader("Step 1: Data Collection")
    st.write("""
        Data collection involves gathering a dataset of images with annotated keypoints. 
        This can involve using existing datasets or creating custom datasets with specific keypoints labeled.
    """)
    
    st.subheader("Step 2: Data Preparation")
    st.write("""
        Data preparation includes cleaning the dataset, organizing images and annotations, and 
        ensuring that the keypoint annotations are in a consistent format.
    """)
    
    st.image("https://example.com/data-preparation-image.jpg", caption="Data Preparation Example", width=600)  # Replace with actual image path

# Model Defining Step
elif selected == "Model Defining":
    st.title("Model Defining")
    st.subheader("Step 3: Defining the Model")
    st.write("""
        Model defining involves selecting and building a neural network architecture suitable for keypoint detection tasks. 
        Common architectures include Hourglass Networks and Convolutional Pose Machines.
    """)
    
    st.image("https://example.com/model-architecture-image.jpg", caption="Keypoint Detection Model Architecture", width=600)  # Replace with actual image path

# Training Step
elif selected == "Training":
    st.title("Training the Model")
    st.subheader("Step 4: Training")
    st.write("""
        Training the model involves using the labeled dataset to teach the model to accurately predict the location of keypoints 
        using appropriate loss functions like Mean Squared Error.
    """)
    
    st.image("https://example.com/training-process-image.jpg", caption="Training Process", width=600)  # Replace with actual image path

# Testing Step
elif selected == "Testing":
    st.title("Testing the Model")
    st.subheader("Step 5: Testing")
    st.write("""
        After training, the model is evaluated on a separate test dataset to measure its keypoint detection accuracy. 
        Metrics such as PCK (Percentage of Correct Keypoints) are often used.
    """)
    
    st.image("https://example.com/testing-results-image.jpg", caption="Testing the Model", width=600)  # Replace with actual image path

# Main entry point
if __name__ == "__main__":
    pass
