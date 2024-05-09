import streamlit as st
from TexSoup import TexSoup
import os
from glob import glob


# List all .tex files in the below path
PATH = os.path.join(os.getcwd(), "InputFiles")
EXT = "*.tex"
all_tex_files = [file
                 for path, subdir, files in os.walk(PATH)
                 for file in glob(os.path.join(path, EXT))]

st.title('Latex Extractor')
st.markdown("**Extracted all Physics and Mathematical equations from the .tex latex files**")

# Select Box
file = st.selectbox('Select Latex File', all_tex_files)

# Parse .tex files and extract only latex equation
soup = TexSoup(open(file, 'r'))
equations = soup.find_all("equation")
#print(equations)
for equation in equations:
    try:
        equation_text = str(equation).replace("\\label", "").replace("\\mathds", "").replace("\\Hat", "")
        st.latex(equation_text)
    except Exception as e:
        st.error(f"Error displaying equation: {e}")
