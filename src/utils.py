import logging
import os
from datetime import datetime

def setup_custom_logger(name):
    # Create logs directory
    if not os.path.exists('logs'):
        os.makedirs('logs')
        
    log_filename = f"logs/pipeline_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
    
    handler = logging.FileHandler(log_filename)
    handler.setFormatter(formatter)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    return logger