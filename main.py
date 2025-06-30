import io
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from rembg import remove
from PIL import Image

app = FastAPI(
    title="API para Remover Fundo de Imagens",
    description="Uma API que utiliza a biblioteca rembg para remover o fundo de imagens enviadas via upload.",
    version="1.0.0",
)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:5500",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def process_image(image_bytes: bytes) -> bytes:
    """
    Recebe os bytes de uma imagem, remove o fundo e retorna os bytes da imagem processada.
    """
    try:
        output_bytes = remove(image_bytes)
        return output_bytes
    except Exception as e:
        print(f"Erro ao processar a imagem com rembg: {e}")
        raise HTTPException(status_code=500, detail="Erro interno ao processar a imagem.")

@app.post("/remove-background/",
          tags=["Image Processing"],
          summary="Remove o fundo de uma imagem",
          description="Envie uma imagem (JPG, PNG, etc.) e receba a imagem com fundo transparente em formato PNG.")
async def remove_background_endpoint(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="O arquivo enviado não é uma imagem.")

    image_bytes = await file.read()

    processed_image_bytes = process_image(image_bytes)

    return StreamingResponse(io.BytesIO(processed_image_bytes), media_type="image/png")

@app.get("/", tags=["Health Check"])
def health_check():
    return {"status": "ok", "message": "Bem-vindo à API de Remoção de Fundo!"}