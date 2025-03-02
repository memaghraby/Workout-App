import streamlit as st
import random

# Workout Database with Real Images
workouts = {
    "Chest": {
        "Upper Chest": [("Incline Bench Press", ["https://storage.googleapis.com/flex-web-media-prod/content/images/wp-content/uploads/2024/05/muscles-worked-during-incline-bench-press.jpg"]),
                        ("Incline Dumbbell Press", ["https://hips.hearstapps.com/hmg-prod/images/dumbbell-press-1618499448.jpg"]),
                        ("Incline Machine Press", ["https://training.fit/wp-content/uploads/2020/02/schraegbankdruecken-maschine-800x448.png"]),
                        ("Incline Dumbbell Fly", ["https://www.bodybuildingmealplan.com/wp-content/uploads/Incline-Dumbbell-Fly-Muscles-Worked.png"]),
                        ("Decline Push-Ups", ["https://www.fitwirr.com/wp-content/uploads/2022/05/decline-push-ups-workout.jpg"]),
                        ("Reverse-Grip Bench Press", ["https://static.strengthlevel.com/images/exercises/reverse-grip-bench-press/reverse-grip-bench-press-400.avif"])],
        "Middle Chest": [("Flat Bench Press", ["https://training.fit/wp-content/uploads/2018/11/bankdruecken-flachbank-langhantel.png"]),
                         ("Dumbbell Bench Press", ["https://hips.hearstapps.com/hmg-prod/images/dumbbell-bench-press-640733e6e6d2c.jpg"]),
                         ("Chest Press", ["https://training.fit/wp-content/uploads/2020/02/brustpresse-flach-800x448.png"]),
                         ("Svend Press", ["https://liftmanual.com/wp-content/uploads/2023/04/dumbbell-svend-press.jpg"]),
                         ("Dumbbell Fly", ["https://bodybuilding-wizard.com/wp-content/uploads/2014/05/flat-bench-dumbbell-flyes.jpg"]),
                         ("Butterfly Machine", ["https://training.fit/wp-content/uploads/2020/02/butterflys-800x448.png"]),
                         ("Push-Ups", ["https://i.ytimg.com/vi/M2avll-yrtE/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCcf77Gi3tqUmnv05erv_CRw05JTA"]),
                         ("Cable Crossover", ["https://www.inspireusafoundation.org/wp-content/uploads/2024/02/cable-standing-crossover.gif"])],
        "Lower Chest": [("Decline Bench Press", ["https://training.fit/wp-content/uploads/2020/02/bankdruecken-kurzhantel-negativ.png"]),
                        ("Decline Machine Press", ["https://liftmanual.com/wp-content/uploads/2023/04/lever-decline-chest-press.jpg"]),
                        ("Incline Push-Ups", ["https://fitnessprogramer.com/wp-content/uploads/2021/06/Incline-Push-Up.gif"]),
                        ("Dips", ["https://training.fit/wp-content/uploads/2020/02/dips.png"]),
                        ("Decline Dumbbell Press", ["https://fitnessprogramer.com/wp-content/uploads/2021/02/Decline-Dumbbell-Press.gif"])],
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

def get_workout(muscle_group, muscle_part, num_exercises):
    if muscle_part != "All":
        selected_exercises = random.sample(workouts[muscle_group][muscle_part], num_exercises)
    else:
        muscle_parts = list(workouts[muscle_group].keys())
        selected_parts = random.sample(muscle_parts, min(num_exercises, len(muscle_parts)))

        selected_exercises = []
        for part in selected_parts:
            exercise = random.choice(workouts[muscle_group][part])
            selected_exercises.append(exercise)

    return selected_exercises

# Streamlit UI
st.title("Workout Generator")
muscle_group = st.selectbox("Select Muscle Group", list(workouts.keys()))
muscle_part = st.selectbox("Select Muscle Part", ["All"] + list(workouts[muscle_group].keys()))
max_exercises = len(workouts[muscle_group])
slider_disabled = (muscle_part != "All")
slider_value = 1 if slider_disabled else max_exercises
num_exercises = st.slider("Number of Exercises", 1, max_exercises, slider_value, disabled=slider_disabled)

if st.button("Generate Workout"):
    exercises = get_workout(muscle_group, muscle_part, num_exercises)
    for exercise, img_urls in exercises:
        st.subheader(exercise)
        for img_url in img_urls:
            st.image(img_url, use_container_width=True)
