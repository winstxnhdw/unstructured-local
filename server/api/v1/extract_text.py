from fastapi import UploadFile
from unstructured.partition.auto import partition

from server.api.v1 import v1


@v1.post('/extract_text')
async def extract_text(request: UploadFile) -> str:
    """
    Summary
    -------
    the `/extract_text` route is similar to the `/extract` route but it is faster at the cost of only extracting text
    """
    return "\n\n".join(str(element) for element in partition(file=request.file, strategy='fast'))
