import streamlit as st
import random

# Workout Database with Real Images
workouts = {
    "Chest": {
        "Upper Chest": [("Incline Bench Press", ["https://storage.googleapis.com/flex-web-media-prod/content/images/wp-content/uploads/2024/05/muscles-worked-during-incline-bench-press.jpg"]),
                        ("Incline Dumbbell Press", ["https://hips.hearstapps.com/hmg-prod/images/dumbbell-press-1618499448.jpg"]),
                        ("Incline Machine Press", ["https://training.fit/wp-content/uploads/2020/02/schraegbankdruecken-maschine-800x448.png"]),
                        ("Incline Dumbbell Fly", ["https://www.bodybuildingmealplan.com/wp-content/uploads/Incline-Dumbbell-Fly-Muscles-Worked.png"]),
                        ("Decline Push-Ups", ["https://training.fit/wp-content/uploads/2020/02/negativ-liegestuetze.png"]),
                        ("Cable Crossover", ["https://www.inspireusafoundation.org/wp-content/uploads/2024/02/cable-standing-crossover.gif"]),
                        ("Reverse-Grip Bench Press", ["https://static.strengthlevel.com/images/exercises/reverse-grip-bench-press/reverse-grip-bench-press-400.avif"])],
        
        "Middle Chest": [("Flat Bench Press", ["https://training.fit/wp-content/uploads/2018/11/bankdruecken-flachbank-langhantel.png"]),
                         ("Dumbbell Bench Press", ["https://hips.hearstapps.com/hmg-prod/images/dumbbell-bench-press-640733e6e6d2c.jpg"]),
                         ("Chest Press", ["https://training.fit/wp-content/uploads/2020/02/brustpresse-flach-800x448.png"]),
                         ("Svend Press", ["https://liftmanual.com/wp-content/uploads/2023/04/dumbbell-svend-press.jpg"]),
                         ("Dumbbell Fly", ["https://bodybuilding-wizard.com/wp-content/uploads/2014/05/flat-bench-dumbbell-flyes.jpg"]),
                         ("Cable Chest Fly", ["https://training.fit/wp-content/uploads/2020/02/fliegende-kabelzug.png"]),
                         ("Butterfly Machine", ["https://training.fit/wp-content/uploads/2020/02/butterflys-800x448.png"]),
                         ("Push-Ups", ["https://i.ytimg.com/vi/M2avll-yrtE/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCcf77Gi3tqUmnv05erv_CRw05JTA"])],
        
        "Lower Chest": [("Decline Bench Press", ["https://training.fit/wp-content/uploads/2020/02/bankdruecken-kurzhantel-negativ.png"]),
                        ("Decline Machine Press", ["https://liftmanual.com/wp-content/uploads/2023/04/lever-decline-chest-press.jpg"]),
                        ("Incline Push-Ups", ["https://fitnessprogramer.com/wp-content/uploads/2021/06/Incline-Push-Up.gif"]),
                        ("Dips", ["https://training.fit/wp-content/uploads/2020/02/dips.png"]),
                        ("Decline Dumbbell Press", ["https://fitnessprogramer.com/wp-content/uploads/2021/02/Decline-Dumbbell-Press.gif"])],
    },
    "Back": {
        "Upper Back": [("Bent Over Row", []),
                       ("Pendlay Row", []),
                       ("T-Bar Row with Handle", []),
                       ("Chest-Supported Row", []),
                       ("Reverse Fly", []),
                       ("Inverted Row", []),
                       ("Suspended Row", []),
                       ("Renegade Row", []),
                       ("Seated Cable Row", []),
                       ("Wide-Grip Seated Row", []),
                       ("TRX Row", []),
                       ("Face Pulls", [])],  

        "Lats": [("Pull-Up", []),
                 ("Lat Pulldown", []),
                 ("One-Arm Dumbbell Row", []),
                 ("Dumbbell Row", []),
                 ("Barbell Rows", []),
                 ("Dumbbell Pullover", []),
                 ("Close-Grip Lat Pulldown", []),
                 ("Neutral-Grip Pull-Up", []),
                 ("Straight-Arm Lat Pulldown", []),
                 ("Rack Pulls", [])],  

        "Lower Back": [("Deadlift", []),
                       ("Good-Morning", []),
                       ("Back Extension", []),
                       ("Superman", []),
                       ("Jefferson Curl", []),
                       ("Romanian Deadlift", [])],
    },
    "Shoulders": {
        "Front Delts (Anterior)": [("Overhead Barbell Press", []),
                                    ("Overhead Dumbbell Press", []),
                                    ("Arnold Press", []),
                                    ("Front Raise (Dumbbell)", []),
                                    ("Front Raise (Barbell)", []),
                                    ("Cable Front Raise", []),
                                    ("Landmine Press", [])],  

        "Side Delts (Lateral)": [("Lateral Raise (Dumbbell)", []),
                                  ("Lateral Raise (Cable)", []),
                                  ("Upright Row", []),
                                  ("Lean-Away Lateral Raise", []),
                                  ("Wide-Grip Overhead Press", []),
                                  ("Behind-the-Neck Press", [])],  

        "Rear Delts (Posterior)": [("Reverse Fly (Dumbbell)", []),
                                    ("Reverse Fly (Cable)", []),
                                    ("Face Pulls", []),
                                    ("Bent-Over Lateral Raise", []),
                                    ("Rear Delt Row", []),
                                    ("Reverse Pec Deck Machine", []),
                                    ("Wide-Grip Seated Row (Rear Delt Focus)", [])],  

        "Traps": [("Dumbbell Shrugs", []),
                  ("Barbell Shrugs", []),
                  ("Face Pulls", []),
                  ("Farmer's Carry", []),
                  ("Kettlebell Shrugs", []),
                  ("Overhead Shrugs", [])]  
    },
    "Biceps": {
        "Long Head (Outer Bicep)": [("Incline Dumbbell Curl", []),
                                     ("Hammer Curl", []),
                                     ("Cross-Body Hammer Curl", []),
                                     ("Drag Curl", []),
                                     ("Behind-the-Back Cable Curl", []),
                                     ("Narrow-Grip Barbell Curl", [])],  

        "Short Head (Inner Bicep)": [("Preacher Curl", []),
                                      ("Spider Curl", []),
                                      ("Concentration Curl", []),
                                      ("Wide-Grip Barbell Curl", []),
                                      ("Cable Curl with Rope Attachment", []),
                                      ("Dumbbell Curl (Supinated)", [])],  

        "Brachialis (Thickness & Forearm Involvement)": [("Zottman Curl", []),
                                                         ("Reverse Grip Curl", []),
                                                         ("Hammer Curl", []),
                                                         ("Pinwheel Curl", []),
                                                         ("EZ Bar Reverse Curl", [])],
    },
    "Triceps": {
        "Long Head": [("Overhead Dumbbell Extension", []),
                      ("Overhead EZ Bar Extension", []),
                      ("Overhead Cable Extension", []),
                      ("French Press", []),
                      ("Dumbbell Kickback", []),
                      ("Cable Kickback", []),
                      ("Overhead Rope Extension", []),
                      ("Incline Dumbbell Triceps Extension", [])],  

        "Lateral Head": [("Triceps Pushdown (Rope)", []),
                         ("Triceps Pushdown (Straight Bar)", []),
                         ("Dips (Triceps Focus)", []),
                         ("Diamond Push-Ups", []),
                         ("Close-Grip Bench Press", []),
                         ("Reverse Grip Triceps Pushdown", []),
                         ("Parallel Bar Dips", []),
                         ("Decline Close-Grip Bench Press", []),
                         ("Bench Dip", [])],  

        "Medial Head": [("Close-Grip Push-Up", []),
                        ("JM Press", []),
                        ("Bodyweight Triceps Extension", []),
                        ("Floor Press (Triceps Focus)", []),
                        ("Reverse Grip Bench Press", []),
                        ("Cable Triceps Kickback", []),
                        ("Tate Press", [])]
    },
    "Legs": {
        "Quadriceps": [("Back Squat", []),
                       ("Front Squat", []),
                       ("Leg Press", []),
                       ("Bulgarian Split Squat", []),
                       ("Lunges", []),
                       ("Step-Ups", []),
                       ("Hack Squat", []),
                       ("Sissy Squat", []),
                       ("Leg Extension", [])],  

        "Hamstrings": [("Romanian Deadlift", []),
                       ("Seated Leg Curl", []),
                       ("Lying Leg Curl", []),
                       ("Nordic Hamstring Curl", []),
                       ("Good Morning", []),
                       ("Glute-Ham Raise", []),
                       ("Single-Leg Romanian Deadlift", [])],  

        "Glutes": [("Hip Thrust", []),
                   ("Glute Bridge", []),
                   ("Sumo Deadlift", []),
                   ("Cable Kickback", []),
                   ("Step-Ups (Glute Focus)", []),
                   ("Bulgarian Split Squat (Glute Focus)", []),
                   ("Reverse Lunge", [])],  

        "Calves": [("Standing Calf Raise", []),
                   ("Seated Calf Raise", []),
                   ("Donkey Calf Raise", []),
                   ("Jump Rope", []),
                   ("Tibialis Raise", [])],  

        "Adductors (Inner Thighs)": [("Sumo Squat", []),
                                     ("Machine Adduction", []),
                                     ("Side-Lying Leg Lift", []),
                                     ("Cossack Squat", []),
                                     ("Cable Adduction", [])],  

        "Abductors (Outer Thighs)": [("Side-Lying Clamshell", []),
                                     ("Lateral Band Walk", []),
                                     ("Cable Abduction", []),
                                     ("Fire Hydrants", []),
                                     ("Seated Hip Abduction", [])]
    },
    "Core": {
        "Upper Abs": [("Crunches", []),
                      ("Cable Crunch", []),
                      ("Sit-Ups", []),
                      ("Reverse Crunch", []),
                      ("Hanging Knee Raise", []),
                      ("Toe Touches", [])],  

        "Lower Abs": [("Leg Raises", []),
                      ("Hanging Leg Raises", []),
                      ("Flutter Kicks", []),
                      ("Scissor Kicks", []),
                      ("V-Ups", []),
                      ("Pulse Ups", [])],  

        "Obliques": [("Russian Twists", []),
                     ("Side Plank", []),
                     ("Hanging Oblique Knee Raises", []),
                     ("Cable Woodchopper", []),
                     ("Bicycle Crunches", []),
                     ("Side Bends (Dumbbell)", [])],  

        "Transverse Abdominis (Deep Core)": [("Plank", []),
                                             ("Stir the Pot", []),
                                             ("Dead Bug", []),
                                             ("Vacuum Exercise", []),
                                             ("Bird Dog", []),
                                             ("Ab Wheel Rollout", [])],
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
