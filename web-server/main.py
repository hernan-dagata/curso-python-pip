import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/api/v1/list')
def get_list():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]

@app.get('/api/v1/contact')
def get_list():
    return {"name": "Platzi"}

@app.get('/api/v1/html', response_class=HTMLResponse)
def get_list():
    return """
        <h1> Hola soy una pagina desde python </h1>
        <p> y tengo un parrafo. </p>
    """

def run():
    store.get_categories()
    
if __name__ == '__main__':
    run()