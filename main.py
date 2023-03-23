import os

def main():
    count_rows = {}
    txt_content = {}
    sorted_count_rows = []
    directory = 'files/'
    files = [file for file in os.listdir(directory) if os.path.isfile(f'{directory}/{file}')]
    for file in files:
        with open(f'{directory}/{file}', encoding='UTF=8') as txt:
            count_rows[file] = len(txt.readlines())
            txt.seek(0)
            txt_content[file] = txt.readlines()
    sorted_count_rows = sorted(count_rows,key=count_rows.get)
    
    for file in sorted_count_rows:
        with open('newfile.txt', 'a', encoding='UTF-8') as new_file:
            new_file.write(file + '\n')
            new_file.write(str(count_rows[file]) + '\n')
            new_file.write(''.join(txt_content[file]) + '\n')

main()