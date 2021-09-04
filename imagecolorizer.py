import streamlit as st
import pandas as pd
import os




def upload_xlsx(zxc):
    try:
        if zxc:
            df=pd.read_excel(zxc)
            st.dataframe(df)
            df.to_csv(path,index=False)
            return df
    except Exception as e:
        st.write("Oops!",e.__class__,"occurred.")
        return df

def xlsx_to_csv():
    st.sidebar.header("Convert xlsx file to csv file")
    abc=st.sidebar.button("Upload the file")
    if abc:
        st.sidebar.file_uploader("Choose a file")
        df=upload_xlsx(abc)
        st.dataframe(df)
        df.to_csv ("Converted.csv", index = None,header=True)    
        df = pd.DataFrame(pd.read_csv("Converted.csv"))
    return df


#File Upload                
def file_upload():
    st.sidebar.header("Data Import")
    lmn=st.sidebar.radio('Choose a file')
    if lmn:
        st.sidebar.file_uploader("Choose a file",type='xlsx')
        st.sidebar.button('Upload File')
        df=upload_xlsx(lmn)
        return df
     

def main():
    file_upload()
    xlsx_to_csv()


main()


temp='\\temp.csv'
path=os.getcwd()
path=path+temp
st.title("Demo Application")
