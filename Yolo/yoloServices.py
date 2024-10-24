import streamlit as st
from streamlit_option_menu import option_menu
import os

# Function to display YOLO services page
def show_yolo_services():
    current_dir = os.path.dirname(__file__)

    # Join the current directory with the relative path to the image
    Classification_img_path = os.path.join(current_dir, "media/images/onboarding-classification-v2.png")
    segmentation_img_path = os.path.join(current_dir, "media/images/onboarding-iseg.png")
    objdetection_img_path = os.path.join(current_dir, "media/images/onboarding-objdet.png")
    KeypointsDetection_img_path = os.path.join(current_dir, "media/images/onboarding-key.png")

    imgclassification_filepath = os.path.join(current_dir, "Services/ImageClassification.py")
    segmentation_filepath = os.path.join(current_dir, "Services/ImageSegmentation.py")
    objdeection_filepath = os.path.join(current_dir, "Services/ObjectDetection.py")
    KeyPointsDetection_filepath = os.path.join(current_dir, "Services/KeyPointsDetection.py")

    # Sidebar navigation menu using option_menu
  # This ensures the menu is placed on the left sidebar
    selected = option_menu(
        menu_title="YOLO Services",  # Required
        options=["Yolo Services", "Image Classification", "Object Detection", "Image Segmentation", "Keypoints Detection"],  # Options for services
        icons=["","image", "bounding-box", "scissors", "pin-map"],  # Add icons related to each option
        menu_icon="cast",  # The icon for the sidebar
        default_index=0,  # Index of the initially selected option
        orientation="horizontal",  # Sidebar orientation
    )

    # Display selected service page
    if selected == "Yolo Services":
        st.write("""
        YOLO (You Only Look Once) is a state-of-the-art, real-time object detection system. 
        Below are the different services offered using YOLO models:
        """)
        st.write("""
        1. **Image Classification** - Classifies images into predefined categories based on the visual content of the image. 
           Image classification is widely used in applications like facial recognition, medical diagnosis, and autonomous vehicles.
           The model learns features from labeled datasets, allowing it to categorize new images accurately.
           High-quality datasets and advanced neural networks, such as CNNs, are key components in achieving accurate results.
        """)
        st.image(Classification_img_path, caption="Image Classification")

        st.write("""
        2. **Object Detection** - Identifies objects in images or videos and draws bounding boxes around them.
           YOLO is known for its speed and precision in detecting multiple objects within a single frame, making it popular in real-time applications.
           It is used in various fields, such as security surveillance, traffic monitoring, and retail analytics.
           Object detection models not only detect objects but also classify them, offering insights into the scene content.
        """)
        st.image(objdetection_img_path, caption="Object Detection")

        st.write("""
        3. **Image Segmentation** - Divides images into different segments for better analysis. 
           In segmentation, every pixel in the image is classified into a category, making it useful for applications like medical imaging and autonomous driving.
           YOLO-based models are also employed for instance and semantic segmentation, where the goal is to delineate objects from the background.
           Accurate segmentation can help in tasks like object tracking, contour detection, and region-based analysis.
        """)
        st.image(segmentation_img_path, caption="Image Segmentation")

        st.write("""
        4. **Keypoints Detection** - Detects key points on objects or human bodies for more detailed analysis. 
           This service is particularly useful for human pose estimation, facial landmark detection, and activity recognition.
           Keypoints detection is widely applied in sports analytics, motion capture for animation, and human-computer interaction.
           The model predicts the locations of important points like joints, facial landmarks, or object corners for better contextual understanding.
        """)
        st.image(KeypointsDetection_img_path, caption="Keypoints Detection")

    elif selected == "Image Classification":
        st.session_state.menu_open = False  # Close the sidebar
        exec(open(imgclassification_filepath).read())  # Run the Image Classification script

    elif selected == "Object Detection":
        st.session_state.menu_open = False  # Close the sidebar
        exec(open(objdeection_filepath).read())  # Run the Object Detection script

    elif selected == "Image Segmentation":
        st.session_state.menu_open = False  # Close the sidebar
        exec(open(segmentation_filepath).read())  # Run the Image Segmentation script

    elif selected == "Keypoints Detection":
        st.session_state.menu_open = False  # Close the sidebar
        exec(open(KeyPointsDetection_filepath).read())  # Run the Keypoints Detection script

# Initialize session state for menu state
if 'menu_open' not in st.session_state:
    st.session_state.menu_open = True

# Main entry point
if __name__ == "__main__":
    if st.session_state.menu_open:
        show_yolo_services()
    else:
        st.write("Menu is closed. Click the hamburger icon to open it again.")
