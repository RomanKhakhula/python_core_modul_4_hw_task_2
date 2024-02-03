from pathlib import Path

def get_cats_info(path):
    """Arg. -> path to file.txt, return -> list of dictionaries 'id', 'name', 'age'"""
    try:                                                                        #check path errors
        path = Path(path).absolute()
        if path.is_file:                                                        #check if path is file
            if path.suffix == ".txt":                                           #check if file is .txt
                try:                                                            #check file opening errors
                    with open(path, "r", encoding="utf-8") as fh:
                        list_of_dictionaries = []
                        for el in fh.readlines():
                            list_of_dictionaries.append({"id": el.split(",")[0], "name": el.split(",")[1], "age": int(el.split(",")[2])})
                        return list_of_dictionaries
                except Exception as e:
                    return print(e)
            else:
                return print(f"The '{path}' is not a '.txt' file")
        else:
            return print(f"The '{path}' is not a file")
    except Exception as e:
        return print(e)

get_cats_info("create_dict_from_txt.py")
get_cats_info("_initial.txt")
cats_info = get_cats_info("cats_initial.txt")
print(cats_info)
