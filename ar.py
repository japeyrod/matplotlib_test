import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
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

charts = [(day_hours, datas, "True data")]

# sp=np.array([333.53,334.3,340.98,343.55,338.55,343.51,347.64,352.15,354.87,348,353.54,356.71,357.55,360.5,356.52,349.52,337.72,338.61,338.37,344.8,351.12,347.68,348.4,355.92,357.75,351.31,352.25,350.6,344.9,345])
sp = charts[0][1]
N=5
n=np.ones(N)
weights=n/N
sma=np.convolve(weights,sp)[N-1:-N+1]
t=np.arange(N-1,len(sp))

# plot(t,sp[N-1:],lw=1)
# plot(t,sma,lw=2)
# show()
new_chars = [(day_hours[N-1:], datas[N-1:], "True data")]
new_chars.append((day_hours[N-1:], sma, "Prediction data"))

for chart in new_chars:
    for index, x_name in enumerate(chart[0]):
        aa = list(x_name)
        aa.insert(2, "-")
        aa += ":00"
        chart[0][index] = "".join(aa)

fa.show_charts(new_chars)
