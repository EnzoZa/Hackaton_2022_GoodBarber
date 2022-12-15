from fastapi import APIRouter, status

# router
router: APIRouter = APIRouter(prefix="")

@router.get("/", status_code=status.HTTP_200_OK)
def hello_world():
    return {"hello", "world"}
