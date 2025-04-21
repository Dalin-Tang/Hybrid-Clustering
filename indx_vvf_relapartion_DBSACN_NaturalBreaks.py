import numpy as np
import pandas as pd
import openpyxl
import jenkspy #导入jenkspy工具包
from sklearn.cluster import DBSCAN #导入DBSCAN聚类工具包
from pandas import ExcelWriter
from scipy import stats
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

def DB_NB(rawfile,c_number):
    '''
    DBSCAN_Natural-Breaks融合聚类函数
    :param rawfile: 原始城市道路数据文件，例如“CSDATA.csv”
    :param savefile: 输出文件的保存路径
    :param c_number: 聚类数
    :param roadlevel:聚类的道路等级
    :return: 返回输出值
    :vsave,gsave,vsta,gsta:速度和临界速度的数据输出文件路径和统计结果路径
    '''
    # 导入数据
    names = ['seg_id', 'speed']
    df1 = pd.read_csv(rawfile, names=names)
    # 数据预处理
    frame = df1.dropna()  # 删除行中空值
    frame = frame[frame['speed'] != 0]# 删除行中0值
    grouped = frame['speed'].groupby(frame['seg_id'])  # 以道路名称对路段数据集分组
    pieces = dict(list(grouped))  # 将速度转化成道路名和日期的字典
    seg = np.unique(list(frame['seg_id'])).tolist() # 将道路名转换为列表,且去除重复
    # 建立一些空变量
    b = []  # 建立空列表
    news = {}  # 建立一个空字典
    news = pd.DataFrame(news)  # 创建一个空dataframe
    n = int(c_number)-2  # 自然简短点法聚类数
    # 遍历数据进行聚类
    for segid in seg[:]:
        data1 = list(pieces[segid])  # 提取字典的每一个道路的速度数据，并转化为列表
        if len(data1) > 1000:
            data1.sort()  # 对数据进行从小到大排序
            d = list(range(5000))
            d.remove(0)
            d = dict(zip(data1, d))  # 创建一个1-5000的列表对列表data1的速度进行编号
            # （3.1）DBSCAN聚类
            s = np.array(data1).reshape(1, -1).T  # 将列表转换为1×n的矩阵以进行聚类
            dbscan = DBSCAN(eps=0.9, min_samples=3)  # 输入DBSCAN聚类的参数
            dbscan.fit(np.nan_to_num(s))  # 对于数据进行DBSCAN聚类
            label_pred = dbscan.labels_  # 将每一类别使用标签进行划分

            if len(s[label_pred == 0]) == 0:
                x0 = s[label_pred == min(label_pred)]
                breaks = sum(np.array([min(x0), max(x0)]).tolist(), [])

            elif max(label_pred) == 0:
                x0 = s[label_pred == 0]
                breaks = sum(np.array([min(x0), max(x0)]).tolist(), [])
            # 如果DBSCAN仅将速度数据划分为一类，则选择该类别的端点值作为拥堵和自由流的临界速度

            else:
                x0 = s[label_pred == 0]
                # print(len(x0))
                # x0 = s[label_pred == min(label_pred)]
                xmax = s[label_pred == max(label_pred)]
                breaks = sum(np.array([min(x0), max(xmax)]).tolist(), [])
            # 如果聚类多个类别，则使用第一个类的最小值作为拥挤临界速度，最后一类的最大值为自由流速度
            # breaks聚类出v1和vf
            ffs = max(breaks)
            breakd = []
            breaked = []
            rela_v = []
            for i in breaks:
                breakd.append(d[i])
                breaked.append(d[i])

            for i in breaks:
                breakd.append(i)
            # 将速度分位值与临界速度放入列表breakd

            # 开始进行自然间断点法聚类

            data2 = data1[int(min(breaked) - 1):int(max(breaked))] # 确定了v1 vf
            #data2 = data1[:int(max(breaked))]
            for i in data2:
                rv = i / ffs
                rela_v.append(rv)
            if len(rela_v) > 500 and len(np.unique(rela_v))>n:
                breaks2 = list(jenkspy.jenks_breaks(rela_v, n_classes=n))
            # 如果列表的个数大于5个 则进行聚类
            else:
                print('未完成自然间断点聚类路段id：')
                print(segid)
                #for i in data1[:int(n + 1)]:
                    #breaks2.append(i / ffs)

            # 没有5个不进行聚类，直接放入breaks

            # for i in breaks2:
            # breakd.append(d[i])
            for i in breaks2:
                breakd.append(i)
            b.append(breaks2)
            # 将速度临界速度放入列表b
        else:
            print(segid)

    a = list(range(1, 1001))
    c = dict(zip(a, b))
    #相对速度值
    new = pd.DataFrame(c)
    #计算相对速度的斜率截距
    slopes=[]
    intercepts=[]
    r_values = []
    p_values=[]
    std_errs = []

    xt=[]
    yt=[]
    vlist = new.values.tolist()
    rows_list = []
    for row in vlist:
        rows_list.append(row)
    for i in range(0,n-1):
        x=rows_list[i]
        j=i+1
        y=rows_list[j]
        for xi in x:
            xt.append(xi)
        for yi in y:
            yt.append(yi)

        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        slopes.append(slope)
        intercepts.append(intercept)
        r_values.append(r_value)
        p_values.append(p_value)
        std_errs.append(std_err)
    slope_t, intercept_t, r_value_t, p_value_t, std_err_t = stats.linregress(xt, yt)

    slopes.append(slope_t)
    intercepts.append(intercept_t)
    r_values.append(r_value_t)
    p_values.append(p_value_t)
    std_errs.append(std_err_t)

    liner_para = pd.DataFrame({'斜率': slopes,
                               '截距': intercepts,
                               '线性回归的相关系数R': r_values,
                               '假设检验的p值':p_values,
                               '回归系数的标准误差std_err': std_errs})


    #计算统计指标


    new_mean = new.mean(axis=1)
    new_sdv = new.std(axis=1)
    new_byxs = new_sdv / new_mean
    new_total = pd.DataFrame({'均值': new_mean,
                          '标准差': new_sdv,
                          '变异系数': new_byxs})

    # 得出聚类结果
    #数据结果
    print('相对速度')
    print(new.T)
    print(new.T.columns)


    #统计结果

    print('相对速度统计结果')
    print(new_total.T)
    #拟合参数
    print('相对速度拟合参数')
    print(liner_para.T)

    #保存结果
    # 将转置后的结果输出到excel表格
    return new.T,new_total.T,liner_para.T
    '''
        with ExcelWriter(savepath) as writer:
        new.T.to_excel(writer,sheet_name='临界速度')
        new_total.T.to_excel(writer,sheet_name='临界速度统计指标')
        gv_pd.T.to_excel(writer,sheet_name='相对临界速度')
        gv_total.T.to_excel(writer,sheet_name='相对临界速度统计指标')
        writer.save()
    '''





