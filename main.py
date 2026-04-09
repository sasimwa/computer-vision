import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

print("Connected to Supabase!")

data = {
    "moisture": 30,
    "temperature": 22,
    "status": "Dry"
}

supabase.table("Plants").insert(data).execute()

print("Data inserted!")
