# TODO: define the 'EXPECTED_BAKE_TIME' constant below.
EXPECTED_BAKE_TIME = 40  # Typically, lasagna bakes for 40 minutes

# TODO: Define the 'PREPARATION_TIME' constant.
PREPARATION_TIME = 2  # Let's assume 2 minutes per layer to prepare

# TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_bake_time

# TODO: Define the 'preparation_time_in_minutes()' function below.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - the number of layers of lasagna.
    :return: int - preparation time in minutes based on the number of layers.
    
    Function that calculates how many minutes it takes to prepare the lasagna 
    based on the number of layers.
    """
    return number_of_layers * PREPARATION_TIME

# TODO: Define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time in minutes.

    :param number_of_layers: int - the number of layers of lasagna.
    :param elapsed_bake_time: int - the time the lasagna has spent in the oven.
    :return: int - total time (preparation + baking).
    
    Function that calculates the total time spent making the lasagna, which is the 
    sum of the preparation time and the time already spent baking.
    """
    prep_time = preparation_time_in_minutes(number_of_layers)
    return prep_time + elapsed_bake_time
