import os

bind = "0.0.0.0:" + str(os.environ.get("PORT", 5000))
workers = os.environ.get("GWORKERS", 2)