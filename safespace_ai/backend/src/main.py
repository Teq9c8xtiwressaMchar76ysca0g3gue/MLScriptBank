from fastapi import FastAPI
app = FastAPI()
@app.post('/api/moderate/text')
async def moderate_text(content: str): pass
