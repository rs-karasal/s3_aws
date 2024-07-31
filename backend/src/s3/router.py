import uuid

from fastapi import APIRouter

from backend.src.s3.aws_s3 import UploadClient
from backend.src.models import UploadPayload, UploadResponse, CompleteUploadPayload, CompleteUploadResponse

router = APIRouter(
    prefix="/s3",
    tags=["s3"],
    responses={404: {"description": "Not found"}},
)

client = UploadClient()


@router.post("/upload/")
async def upload_file(payload: UploadPayload) -> UploadResponse:

    key = f"{uuid.uuid4()}/{payload.file_name}"

    return client.get_presigned_multipart(
        key,
        payload.file_name,
        payload.content_type,
        payload.file_size,
    )


@router.post("/complete-upload/")
async def complete_upload(payload: CompleteUploadPayload) -> CompleteUploadResponse:
    
    result = client.complete_multipart_upload(
        payload.key,
        payload.upload_id,
        payload.etags,
    )

    return CompleteUploadResponse(url=result["Location"])