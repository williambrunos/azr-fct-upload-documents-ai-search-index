import azure.functions as func
import logging
import json
import os
from core.upload_documents import upload_document

app = func.FunctionApp()

@app.blob_trigger(arg_name="blob", 
                  path="central/teste/{name}.json",
                  connection="azrloadocumentsintoindex_STORAGE") 
def ingestion(blob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {blob.name}"
                f"Blob Size: {blob.length} bytes")
    
    # Blob content as a python dict
    blob_content = json.loads(blob.read().decode('utf-8'))
    logging.info(f"Blob content: {blob_content}.\nType in the code: {type(blob_content)}")
    
    upload_document(blob_content)
    
    logging.info("\n\nSucesso!!!\n\n")