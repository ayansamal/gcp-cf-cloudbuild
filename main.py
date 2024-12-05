import os
from datetime import datetime
import mysql.connector

def return_basic(request):
  now = datetime.now()
  return '<h1>Welcome to Cloud Functions and Cloud Build demo by Simform</h1><br/>' + str(now)
