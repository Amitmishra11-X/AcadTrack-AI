from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from database.db_connect import get_collection

app = FastAPI(title="AcadTrack AI API")

# ✅ Enable frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Fix MongoDB ObjectId
def fix_id(doc):
    doc = dict(doc)
    doc["_id"] = str(doc["_id"])
    return doc


# 🔹 Home route
@app.get("/")
def home():
    return {"message": "AcadTrack AI API running 🚀"}


# 🔹 Get jobs (filter + sorting)
@app.get("/jobs")
def get_jobs(
    category: str = None,
    institute: str = None,
    limit: int = Query(50, le=100)
):
    collection = get_collection("jobs")

    query = {}

    if category:
        query["category"] = category
    if institute:
        query["institute"] = institute

    jobs = list(
        collection.find(query)
        .sort("scraped_at", -1)   # latest first
        .limit(limit)
    )

    return [fix_id(j) for j in jobs]


# 🔹 Search endpoint
@app.get("/search")
def search_jobs(keyword: str):
    collection = get_collection("jobs")

    jobs = list(
        collection.find({
            "title": {"$regex": keyword, "$options": "i"}
        }).limit(50)
    )

    return [fix_id(j) for j in jobs]


# 🔹 Get categories
@app.get("/categories")
def get_categories():
    collection = get_collection("jobs")
    return collection.distinct("category")


# 🔹 Get institutes
@app.get("/institutes")
def get_institutes():
    collection = get_collection("jobs")
    return collection.distinct("institute")

@app.get("/favicon.ico")
def favicon():
    return {}