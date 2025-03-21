def serialize_to_json(data):
    string=json.dumps(data, ensure_ascii=False, indent=2)
    return string

'''obj={"name": "Alice", "age": 25, "is_student": False}
serialize_to_json(obj)'''
if __name__ == "__main__": 
    import base64 
    import json
    print(serialize_to_json(eval(input())))