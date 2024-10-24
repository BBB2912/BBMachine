import streamlit as st
import os
from streamlit_option_menu import option_menu

st.header("Object Detection")
st.markdown(
    """
    <h3 style='text-align: center; color: #FF6347; font-weight: bold;'>
    **By following these  beside steps one by one, train your own model**
    </h3>
    """, unsafe_allow_html=True
)

current_dir = os.path.dirname(__file__)

objdetection_img_path = os.path.join(current_dir, "media/images/onboarding-objdet.png")
# Sidebar navigation menu for steps in Object Detection

selected = option_menu(
    menu_title="Object Detection Steps",  # Required
    options=["Introduction", "Data Collection & Preparation", "Model Defining", "Training", "Testing"],  # Steps
    icons=["book", "database", "brain", "play", "check-circle"],  # Icons for each step
    menu_icon="list",  # Sidebar icon
    default_index=0,  # Initially selected option
    orientation="vertical",  # Sidebar vertical orientation
)

# Introduction Step
if selected == "Introduction":
    st.title("Introduction to Object Detection")
    st.subheader("What is Object Detection?")
    # Introduction section with one mini paragraph
    st.write("""
        Object detection is a critical task in computer vision where the goal is not only to classify objects in an image 
        but also to determine their location by drawing bounding boxes around them. This technique is essential for applications 
        like surveillance, self-driving cars, and robotics.
    """)

    # Display the image
    st.image(objdetection_img_path, caption="Example of Object Detection", width=600)

    # Two medium paragraphs
    st.write("""
        Object detection involves both classification and localization. Models like YOLO (You Only Look Once) and Faster R-CNN 
        have become popular due to their ability to detect multiple objects in real-time. They learn to draw bounding boxes 
        around objects and predict their categories simultaneously.

        These models rely heavily on deep learning frameworks, particularly Convolutional Neural Networks (CNNs), which help them 
        capture spatial information. Object detection is applied in diverse fields, including retail for tracking inventory, 
        healthcare for identifying medical anomalies, and security for monitoring sensitive areas.
    """)


# Data Collection & Preparation Step
elif selected == "Data Collection & Preparation":
    st.title("Data Collection & Preparation")
    st.subheader("Step 1: Data Collection")
    st.write("""
        Data collection involves gathering a labeled dataset containing images with annotated bounding boxes for each object. 
        Public datasets like COCO or PASCAL VOC can be used.
    """)
    
    st.subheader("Step 2: Data Preparation")
    st.write("""
        Data preparation includes organizing the dataset, converting annotations into a suitable format, 
        and splitting the data into training, validation, and testing sets.
    """)
    
    st.image("https://example.com/data-preparation-image.jpg", caption="Data Preparation Example", width=600)  # Replace with actual image path

# Model Defining Step
elif selected == "Model Defining":
    st.title("Model Defining")
    st.subheader("Step 3: Defining the Model")
    st.write("""
        Model defining involves selecting and building a neural network architecture designed for object detection tasks. 
        Popular models include YOLO, SSD, and Faster R-CNN.
    """)
    
    st.image("https://example.com/model-architecture-image.jpg", caption="Object Detection Model Architecture", width=600)  # Replace with actual image path

# Training Step
elif selected == "Training":
    st.title("Training the Model")
    st.subheader("Step 4: Training")
    st.write("""
        Training the model involves using the labeled dataset to optimize the model's ability to detect objects accurately 
        through techniques like transfer learning or training from scratch.
    """)
    
    st.image("https://example.com/training-process-image.jpg", caption="Training Process", width=600)  # Replace with actual image path

# Testing Step
elif selected == "Testing":
    st.title("Testing the Model")
    st.subheader("Step 5: Testing")
    st.write("""
        After training, the model is evaluated using a test dataset to assess its performance in detecting objects 
        and measuring metrics such as mean Average Precision (mAP).
    """)
    
    st.image("https://example.com/testing-results-image.jpg", caption="Testing the Model", width=600)  # Replace with actual image path

# Main entry point
if __name__ == "__main__":
    pass
