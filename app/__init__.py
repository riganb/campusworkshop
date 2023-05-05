"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaaai3hp8u791gt3tjg-a.oregon-postgres.render.com",
        database="betsol_todo_bnzc",
        user="betsol_todo_bnzc_user",
        password="nItsBMgxVWLfYiyeyIlCXJurecJHAbP6")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
