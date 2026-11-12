
Prompt:
Final Project Design Phase\
Computer Science - Week 11\
Oct 3, 2026 - Version 0.0.4\
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\
\
For complete instructions and project ideas, refer to the assignment in Canvas. Specifically, review the final project requirements before you continue below. If you have not reviewed the project requirements in Canvas (you might have to go to the modules view and check the current or past week's content), you will not be able to properly complete the parts below. In addition, it may be helpful to review the information on this Drafter documentation page.\
0\) Project Planning and Preparation\
Successful programmers spend time planning before they begin coding. After reviewing the project requirements, answer the following questions to help guide your design and development process. \
A.	What concepts from class or previous assignments might help you complete this project? Which programming concepts (loops, conditionals, lists, classes, etc.) do you expect to use? What programming skills do you want to improve while completing this project?\
I expect to use conditionals for not including 0 and negative numbers, classes and lists to help organize each lift I am doing.\
\
B.	Which parts of the project do you expect to be the easiest for you? The hardest? Why?\
I expect the easiest part of the project would be defining the different functions I need for the code and the hardest part I think would be trying to loop things because I struggle with creating for loops.\
\
C.	Even though you have not yet designed the final project, estimate which tasks will likely require the most time and effort? Which features or components should be implemented first? \
THe component that will likely take the most time and effort is creating the different pages for the website. The features that should be implemented first are the different functions I need so that the code runs smoothly.\
\
D.	What distractions might interfere with your work and how will you minimize them? What resources will you need available while working? What questions, if any, do you still have about the assignment requirements? \
The distractions that could interfere with my work could be the 5th exam for this class and I could minimize them by studying early and completing the work well before due date to make sure Im on tract.\
\
1\) Site Diagram\
Create a mock-up of your planned website. We suggest you make the mockup on paper, although you can also use software like PowerPoint or Slides to make a mockup. There is other design software that could also be used, but we strongly encourage you to keep it simple. Do not spend more than 15-30 minutes detailing the mock-up. Your goal should be to make a very quick and dirty diagram, to show that you have some kind of idea.\
\
We recommend drawing each page as a rectangle, and laying out the text, buttons, and other components inside. Then, use arrows to indicate links between pages. Label each page the way you will name each function, and then put labels on the arrows to indicate what the button links. Also write down any parameters that should come into the pages.\
\
In addition to the pages and routes, write down what fields your \`State\` will have, both their names and types. Think clearly about what data will need to be persistent across the entire website.\
\
Add photo(s) or screenshot(s) of your website mock-up and labeled diagram on the next page. \
&#x20;  2\) Implementing Requirements\
This table should serve as a draft for how you will implement the requirements into your final project. You may change your ideas later on, but your final site must fulfill all the requirements.\
\
Requirement	Implementation\
Purpose/Functionality\
\
A 1-2 sentence description of the purpose or functionality of your site	My website will be a One Rep Max Calculator that allows users to calculate their estimated maximum weight for different exercises, including bench press, squat, and deadlift. Users can enter the weight lifted and number of repetitions, view their estimated one rep max, and save their results to look back at their previous lifts.\
State Dataclass Attributes\
&#x20;\
Minimum of 4 attributes, one of which must be a list/dict of instances of your second dataclass.\
\
Briefly describe each attribute, its type, and how it will be meaningfully modified throughout the site.	1. exercise: str – Stores the exercise the user selected (bench press, squat, deadlift, etc.). Changes whenever the user selects a different exercise. \
2\. weight: float – Stores the total weight lifted. Changes whenever the user enters a new weight. \
3\. reps: int – Stores the number of repetitions completed. Changes whenever the user enters a new number of reps.\
4\. estimated_max: float – Stores the calculated one rep max using the weight and repetitions entered. Changes after each calculation. \
5\. lift_history: list[LiftEntry] – Stores all previous lift entries, including the exercise, weight, reps, and estimated max. A new entry is added whenever the user saves a calculation.\
Second Dataclass\
\
Your second dataclass, including its attributes, their types, and how they will be meaningfully modified (if they are modified)	LiftEntry\
&#x20;\- exercise: str – The name of the exercise performed. \
\- weight: float – The weight lifted.\
&#x20;\- reps: int – The number of repetitions completed.\
&#x20;\- estimated_max: float – The calculated one rep max for that lift. Each time a user saves a new calculation, a new LiftEntry is created and added to the history list.\
Routes (minimum 7) \
\
The names of your route functions	1. home – Displays the homepage and navigation options. \
2\. calculator – Displays the one rep max calculator. \
3\. calculate_max – Calculates the estimated one rep max. \
4\. results – Displays the calculated result. \
5\. save_lift – Saves the current calculation to the user's history. \
6\. view_history – Displays previous lifts. \
7\. exercise_details – Displays information about different exercises and their records.\
Pages (minimum 5)\
\
A brief description of the pages in your site	1. Home Page: Welcomes users and provides navigation to the calculator and workout history. \
2\. Calculator Page: Allows users to select an exercise and enter their weight and repetitions. \
3\. Results Page: Displays their estimated one rep max after completing a calculation. \
4\. History Page: Shows previous calculations so users can track their progress. \
5\. Exercise Details Page: Displays previous bests for individual exercises and information about bench press, squat, and deadlift.\
User Input (minimum 3)\
\
Description of user input components (TextBox, TextArea, CheckBox, or SelectBox) and their purposes\
\
For more information on these input types, see Drafter Documentation.\
1\. SelectBox – Allows users to select an exercise, such as bench press, squat, or deadlift. \
2\. TextBox – Allows users to enter the amount of weight lifted. \
3\. TextBox – Allows users to enter the number of repetitions completed. \
4\. CheckBox – Allows users to choose whether to save their calculation to their workout history.\
If Statements (minimum 3)\
Brief description of what will be evaluated in your if statements and how they will meaningfully change the logic of the site	1. Check whether the user entered a valid weight and repetition amount. If either value is invalid, display an error message instead of calculating. \
2\. Check whether the selected exercise is bench press, squat, or deadlift to organize the user's results by exercise. \
3\. Check whether the user wants to save their calculation. If they do, add it to their history; otherwise, display the result without saving it.\
&#x20;4\. Check whether a new estimated max is higher than the user's previous best for that exercise. If it is, display a personal record message.\
Loop (minimum 1)\
This loop must iterate over the list/dict of dataclass instances in your State attribute.\
Description of this loop and why it is meaningful to the site	Use a for loop to iterate through the lift_history list and display each saved lift on the history page. The loop will show the exercise, weight, repetitions, and estimated one rep max for every previous calculation. This allows users to track their progress over time.\
LLM Conversation\
If you used an LLM in any part of this work, copy and paste every part of that conversation below. Otherwise, you may be given a zero for the assignment. Obviously, these words will not all be yours, and this is the exception to the requirement at the top of this assignment that all responses be in your own words. If you did not use an LLM to assist you in this assignment, simply say so below.\
Final Submission\
When you are finished, download this file as a Word Document (docx) and upload the file to the appropriate assignment on Canvas.\
\
\
okay this was part 1 now write a code that will work in thonny using drafter again here are the requriemtents:&#x20;

### Site Functionality Requirements

Below are the requirements that your site must fulfill. Plan ahead so that meeting these requirements is easier as you develop your project.

- At least 7 routes.
- At least 5 Pages, or 10 [FragmentsLinks to an external site.](https://drafter-edu.github.io/drafter/concepts/live-updates/), or a combination thereof.
- The implementation of the *State&#xA0;*&#x64;ataclass must have at least 4 fields.
  - At least one field must be a list of class instances or a dictionary of class instances.
    - This means that there must be a second dataclass.
  - At least 4 state fields, including the list or dictionary of class instances, must each be meaningfully modified in at least one route; those 4 state fields cannot be constants.
- At least 3 input fields (TextBox, CheckBox, SelectBox, TextArea). They don't have to be the same type.
- At least 3 meaningful if statements.
- At least 1 loop that iterates over an attribute of the list of class instances or dictionary of class instances in a meaningful way.
- The site should have a legitimate purpose or functionality.
- No global variables ([global constantsLinks to an external site.](https://blockpy.cis.udel.edu/assignments/textbook/bakery_textbook?page=bakery_functions_scopes_read) are fine).
- You must use the Drafter library.
- Any advanced coding techniques (i.e. that weren't covered in this course) used are thoroughly documented in the code.

More creative and impressive designs are given flexibility on the above requirements - impress us! However, impressive websites tend to do more than the above requirements. Further, **if you miss more than 2 requirements, you will get no credit for that submission**. For example, missing a second dataclass means you would be missing not only that requirement, but also the list or dictionary of such dataclass instances, and the loop iterating over that list. This would mean that the submission would get a zero.

### Code Requirements

Make sure your program and website runs; **broken programs do not earn points**. This means that if your program contains a syntax error or runs and doesn't deploy a website, you get zero points for this assignment, and are subject to any other penalties listed in [the syllabus](https://udel.instructure.com/courses/1942356/assignments/syllabus "Syllabus").

Once you are finished with your project code, check over the following:

- Chosen good variable names (check last two sections of [Chapter 1B1Links to an external site.](https://blockpy.cis.udel.edu/assignments/textbook/bakery_textbook?page=bakery_intro_variables_read))
- Unit tested your functions where possible, being [valid and thoroughLinks to an external site.](https://blockpy.cis.udel.edu/assignments/textbook/bakery_textbook?page=bakery_functions_testing_read): each route must have at least one unit test, if possible (routes that have randomization are difficult to unit test, so they are not required to).
  - If a function can't be unit tested, you must note as much in a docstring or comment.
- Broke up excessively long lines (80 characters is a good rule of thumb, but we'll be strict about not exceeding 120 characters)
- Included types in your function headers
- Included good [docstrings Links to an external site.](https://blockpy.cis.udel.edu/assignments/textbook/bakery_textbook?page=bakery_functions_docstrings_read)as the first line of your function's body
- Decomposed complicated functions with helper functions

Your TA will be grading your code's quality based on the ideas above.

### Repository Requirements

Your final project's GitHub repository should meet the following requirements.

- Planning document should be uploaded to the repository.
- Website should be deployed without error.
- Site information should be set in `main.py` using `set_site_information(...)`.
- When changing/adding files in the repository, commit messages should be **concise and descriptive**, not the default "Update (filename)" message.
- A video fulfilling the following requirements should be linked in the repository.
  - Shows functioning deployed website
  - Audible and visible
  - Accesses and explains all necessary parts of the website
- All conversations with any AI should be uploaded to the repository.

The above are either present on the final rubric or are necessary for your site to be graded.

Response:
Based on your Part 1 design, I would build your final project as a One Rep Max Calculator and Workout Tracker using Python and the Drafter library.

I'll keep the project aligned with the requirements you submitted, including:
- 7 or more routes.
- At least 5 pages.
- Two dataclasses (State and LiftEntry).
- At least 4 meaningfully modified State attributes.
- At least 3 user input fields.
- At least 3 meaningful if statements.
- A for loop that displays saved workout history.
- Function type annotations, docstrings, and unit tests.
For the one-rep-max calculation, I'll use the Epley estimation formula:
\[
1RM = weight \times (1 + reps/30)
\]

This estimates the maximum weight someone could lift for one repetition.
Complete Thonny project code
The following is designed as a single main.py file. It uses the Drafter components and routing patterns documented in the current Drafter documentation. 
Drafter Documentation+2


Before running: Make sure Drafter is installed in Thonny. You can install it through Tools → Manage Packages → search for drafter.


from drafter import *
from dataclasses import dataclass


# --------------------------------------------------
# WEBSITE INFORMATION
# --------------------------------------------------

set_website_title("One Rep Max Calculator")

set_site_information(
    author="Your Name",
    description="A website that calculates estimated one rep "
                "maxes and tracks workout history.",
    sources="Drafter documentation and Epley 1RM formula.",
    planning="See the final project planning document.",
    links=[]
)


# --------------------------------------------------
# SECOND DATACLASS
# Stores each individual saved lift
# --------------------------------------------------

@dataclass
class LiftEntry:
    exercise: str
    weight: float
    reps: int
    estimated_max: float


# --------------------------------------------------
# MAIN STATE DATACLASS
# Stores information throughout the website
# --------------------------------------------------

@dataclass
class State:
    exercise: str
    weight: float
    reps: int
    estimated_max: float
    lift_history: list[LiftEntry]
    message: str
    current_saved: bool


# --------------------------------------------------
# ROUTE 1: INDEX
# Opens the homepage
# --------------------------------------------------

@route
def index(state: State) -> Page:
    """Open the main homepage."""
    return home(state)


# --------------------------------------------------
# ROUTE 2: HOME
# Main navigation page
# --------------------------------------------------

@route
def home(state: State) -> Page:
    """Display the homepage and navigation options."""
    return Page(state, [
        Header("One Rep Max Calculator"),
        "Welcome to your personal workout tracker!",
        "Calculate your estimated one rep max for "
        "bench press, squat, and deadlift.",
        Header("Navigation", 2),
        Button("Open Calculator", "calculator"),
        Button("View Workout History", "view_history"),
        Button("Exercise Details", "exercise_details")
    ])


# --------------------------------------------------
# ROUTE 3: CALCULATOR
# Collects information from the user
# --------------------------------------------------

@route
def calculator(state: State) -> Page:
    """Display the calculator and collect workout information."""
    return Page(state, [
        Header("One Rep Max Calculator"),
        "Choose an exercise:",
        SelectBox(
            "exercise",
            ["Bench Press", "Squat", "Deadlift"],
            state.exercise
        ),
        "Enter the weight lifted (lbs):",
        TextBox("weight", state.weight),
        "Enter the number of repetitions:",
        TextBox("reps", state.reps),
        CheckBox("save_result", False),
        " Save this calculation to workout history.",
        Button("Calculate My Max", "calculate_max"),
        Button("Home", "home")
    ])


# --------------------------------------------------
# ROUTE 4: CALCULATE MAX
# Calculates the estimated one rep max
# --------------------------------------------------

@route
def calculate_max(state: State, exercise: str,
                  weight: float, reps: int,
                  save_result: bool) -> Page:
    """Calculate the estimated one rep max and update state."""

    state.exercise = exercise
    state.weight = weight
    state.reps = reps
    state.current_saved = False

    # Check that the user entered valid numbers.
    if weight <= 0 or reps <= 0:
        state.estimated_max = 0.0
        state.message = "Weight and reps must be greater than zero."
        return results(state)

    # Check that the exercise is supported.
    if exercise not in ["Bench Press", "Squat", "Deadlift"]:
        state.estimated_max = 0.0
        state.message = "Please select a valid exercise."
        return results(state)

    # Epley formula for estimated one rep max.
    estimated = weight * (1 + reps / 30)
    state.estimated_max = round(estimated, 1)

    # Find the previous best for this exercise.
    previous_best = 0.0

    for entry in state.lift_history:
        if (entry.exercise == exercise and
                entry.estimated_max > previous_best):
            previous_best = entry.estimated_max

    # Check whether the user achieved a personal record.
    if state.estimated_max > previous_best:
        state.message = "New personal record for " + exercise + "!"
    else:
        state.message = "Calculation complete!"

    # Save the lift if the checkbox was selected.
    if save_result:
        state.lift_history.append(
            LiftEntry(
                exercise,
                weight,
                reps,
                state.estimated_max
            )
        )
        state.current_saved = True
        state.message += " Lift saved to history."

    return results(state)


# --------------------------------------------------
# ROUTE 5: RESULTS
# Displays the calculated result
# --------------------------------------------------

@route
def results(state: State) -> Page:
    """Display the estimated one rep max."""
    content = [
        Header("Your Results"),
        state.message
    ]

    if state.estimated_max > 0:
        content.append("Exercise: " + state.exercise)
        content.append("Weight lifted: " + str(state.weight) + " lbs")
        content.append("Repetitions: " + str(state.reps))
        content.append(
            "Estimated one rep max: " +
            str(state.estimated_max) + " lbs"
        )

        if state.current_saved:
            content.append("This lift is already saved.")

        else:
            content.append(
                Button("Save This Lift", "save_lift")
            )

    content.append(Button("Calculate Again", "calculator"))
    content.append(Button("View History", "view_history"))
    content.append(Button("Home", "home"))

    return Page(state, content)


# --------------------------------------------------
# ROUTE 6: SAVE LIFT
# Adds the current calculation to workout history
# --------------------------------------------------

@route
def save_lift(state: State) -> Page:
    """Save the current calculation to workout history."""

    if state.estimated_max <= 0:
        state.message = "Calculate a valid lift before saving."

    elif state.current_saved:
        state.message = "This lift has already been saved."

    else:
        new_lift = LiftEntry(
            state.exercise,
            state.weight,
            state.reps,
            state.estimated_max
        )

        state.lift_history.append(new_lift)
        state.current_saved = True
        state.message = "Lift saved to history!"

    return results(state)


# --------------------------------------------------
# ROUTE 7: VIEW HISTORY
# Displays all previously saved lifts
# --------------------------------------------------

@route
def view_history(state: State) -> Page:
    """Display all saved workout history."""

    content = [
        Header("Workout History"),
        "Here are your previously saved lifts:"
    ]

    if len(state.lift_history) == 0:
        content.append("No lifts saved yet.")

    else:
        # Loop through the saved lifts and display each one.
        for entry in state.lift_history:
            content.append("--------------------")
            content.append("Exercise: " + entry.exercise)
            content.append("Weight: " + str(entry.weight) + " lbs")
            content.append("Repetitions: " + str(entry.reps))
            content.append(
                "Estimated max: " +
                str(entry.estimated_max) + " lbs"
            )

    content.append(Button("Calculate Another Lift", "calculator"))
    content.append(Button("Exercise Details", "exercise_details"))
    content.append(Button("Clear History", "clear_history"))
    content.append(Button("Home", "home"))

    return Page(state, content)


# --------------------------------------------------
# ROUTE 8: EXERCISE DETAILS
# Displays information about each exercise
# --------------------------------------------------

@route
def exercise_details(state: State) -> Page:
    """Display exercise information and saved results."""

    content = [
        Header("Exercise Details"),
        Header("Bench Press", 2),
        "The bench press works the chest, shoulders, and triceps.",
        Header("Squat", 2),
        "The squat works the quadriceps, glutes, and legs.",
        Header("Deadlift", 2),
        "The deadlift works the back, glutes, and hamstrings.",
        Header("Your Saved Lifts", 2)
    ]

    found_lift = False

    # Display saved lifts for the currently selected exercise.
    for entry in state.lift_history:
        if entry.exercise == state.exercise:
            found_lift = True
            content.append(
                entry.exercise + ": " +
                str(entry.estimated_max) + " lbs"
            )

    if not found_lift:
        content.append(
            "No saved lifts for " + state.exercise + " yet."
        )

    content.append(Button("Calculator", "calculator"))
    content.append(Button("Workout History", "view_history"))
    content.append(Button("Home", "home"))

    return Page(state, content)


# --------------------------------------------------
# ROUTE 9: CLEAR HISTORY
# Removes all saved lifts
# --------------------------------------------------

@route
def clear_history(state: State) -> Page:
    """Clear all saved workout history."""

    state.lift_history = []
    state.current_saved = False
    state.message = "Your workout history has been cleared."

    return Page(state, [
        Header("History Cleared"),
        state.message,
        Button("Back to Calculator", "calculator"),
        Button("Home", "home")
    ])


# --------------------------------------------------
# UNIT TESTS
# These run before the website starts.
# --------------------------------------------------

# Test the homepage.
assert_has(
    home(State("Bench Press", 0.0, 1, 0.0, [], "", False)),
    "One Rep Max Calculator"
)

# Test the index route.
assert_has(
    index(State("Bench Press", 0.0, 1, 0.0, [], "", False)),
    "Welcome to your personal workout tracker!"
)

# Test the calculator page.
assert_has(
    calculator(State("Bench Press", 0.0, 1, 0.0, [], "", False)),
    "Weight lifted"
)

# Test calculating a one rep max.
test_state = State("Bench Press", 0.0, 1, 0.0, [], "", False)

assert_state(
    calculate_max(test_state, "Bench Press", 100.0, 5, False),
    State(
        "Bench Press",
        100.0,
        5,
        116.7,
        [],
        "New personal record for Bench Press!",
        False
    )
)

# Test the results page.
assert_has(
    results(State("Squat", 100.0, 5, 116.7, [], "Test result", False)),
    "Estimated one rep max"
)

# Test saving a lift.
save_test_state = State(
    "Squat", 100.0, 5, 116.7, [], "", False
)

assert_state(
    save_lift(save_test_state),
    State(
        "Squat",
        100.0,
        5,
        116.7,
        [LiftEntry("Squat", 100.0, 5, 116.7)],
        "Lift saved to history!",
        True
    )
)

# Test the workout history page.
history_test_state = State(
    "Deadlift",
    150.0,
    3,
    165.0,
    [LiftEntry("Deadlift", 150.0, 3, 165.0)],
    "",
    True
)

assert_has(view_history(history_test_state), "Deadlift")

# Test the exercise details page.
assert_has(
    exercise_details(history_test_state),
    "Your Saved Lifts"
)

# Test clearing workout history.
assert_state(
    clear_history(history_test_state),
    State(
        "Deadlift",
        150.0,
        3,
        165.0,
        [],
        "Your workout history has been cleared.",
        False
    )
)


# --------------------------------------------------
# START WEBSITE
# --------------------------------------------------

start_server(
    State(
        "Bench Press",
        0.0,
        1,
        0.0,
        [],
        "Welcome!",
        False
    )
)

How this meets your assignment
9 routes
 6 pages
 2 dataclasses

Requirement	Where it is implemented
7+ routes	9 route functions
5+ pages	Home, Calculator, Results, History, Exercise Details, History Cleared
4+ State attributes	7 attributes
Second dataclass	LiftEntry
List of dataclass instances	lift_history
3+ inputs	SelectBox, 2 TextBoxes, CheckBox
3+ if statements	Validation, personal records, saving, etc.
1+ loop	Displays saved lifts
Unit tests	Tests for all 9 routes
Type annotations	Included throughout
Docstrings	Included in route functions
No global variables	No custom global variables

How to run it in Thonny
1. Open Thonny.
2. Make sure drafter is installed.
3. Create a new Python file.
4. Paste the complete code.
5. Change "Your Name" to your name.
6. Save the file as main.py.
7. Click Run.
You should see the test results in the Shell and your website should open in a browser at a local address.
Important things before submitting
There are three things I want you to be aware of:
1. Workout history: This version maintains history in the website's current state. It does not permanently save workouts between separate sessions or restarts.
2. GitHub: You will still need to upload your planning document, code, and AI conversation to your repository.
3. Site information: Add your actual GitHub repository link to set_site_information when you create the repository.
I used the current Drafter documentation for the routing, inputs, state management, testing, and site configuration patterns. 
Drafter Documentation+3


My recommendation: Run this in Thonny before submitting anything. If an error appears, share the exact error message with me so we can fix it. Also, make sure you understand the functions well enough to explain them in your project demonstration.
