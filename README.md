# jam-or-not

jam-or-not

The goal of this project is to leverage computer vision, specifically using the `supervision` and `inference` library, to detect various types of vehicles such as cars, motorcycles, buses, and trucks at a bridge or checkpoint.

This detection system will help in monitoring traffic congestion, estimating waiting times, and assessing the crowdedness of the area.

documentation: <>

api url: <http://localhost:8000>

web url: <http://localhost:8501>

## Requirement

- install python (v3.11)

## Testing and run

```zsh
// install dependencies
$ cd packages/api
$ pip install -r requirements.txt

// run in dev
$ cd packages/api
$ uvicorn main:app --host localhost --port 8000

// run in prod
$ cd packages/api
$ uvicorn main:app --host 0.0.0.0 --port 80
```

```zsh
// install dependencies
$ cd packages/web
$ pip install -r requirements.txt

// open jam_or_not web
$ streamlit run jam_or_not.py
```
