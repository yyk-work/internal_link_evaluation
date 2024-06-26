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

    # Display the DataFrame
    st.write("PageRank scores:")
    st.write(pagerank_df)

    # Create csv
    csv_file_path = "pagerank_scores.csv"
    pagerank_df.to_csv(csv_file_path)

    # Provide a download link
    st.download_button("Download CSV", csv_file_path, file_name="pagerank_scores.csv", key="download_button")



st.write(
    "Here we are at the end of getting started with streamlit! Happy Streamlit-ing! :balloon:"
)

