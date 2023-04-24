from fastapi import UploadFile
from unstructured.partition.auto import partition

from server.api.v1 import v1


@v1.post('/extract')
async def extract(request: UploadFile) -> str:
    """
    Summary
    -------
    the `/extract` route consumes a file and returns a string of extracted elements
    """
    return "\n\n".join(str(element) for element in partition(file=request.file))
