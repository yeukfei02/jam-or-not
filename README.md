# jam-or-not

jam-or-not

This project aims to detect object like car, motorcycle, bus, truck near the bridge/checkpoint with computer vision lib `supervision`, so we can know the waiting time and crowded situation.

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
