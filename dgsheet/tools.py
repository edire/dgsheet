
import os
import gspread
import pandas as pd


def read_gsheet(
        url,
        filepath_cred=os.getenv('GSHEET_CRED'),
        skiprows=0,
        usecols=None,
        nrows=0
):
    gc = gspread.service_account(filename=filepath_cred)
    wb = gc.open_by_url(url)
    sheet_id = url.split('gid=')[1]

    for ws in wb.worksheets():
        if f'id:{sheet_id}' in str(ws):
            if usecols != None:
                clmn_1, clmn_2 = usecols.split(':')
                if nrows > 0:
                    rw_2 = skiprows + 1 + nrows
                else:
                    rw_2 = ''
                rng = f'{clmn_1}{skiprows+1}:{clmn_2}{rw_2}'
                df = pd.DataFrame(ws.get(rng))
                df.columns = df.iloc[0]
                df = df.drop(0, axis=0)
                df = df.reset_index(drop=True)
            else:
                df = pd.DataFrame(ws.get_all_records(expected_headers=[], head=skiprows + 1))
                if nrows > 0:
                    df = df.iloc[:nrows]
            break
    
    return df