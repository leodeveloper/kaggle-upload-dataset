import os
import json
import glob

# Set Kaggle API credentials using environment variables
os.environ['KAGGLE_USERNAME'] = ''
os.environ['KAGGLE_KEY'] = ''

# Define the folder containing the CSV files
csv_folder_path = ''
username = ''  # Your Kaggle username

# Define the common metadata
dataset_title_template = ' Youtube Channel {}'
dataset_description_template = 'Description for the {} , youtube channel videos. include title, description, view_count,  publish_date, length, author. This CSV dataset contains detailed information about videos YouTube channel, last update on June 24, 2024.'

# Get the list of all CSV files in the folder
csv_files = glob.glob(os.path.join(csv_folder_path, '*.csv'))

# Function to create the metadata dictionary
def create_metadata(filename, title, description):
    return {
        "title": title,
        "subtitle": title,
        "id": f"{username}/{filename}",
        "licenses": [
            {
                "name": "CC0-1.0"
            }
        ],
        "description": description,
        "keywords": [
    "Video",
    "Advanced","English","Python"
  ]
        
    }

# Iterate over each CSV file and create a dataset
for csv_file_path in csv_files:
    # Extract the file name without extension
    filename = os.path.splitext(os.path.basename(csv_file_path))[0]
    # Define the dataset-specific metadata
    dataset_title = dataset_title_template.format(filename)
    dataset_description = dataset_description_template.format(filename)

    # Create the metadata
    metadata = create_metadata(filename, dataset_title, dataset_description)

    # Create a temporary directory for the dataset
    dataset_dir = filename
    os.makedirs(dataset_dir, exist_ok=True)


    # Save the metadata to a json file
    metadata_path = os.path.join(dataset_dir, 'dataset-metadata.json')
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=4)

    # Copy the CSV file to the dataset directory
    csv_dest_path = os.path.join(dataset_dir, os.path.basename(csv_file_path))
    os.system(f'cp {csv_file_path} {csv_dest_path}')

    # Use Kaggle API to create the dataset
    os.system(f'kaggle datasets create -u -p {dataset_dir}')

    # Cleanup the temporary directory after creating the dataset
    os.system(f'rm -r {dataset_dir}')

print("All datasets have been created.")
