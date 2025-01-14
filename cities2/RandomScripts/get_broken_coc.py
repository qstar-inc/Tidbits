import os

output_file = "broken_coc.txt"
user_home = os.path.expanduser("~")
folder = os.path.join(user_home, 'AppData', 'LocalLow', 'Colossal Order', 'Cities Skylines II')

def check_coc():
    with open(output_file, 'w') as output:
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith('.coc'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        first_line = lines[0].strip() if len(lines) > 0 else None
                        second_line = lines[1].strip() if len(lines) > 1 else None
                        last_line = lines[-1].strip() if len(lines) > 0 else None
                        print(f"file: {file_path}")
                        print(f"1st: {first_line}")
                        print(f"2nd: {second_line}")
                        print(f"3rd: {last_line}")
                        print("-----------------------------")
                        if first_line == None and second_line == None and last_line == None:
                            output.write(f"{file_path} looks empty\n")
                        elif first_line == None or second_line != "{" or last_line != "}":
                            output.write(f"{file_path} doesn't look right\n")

check_coc()
