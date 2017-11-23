import os
from app import app
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

#----------------------------------------
# launch
#----------------------------------------

if __name__ == "__main__":
	port = int(os.environ.get("MAESTRO_PORT", 5000))
	app.run(host='0.0.0.0', port=port)