

def validateStructure(data_dict, structure):
    for field in structure:
        if ( not field in data_dict.keys() ):
            return False
    return True
