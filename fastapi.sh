#!/usr/bin/bash
 
echo [FastAPI]::Server started

uvicorn main:app --reload
