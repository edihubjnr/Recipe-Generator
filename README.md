# 🍳 Recipe Generator

A full-stack web app that generates food recipes from [a dish name / a list of ingredients / user preferences], with clear ingredients and step-by-step instructions. The front end is built with HTML, CSS, and JavaScript, and the backend is written in Python.

## Overview

Deciding what to cook can be harder than cooking itself. Recipe Generator lets users [enter what they want to make or what they have on hand] and get a ready-to-follow recipe in seconds. I built it to practise [full-stack development, building a Python backend, connecting a front end to an API, handling user input, etc.].

## Features

- [Enter a dish name or ingredients to generate a recipe]
- [Recipe displayed with an ingredients list and numbered steps]
- [Python backend that handles requests and returns recipe data as JSON]
- [Loading and error messages when a recipe can't be generated]
- [Responsive layout that works on desktop and mobile]

## Tech Stack

| Area | Tools |
| --- | --- |
| Frontend | HTML5, [CSS3], [JavaScript] |
| Backend | Python, [Flask / FastAPI / Django] |
| Data / API | [Openai API] |
| Hosting | [Netlify] |

## Getting Started

### Prerequisites

- Python 3.[x] or higher
- pip
- [An API key from openai]

### Installation

```bash
# Clone the repository
git clone https://github.com/edihubjnr/Recipe-Generator.git
cd Recipe-Generator

# (Recommended) create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

[create a `.env` file in the project root and add:]

```
[API_KEY_NAME]=your_key_here
```

Never commit your `.env` file or API keys to GitHub.

### Run the app

```bash
python [app.py]
```

Then open [http://localhost:5000] in your browser.

## Usage

1. Open the app in your browser.
2. [Type a dish or list ingredients in the input field.]
3. [Click the generate button.]
4. View the recipe and follow the steps.

## Project Structure

```
Recipe-Generator/
├── [app.py]            # Python backend entry point
├── requirements.txt    # Python dependencies
├── [templates/]        # HTML pages
├── [static/]           # CSS, JavaScript, images
└── README.md
```

## How It Works

[Two or three sentences on the flow: the user submits input in the browser, the front end sends it to the Python backend, the backend [calls an API / processes the data], and the recipe is returned and rendered on the page.]

## Roadmap

- [ ] [Save favourite recipes]
- [ ] [Dietary filters (vegetarian, gluten-free, etc.)]
- [ ] [Add recipe images to generate preparation procedure]
- [ ] [Add AI to generate video of the procedure to prepare the recipe]

## Author

**Edwin Ashley**, Software Engineering student at GCTU
GitHub: [@edihubjnr](https://github.com/edihubjnr) · LinkedIn link: https://www.linkedin.com/in/edwin-ashley-653b17265
