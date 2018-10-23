import os
import matplotlib.pyplot as plt
import numpy as np

interface_name = "odchkorderinfo"
path = "data/fanhuima/"
files = os.listdir(path)

global year
global month

# 天 - [[小时][调用次数]]
def count_all_day_dict():
    global year
    global month
    # 创建字典
    all_logs = {}
    for file in files:
        # print("file:" + file)
        if os.path.isdir(file):
            continue

        f_obj = open(path + file, encoding="UTF-8")
        log = {}
        for line in f_obj.readlines():
            line_split = line.split("|")
            process_code = line_split[0]
            v = log.get(process_code)
            if v:
                log[process_code] = int(v) + int(line_split[3])
            else:
                log[process_code] = int(line_split[3])
        all_logs[file.replace("fanhuima", "")] = log

    # print(all_logs)
    day_dict = {}
    for k, v in all_logs.items():
        split = k.split("-")
        year = split[0]
        month = split[1]
        day = split[2]
        hour = split[3]
        hour_list = day_dict.get(day)
        if not hour_list:
            keys = []
            values = []
            hour_list = [keys, values]
            day_dict[day] = hour_list

        count = v.get(interface_name)
        if not count:
            count = 0
        hour_list[0].append(hour)
        hour_list[1].append(count)

    return day_dict


# 天 - [[小时][调用次数]]
def count_day_dict(hour1, hour2):
    all_day_dict = count_all_day_dict()
    for key, days in all_day_dict.items():
        hours = days[0]
        datas = days[1]
        new_hours = []
        new_datas = []
        for i in range(0, len(hours)):
            if int(hours[i]) >= hour1 and int(hours[i]) <= hour2:
                new_hours.append(hours[i])
                new_datas.append(datas[i])

        all_day_dict[key] = [new_hours, new_datas]
    return all_day_dict


def init_chart(axis):
    global year
    global month
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.title(interface_name + "接口调用情况")
    plt.xlabel(year + "-" + month)
    plt.ylabel("调用次数")
    plt.axis(axis)
    # plt.grid(True)


#chart_data_tups是元组列表[([x数据],[y数据]),{}]
def show_charts(chart_data_tups):
    for chart_data_tup in chart_data_tups:
        x_names = chart_data_tup[0]
        y_values = chart_data_tup[1]
        np_max = np.max(y_values)
        init_chart([0, len(y_values), 0, np_max * 1.5])
        if len(x_names) != 0:
            plt.plot(x_names, y_values)
        else:
            plt.plot(y_values)
        # plt.legend(loc='upper right')
    plt.show()


def show_day_dict_chart(day_dict):
    init_chart([0, 6, 0, 10000])

    for day_k, day_v in day_dict.items():
        hour_k = day_v[0]
        count = day_v[1]

        plt.plot(hour_k, count, label=day_k)

        # 每条线条相关
        # 标签，颜色，形状
        # param = []
        # if len(day_v) > 2:
        #     param = day_v[2]
        #     lab = param[0]
        #     col = param[1]
        #     type = param[2]
        #     #plt.plot(x, y, linewidth = '1', label = "test", color=' coral ', linestyle=':', marker='|')
        #     plt.plot(label = day_k, color = col)
        # else:
        #     plt.plot(label=day_k)

    plt.legend(loc='upper right')
    plt.show()


#将每天的同一时刻调用次数归组，得到时刻为key，数组为value的字典
def count_hour_dict(day_dict):
    hour_dic = {}
    for day_k, day_v in day_dict.items():
        #     continue
        hour_k = day_v[0]
        count = day_v[1]

        # 按小时统计
        for i in range(0, len(hour_k)):
            key = hour_k[i]
            hour_counts = hour_dic.get(key)
            if not hour_counts:
                hour_counts = []
                hour_dic[key] = hour_counts
            hour_counts.append(count[i])

    return hour_dic


