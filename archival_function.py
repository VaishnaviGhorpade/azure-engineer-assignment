import azure.cosmos.cosmos_client as cosmos_client
from azure.storage.blob import BlobServiceClient
import json

COSMOS_URL = "<YOUR_COSMOS_DB_URL>"
COSMOS_KEY = "<YOUR_COSMOS_DB_KEY>"
STORAGE_CONNECTION_STRING = "<YOUR_STORAGE_CONNECTION_STRING>"

# Cosmos DB client
client = cosmos_client.CosmosClient(COSMOS_URL, {'masterKey': COSMOS_KEY})
database = client.get_database_client('BillingDB')
container = database.get_container_client('BillingRecords')

# Blob Storage client
blob_service_client = BlobServiceClient.from_connection_string(STORAGE_CONNECTION_STRING)
blob_container_client = blob_service_client.get_container_client('archived-billing')

# Query for old records
query = "SELECT * FROM c WHERE c.createdDate < '<date-90-days-ago>'"
for item in container.query_items(query=query, enable_cross_partition_query=True):
    blob_name = f"{item['id']}.json"
    blob_container_client.upload_blob(blob_name, json.dumps(item))
    container.delete_item(item['id'], partition_key=item['partitionKey'])

print("Archival complete.")
