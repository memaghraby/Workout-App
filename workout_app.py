import streamlit as st
import random

# Workout Database with Real Images
workouts = {
    "Chest": {
        "Upper Chest": [("Incline Bench Press", ["https://storage.googleapis.com/flex-web-media-prod/content/images/wp-content/uploads/2024/05/muscles-worked-during-incline-bench-press.jpg"]),
                        ("Incline Dumbbell Press", ["https://hips.hearstapps.com/hmg-prod/images/dumbbell-press-1618499448.jpg"]),
                        ("Incline Cable Fly", [])],
        "Middle Chest": [("Flat Bench Press", []),
                         ("Dumbbell Fly", []),
                         ("Cable Crossover", [])],
        "Lower Chest": [("Decline Bench Press", []),
                        ("Dips", []),
                        ("Decline Dumbbell Press", [])],
    },
    "Back": {
        "Upper Back": [("Pull-Ups", []),
                        ("Face Pulls", []),
                        ("Wide-Grip Lat Pulldown", [])],
        "Middle Back": [("Seated Row", []),
                         ("Bent-over Row", []),
                         ("T-Bar Row", [])],
        "Lower Back": [("Deadlift", []),
                        ("Hyperextensions", []),
                        ("Good Mornings", [])],
    },
    "Shoulders": {
        "Front Delts": [("Overhead Press", []),
                         ("Front Raises", [])],
        "Side Delts": [("Lateral Raises", []),
                        ("Arnold Press", [])],
        "Rear Delts": [("Reverse Fly", []),
                        ("Face Pulls", [])]
    },
    "Biceps": {
        "Short Head": [("Preacher Curl", []),
                        ("Concentration Curl", [])],
        "Long Head": [("Incline Dumbbell Curl", []),
                       ("Hammer Curl", [])],
        "Brachialis": [("Reverse Curl", [])]
    },
    "Triceps": {
        "Long Head": [("Overhead Triceps Extension", []),
                       ("Skull Crushers", [])],
        "Lateral Head": [("Rope Pushdown", []),
                          ("Close Grip Bench Press", [])],
        "Medial Head": [("Dips", [])]
    },
    "Forearms": {
        "Flexors": [("Wrist Curls", [])],
        "Extensors": [("Reverse Wrist Curls", [])],
        "Grip Strength": [("Farmer's Walk", [])]
    },
    "Legs": {
        "Quadriceps": [("Squats", []),
                        ("Leg Extensions", [])],
        "Hamstrings": [("Romanian Deadlifts", []),
                        ("Leg Curls", [])],
        "Glutes": [("Hip Thrusts", [])],
        "Calves": [("Standing Calf Raise", []),
                    ("Seated Calf Raise", [])],
    },
    "Core": {
        "Upper Abs": [("Crunches", [])],
        "Lower Abs": [("Leg Raises", [])],
        "Obliques": [("Russian Twists", [])]
    }
}

def get_workout(muscle_group, num_exercises):
    if muscle_group not in workouts:
        return []
    
    muscle_parts = list(workouts[muscle_group].keys())
    selected_parts = random.sample(muscle_parts, min(num_exercises, len(muscle_parts)))
    
    selected_exercises = []
    for part in selected_parts:
        exercise = random.choice(workouts[muscle_group][part])
        selected_exercises.append(exercise)

    return selected_exercises

# Streamlit UI
st.title("Random Workout Generator")
muscle_group = st.selectbox("Choose a muscle group:", list(workouts.keys()))
max_exercises = len(workouts[muscle_group])
num_exercises = st.slider("Number of exercises:", min_value=1, max_value=max_exercises, value=max_exercises, step=1)

if st.button("Generate Workout"):
    exercises = get_workout(muscle_group, num_exercises)
    for exercise, img_urls in exercises:
        st.subheader(exercise)
        for img_url in img_urls:
            st.image(img_url, use_container_width=True)
