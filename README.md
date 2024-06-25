# Kaggle Upload Dataset

A Python script to upload CSV datasets to Kaggle.

## Overview

This repository contains a Python script that simplifies the process of uploading CSV datasets to Kaggle. This can be particularly useful for data scientists and analysts who frequently work with Kaggle for data competitions or sharing datasets.

## Features

- Upload CSV files directly to Kaggle.
- Simple and easy-to-use command-line interface.

## Requirements

- Python 3.x
- Kaggle API Key

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/leodeveloper/kaggle-upload-dataset.git
    cd kaggle-upload-dataset
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. If you do not have a Kaggle API key, you can create one from the [Kaggle website](https://www.kaggle.com/account).

2. Run the script with your CSV file and other required parameters:

    ```bash
    python upload-dataset.py --file path/to/your/dataset.csv --title "Your Dataset Title" --dataset "username/dataset-name" --description "Description of your dataset"
    ```

## Parameters

- `--file`: Path to the CSV file to be uploaded.
- `--title`: Title of the dataset on Kaggle.
- `--dataset`: Dataset identifier in the format `username/dataset-name`.
- `--description`: Description of the dataset.

## License

This project is licensed under the AGPL-3.0 License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For any issues or questions, please open an issue in the repository.


