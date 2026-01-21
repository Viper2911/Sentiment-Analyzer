from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from textblob import TextBlob
import logging
import time

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger("sentiment-api")

app = FastAPI(title="Sentiment Analysis API", version="1.0.0")

class TextInput(BaseModel):
    text: str

@app.get("/")
def home():
    return{"status":"healthy", "message":"Sentiment API is running"}

@app.post("/analyze")
def analyze_sentiment(input_data: TextInput):
    start_time=time.time()
    
    if not input_data.text.strip():
        logger.warning("Validation Error: User sent empty text.")
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    
    try:
        blob=TextBlob(input_data.text)
        polarity=blob.sentiment.polarity
        subjectivity=blob.sentiment.subjectivity
        if polarity>0.1:
            label="Positive"
        elif polarity<-0.1:
            label="Negative"
        else:
            label="Neutral"
        process_time=round((time.time()-start_time)*1000,2)
        logger.info(f"Success | Label: {label} | Time: {process_time}ms")
        
        return{
            "text_preview": input_data.text[:50],
            "polarity": round(polarity,2),
            "subjectivity": round(subjectivity,2),
            "label": label,
            "meta": {
                "processing_time in ms": process_time
            }
        }
    except Exception as e:
        logger.error(f"Internal Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal processing error")