import pandas as pd
import requests
import os


def get_data(year):
    if not os.path.exists('../session_cookie.txt'):
        return read_tables(year)

    json_data = get_json(year)
    return get_table(json_data, year)


def read_tables(year):
    df_path, acc_times_path = get_paths(year)

    df = pd.read_csv(df_path)
    for col in df.columns:
        if col[-1]=='1':
            df[col] = pd.to_datetime(df[col])
        if col[-1]=='2' or col=='accumulated_time':
            df[col] = pd.to_timedelta(df[col])
    
    acc_times = pd.read_csv(acc_times_path)
    for col in acc_times.columns[1:]:
        acc_times[col] = pd.to_timedelta(acc_times[col])
    
    return df, acc_times


def write_tables(df, acc_times, year):
    df_path, acc_times_path = get_paths(year)
    df.to_csv(df_path, index=False)
    acc_times.to_csv(acc_times_path, index=False)


def get_paths(year):
    return f'data/df{year}.csv', f'data/acc_times{year}.csv'


def get_json(year):
    request = requests.get(get_url(year), cookies=get_cookies())
    return request.json()


def get_url(year):
    user_id = {2021: 1075819, 2020: 1066392}
    return f'https://adventofcode.com/{year}/leaderboard/private/view/{user_id[year]}.json'


def get_cookies():
    with open('../session_cookie.txt', 'r') as f:
        return {'session': f.read()}


def get_table(data, year):
    df = pd.json_normalize(data['members'].values())
    df = df[['name', 'local_score', 'stars'] + list(sorted(df.columns[6:], key=lambda x: float(x[21:-12])))]
    df.columns = ['name', 'score' ,'stars'] + [col[21:-12] for col in df.columns[3:]]

    local_time = + 1 # CEST

    acc_times = pd.DataFrame(data=df['name'])
    df['accumulated_time'] = pd.Timedelta(0)
    for i in range(3, df.shape[1]-1):
        df[df.columns[i]] = pd.to_datetime(df[df.columns[i]], unit='s') + pd.Timedelta(local_time, unit='H')
        if i%2 == 0:
            df[df.columns[i]] -= df[df.columns[i-1]]
            df['accumulated_time'] += df[df.columns[i]]
            
            day = df.columns[i].split('.')[0]
            prev_day = str(int(day)-1)
            acc_times[day] = df[df.columns[i]] if prev_day not in acc_times else acc_times[prev_day] + df[df.columns[i]]

    df = df.sort_values(['stars', 'score'], ascending=False)
    df.index = range(1, df.shape[0]+1)

    write_tables(df, acc_times, year)

    return df, acc_times


def style_table(df):
    return df[df.stars>0].style.format(style_data)


def style_data(x):
    if isinstance(x, pd.Timestamp):
        return x.strftime('%H:%M:%S')
    if isinstance(x, pd.Timedelta):
        if x > pd.Timedelta(1, 'H'):
            return str(x)[-8:]
        else:
            return str(x)[-5:]
    return x
