from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
import pandas as pd

# Step 1: Load CSV Data
def load_csv(file_path):
    """Load CSV into a DataFrame and create Documents for embedding."""
    df = pd.read_csv(file_path)
    #df = df.iloc[:10000]
    documents = []
    for _, row in df.iterrows():
        content = (
    f"Track ID: {row['track_id']}, Artists: {row['artists']}, "
    f"Album Name: {row['album_name']}, Track Name: {row['track_name']}, "
    f"Popularity: {row['popularity']}, Duration (ms): {row['duration_ms']}, "
    f"Explicit: {row['explicit']}, Danceability: {row['danceability']}, "
    f"Energy: {row['energy']}, Key: {row['key']}, Loudness: {row['loudness']}, "
    f"Mode: {row['mode']}, Speechiness: {row['speechiness']}, "
    f"Acousticness: {row['acousticness']}, Instrumentalness: {row['instrumentalness']}, "
    f"Liveness: {row['liveness']}, Valence: {row['valence']}, "
    f"Tempo: {row['tempo']}, Time Signature: {row['time_signature']}, "
    f"Track Genre: {row['track_genre']}"
                                                )
        metadata = {
    "track_id": row['track_id'],
    "artists": row['artists'],
    "album_name": row['album_name'],
    "track_name": row['track_name'],
    "popularity": row['popularity'],
    "duration_ms": row['duration_ms'],
    "explicit": row['explicit'],
    "danceability": row['danceability'],
    "energy": row['energy'],
    "key": row['key'],
    "loudness": row['loudness'],
    "mode": row['mode'],
    "speechiness": row['speechiness'],
    "acousticness": row['acousticness'],
    "instrumentalness": row['instrumentalness'],
    "liveness": row['liveness'],
    "valence": row['valence'],
    "tempo": row['tempo'],
    "time_signature": row['time_signature'],
    "track_genre": row['track_genre'],
}
        documents.append(Document(page_content=content, metadata=metadata))
    return documents

# Step 2: Initialize ChromaDB and Add Data
def create_vector_db(documents, persist_directory="./chroma_db"):
    """Embed documents and store in ChromaDB."""
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")  # SentenceTransformers model
    vector_db = Chroma.from_documents(documents, embeddings, persist_directory=persist_directory)
    #vector_db.persist('./vector_database')
    return vector_db

def load_vector_db(save_path):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")  # SentenceTransformers model
    vectordb = Chroma(persist_directory=save_path, embedding_function=embeddings)
    return vectordb

# Step 3: Query Vector Database
def query_vector_db(vector_db, query, top_k=5):
    """Query the vector database."""
    results = vector_db.similarity_search(query, k=top_k)
    return results

# Main Workflow
if __name__ == "__main__":
    csv_file = "/home/drdo/multi_agentic_rag/dataset.csv"  # Path to your CSV file
    docs = load_csv(csv_file)

    # Create and persist Chroma vector database
    # chroma_db = create_vector_db(docs)
    save_path = '/home/drdo/multi_agentic_rag/chroma_db'
    chroma_db = load_vector_db(save_path)

    # Example Query
    query = "Suggest a pop song with a medium tempo and uplifting mood."
    results = query_vector_db(chroma_db, query)

    # Print Results
    print("Query Results:")
    for result in results:
        print(result.page_content)
