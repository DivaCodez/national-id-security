from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

app = FastAPI(title="National ID Smart Security API")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[
        logging.FileHandler("security.log"),
        logging.StreamHandler()
    ]
)

class Card(BaseModel):
    id: str
    name: str 
    status: str
    face_id: str


cards_db = {
    "12345": Card(id="12345", name="Yacine", status="Active", face_id="face_yacine"),
    "67890": Card(id="67890", name="Sara", status="Active", face_id="face_sara")
}


class Card (BaseModel):
    id : int
    name : str 
    status : str
    face_id : int
    
    
# Schema for incoming reactivation requests
class ReactivateRequest(BaseModel):
    card_id: str
    photo_name: str
    selfie_features: str

@app.post("/lost/{card_id}")
def api_report_lost(card_id: str):
    """Endpoint for the citizen to report their card as lost instantly"""
    success = report_lost(card_id)
    if not success:
        raise HTTPException(status_code=404, detail="Card not found")
    return {"message": f"Card {card_id} deactivated successfully."}

@app.post("/scan")
def api_scan_card(card: Card):
    """Endpoint used by banks/police checkpoints to check card status"""
    result = scan_card(card)
    if result == "Fake Card":
        raise HTTPException(status_code=400, detail="Invalid card signature")
    elif result == "Blocked":
        raise HTTPException(status_code=403, detail="ACCESS DENIED: Card reported stolen/lost")
    
    return {"status": "Allowed", "message": f"Welcome back, {card.name}"}

@app.post("/reactivate")
def api_reactivate(req: ReactivateRequest):
    """Endpoint to securely reactivate the card using Face ID validation"""
    success = reactivate_card(req.card_id, req.photo_name, req.selfie_features)
    if not success:
        raise HTTPException(status_code=401, detail="Biometric verification failed or card invalid")
        
    return {"message": "Identity verified. Card has been reactivated successfully."}



