def get_sorted_keys_values(file_path):
    with open(file_path,'rb') as f:
        dic=pickle.load(f)
    a=sorted(dic.keys())
    b=[dic[key] for key in a]
    return [a,b]

if __name__ == "__main__": 
    import base64 
    import pickle 
    print(get_sorted_keys_values('input.pkl'))