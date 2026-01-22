from fastapi import APIRouter

# Create a router instance
router = APIRouter(
    prefix="/teacher",
    tags=["teacher"],
    responses={404: {"description": "Not found"}},
)

@router.get("/dashboard")
async def read_admin_dashboard():
    return {"username": "admin", "access": "full"}