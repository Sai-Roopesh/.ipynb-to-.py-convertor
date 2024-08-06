import streamlit as st
import nbformat
import io

def convert_ipynb_to_py(ipynb_file):
    notebook = nbformat.read(ipynb_file, as_version=4)
    py_content = ""
    
    for cell in notebook.cells:
        if cell.cell_type == "code":
            py_content += cell.source + "\n\n"
    
    return py_content

st.title("Jupyter Notebook to Python Converter")

uploaded_file = st.file_uploader("Choose a .ipynb file", type="ipynb")

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    
    if st.button("Convert to .py"):
        py_content = convert_ipynb_to_py(uploaded_file)
        
        st.text_area("Python Code", py_content, height=300)
        
        py_file = io.BytesIO(py_content.encode())
        
        st.download_button(
            label="Download .py file",
            data=py_file,
            file_name=uploaded_file.name.replace(".ipynb", ".py"),
            mime="text/plain"
        )
