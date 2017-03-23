import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
from . import cm

def get_data_lim(ax=None):
    if ax is None: ax=plt.gca()
    lim=ax.dataLim
    lim=ax.dataLim
    xmin=lim.xmin
    xmax=lim.xmax
    ymin=lim.ymin
    ymax=lim.ymax
    return (xmin,xmax), (ymin,ymax)

def fit_data_lim(ax=None,which="both",margin=0,xlog=True,ylog=True):
    if ax is None: ax=plt.gca()
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
    if which=="both" or which=="x":
        ax.set_xlim((xmin,xmax))
    if which=="both" or which=="y":
        ax.set_ylim((ymin,ymax))
    return (xmin,xmax), (ymin,ymax)

def set_log_minor(ax=None,which="both",subs=(2,5)):
    if ax is None: ax=plt.gca()
    if which in ("both","x"):
        ax.xaxis.set_minor_locator(ticker.LogLocator(subs=subs))
        ax.xaxis.set_minor_formatter(ticker.LogFormatter(labelOnlyBase=False))
    if which in ("both","y"):
        ax.yaxis.set_minor_locator(ticker.LogLocator(subs=subs))
        ax.yaxis.set_minor_formatter(ticker.LogFormatter(labelOnlyBase=False))
#    else:
#        raise ValueError("which parameter must be both, x, or y")

def plot_guideline(b,e,slope,label="",style="-b",left=False,ha="left",va="bottom",fontsize=10,plotargs={},textargs={},ax=None):
    if ax is None: ax=plt.gca()
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
    ax.plot([bx,ex],[by,ey],style,**plotargs)
    x = bx if left else ex
    y = by if left else ey
    ax.text(x,y,label,ha=ha,va=va,fontsize=fontsize,**textargs)

def plot_guideline_log(b,e,exponent,label="",style="-b",left=False,ha="left",va="bottom",
        fontsize=10,plotargs={},textargs={},ax=None):
    if ax is None: ax=plt.gca()
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
    ax.loglog([bx,ex],[by,ey],style,**plotargs)
    x = bx if left else ex
    y = by if left else ey
    ax.text(x,y,label,ha=ha,va=va,fontsize=fontsize,**textargs)

def plot_horizontal_line(y,label="",linestyle="--",color="k",left=False,ha="left",va="center",fontsize=10,xoffset=0,yoffset=0,plotargs={},textargs={},ax=None):
    if ax is None: ax=plt.gca()
    ax.axhline(y,linestyle=linestyle,color=color,**plotargs)
    xlims=ax.get_xlim()
    x=xlims[0] if left else xlims[1]
    ax.text(x+xoffset,y+yoffset,label,horizontalalignment=ha,va=va,fontsize=fontsize,**textargs)
def imshow_color(img1,img2,img3,ax=None,*args,**kargs):
    if ax is None: ax=plt.gca()
    im = np.transpose([img1,img2,img3],(1,2,0))
    kargs.update({"interpolation":"none"})
    ax.imshow(im,*args,**kargs)

def set_str_formatters(fmt,ax=None,which="both"):
    if ax is None: ax=plt.gca()
    if which=="both" or which=="x":
        ax.xaxis.set_major_formatter(ticker.FormatStrFormatter(fmt))
        ax.xaxis.set_minor_formatter(ticker.FormatStrFormatter(fmt))
    if which=="both" or which=="y":
        ax.yaxis.set_major_formatter(ticker.FormatStrFormatter(fmt))
        ax.yaxis.set_minor_formatter(ticker.FormatStrFormatter(fmt))

def hide_tick_label(ax=None,which="both"):
    if ax is None: ax=plt.gca()
    if which=="both" or which=="x":
        plt.setp(ax.get_xmajorticklabels(), visible=False)
        plt.setp(ax.get_xminorticklabels(), visible=False)
    if which=="both" or which=="y":
        plt.setp(ax.get_ymajorticklabels(), visible=False)
        plt.setp(ax.get_yminorticklabels(), visible=False)
