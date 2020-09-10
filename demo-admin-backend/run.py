import os
from app import flask_app

import settings

if __name__ == '__main__':
    logger = flask_app.logger
    logger.info("===============================")
    logger.info("= DEMO ADMIN SERVER SETTINGS  =")
    logger.info("===============================")
    logger.info(f"API_SERVER_HOST:   {settings.API_SERVER_HOST}")
    logger.info(f"API_SERVER_PORT:   {settings.API_SERVER_PORT}")
    logger.info(f"API_SERVER_DEBUG:  {settings.API_SERVER_DEBUG}")
    logger.info(f"DB_NAME:           {settings.DB_NAME}")
    logger.info(f"DB_HOST:           {settings.DB_HOST}")
    logger.info(f"DB_PORT:           {settings.DB_PORT}")
    logger.info("===============================")
    logger.info("===============================")


    flask_app.run(
        debug=settings.API_SERVER_DEBUG,
        host=settings.API_SERVER_HOST,
        port=settings.API_SERVER_PORT,
        use_reloader=False)
