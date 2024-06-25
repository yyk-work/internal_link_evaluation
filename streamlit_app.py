import streamlit as st
import pandas as pd
# import networkx as nx



st.title("🕸 Internal Link Evaluation App")

st.write(
    "This app helps to evaluate internal links on a website "
)

# Upload a CSV file containing edges (assuming 'Source' and 'Destination' columns)
uploaded_file = st.file_uploader("Upload a CSV file with 'Source' and 'Destination' columns", type=['csv'])

# If a file is uploaded
if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    edges_df = pd.read_csv(uploaded_file)

    # Create a directed graph (DiGraph)
    G = nx.DiGraph()

    # Add edges from the DataFrame
    edges = [(row['Source'], row['Destination']) for _, row in edges_df.iterrows()]
    G.add_edges_from(edges)

    # Calculate PageRank
    pagerank = nx.pagerank(G)

    # Display PageRank scores
    st.write("PageRank scores:")
    for node, score in pagerank.items():
        st.write(f"{node}: {score:.4f}")



st.write(
    "Here we are at the end of getting started with streamlit! Happy Streamlit-ing! :balloon:"
)

