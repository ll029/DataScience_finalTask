from pyecharts.charts import Line,Page,Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType
import pandas as pd



def plot(data, x_name, y_name, name):
    x = list(data.index)
    y = list(data.columns)[:-1]

    c = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width="1200px"))  # 设置主题（color）
            .add_xaxis(xaxis_data=x)
            .set_global_opts(
            title_opts=opts.TitleOpts(title=name),
            xaxis_opts=opts.AxisOpts(type_="category", name=x_name, name_location='middle', name_gap=30,axislabel_opts={"interval": "0", "rotate": 30}),
            yaxis_opts=opts.AxisOpts(name=y_name, name_location='middle', name_gap=50),
            toolbox_opts=(opts.ToolBoxFeatureSaveAsImageOpts(background_color='white'),
                          opts.ToolboxOpts(is_show=True, pos_top='30',pos_right='30'),),
            #设置各标题位置及颜色
            legend_opts=opts.LegendOpts(is_show=True))
            .extend_axis(
            yaxis=opts.AxisOpts(
                name="总计",
                type_="value",)

            )#为折线图添加y轴
    )
    for i in y:
        c.add_yaxis(series_name=i, y_axis=list(data[i]), label_opts=opts.LabelOpts(is_show=False))
    c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))

    # l = (
    #     Line(init_opts=opts.InitOpts( width="1200px"))
    #         .add_xaxis(xaxis_data=x)
    #         .add_yaxis(series_name="总计",
    #                    yaxis_index=1,y_axis=list(data['总计']),
    #                    label_opts=opts.LabelOpts(is_show=True)
    #     )
    # )
    return c
page = Page()
city = pd.read_excel('mood.xlsx',index_col = '月份')
city = city.iloc[1:, :]
page.add(plot(city,"月份","心态","心态变化趋势"))
covid = [291, 76288, 81054, 82788, 82971, 83396]
x = list(city.index)
bar = (Line(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE, width="1200px"))
       .add_xaxis(x)
       .add_yaxis('人数（万人次）', covid)
       .set_global_opts(title_opts=opts.TitleOpts(title="累积确诊病例"),
                        xaxis_opts=opts.AxisOpts(axislabel_opts={"interval": "0"},name = '月份',name_location='middle', name_gap=30)
                        )
       .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                        markline_opts=opts.MarkLineOpts(
                        data=[
                        opts.MarkLineItem(type_="min", name="最小值"),
                        opts.MarkLineItem(type_="max", name="最大值"),
                        opts.MarkLineItem(type_="average", name="平均值"),
                        ]
                        ))
       )
page.add(bar)
page.render('心态分析.html')