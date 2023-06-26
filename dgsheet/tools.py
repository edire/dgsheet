

import os
import gspread
import pandas as pd

filepath_cred = r"/home/ark/Dropbox/git/dbt_mm/bigquery-bbg-platform.json"


def read_gsheet(
        url,
        filepath_cred=os.getenv('filepath_gcred'),
        skiprows=0
):
    gc = gspread.service_account(filename=filepath_cred)
    wb = gc.open_by_url(url)
    sheet_id = url.split('gid=')[1]

    for ws in wb.worksheets():
        if f'id:{sheet_id}' in str(ws):
            df = pd.DataFrame(ws.get_all_records(expected_headers=[], head=skiprows))
            break
    
    return df