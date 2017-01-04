import numpy as np
from matplotlib.ticker import LogLocator, LogFormatter

def get_data_lim(ax):
    lim=ax.dataLim
    lim=ax.dataLim
    xmin=lim.xmin
    xmax=lim.xmax
    ymin=lim.ymin
    ymax=lim.ymax
    return (xmin,xmax), (ymin,ymax)

def fit_data_lim(ax,axis="both",margin=0,xlog=True,ylog=True):
    lim=ax.dataLim
    lim=ax.dataLim
    xmin=lim.xmin
    xmax=lim.xmax
    ymin=lim.ymin
    ymax=lim.ymax
    if xlog:
        xr=lim.xmax/lim.xmin
        xm=np.exp(np.log(xr)*margin)
        xmin=xmin/xm ; xmax=xmax*xm
    else:
        xr=lim.xmax-lim.xmin
        xm=xr*margin
        xmin=xmin-xm ; xmax=xmax+xm
    if ylog:
        yr=lim.ymax/lim.ymin
        ym=np.exp(np.log(yr)*margin)
        ymin=ymin/ym ; ymax=ymax*ym
    else:
        yr=lim.ymax-lim.ymin
        ym=yr*margin
        ymin=ymin-ym ; ymax=ymax+ym
    if axis=="both" or axis=="x":
        ax.set_xlim((xmin,xmax))
    if axis=="both" or axis=="y":
        ax.set_ylim((ymin,ymax))
    return (xmin,xmax), (ymin,ymax)

def set_log_minor(ax,axis="both",subs=np.arange(1,10,1)):
    if axis=="both" or axis=="x":
        ax.xaxis.set_minor_locator(LogLocator(subs=subs))
        ax.xaxis.set_minor_formatter(LogFormatter(labelOnlyBase=False))
    if axis=="both" or axis=="y":
        ax.yaxis.set_minor_locator(LogLocator(subs=subs))
        ax.yaxis.set_minor_formatter(LogFormatter(labelOnlyBase=False))
    else:
        raise ValueError("axis parameter have to be both, x, or y")

def plot_guideline(plot_dist,b,e,slope,label="",style="-b",left=False,ha="right",va = "top",fontsize=10,plotargs={},textargs={}):
    if len(b) == 2 and len(e) == 1:
        bx = b[0]
        by = b[1]
        ex = e[0]
        ey = by+((ex-bx)*slope)
    elif len(b) == 1 and len(e) == 2:
        bx = b[0]
        ex = e[0]
        ey = e[1]
        by = ey-((ex-bx)*slope)
    plot_dist.plot([bx,ex],[by,ey],style,**plotargs)
    x = bx if left else ex
    y = by if left else ey
    plot_dist.text(x,y,label,ha=ha,va=va,fontsize=fontsize,**textargs)

def plot_guideline_log(plot_dist,b,e,exponent,label="",style="-b",left=False,ha="right",va = "top",fontsize=10,plotargs={},textargs={}):
    if len(b) == 2 and len(e) == 1:
        bx = b[0]
        by = b[1]
        ex = e[0]
        ey = by*((ex/bx)**exponent)
    elif len(b) == 1 and len(e) == 2:
        bx = b[0]
        ex = e[0]
        ey = e[1]
        by = ey/((ex/bx)**exponent)
    plot_dist.loglog([bx,ex],[by,ey],style,**plotargs)
    x = bx if left else ex
    y = by if left else ey
    plot_dist.text(x,y,label,ha=ha,va=va,fontsize=fontsize,**textargs)

def plot_horizontal_line(ax,y,label="",linestyle="--",color="k",left=False,ha="right",va = "top",fontsize=10,plotargs={},textargs={}):
    ax.axhline(y,linestyle=linestyle,color=color,**plotargs)
    xlims,ylims=get_data_lim(ax)
    x=xlims[0] if left else xlims[1]
    ax.text(x,y,label,horizontalalignment=ha,va=va,fontsize=fontsize,**textargs)

def imshow_color(plot_dist,img1,img2,img3,*args,**kargs):
    im = np.transpose([img1,img2,img3],(1,2,0))
    kargs.update({"interpolation":"none"})
    plot_dist.imshow(im,*args,**kargs)

