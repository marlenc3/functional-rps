from fastapi import APIRouter

router = APIRouter()


@router.get("/health-check", tags=["general"])
def health_check():
    return {"status": "good"}
