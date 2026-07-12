#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import secrets
import sqlite3
import getpass
from pathlib import Path
from hashlib import sha256

BASE_DIR = Path(__file__).resolve().parent

CONFIG_DIR = BASE_DIR / "config"
CONFIG_FILE = CONFIG_DIR / "settings.json"

DATABASE_FILE = BASE_DIR / "database.db"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def line():
    print("=" * 60)


def ask(message, default=None, password=False):
    while True:
        if default:
            text = f"{message} [{default}]: "
        else:
            text = f"{message}: "

        if password:
            value = getpass.getpass(text)
        else:
            value = input(text)

        value = value.strip()

        if value:
            return value

        if default is not None:
            return default

        print("این مقدار نمی‌تواند خالی باشد.\n")


def create_directories():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)


def hash_password(password):
    return sha256(password.encode()).hexdigest()


def create_database():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admins(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER UNIQUE,
        username TEXT UNIQUE,
        password TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
   
