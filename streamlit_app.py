import streamlit as st
import pandas as pd
import networkx as nx
import csv



st.title("🕸 Internal Link Evaluation App")

st.write(
    "This app helps to evaluate internal links on a website "
)

# Upload a CSV file containing edges (assuming 'Source' and 'Destination' columns)
uploaded_file = st.file_uploader("Upload a CSV file with 'Source' and 'Destination' columns", type=['csv'])

# If a file is uploaded
if uploaded_file is not None:
    edges_df = pd.read_csv(uploaded_file)
    G = nx.DiGraph()
    edges = [(row['Source'], row['Destination']) for _, row in edges_df.iterrows()]
    G.add_edges_from(edges)
    pagerank = nx.pagerank(G)

    # Create a DataFrame from the pagerank dictionary
    pagerank_df = pd.DataFrame(pagerank.items(), columns=['Node', 'Score'])

    #pagerank_df['Normalized Score']=(pagerank_df['Score']-pagerank_df['Score'].mean())/pagerank_df['Score'].std()
    pagerank_df['Normalized Score']=(pagerank_df['Score']-pagerank_df['Score'].min())/(pagerank_df['Score'].max()-pagerank_df['Score'].min())*100

    # Display the DataFrame
    st.write("PageRank scores:")
    st.write(pagerank_df)



st.write("More options for analysis will be added in the future.")

