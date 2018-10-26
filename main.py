import fanhuima_analyse as fa
import java_excu as je

day_dict = fa.count_all_day_dict()

# hour_dict = fa.count_hour_dict(day_dict#排序
# tups = [(k, day_dict[k]) for k in sorted(day_dict.keys())])
# # dict_08 = hour_dict["08"]
# hour_k = []
# inputs = []
# for k, v in hour_dict.items():
#     hour_k.append(k)
#     inputs.append(v)
#
# #arma计算
# count = je.excute(je.arma_days, inputs)
#
# day_dict["ALL"] = [hour_k, count]
# print("")
#排序
tups = [(k, day_dict[k]) for k in sorted(day_dict.keys())]
#重新整理day_hours_datas[["0808"...][数据]]

charts = []
for tup in tups:
    day_hours = []
    day = tup[0]
    hours = tup[1][0]
    datas = tup[1][1]
    # for hour in hours:
    #     day_hours.append(day + hour)
    charts.append((hours, datas, day))


# for chart in charts:
#     for index, x_name in enumerate(chart[0]):
#         aa = list(x_name)
#         aa.insert(2, "-")
#         aa += ":00"
#         chart[0][index] = "".join(aa)

del(charts[0])
del(charts[len(charts) - 1])

fa.show_charts(charts)
