from pathlib import Path
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
BASE = Path(__file__).resolve().parents[2]
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE/'data'/'business.db'}")
engine = create_engine(DATABASE_URL, future=True)
