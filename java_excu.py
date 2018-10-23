from jpype import *

# jvm_path = jpype.getDefaultJVMPath()
jar_path = "E:/Develop/python/matplotlib_test/jar/";
# jar_name = "ARIMA.jar"
jar_name = "ARMA-Java--master.jar"
jvm = "D:/Program Files/Java/jre1.8.0_191/bin/client/jvm.dll"

global Excutor
global ArrayList


def excute(func, *input):
    global Excutor
    global ArrayList
    startJVM(jvm, "-ea", "-Djava.class.path=" + jar_path + jar_name)
    # jpype.java.lang.System.out.println("Hello World")
    try:
        # 生成class
        # Mytest = JClass("arima.Mytest")
        Excutor = JClass("arima.Excutor");
        ArrayList = JClass("java.util.ArrayList");

        result = func(*input)
        return result
    finally:
        # 关闭jvm
        shutdownJVM()


#days[日期][小时]
def arma_days(days):

    # 使用class
    # mytest = Mytest()
    # mytest.sayHello()

    rsls = []
    for datarow in days:
        arrayList = ArrayList()
        for data in datarow:
            arrayList.add(data)

        excutor = Excutor()
        rsl = excutor.excu(arrayList)
        rsls.append(rsl)

    return rsls


#datas[]
def arma(datas):
    arrayList = ArrayList()
    for data in datas:
        arrayList.add(data)

    excutor = Excutor()
    rsl = excutor.excu(arrayList)
    return rsl


#datas[][]
def arma_mul_datas(datas):
    rsls = []
    for row in datas:
        rsls.append(arma(row))

    return rsls