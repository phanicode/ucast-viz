
import pandas as pd, matplotlib.pyplot as plt, numpy as np
import sys
from datetime import datetime
from bokeh.plotting import figure, output_file, show
from bokeh.models import Range1d,Column

# if sys.argv() > 1:
    

import sys
file_type=sys.argv[1:][0]
# if sys.argv() > 1:
    



ALMA = pd.read_csv(
'./ALMA/{}'.format(file_type), skiprows=[0],names="date,tau225,Tb[K],pwv[mm],lwp[kg*m^-2],iwp[kg*m^-2],o3[DU]".split(","),
  sep = '\s+'
)
ALMA["site"] = "ALMA"

APEX = pd.read_csv(
"./APEX/{}".format(file_type), skiprows=[0],names="date,tau225,Tb[K],pwv[mm],lwp[kg*m^-2],iwp[kg*m^-2],o3[DU]".split(","),
  sep = '\s+'
)
APEX["site"] = "APEX"

GLT = pd.read_csv(
"./GLT/{}".format(file_type), skiprows=[0],names="date,tau225,Tb[K],pwv[mm],lwp[kg*m^-2],iwp[kg*m^-2],o3[DU]".split(","),
  sep = '\s+'
)
GLT["site"] = "GLT"



JCMT= pd.read_csv(
"./JCMT/{}".format(file_type), skiprows=[0],names="date,tau225,Tb[K],pwv[mm],lwp[kg*m^-2],iwp[kg*m^-2],o3[DU]".split(","),
  sep = '\s+'
)
JCMT["site"] = "JCMT"

KP= pd.read_csv(
"./KP/{}".format(file_type), skiprows=[0],names="date,tau225,Tb[K],pwv[mm],lwp[kg*m^-2],iwp[kg*m^-2],o3[DU]".split(","),
  sep = '\s+'
)
KP["site"] = "KP"
LMT= pd.read_csv(
"./LMT/{}".format(file_type), skiprows=[0],names="date,tau225,Tb[K],pwv[mm],lwp[kg*m^-2],iwp[kg*m^-2],o3[DU]".split(","),
  sep = '\s+'
)
LMT["site"] = "LMT"

PDB= pd.read_csv(
"./PDB/{}".format(file_type), skiprows=[0],names="date,tau225,Tb[K],pwv[mm],lwp[kg*m^-2],iwp[kg*m^-2],o3[DU]".split(","),
  sep = '\s+'
)
PDB["site"] = "PDB"
PV= pd.read_csv(
"./PV/{}".format(file_type), skiprows=[0],names="date,tau225,Tb[K],pwv[mm],lwp[kg*m^-2],iwp[kg*m^-2],o3[DU]".split(","),
  sep = '\s+'
)
PV["site"] = "PV"

SMA= pd.read_csv(
"./SMA/{}".format(file_type), skiprows=[0],names="date,tau225,Tb[K],pwv[mm],lwp[kg*m^-2],iwp[kg*m^-2],o3[DU]".split(","),
  sep = '\s+'
)
SMA["site"] = "SMA"
SMT= pd.read_csv(
"./SMT/{}".format(file_type), skiprows=[0],names="date,tau225,Tb[K],pwv[mm],lwp[kg*m^-2],iwp[kg*m^-2],o3[DU]".split(","),
  sep = '\s+'
)
SMT["site"] = "SMT"
SPT= pd.read_csv(
"./SPT/{}".format(file_type), skiprows=[0],names="date,tau225,Tb[K],pwv[mm],lwp[kg*m^-2],iwp[kg*m^-2],o3[DU]".split(","),
  sep = '\s+'
)
SPT["site"] = "SPT"

dfs=[ALMA, APEX, GLT, JCMT, KP, LMT, PDB, PV, SMA, SMT, SPT]

def set_dates(dfs):
    for df in dfs:
        df['date'] = pd.to_datetime(df['date'],format='%Y%m%d_%H:%M:%S')
set_dates(dfs)
output_file("forecast.html")
# p = figure(plot_width=1600, plot_height=500, x_axis_type="datetime")
# p.sizing_mode = 'scale_width'

# p.y_range = Range1d(0, 1)
# p.line(ALMA['date'], ALMA['tau225'], color='navy', alpha=0.5,legend_label="ALMA")
# p.line(APEX['date'], APEX['tau225'], color='red', alpha=0.5,legend_label="APEX")
# p.line(GLT['date'], GLT['tau225'], color='blue', alpha=0.5,legend_label="GLT")
# p.line(JCMT['date'], JCMT['tau225'], color='green', alpha=0.5,legend_label="JCMT")
# p.line(KP['date'], KP['tau225'], color='pink', alpha=0.5,legend_label="KP")
# p.line(LMT['date'], LMT['tau225'], color='purple', alpha=0.5,legend_label="LMT")
# p.line(PDB['date'], PDB['tau225'], color='violet', alpha=0.5,legend_label="PDB")
# p.line(PV['date'], PV['tau225'], color='darkcyan', alpha=0.5,legend_label="PV")
# p.line(SMA['date'], SMA['tau225'], color='royalblue', alpha=0.5,legend_label="SMA")
# p.line(SMT['date'], SPT['tau225'], color='seagreen', alpha=0.5,legend_label="SMT")
# p.line(SPT['date'], SPT['tau225'], color='gold', alpha=0.5,legend_label="SPT")
# p.legend.location = "top_left"
# p.legend.click_policy="hide"
# show(p)
      
def create_plot(var):
    p2 = figure(title = var,plot_width=1600, plot_height=500, x_axis_type="datetime")
    if var=="tau225":
        p2.y_range = Range1d(0, 1)
    elif var=="pwv[mm]":
        p2.y_range = Range1d(0, 15)
    elif var=="lwp[kg*m^-2]":
        p2.y_range = Range1d(0,1)
    elif var=="iwp[kg*m^-2]":
        p2.y_range = Range1d(0,2)
          
    p2.line(ALMA['date'], ALMA[var], color='navy', alpha=0.5,legend_label="ALMA")
    p2.line(APEX['date'], APEX[var], color='red', alpha=0.5,legend_label="APEX")
    p2.line(GLT['date'], GLT[var], color='blue', alpha=0.5,legend_label="GLT")
    p2.line(JCMT['date'], JCMT[var], color='green', alpha=0.5,legend_label="JCMT")
    p2.line(KP['date'], KP[var], color='pink', alpha=0.5,legend_label="KP")
    p2.line(LMT['date'], LMT[var], color='purple', alpha=0.5,legend_label="LMT")
    p2.line(PDB['date'], PDB[var], color='violet', alpha=0.5,legend_label="PDB")
    p2.line(PV['date'], PV[var], color='darkcyan', alpha=0.5,legend_label="PV")
    p2.line(SMA['date'], SMA[var], color='royalblue', alpha=0.5,legend_label="SMA")
    p2.line(SMT['date'], SPT[var], color='seagreen', alpha=0.5,legend_label="SMT")
    p2.line(SPT['date'], SPT[var], color='gold', alpha=0.5,legend_label="SPT")
    p2.legend.location = "top_left"
    p2.legend.click_policy="hide"
    return p2
plot_list=[]
for var in "tau225,pwv[mm],lwp[kg*m^-2],iwp[kg*m^-2]".split(","):
      plot_list.append(create_plot(var))
      
p = Column(plot_list[0],plot_list[1],plot_list[2],plot_list[3])


show(p)


