import uvicorn
from app.db.models import create_tables
from app.main import app

if __name__ == "__main__":
    create_tables()

    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
