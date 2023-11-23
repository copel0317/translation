from fastapi import FastAPI, HTTPException
from translators import google, mozilla, papago
import uvicorn

app = FastAPI()

@app.get('/test')
def return_hello():
    return {"message": "hello"}

@app.post('/translation')
def translate(text: str, translation_service : str):

    if translation_service.lower() == "google" :
        translated_text = google.translate(text)
    elif translation_service.lower() == "mozilla" :
        translated_text = mozilla.translate(text)  
    elif translation_service.lower() == "papago" :
        translated_text = papago.translate(text)
    else:
        raise HTTPException(
            status_code= 400, 
            detail = f"'translation_service'(query parameter) must be one of 'google', 'papago', mozilla', input 'translation_service' : {translation_service}"
        )
        
    if translated_text =
    
    return {
        "original_text" : text, 
        "translated_text" : translated_text,
        "translation_service" : translation_service.lower()
    }

if __name__ == '__main__':
    uvicorn.run(app, host='172.16.162.72', port=8895) 
