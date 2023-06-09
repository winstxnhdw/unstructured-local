from typing import BinaryIO, Optional

from pdfminer.pdfparser import PDFSyntaxError
from starlette.exceptions import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from unstructured.partition.auto import partition

from server.features.types import Strategy


def unstructured_partition(
    file: BinaryIO,
    file_name: Optional[str] = None,
    file_type: Optional[str] = 'Unknown',
    strategy: Optional[Strategy] = 'hi_res'
) -> str:
    """
    Summary
    -------
    this function uses the unstructured library to partition a file

    Parameters
    ----------
    file (BinaryIO): the file to partition
    file_name (Optional[str]): the name of the file
    file_type (Optional[str]): the type of the file
    strategy (Optional[Strategy]): the strategy to use

    Returns
    -------
    extracted_text (str): the extracted text
    """
    try:
        return '\n\n'.join(str(element) for element in partition(file=file, strategy=strategy))

    except PDFSyntaxError as exception:
        raise HTTPException(HTTP_422_UNPROCESSABLE_ENTITY, f'{file_name} is not a valid PDF file') from exception

    except ValueError as exception:
        if 'Invalid file' not in exception.args[0]:
            raise exception

        raise HTTPException(HTTP_422_UNPROCESSABLE_ENTITY, f'{file_type} is not currently supported') from exception
