import os
from datetime import datetime


def save_json(json_data,numero_processo :str,dir = os.getcwd()):
    current_date_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    try:
        with open(dir +"/"+ numero_processo+"_data_"+current_date_time+".json", "w",encoding='utf-8') as file:
            file.write(json_data)
        print("JSON saved successfully!")
    except Exception as e:
        print(f"Error saving JSON: {e}")