
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
