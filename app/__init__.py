"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaagsbhp8u791gu7540-a.oregon-postgres.render.com",
        database="todo_pyu1",
        user="todo_pyu1_user",
        password="KZKCWwiIgBPHSGRPlvZ1g7AXJzgbRuGq")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
