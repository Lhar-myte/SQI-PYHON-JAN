def read_data(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        data = []
        for line in lines:
            name, age = line.split(",")
            data.append((name, int(age)))
    return data
