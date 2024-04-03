from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/Home")    
def  Homepage():
    return "Where we begin our digital quest,"


@app.get("/about")    
def  about():
    return "Discover who we are, at our best."


@app.get("/contact us")    
def  contactus():
    return "Get in touch with ease, don't stress,"


@app.get("/biography")    
def  biography():
    return "My story, from the start I did try,Creating my first API, reaching for the sky."
