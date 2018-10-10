import os

path = "data/fanhuima/"
files = os.listdir(path)

#创建字典
all_logs = {}
for file in files:
    print("file:" + file)
    if os.path.isdir(file):
        continue

    f_obj = open(path + file, encoding="UTF-8")
    log = {}
    for line in f_obj.readlines():
        process_code = line.split("|")[0]
        v = log.get(process_code)
        if v:
            log[process_code] = v + 1
        else:
            log[process_code] = 1
    all_logs[file] = log

print(all_logs)
        

