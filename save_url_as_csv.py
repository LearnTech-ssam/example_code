from datetime import date
import pandas as pd


def save_url_as_csv(url_dtype, url, filename):
    if url_dtype=='json':
        data = pd.read_json(url)
    elif url_dtype=='csv':
        data = pd.read_csv(url)
    else:
        raise Exception("url_dtype: json or csv")

    today_as_str = str(date.today())
    data['Indicator Information Downloaded Date'] = today_as_str
    csvname = today_as_str + '_' + filename + '.csv'
    data.to_csv(csvname, index = False)
    print(csvname + ' successfully saved')


url = 'https://fingertips.phe.org.uk/api/area_types'
filename = 'areatypeid_ref'
save_url_as_csv('json', url, filename)
