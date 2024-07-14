from fastapi import APIRouter

router = APIRouter()


@router.get("/health-check", tags=['general'])
def health_check():
    return {"status": "good"}


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
