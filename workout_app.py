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
                         ("Dumbbell Fly", ["https://training.fit/wp-content/uploads/2019/02/fliegende-flachbank-kurzhanteln-1.png"]),
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
        "Front Delts (Anterior)": [("Overhead Barbell Press", ["https://training.fit/wp-content/uploads/2020/03/schulterdruecken-langhantel.png"]),
                                    ("Overhead Dumbbell Press", ["https://training.fit/wp-content/uploads/2020/03/schulterdruecken-kurzhanteln.png"]),
                                    ("Arnold Press", ["https://training.fit/wp-content/uploads/2020/03/arnold-press-2.png"]),
                                    ("Dumbbell Front Raise", ["https://training.fit/wp-content/uploads/2020/03/frontheben-kurzhanteln.png"]),
                                    ("Barbell Front Raise", ["https://training.fit/wp-content/uploads/2020/03/frontheben-langhantel.png"]),
                                    ("Cable Front Raise", ["https://i.pinimg.com/736x/e7/02/b6/e702b62982eec5497bd8ab81923f183d.jpg"]),
                                    ("Landmine Press", ["https://i.pinimg.com/originals/78/d9/a6/78d9a6eaab1b5a60984fa93e2473a33c.gif"])],  

        "Side Delts (Lateral)": [("Dumbbell Lateral Raise", ["https://training.fit/wp-content/uploads/2020/03/seitenheben-kurzhanteln.png"]),
                                  ("Cable Lateral Raise", ["https://liftmanual.com/wp-content/uploads/2023/04/cable-leaning-lateral-raise.jpg"]),
                                  ("Upright Row", ["https://training.fit/wp-content/uploads/2020/02/aufrechtes-rudern-kurzhantel.png"]),
                                  ("Behind-the-Neck Press", ["https://liftmanual.com/wp-content/uploads/2023/04/smith-behind-neck-press.jpg"])],  

        "Rear Delts (Posterior)": [("Dumbbell Reverse Fly", ["https://training.fit/wp-content/uploads/2020/02/reverse-flys-schraegbank.png"]),
                                    ("Cable Reverse Fly", ["https://training.fit/wp-content/uploads/2020/02/reverse-flys-fitnessbank.png"]),
                                    ("Face Pulls", ["https://fitnessprogramer.com/wp-content/uploads/2021/02/Face-Pull.gif"]),
                                    ("Bent-Over Lateral Raise", ["https://liftmanual.com/wp-content/uploads/2023/04/dumbbell-rear-lateral-raise.jpg"]),
                                    ("Rear Delt Fly", ["https://anabolicaliens.com/cdn/shop/articles/5f9892a2b0625c92c74ee6b8_rear-delt-fly-machine-picture_500x.png?v=1641754148"]),
                                    ("Rear Delt Row", ["https://training.fit/wp-content/uploads/2020/02/rudern-geraet.png"])],

        "Traps": [("Dumbbell Shrugs", ["https://training.fit/wp-content/uploads/2020/02/shrugs-kurzhantel.png"]),
                  ("Barbell Shrugs", ["https://static.strengthlevel.com/images/exercises/barbell-shrug/barbell-shrug-800.jpg"]),
                  ("Kettlebell Shrugs", ["https://www.kettlebellkings.com/cdn/shop/articles/Kettlebell_Upright_row.jpg?v=1732871020"])],
    },
    "Biceps": {
        "Long Head (Outer Bicep)": [("Incline Dumbbell Curl", ["https://training.fit/wp-content/uploads/2020/02/bizepscurls-schraegbank.png"]),
                                     ("Cross-Body Hammer Curl", ["https://apilyfta.com/static/GymvisualPNG/16571101-Dumbbell-Cross-Body-Hammer-Curl-(Version-2)_Upper-Arms_small.png"]),
                                     ("Drag Curl", ["https://miro.medium.com/v2/resize:fit:1166/1*-_Tz8c4mQhUC3w8OaMSGwA.jpeg"]),
                                     ("Behind-the-Back Cable Curl", ["https://fitliferegime.com/wp-content/uploads/2023/06/Behind-The-Back-Cable-Curl.gif"]),
                                     ("Narrow-Grip Barbell Curl", ["https://images.squarespace-cdn.com/content/v1/5ffcea9416aee143500ea103/1638183512453-1LQXFJKQWC9MEHOAIBG5/Narrow-Grip%2BStanding%2BBarbell%2BBiceps%2BCurl.png"])],  

        "Short Head (Inner Bicep)": [("Preacher Curl", ["https://www.kettlebellkings.com/cdn/shop/articles/Preacher_Curl_Alternatives.png?v=1731324163"]),
                                      ("Concentration Curl", ["https://training.fit/wp-content/uploads/2020/02/bizeps-konzentrationscurls.png"]),
                                      ("Wide-Grip Barbell Curl", ["https://training.fit/wp-content/uploads/2020/02/bizepscurls-stehend-langhantel.png"]),
                                      ("Cable Curl with Rope Attachment", ["https://www.lyfta.app/_next/image?url=https%3A%2F%2Flyfta.app%2Fimages%2Fexercises%2F01651101.png&w=640&q=10"]),
                                      ("Supinated Dumbbell Curl", ["https://newlife.com.cy/wp-content/uploads/2019/11/23211301-Dumbbell-Standing-Inner-Biceps-Curl-version-2_Upper-Arms_360.gif"])],  

        "Brachialis (Thickness & Forearm Involvement)": [("Zottman Curl", ["https://liftmanual.com/wp-content/uploads/2023/04/dumbbell-zottman-curl.jpg"]),
                                                         ("Reverse Grip Curl", ["https://cdn.shopify.com/s/files/1/1497/9682/files/2_f2d1dab5-fca3-4f35-9425-0a1cc728993c.jpg?v=1653395042"]),
                                                         ("Hammer Curl", ["https://training.fit/wp-content/uploads/2020/02/bizeps-hammercurls.png"]),
                                                         ("EZ Bar Reverse Curl", ["https://fitliferegime.com/wp-content/uploads/2022/03/EZ-bar-reverse-grip-curl.jpg"])],
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
        "Quadriceps": [("Back Squat", ["https://training.fit/wp-content/uploads/2020/03/kniebeugen-langhantel.png"]),
                       ("Front Squat", ["https://training.fit/wp-content/uploads/2020/03/kniebeugen-langhantel-vorne.png"]),
                       ("Leg Press", ["https://training.fit/wp-content/uploads/2020/03/beinpresse.png"]),
                       ("Bulgarian Split Squat", ["https://www.burnthefatinnercircle.com/members/images/2003b.png?cb=20250102035912"]),
                       ("Lunges", ["https://trainingstation.co.uk/cdn/shop/articles/Lunges-movment_900x.webp?v=1719507455"]),
                       ("Step-Ups", ["https://training.fit/wp-content/uploads/2020/03/aufsteiger-seitlich-kurzhantel.png"]),
                       ("Hack Squat", ["https://www.inspireusafoundation.org/wp-content/uploads/2021/10/hack-squat-machine-1536x883.png"]),
                       ("Leg Extension", ["https://lyfta.app/_next/image?url=%2Fthumbnails%2F05851201.jpg&w=1920&q=20"])],  

        "Hamstrings": [("Seated Leg Curl", ["https://www.burnthefatinnercircle.com/members/images/198b.jpg?cb=20250102040452"]),
                       ("Lying Leg Curl", ["https://www.burnthefatinnercircle.com/members/images/1255b.jpg?cb=20250102035845"]),
                       ("Nordic Hamstring Curl", ["https://www.kettlebellkings.com/cdn/shop/articles/nordic_curls.gif?v=1699444790"])],  

        "Glutes": [("Hip Thrust", ["https://liftmanual.com/wp-content/uploads/2023/04/dumbbell-hip-thrust.jpg"]),
                   ("Sumo Deadlift", ["https://www.kettlebellkings.com/cdn/shop/articles/kettlebell_sumo_deadlift.jpg?v=1732018260"]),
                   ("Cable Kickback", ["https://static.strengthlevel.com/images/exercises/cable-kickback/cable-kickback-800.jpg"]),
                   ("Reverse Lunge", ["https://homeworkouts.org/wp-content/uploads/anim-reverse-lunges.gif"])],  

        "Calves": [("Standing Calf Raise", ["https://liftmanual.com/wp-content/uploads/2023/04/dumbbell-standing-calf-raise.jpg"]),
                   ("Seated Calf Raise", ["https://training.fit/wp-content/uploads/2020/03/wadenheben-kurzhantel-sitzend.png"])],  

        "Adductors (Inner Thighs)": [("Machine Adduction", ["https://training.fit/wp-content/uploads/2020/03/adduktoren-geraet-800x448.png"]),
                                     ("Cossack Squat", ["https://liftmanual.com/wp-content/uploads/2023/04/weighted-cossack-squats.jpg"]),
                                     ("Cable Adduction", ["https://training.fit/wp-content/uploads/2020/03/adduktion-kabelzug.png"])],  

        "Abductors (Outer Thighs)": [("Cable Abduction", ["https://liftmanual.com/wp-content/uploads/2023/04/band-hip-abduction.jpg"]),
                                     ("Seated Hip Abduction", ["https://www.lyfta.app/_next/image?url=%2Fthumbnails%2F05971201.jpg&w=1920&q=20"])]
    },
    "Core": {
        "Upper Abs": [("Crunches", ["https://training.fit/wp-content/uploads/2019/08/crunches-liegend.png"]),
                      ("Cable Crunch", ["https://training.fit/wp-content/uploads/2020/01/kabelzugcrunches.png"]),
                      ("Sit-Ups", ["https://training.fit/wp-content/uploads/2020/01/situps-800x448.png"]),
                      ("Hanging Knee Raise", ["https://training.fit/wp-content/uploads/2020/01/knieheben-800x448.png"]),
                      ("Toe Touches", ["https://fitnessprogramer.com/wp-content/uploads/2022/12/Lying-Toe-Touches.gif"])],  

        "Lower Abs": [("Leg Raises", ["https://www.hevyapp.com/wp-content/uploads/leg-raises.png"]),
                      ("Flutter Kicks", ["https://www.lyfta.app/_next/image?url=%2Fthumbnails%2F12441201.jpg&w=3840&q=20"]),
                      ("V-Ups", ["https://www.inspireusafoundation.org/wp-content/uploads/2023/08/v-sit-up-muscles-1024x285.png"]),
                      ("Pulse Ups", ["https://liftmanual.com/wp-content/uploads/2023/04/pulse-up.jpg"])],  

        "Obliques": [("Russian Twists", ["https://www.inspireusafoundation.org/wp-content/uploads/2021/12/the-kettlebell-russian-twist-2048x736.png"]),
                     ("Side Plank", ["https://www.lyfta.app/_next/image?url=%2Fthumbnails%2F07151201.jpg&w=3840&q=20"]),
                     ("Cable Woodchopper", ["https://static.strengthlevel.com/images/exercises/cable-woodchopper/cable-woodchopper-800.jpg"]),
                     ("Bicycle Crunches", ["https://training.fit/wp-content/uploads/2020/01/bicycle-exercise-800x448.png"]),
                     ("Side Bends", ["https://training.fit/wp-content/uploads/2020/01/oberkoerperbeugen-geraet.png"]),
                     ("Dumbbell Side Bends", ["https://training.fit/wp-content/uploads/2020/01/seitliches-oberkoerpernbeugen-800x448.png"])],  

        "Transverse Abdominis (Deep Core)": [("Plank", ["https://fitnessprogramer.com/wp-content/uploads/2021/02/plank.gif"]),
                                             ("Dead Bug", ["https://fitnessprogramer.com/wp-content/uploads/2021/05/Dead-Bug.gif"]),
                                             ("Ab Wheel Rollout", ["https://training.fit/wp-content/uploads/2020/01/ausrollen-kurzhantel-gewichte-800x448.png"])],
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
