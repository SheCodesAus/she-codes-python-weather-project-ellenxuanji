import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    date_obj = datetime.fromisoformat(iso_string)
    date_format = date_obj.strftime("%A %d %B %Y")
    return date_format
    pass


def convert_f_to_c(temp_in_farenheit):
    temp_in_f = float(temp_in_farenheit)
    temp_in_c = (temp_in_f - 32)/1.8
    return round(temp_in_c, 1)
    pass


def calculate_mean(weather_data):
    sum=0
    for i in weather_data:
        sum += float(i)
    return float(sum/len(weather_data))
    pass


def load_data_from_csv(csv_file):
    with open(csv_file, encoding='utf-8') as f:
        rd = csv.reader(f)
        f_list = list(rd)
        clean_list = [x for x in f_list if x]
        clean_list.pop(0)
        for i in clean_list:
            i[1] = int(i[1])
            i[2] = int(i[2])
    return clean_list
    pass


def find_min(weather_data):
    if len(weather_data)<= 0:
        return ()
    else:
        foalt_list = [float(i) for i in weather_data]
        min_num = min(foalt_list)
        a = [i for i,val in enumerate(foalt_list) if val==min_num] #find all of the index of the element
        min_index = a[-1] #only pick the last index 
    
        return (min_num, min_index)
    pass


def find_max(weather_data):
    if len(weather_data)<= 0:
        return ()
    else:
        foalt_list = [float(i) for i in weather_data]
        max_num = max(foalt_list)
        a = [i for i,val in enumerate(foalt_list) if val==max_num] #find all of the index of the element
        max_index = a[-1] #only pick the last index 
    
        return (max_num, max_index)
    pass


def generate_summary(weather_data):
    heading = f"{len(weather_data)} Day Overview\n"

    lowest_temp_list = [i[1] for i in weather_data]
    lowest_temp_f = find_min(lowest_temp_list)[0]
    lowest_temp_c = convert_f_to_c(lowest_temp_f)
    lowest_temp = format_temperature(lowest_temp_c)
    lowest_temp_date_index = find_min(lowest_temp_list)[1]
    lowest_temp_date = convert_date(weather_data[lowest_temp_date_index][0])
    lowest_temp_average = format_temperature(convert_f_to_c(calculate_mean(lowest_temp_list)))

    highest_temp_list = [i[2] for i in weather_data]
    highest_temp_f = find_max(highest_temp_list)[0]
    highest_temp_c = convert_f_to_c(highest_temp_f)
    highest_temp = format_temperature(highest_temp_c)
    highest_temp_date_index = find_max(highest_temp_list)[1]
    highest_temp_date = convert_date(weather_data[highest_temp_date_index][0])
    highest_temp_average = format_temperature(convert_f_to_c(calculate_mean(highest_temp_list)))

    summary =f"{heading}  The lowest temperature will be {lowest_temp}, and will occur on {lowest_temp_date}.\n  The highest temperature will be {highest_temp}, and will occur on {highest_temp_date}.\n  The average low this week is {lowest_temp_average}.\n  The average high this week is {highest_temp_average}.\n"
    
    return summary
    pass


def generate_daily_summary(weather_data):
    summary = ""
    for i in weather_data:
        min_temp = format_temperature(convert_f_to_c(i[1]))
        max_temp = format_temperature(convert_f_to_c(i[2]))
        date = convert_date(i[0])
        summary1 = f"---- {date} ----\n  Minimum Temperature: {min_temp}\n  Maximum Temperature: {max_temp}\n\n"
        summary += summary1
    return summary
    pass