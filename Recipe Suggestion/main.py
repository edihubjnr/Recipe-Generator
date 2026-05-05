from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import httpx
from jinja2 import Template

app = FastAPI()

# Allow requests from the frontend (adjust in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve the static single-page app
app.mount("/static", StaticFiles(directory="static"), name="static")

THEMEAL_BASE = "https://www.themealdb.com/api/json/v1/1"


@app.get("/", response_class=HTMLResponse)
async def index():
    try:
        with open("static/index.html", "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        raise HTTPException(status_code=500, detail="Could not load frontend")


@app.get("/api/search")
async def search(ingredient: str = Query(..., min_length=1)):
    url = f"{THEMEAL_BASE}/filter.php"
    params = {"i": ingredient}
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params, timeout=10.0)
        resp.raise_for_status()
        data = resp.json()
    # The API returns {'meals': [...]} or {'meals': None}
    meals = data.get("meals") or []
    return {"meals": meals}


@app.get("/api/random")
async def random_recipe():
    url = f"{THEMEAL_BASE}/random.php"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, timeout=10.0)
        resp.raise_for_status()
        data = resp.json()
    meals = data.get("meals") or []
    return {"meals": meals}


@app.get("/api/lookup")
async def lookup(id: str = Query(...)):
    url = f"{THEMEAL_BASE}/lookup.php"
    params = {"i": id}
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params, timeout=10.0)
        resp.raise_for_status()
        data = resp.json()
    meals = data.get("meals") or []
    if not meals:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return meals[0]


@app.get("/recipe/{meal_id}", response_class=HTMLResponse)
async def recipe_page(meal_id: str):
    # Fetch meal details and render a simple instructions page
    url = f"{THEMEAL_BASE}/lookup.php"
    params = {"i": meal_id}
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params, timeout=10.0)
        resp.raise_for_status()
        data = resp.json()
    meals = data.get("meals") or []
    if not meals:
        raise HTTPException(status_code=404, detail="Recipe not found")
    meal = meals[0]
    tpl = Template("""
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      <title>{{ meal.strMeal }}</title>
      <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-50 p-6">
      <div class="max-w-3xl mx-auto bg-white shadow rounded p-6">
        <h1 class="text-2xl font-bold mb-2">{{ meal.strMeal }}</h1>
        {% if meal.strMealThumb %}
        <img src="{{ meal.strMealThumb }}" alt="{{ meal.strMeal }}" class="w-full rounded mb-4" />
        {% endif %}
        <p class="whitespace-pre-line">{{ meal.strInstructions }}</p>
        {% if meal.strSource %}
        <p class="mt-4">Source: <a class="text-blue-600 underline" href="{{ meal.strSource }}" target="_blank">{{ meal.strSource }}</a></p>
        {% endif %}
        <div class="mt-6">
          <a class="inline-block bg-indigo-600 text-white px-4 py-2 rounded" href="/" >Back</a>
        </div>
      </div>
    </body>
    </html>
    """)
    return tpl.render(meal=meal)
