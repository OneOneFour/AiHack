import pandas as pd
from sqlalchemy.types import DateTime, Integer, String
from . import engine
from glob import glob
import os


def write_new_data_to_db(csv_file_name,table_name):
    df = pd.read_csv(csv_file_name)
    df.to_sql()

def load_by_shortcode(datadir, prefix="04"):
    paths = glob(f"{datadir}/{prefix}**.csv")
    for file in paths:
        write_new_data_to_db(file)
