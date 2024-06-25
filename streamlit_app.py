import streamlit as st
import pandas as pd
# import networkx as nx



st.title("🕸 Internal Link Evaluation App")

st.write(
    "This app helps to evaluate internal links on a website "
)

# Upload a CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])

# If a file is uploaded
if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    dataframe = pd.read_csv(uploaded_file)

    st.write("Uploaded file name:", uploaded_file.name)

df = dataframe

# clean dataframe
df['Source'] = df['Source'].astype('string')
df['Destination'] = df['Destination'].astype('string')
df['Anchor'] = df['Anchor'].astype('string')
df['Status Code'] = df['Status Code'].astype('string')
df['Follow'] = df['Follow'].astype('string')
df['Link Position'] = df['Link Position'].astype('string')

df = df[df['Type'] == 'Hyperlink']
df = df.filter(items = ['Source', 'Destination', 'Anchor', 'Status Code', 'Follow', 'Link Position'])
df['Anchor'].fillna('missing anchor', inplace=True)
df['Status Code'].fillna('none', inplace=True)

# Display the DataFrame
st.write(df)



st.write(
    "Here we are at the end of getting started with streamlit! Happy Streamlit-ing! :balloon:"
)

