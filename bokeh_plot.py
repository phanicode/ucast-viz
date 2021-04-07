import pandas as pd, matplotlib.pyplot as plt, numpy as np
import sys
from bokeh.plotting import figure, output_file, show
from bokeh.models import Range1d,Column

# if sys.argv() > 1:
    
names="date,tau225,Tb[K],pwv[mm],lwp[kg*m^-2],iwp[kg*m^-2],o3[DU]".split(",")
sites=["ALMA", "APEX", "GLT", "JCMT", "KP", "LMT", "PDB", "PV", "SMA", "SMT", "SPT"]
colors=['navy','red','blue','green','pink','purple','violet','darkcyan','royalblue','seagreen','gold']
import sys
file_type=sys.argv[1:][0]
# if sys.argv() > 1:
dfs= [pd.read_csv(
'./{site}/{file}'.format(site=site, file=file_type), skiprows=[0],names=names,
  sep = '\s+'
) for site in sites]
def set_dates(dfs):
    for df in dfs:
        df['date'] = pd.to_datetime(df['date'],format='%Y%m%d_%H:%M:%S')
set_dates(dfs)
output_file("forecast.html")

def create_plot(var):
    p2 = figure(title = var,plot_width=1600, plot_height=500, x_axis_type="datetime",tools="pan,box_zoom,box_select,lasso_select,undo,wheel_zoom,redo,reset,save".split())
    if var=="tau225":
        p2.y_range = Range1d(0, 1)
    elif var=="pwv[mm]":
        p2.y_range = Range1d(0, 15)
    elif var=="lwp[kg*m^-2]":
        p2.y_range = Range1d(0,1)
    elif var=="iwp[kg*m^-2]":
        p2.y_range = Range1d(0,2)
    for i in range(11):
        p2.line(dfs[i]['date'], dfs[i][var], color=colors[i], alpha=0.5,legend_label=sites[i])
    p2.legend.location = "top_left"
    p2.legend.click_policy="hide"
    return p2
plot_list=[create_plot(var) for var in"tau225,pwv[mm],lwp[kg*m^-2],iwp[kg*m^-2]".split(",") ]

p = Column(*plot_list)


show(p)
