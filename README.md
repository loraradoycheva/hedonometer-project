# Seminars 3 & 4 — Hedonometer (Project Folder)

This folder provides an **example project structure** (and an instructor/demo script) for the Seminars 3 & 4 group project using the **labMT 1.0** dataset (Data Set S1 from the Hedonometer paper).

It includes:
- the labMT 1.0 dataset file (`data/raw/Data_Set_S1.txt`)
- a runnable demo analysis script (`src/hedonometer_labmt_demo.py`) that produces a *typical* set of outputs aligned to the assignment
- course documents in `docs/` (original paper + paper companion + assignment + project quickstart), provided as **.pdf**

## Folder layout (course convention)

- `src/` — Python scripts you run
- `data/raw/` — input data (treat as read-only)
- `figures/` — PNG plots (embed these in your GitHub README)
- `tables/` — CSV tables/summaries (optional to embed, but useful for analysis)
- `docs/` — assignment + paper companion + quickstart handout

## Setup + run (from the project root)

### 1) Create a virtual environment

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
```

**Windows (PowerShell)**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
```

### 2) Install dependencies
```bash
python3 -m pip install -r requirements.txt
```

### 3) Run the demo analysis
```bash
python3 src/run_analysis.py
```

### What gets generated?
After running, look in:
- `figures/` — PNG plots
- `tables/` — CSV summary tables

### 3.1) “exhibit” of words

####  Very positive
Words “laughter”, “happiness”, “love”, “happy”, “ laughed” are rated very positive. These words don’t have any ambiguity, therefor no conflict in meaning interpretation.

#### Very negative
Words “terrorist”, “suicide”, “rape”, “terrorism”, “murder” were rated as very negative. These words also have one meaning and the rating reflects that.

#### Highly contested
“Whiskey” can be associated with a positive connotation, such as a party or drinking with friends, but it can also be associated with alcoholism or health risks. A community that follows religious restrictions on alcohol can interpret this word negatively. Words “pussy”, “fucked” , ‘fucking”, “fuckin’ can be interpreted as slurs or words relating to intercourse, which can have both positive or negative interpretations, hence the conflicting ratings.

#### Weird / culturally loaded
These words are context sensitive and as they were rated as stand alone words, they may have been interpteted diffenenrly.
WID and NFl are acronims, so they can have multiple meanings.
“After-tax” and “overview” follow the same trend but are somewhat unexpected in this rating.
“After-tax” is likely rated as weird as it appears in economic or political context. Despite the term apprearing to be neutural, taxes are an emotionally and ideologically charged topics, so croedworkers can associate it with either positive or negative connotation. 
“Overview” is used in many fields, such as corporate or academic.The word also appers to be a neututal term but can be assosiated with a problem focused context.
