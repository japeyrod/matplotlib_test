import fanhuima_analyse as fa
import java_excu as je

day_dict = fa.count_day_dict(8, 14)

hour_dict = fa.count_hour_dict(day_dict)
# dict_08 = hour_dict["08"]
hour_k = []
inputs = []
for k, v in hour_dict.items():
    hour_k.append(k)
    inputs.append(v)

#arma计算
count = je.excute(je.arma_days, inputs)

day_dict["ALL"] = [hour_k, count]
print("")

fa.show_day_dict_chart(day_dict)
