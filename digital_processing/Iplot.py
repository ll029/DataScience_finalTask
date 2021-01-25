import pyecharts.options as opts
from pyecharts.charts import Radar,Page

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.baidu.com/examples/editor.html?c=radar

目前无法实现的功能:

1、雷达图周围的图例的 textStyle 暂时无法设置背景颜色
"""
from pyecharts.charts import Bar,Line
from pyecharts import options as opts
from pyecharts.globals import ThemeType
import pandas as pd

#
# def stackPlot(data, x_name, y_name, name):
#     x = list(data.index)
#     y = list(data.columns)[:-1]
#     c = (
#         Bar(init_opts=opts.InitOpts(theme=ThemeType.theme, width="1200px"))  # 设置主题（color）
#             .add_xaxis(xaxis_data=x)
#             .set_global_opts(
#             title_opts=opts.TitleOpts(title=name),
#             xaxis_opts=opts.AxisOpts(type_="category", name=x_name, name_location='middle', name_gap=30,axislabel_opts={"interval": "0", "rotate": 30}),
#             yaxis_opts=opts.AxisOpts(name=y_name, name_location='middle', name_gap=50),
#             toolbox_opts=(opts.ToolBoxFeatureSaveAsImageOpts(background_color='white'),
#                           opts.ToolboxOpts(is_show=True, pos_top='30',pos_right='30'),),
#             #设置各标题位置及颜色
#             legend_opts=opts.LegendOpts(is_show=True))
#             .extend_axis(
#             yaxis=opts.AxisOpts(
#                 name="总计",
#                 type_="value",)
#
#             )#为折线图添加y轴
#     )
#     for i in y:
#         c.add_yaxis(series_name=i, yaxis_data=list(data[i]), stack='stack1', label_opts=opts.LabelOpts(is_show=False))
#     c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#
#     l = (
#         Line(init_opts=opts.InitOpts( width="1200px"))
#             .add_xaxis(xaxis_data=x)
#             .add_yaxis(series_name="总计",
#                        yaxis_index=1,y_axis=list(data['总计']),
#                        label_opts=opts.LabelOpts(is_show=True)
#         )
#     )
#     c.overlap(l).render(name+".html")
# stackPlot([],'城市', "数量", "城市景区等级数量")





def radar_plot(v1,v2,v3,i):
    m = max([max(v1[0]),max(v2[0]),max(v3[0])])
    c = (Radar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT,width="640px", height="360px",bg_color="#CCCCCC"))
        .add_schema(

            shape='polygon',
            schema=[
                opts.RadarIndicatorItem(name="焦虑", max_=m),
                opts.RadarIndicatorItem(name="悲伤", max_=m),
                opts.RadarIndicatorItem(name="愤怒", max_=m),
                opts.RadarIndicatorItem(name="喜悦", max_=m),
                opts.RadarIndicatorItem(name="感激", max_=m),
                opts.RadarIndicatorItem(name="信任", max_=m),
            ],

            splitarea_opt=opts.SplitAreaOpts(
            is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
        ),
        textstyle_opts=opts.TextStyleOpts(color="#fff"),
    )
        .add(
            symbol = None,
            series_name="官方媒体",
            data=v1,
            linestyle_opts=opts.LineStyleOpts(width=1),
            areastyle_opts=opts.AreaStyleOpts(opacity=0.1),
        )
    # .add("北京", value_bj, color=)
    # .add("上海", value_sh, color="#b3e4a1")
    # .set_series_opts(label_opts=opts.LabelOpts(is_show=False))

        .add(
            symbol=None,
            series_name="大众心理",
            data=v2,
            linestyle_opts=opts.LineStyleOpts(color='#61a0a8'),
            areastyle_opts=opts.AreaStyleOpts(opacity=0.1,color='#61a0a8'),)

        ).add(
            series_name="自媒体",
            symbol=None,
            data=v3,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.1,color="#fab27b"),
            linestyle_opts=opts.LineStyleOpts(color="#fab27b"),
        )\
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))\
        .set_global_opts(
            title_opts=opts.TitleOpts(title="第"+str(i+1)+"阶段心态分析"), legend_opts=opts.LegendOpts()
        )

    return c

city = pd.read_excel('雷达图数据.xlsx')
page = Page()
for i in range(4):
    x1 = [list(city.iloc[3*i+0, :])[1:]]
    x2 = [list(city.iloc[3*i+1, :])[1:]]
    x3 = [list(city.iloc[3*i+2, :])[1:]]
    page.add(radar_plot(x1,x2,x3,i))
page.render('心态分析.html')