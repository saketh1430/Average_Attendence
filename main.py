
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import webbrowser

st.markdown("""            
            <style>
            .css-1rs6os.edgvbvh3
            {
                visibility: hidden;
            }
            .css-1lsmgbg.egzxvld0
            {
                visibility: hidden;
            }
            </style>
            
            """,unsafe_allow_html=True)
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Welcome","Average","Attendence","Mid Payments","About Developer"],
        icons=["house","book","at","bi-credit-card-2-back"],
        menu_icon="cast",
        default_index=0,
    )

if selected=="Welcome":
    
   
        
    st.header("Welcome To Our Website")
    st.markdown("Here You Will Do Your Mid Marks Calculation📅 In an Easy and Efficent Manner")
    st.snow()
    st.markdown("""
                <!DOCTYPE html>
<html>
<head>
<title>AI Average</title>
</head>
<body>

<h1>Click On Average On The Left Side TO Start</h1>


</body>
</html
                """,unsafe_allow_html=True)

if selected=="Average":
    
    st.subheader('Note ⚠️:')
    st.subheader("Step 1: Make the Excel file in Below Format")
    st.image('1.png')
    st.subheader("Step 2: Click on Browse File(i.e. CSV)")
    st.image('2.png')
    st.subheader("Step 3: Select the desired file and that's it")
    st.subheader("Step 4: Then Click On Download CSV Your file will be downloaded")
    st.image('3.png')
    
    q = st.file_uploader("Upload CSV",type=["csv"])
    if q is not None:
        f = pd.read_csv(q)
        f=pd.DataFrame(f)
        st.dataframe(f)
        Average=[]
        for i in range(len(f)):
            arr=np.empty(3)
            arr = np.array(f.iloc[i][2:4])
            arr.sort()
            avg = (arr[-1]+arr[-2])/2
            Average.append(avg)
        f['Average']=Average
        st.markdown("<h1>Average of Mid Marks</h1>",unsafe_allow_html=True)
        st.dataframe(f)
        @st.cache
        def convert_df(f):

            return f.to_csv().encode('utf-8')

        csv = convert_df(f)

        st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='Average.csv',
        mime='text/csv',
        )
if selected=="Attendence":
        
        s = st.file_uploader("Upload Csv",type=["txt","csv"])
        if s is not None:
            df = pd.read_csv(s)
            df=pd.DataFrame(df)
            st.dataframe(df)
            total = st.number_input("Enter Total Number Of Classes",value=0)
        gettotal = st.button("Get Total")
        if gettotal:
            Total=[]
            Percentage=[]
            perc=0
            sum=0
            for i in range(len(df)):
                arr=np.empty(10)
                arr = np.array(df.iloc[i][3:13])
                sum = (arr[0]+arr[1]+arr[2]+arr[3]+arr[4]+arr[5]+arr[6]+arr[7]+arr[8]+arr[9])   #+arr[0]+arr[1]+arr[2]+arr[3]+arr[4]+arr[5]+arr[6]+arr[7]+arr[8]+arr[9]   
                Total.append(sum)
            df['Total']=Total
            for i in range(len(Total)):
                perc=(Total[i]*100)/total
                Percentage.append(perc)
            df['Percentage']=Percentage
        
            st.markdown("<h1>Average of Mid Marks</h1>",unsafe_allow_html=True)
            st.dataframe(df,width=10000)
            @st.cache
            def convert_df(df):

                return df.to_csv().encode('utf-8')

            csv = convert_df(df)

            st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='Attendence.csv',
            mime='text/csv',
            )  

    
if selected=="Mid Payments": 
    

    form = st.form("Form3")
  
    url = 'https://payu.in/business/buttons'

    if st.button('DashBoard for Transactions Details'):
        webbrowser.open_new_tab(url)
if selected=="About Developer":
    st.subheader("Ruthvik => kattaruthvik7@gmail.com")
    st.subheader("Yashwanth => pulimiyashwanth123@gmail.com")
    st.subheader("Saketh => saketh9533886088@gmail.com")
        
   
