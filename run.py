#!/usr/bin/env python3
"""
Production startup script for Legal Document Processing System
"""
import os
import uvicorn

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=False,
        workers=1,
        log_level="info",
    )
