import datetime

def format_year(dates):
    year = dates.astype('datetime64[Y]').astype(int) + 1970
    return year