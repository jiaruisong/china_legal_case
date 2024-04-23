import os
import json
import glob


def create_state_file(base_path, output_folder, state_file_path):
    # Pattern to find all CSV files in the output folder
    path_pattern = os.path.join(output_folder, "**", "*.csv")
    processed_files = [os.path.basename(
        file_path) for file_path in glob.glob(path_pattern, recursive=True)]

    # Create a dictionary with file names as keys and 'True' as values
    state_data = {file_name: True for file_name in processed_files}

    # Write this dictionary to a JSON file
    with open(state_file_path, "w") as file:
        json.dump(state_data, file)
    print(
        f"State file created at {state_file_path} with {len(processed_files)} entries.")


# Base path where processing starts (used for any additional logic you might need)
base_path = ""

# Path where processed files are located
output_folder = "/Users/jiaruisong/Documents/Coding/INFO 288 Big Data and Development_Data/drug_related_full_dataset_percent_type_amount"

# Specify the path to save the state file
state_file_path = "/Users/jiaruisong/Documents/Coding/INFO 288 Big Data and Development_Data/statefile/state_file.json"

# Create the state file using the detected processed files
create_state_file(base_path, output_folder, state_file_path)
