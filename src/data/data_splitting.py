

def data_spliting(data):
    weather_input1=data.drop('power_normed',axis=1)
    weather_input=weather_input1.drop('time_idx',axis=1)
    solpow=data['power_normed']
    return weather_input,solpow