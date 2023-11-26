def get_from_file():
    with open("file/data.txt", "r") as file:
        return file.readlines()


def avg_int():
    temperatures = get_from_file()
    temperatures_cleaned = [float(item) for item in temperatures[1:]]
    return sum(temperatures_cleaned) / len(temperatures_cleaned)


print(f"Average temperature is : {avg_int()}")

