# Jupyter Notebook to Python Converter

This Streamlit app allows users to convert Jupyter Notebook (.ipynb) files to Python (.py) files. You can access the live app at: [https://ipynb-to-py-convertor.streamlit.app/](https://ipynb-to-py-convertor.streamlit.app/)

## Features

- Upload .ipynb files
- Convert .ipynb files to .py files
- View the converted Python code
- Download the converted .py file

## How to Use

1. Visit the app at [https://ipynb-to-py-convertor.streamlit.app/](https://ipynb-to-py-convertor.streamlit.app/)
2. Click on "Choose a .ipynb file" to upload your Jupyter Notebook file
3. Once the file is uploaded, click on "Convert to .py"
4. The converted Python code will be displayed in a text area
5. Click on "Download .py file" to download the converted Python script

## Local Development

To run this app locally:

1. Clone the repository:
    ```bash
    git clone https://github.com/Sai-Roopesh/.ipynb-to-.py-convertor.git
    ```
2. Navigate to the project directory:
    ```bash
    cd .ipynb-to-.py-convertor
    ```
3. Create a virtual environment:
    ```bash
    python -m venv env
    ```
4. Activate the virtual environment:
    ```bash
    # On Windows
    .\env\Scripts\activate

    # On macOS/Linux
    source env/bin/activate
    ```
5. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
6. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Requirements

- streamlit==1.27.0
- nbformat==5.9.2

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Here are some ways you can contribute:

