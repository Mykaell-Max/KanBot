from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGO = os.getenv('MONGO')

client = MongoClient(MONGO)
database = client['kanban']
tasks = database['tasks']
