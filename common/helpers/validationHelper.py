

def validateStructure(data_dict, structure):
    for field in structure:
        if ( not hasattr(data_dict, field)):
            return False
    return True
