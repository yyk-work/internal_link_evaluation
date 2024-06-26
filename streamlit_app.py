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
    # Read the CSV file into a DataFrame
    edges_df = pd.read_csv(uploaded_file)

    # Create a directed graph (DiGraph)
    G = nx.DiGraph()

    # Add edges from the DataFrame
    edges = [(row['Source'], row['Destination']) for _, row in edges_df.iterrows()]
    G.add_edges_from(edges)

    # Calculate PageRank
    pagerank = nx.pagerank(G)

    # Create a CSV file for download
    # Create a CSV file for download
    csv_file_path = "pagerank_scores.csv"
    with open(csv_file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Node", "Score"])  # Write header
        writer.writerows(pagerank.items())  # Write data rows

    # Provide a download link
    st.download_button("Download CSV", csv_file_path, file_name="pagerank_scores.csv", key="download_button")



st.write(
    "Here we are at the end of getting started with streamlit! Happy Streamlit-ing! :balloon:"
)

