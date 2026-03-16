import os
import json
from datetime import datetime
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Storage setup
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = "support-logs"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)

# Auto-create container if it doesn't exist
try:
    container_client.create_container()
except Exception:
    pass

# --- Step 1: Simulate a form submission ---
email = "testuser@example.com"
query = "How do I reset my password?"
ai_response = "You can reset your password by following these steps: ..."

data = {
    "email": email,
    "query": query,
    "ai_response": ai_response,
    "timestamp": str(datetime.utcnow())
}

blob_name = f"log-{datetime.utcnow().timestamp()}.json"

# Upload the blob
container_client.upload_blob(blob_name, json.dumps(data), overwrite=True)
print(f"✅ Submitted test query and uploaded blob: {blob_name}\n")

# --- Step 2: List all blobs in the container ---
print("=== Stored Blobs ===")
blobs = container_client.list_blobs()
for blob in blobs:
    print(f"- {blob.name}")

# --- Step 3: Download and print content of all blobs ---
print("\n=== Blob Contents ===")
for blob in blobs:
    content = container_client.download_blob(blob).readall()
    print(f"--- {blob.name} ---")
    print(json.dumps(json.loads(content), indent=2))
    print()