import numpy as np
def fit_data_lim(ax,margin=0,xlog=True,ylog=True):
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
    ax.set_xlim((xmin,xmax))
    ax.set_ylim((ymin,ymax))

def plt_guideline(plot_dist,b,e,slope,label="",style="-b",left=False,ha="right",va = "top",fontsize=10,plotargs={},textargs={}):
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


def plt_guideline_log(plot_dist,b,e,exponent,label="",style="-b",left=False,ha="right",va = "top",fontsize=10,plotargs={},textargs={}):
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

def plt_horizontal_line(plot_dist,xs,y,label="",style="--",left=False,ha="right",va = "top",fontsize=10,plotargs={},textargs={}):
    bx = xs[0]
    ex = xs[1]
    plot_dist.plot([bx,ex],[y,y],style,**plotargs)
    x = bx if left else ex
    plot_dist.text(x,y,label,horizontalalignment=ha,va=va,fontsize=fontsize,**textargs)

