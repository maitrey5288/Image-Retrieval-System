import json
JSON_FILE_PATH = 'data/data.json'
def jsonread():
    with open(JSON_FILE_PATH, "r") as json_file:
        data = json.load(json_file)
    return data

def jsonsave(file_name,text):
    temp_dict = jsonread()
    print("hi tempdict")
    print(temp_dict)
    temp_dict[file_name] = text
    print(temp_dict)
    with open(JSON_FILE_PATH, "w") as json_file:
        json.dump(temp_dict, json_file)


def jsonsavepdf(file_name,data):
    temp_dict = jsonread()
    temp_dict['pdf'][file_name] = data
    with open(JSON_FILE_PATH, "w") as json_file:
        json.dump(temp_dict, json_file)

def jsonclear():
    a={"pdf" :{}}
    with open(JSON_FILE_PATH, "w") as json_file:
        json.dump(a, json_file)
    

    
