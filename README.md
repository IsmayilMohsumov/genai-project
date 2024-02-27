# GENAI Project 

This script utilizes OpenAI's GPT models to generate content based on different tasks: describing an image, developing functional specifications, and creating test cases.

## Requirements

- Python 3
- OpenAI API key
- OpenAI Python library

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/your_repo.git
    cd your_repo
    ```

2. Set up your OpenAI API key:

    ```bash
    export OPENAI_API_KEY='your_api_key_here'
    ```

3. Run the script:

    ```bash
    python your_script.py
    ```

## Sample Output

### Task 1: Describe Image and Write to File

- Input: Image URL
- Output: `1_sap_description.txt`

### Task 2: Developing Functional Specification and Write to File

- Input: Content from `1_sap_description.txt`
- Output: `2_func_spec.txt`

### Task 3: Developing Test Cases and Write to File

- Input: Content from `2_func_spec.txt`
- Output: `3_testcases.txt`

## Troubleshooting

- Ensure your OpenAI API key is correctly set in your environment variables.
- For any issues, verify the key's validity and required permissions.

Feel free to customize the script or integrate it into your project as needed.
