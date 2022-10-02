# This file is based on --- "jcharis___app_____basic_file_upload___images_csv_txt___worked.py"

import numpy as np
import json
import requests
import streamlit as st
import streamlit.components.v1 as stc

# File Processing Pkgs
from PIL import Image 
import pandas as pd
# import docx2txt
# from PyPDF2 import PdfFileReader
# import pdfplumber

labels = '''T-shirt/top
Trouser
Pullover
Dress
Coat
Sandal
Shirt
Sneaker
Bag
Ankle boot'''.split("\n")

# not using this load_image() function!
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
    st.title("Classifying FashionMNIST data")

    menu = ["Home", "Dataset", "DocumentFiles", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":       # Note --- 'Home' is for images
        st.subheader("Home")

        # Upload image on Streamlit web site:
        image_file = st.file_uploader("Upload Image", type=['png','jpeg','jpg'])      # this image_file is ready to go into PIL.Image.open() !
        
        if image_file is not None:
            file_details = {"Filename":image_file.name, "FileType":image_file.type, "FileSize":image_file.size}
            st.write(file_details)

            # Import image into a PIL object
            img = Image.open(image_file)         # this is a (28, 28) image
           
            # Convert PIL object to np array, then pre-process the image ie. expand_dims + normalize
            arr = np.expand_dims(np.expand_dims(np.array(img), -1), 0)/255     # final shape is (1, 28, 28, 1) in this case, with values btwn 0 and 1

            DEPLOYED_ENDPOINT = "http://localhost:8601/v1/models/FashionMNIST_model:predict"  # this is the RestAPI end-point created by TF Serving

            # use json.dumps() to convert dictionary to json string
            data = json.dumps({"signature_name": "serving_default", 
                               "instances": arr.tolist()})
            headers = {"content-type": "application/json"}     # works even without headers --- need to verify!

            r = requests.post(url = DEPLOYED_ENDPOINT, data=data, headers=headers)
            # r above is just the status. 200 is success! 400 is error!

            pred = r.json()       # r.json() returns a regular dictionary
            st.write(f"Model prediction (r.json() ie. softmax output) ---> {pred}")
            pred_idx = np.argmax(pred['predictions'][0])       # use axis=1 if uploading multiple files - need to verify!
            pred_label = labels[pred_idx]

            #print(r)
            #print(type(pred['predictions'][0][0]) == np.float)
            #print(pred)
            #print(pred_idx)
            #print(pred_label)  # need to display this in Streamlit

            # To display the predicted label:
            #st.text(f"Predicted label: {pred_label}")
            st.write(f"Predicted label ---> {pred_label}")  # I don't see any diff btwn st.text() & st.write() --- need to verify!

            # To display the original image (looks like height argument is depricated):
            st.image(img, width=250)#,height=250)  

#---------------- That's it for this lesson on classifying FashionMNIST data ------------------

    elif choice == "Dataset":    # this 'Dataset' is for uploading CSV files - see JCharis's video
        st.subheader("Dataset")
        data_file = st.file_uploader("Upload CSV", type=['csv'])
        if st.button("Process"):
            if data_file is not None:
                file_details = {"Filename":data_file.name,"FileType":data_file.type,"FileSize":data_file.size}
                st.write(file_details)

                df = pd.read_csv(data_file)
                st.dataframe(df)  # for displaying a csv file I guess

    elif choice == "DocumentFiles":     # this 'DocumentFiles' is for uploading txt, docx & pdf files 
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
