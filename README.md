### To launch the Streamlit web page --- using the following app.py file - "jcharis___LazyP_CNN_FashionMNIST_worked___app.py" --- which is stored both on the laptop and github:

1) First **start the TFServing Docker Container on laptop** with the -v pointing to the "48_tf_serving" folder containing the saved FashionMNIST model **and launch TFServing from the bash terminal looking into the container** --- see Codebasics Tutorial 48 in 'Deployment_MAIN/codebasics' folder. This TFServing will now provide us with a RestAPI end-point.

2) **Launch the Streamlit web page** from the laptop by doing one of the following:
  - **using the app.py file stored on the laptop** --- open windows explorer, navigate to the "__Deploying_Models___MAIN/___Streamlit_and_mlflow/worked___JCharis___LazyP_CNN_FashionMNIST/
" folder and type cmd in the address bar - this will open a black cmd window in the above folder. Now type:

      streamlit run jcharis___LazyP_CNN_FashionMNIST_worked___app.py
 
      OR
      
  - **using the app.py file stored on github** --- just open a black cmd window on the laptop and type:
  
      streamlit run path-to-app.py-in-Github
