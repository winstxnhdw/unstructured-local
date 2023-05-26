from fastapi import UploadFile

from server.api.v1 import v1
from server.features.partition import unstructured_partition


@v1.post('/extract', response_model=str)
async def extract(request: UploadFile):
    """
    Summary
    -------
    the `/extract` route consumes a file and returns a string of extracted elements
    """
    return unstructured_partition(request.file, request.filename, request.content_type)
