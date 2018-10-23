import fanhuima_analyse as fa
import java_excu as je


day_dict = fa.count_all_day_dict()
# print(list(map(int, day_dict.keys())))
#排序
tups = [(k, day_dict[k]) for k in sorted(day_dict.keys())]

#重新整理day_hours_datas[["0808"...][数据]]
day_hours = []
datas = []
for tup in tups:
    day = tup[0]
    hours = tup[1][0]
    for hour in hours:
        day_hours.append(day + hour)
    datas += tup[1][1]

charts = [(day_hours, datas)]


#起点和当前时间点每次+1
all_cu_datas = [[],[]]
# pre_hours = []
# cu_data_rows = []
def recu(start_index, end_index):
    if not end_index < len(day_hours) - 1:
        return
    cu_datas = []
    for i in range(start_index, end_index):
        cu_datas.append(datas[i])
    # day_hour = ""
    # if end_index < len(day_hours) - 1:
    #     day_hour = day_hours[end_index + 1]
    # else:
    #     day_hour = day_hours[end_index]
    #时间点是下一个,end_index循环是不包含本身的
    # all_cu_datas.append((day_hours[end_index], cu_datas))
    all_cu_datas[0].append(day_hours[end_index])
    all_cu_datas[1].append(cu_datas)
    start_index += 1
    end_index += 1
    recu(start_index, end_index)


# 移位整理
recu(0, 24)

#计算
results = je.excute(je.arma_mul_datas, all_cu_datas[1])

charts.append((all_cu_datas[0], results))
fa.show_charts(charts)