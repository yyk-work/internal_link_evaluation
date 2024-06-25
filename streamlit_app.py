import streamlit as st
import pandas as pd


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

# classify rows
def classify_links(source, destination, anchor, similarity, similiarity_cleaned):
    match (source, destination, anchor, similarity, similiarity_cleaned):
        #case _ if len(anchor) <= 5:
            #return 'Short Anchor'
        case _ if 'encoded' in destination:
            return 'Encoded Link'
        case _ if 'encoded' in source:
            return 'Encoded Link'
        case _ if 'v_' in destination:
            return 'Filter Link'
        case _ if 'google' in destination:
            return 'Google Link'
        case _ if 'pdf' in destination:
            return 'PDF Link'
        case _ if 'media' in destination:
            return 'Media Link'
        case _ if similiarity_cleaned < 20:
            return 'No Match'
        case _ if similarity > 98:
            return 'Complete Match'
        case _ if 20 <= similiarity_cleaned < 60:
            return 'Bad Match'
        case _ if similiarity_cleaned >= 60:
            return 'Good Match'
        case _ if source == destination:
            return 'Anchor Link'
        case _:
            return 'Other'

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

