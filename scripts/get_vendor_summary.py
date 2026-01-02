import sqlite3
import pandas as pd
import logging
logging.basicConfig(
    filename="logs/get_vendor_summary.log", 
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s", 
    filemode="a"  
)

c