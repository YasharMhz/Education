#**** when we want to use .env we need to write source .venv/bin/activate in terminal


# What are Environment Variables?
# Environment variables are values stored outside your code.
# Example:
# Your code:
# DATABASE_URL
# The actual value lives somewhere else:
# DATABASE_URL=postgresql://localhost/mydb
# Your application reads it when starting.
#
# Why Do We Need Them?
# Imagine:
# Development
# DATABASE_URL=sqlite:///dev.db
# Production
# DATABASE_URL=postgresql://production-server/mydb
# You don't want to change your code every time.
#
# Install pydantic-settings
# Modern FastAPI uses:
# pip install pydantic-settings


# Create a .env File
# Project:
# app/
# │
# ├── main.py
# ├── config.py
# └── .env
#
# .env
# APP_NAME=My FastAPI App
# DEBUG=True
# DATABASE_URL=sqlite:///database.db
# SECRET_KEY=my-secret-key
# Create Settings Class
#
# config.py
# from pydantic_settings import BaseSettings
# class Settings(BaseSettings):
#     app_name: str
#     debug: bool
#     database_url: str
#     secret_key: str
#
#     class Config:
#         env_file = ".env"
#
# settings = Settings()

# Understanding This
# This:
# class Settings(BaseSettings):
# creates a configuration model.
# Similar to:
# class User(BaseModel):
# but instead of validating API input, it validates environment variables.
#
# This:
# env_file = ".env"
# tells Pydantic:
# "Read values from the .env file."
#
# Using Settings in FastAPI
# main.py
# from fastapi import FastAPI
# from config import settings
#
# app = FastAPI()
#
# @app.get("/")
# def home():
#     return {
#         "app": settings.app_name,
#         "debug": settings.debug
#     }
#
# Response:
#
# {
#     "app": "My FastAPI App",
#     "debug": true
# }

# Why Not Just Import Variables?
# Bad:
# DATABASE_URL = "something"
# SECRET_KEY = "secret"
# Because:
# Anyone who sees the code sees secrets.
# Changing environments is painful.
# Better:
# settings.database_url
# settings.secret_key
# Real Project Structure
#
# A professional structure:
# app/
# │
# ├── main.py
# │
# ├── core/
# │   └── config.py
# │
# ├── routers/
# │   ├── users.py
# │   └── auth.py
# │
# ├── database.py
# │
# └── .env
#
# Usually configuration lives in:
#
# core/config.py

# Environment Variables in Production
# You usually DON'T upload:
# .env
# to GitHub.
# Your .gitignore:
# .env

# Then your server provides variables:
# Linux example:
# export DATABASE_URL="postgresql://server/db"
#
# Docker:
# environment:
#   DATABASE_URL: postgres://server/db
#
# Cloud providers also have environment variable settings.
#
# Adding Defaults
# You can provide defaults:
# class Settings(BaseSettings):
#
#     app_name: str = "FastAPI App"
#     debug: bool = False
#
# Now if .env doesn't contain them:
# settings.app_name
# returns:
# FastAPI App

# Secret Example
# Authentication later will need:
# SECRET_KEY=random-long-string
# ALGORITHM=HS256
# ACCESS_TOKEN_EXPIRE_MINUTES=30
# Then:
# settings.secret_key
# settings.algorithm

# Cached Settings
# A good practice is loading settings once.
# Instead of:
# settings = Settings()
# use:
# from functools import lru_cache
#
# @lru_cache
# def get_settings():
#     return Settings()
#
# Then:
# settings = get_settings()
# Why?
# Without caching:
# Request 1 -> read .env
# Request 2 -> read .env
# Request 3 -> read .env
# With caching:
# Start app -> read .env once
#

# Using Settings with Depends
# FastAPI style:
# from fastapi import Depends
#
# @app.get("/")
# def home(settings=Depends(get_settings)):
#     return {
#         "name": settings.app_name
#     }
#
# Now configuration is injected like a dependency.

# Example: Database Configuration
# .env
#
# DATABASE_HOST=localhost
# DATABASE_PORT=5432
# DATABASE_USER=admin
# DATABASE_PASSWORD=password
# DATABASE_NAME=mydb
#
# Config:
# class Settings(BaseSettings):
#
#     database_host: str
#     database_port: int
#     database_user: str
#     database_password: str
#     database_name: str
#
#     class Config:
#         env_file=".env"
#
# Now your database code doesn't contain passwords.
#
# Common Mistakes
# ❌ Hardcoding secrets
# SECRET_KEY="123456"
# ❌ Uploading .env
# github
#  |
#  .env
# Never do this.
#
# ❌ Mixing configuration everywhere
# Bad:
# # users.py
# DATABASE_URL="..."
# Better:
# from core.config import settings

# Practice Exercise
# app/
# │
# ├── main.py
# ├── config.py
# └── .env
