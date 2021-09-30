# stortings-generator
Dashboard made with [Dash](https://plotly.com/dash/) for generating random election in Norway 2021 elections. Authors are Team Visju, composed of Aksel, Céline and Christopher.

## Run without building with Docker
Create (or not) a virtual environment or conda environment that contains the libraries defined in `requirements.txt`

Then run 
```
python -m stortings-generator
```
to launch the Flask server and type `http://localhost:8080` to launch the dashboard


## Build and run with Docker
```
docker build -t stortings-generator . && docker run --env-file .env -p 0.0.0.0:5000:8080/tcp stortings-generator
```

You access the dashboard through your browser by typing `http://localhost:5000/` in the address bar of the browser