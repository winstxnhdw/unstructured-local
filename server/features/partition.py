from typing import BinaryIO, Literal, Optional, Union

from pdfminer.pdfparser import PDFSyntaxError
from starlette.exceptions import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from unstructured.partition.auto import partition


def unstructured_partition(
    file: BinaryIO,
    file_name: Optional[str] = None,
    file_type: Optional[str] = 'Unknown',
    strategy: Optional[Union[Literal['hi_res'], Literal['fast']]] = 'hi_res'
) -> str:
    """
    Summary
    -------
    this function uses the unstructured library to partition a file
    """
    try:
        return '\n\n'.join(str(element) for element in partition(file=file, strategy=strategy))

    except PDFSyntaxError as exception:
        raise HTTPException(HTTP_422_UNPROCESSABLE_ENTITY, f'{file_name} is not a valid PDF file') from exception

    except ValueError as exception:
        if 'Invalid file' not in exception.args[0]:
            raise exception

        raise HTTPException(HTTP_422_UNPROCESSABLE_ENTITY, f'{file_type} is not currently supported') from exception
