from fastapi import UploadFile

from server.api.v1 import v1
from server.features.partition import unstructured_partition


@v1.post('/extract_text', response_model=str)
async def extract_text(request: UploadFile):
    """
    Summary
    -------
    the `/extract_text` route is similar to the `/extract` route but faster at the cost of only extracting text
    """
    return unstructured_partition(request.file, request.filename, request.content_type, 'fast')
