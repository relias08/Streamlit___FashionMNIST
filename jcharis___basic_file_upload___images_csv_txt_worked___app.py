# This file corresponds to JCharis's - [Working with File Uploads In Streamlit Python](https://www.youtube.com/watch?v=vwFR2bXXzTw&t=1017s) - super stuff!!!

# This code should work for uploading images, csv files & .txt files to a Streamlit web page. 
# For MS Word and PDF files, need to pip install libraries like docx2txt, PyPDF2, pdfplumber, etc.

# Eg. we can just drag and drop any image --- like the 'cars.jpg' file from my 'data' folder onto the Streamlit web page (then need to do Obj Det on it !!!)

import streamlit as st
import streamlit.components.v1 as stc

# File Processing Pkgs
from PIL import Image 
import pandas as pd
# import docx2txt
# from PyPDF2 import PdfFileReader
# import pdfplumber

@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img 

# def read_pdf(file):
# 	pdfReader = PdfFileReader(file)
# 	count = pdfReader.numPages
# 	all_page_text = ""
# 	for i in range(count):
# 		page = pdfReader.getPage(i)
# 		all_page_text += page.extractText()
# 	return all_page_text

# def read_pdf2(file):
# 	with pdfplumber.open(file) as pdf:
# 	    page = pdf.pages[0]
# 	    return page.extract_text()

# import fitz  # this is pymupdf
# def read_pdf_fitz(file):
# 	with fitz.open(file) as doc:
# 		text = ""
# 		for page in doc:
# 			text += page.getText()
# 		return text 

# Fxn



def main():
    st.title("File Upload Tutorial")

    menu = ["Home", "Dataset", "DocumentFiles", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":   # this 'Home' is for uploading images
        st.subheader("Home")
        image_file = st.file_uploader("Upload Image",type=['png','jpeg','jpg'])
        if image_file is not None:

            # To See Details
            # st.write(type(image_file))
            # st.write(dir(image_file))
            file_details = {"Filename":image_file.name,"FileType":image_file.type,"FileSize":image_file.size}
            st.write(file_details)

            img = load_image(image_file)
            st.image(img, width=250)#,height=250)  # height is depricated I think!


    elif choice == "Dataset":    # this 'Dataset' is for uploading CSV files
        st.subheader("Dataset")
        data_file = st.file_uploader("Upload CSV", type=['csv'])
        if st.button("Process"):
            if data_file is not None:
                file_details = {"Filename":data_file.name,"FileType":data_file.type,"FileSize":data_file.size}
                st.write(file_details)

                df = pd.read_csv(data_file)
                st.dataframe(df)  # for displaying a csv file I guess

    elif choice == "DocumentFiles":        # this is for uploading docx, txt & pdf files
        st.subheader("DocumentFiles")
        docx_file = st.file_uploader("Upload File",type=['txt','docx','pdf'])
        if st.button("Process"):
            if docx_file is not None:
                file_details = {"Filename":docx_file.name,"FileType":docx_file.type,"FileSize":docx_file.size}
                st.write(file_details)
                # Check File Type
                if docx_file.type == "text/plain":
                    # raw_text = docx_file.read() # read as bytes
                    # st.write(raw_text)
                    # st.text(raw_text) # fails
                    st.text(str(docx_file.read(),"utf-8")) # empty
                    raw_text = str(docx_file.read(),"utf-8") # works with st.text and st.write,used for further processing
                    # st.text(raw_text) # Works
                    st.write(raw_text) # works
#                     elif docx_file.type == "application/pdf":
#                         # raw_text = read_pdf(docx_file)
#                         # st.write(raw_text)
#                         try:
#                             with pdfplumber.open(docx_file) as pdf:
#                                 page = pdf.pages[0]
#                                 st.write(page.extract_text())
#                         except:
#                             st.write("None")


#                     elif docx_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
#                     # Use the right file processor ( Docx,Docx2Text,etc)
#                         raw_text = docx2txt.process(docx_file) # Parse in the uploadFile Class 
#                         st.write(raw_text)

    else:
        st.subheader("About")
        st.info("Built with Streamlit")
        st.info("Jesus Saves @JCharisTech")
        st.text("Jesse E.Agbe(JCharis)")



if __name__ == '__main__':
    main()
