import matplotlib.pyplot as plt
import seaborn

def plt_guideline(b,e,slope,label="",style="-b",left=False,ha="right",va = "top",plot_dist=plt):
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
    plot_dist.plot([bx,ex],[by,ey],style)
    x = bx if left else ex
    y = by if left else ey
    plot_dist.text(x,y,label,ha=ha,va=va)


def plt_guideline_log(b,e,exponent,label="",style="-b",left=False,ha="right",va = "top",fontsize=10,plot_dist=plt,**args):
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
    plot_dist.loglog([bx,ex],[by,ey],style)
    x = bx if left else ex
    y = by if left else ey
    plot_dist.text(x,y,label,ha=ha,va=va,fontsize=fontsize,**args)

def plt_horizontal_line(xs,y,label="",style="--",left=False,ha="right",va = "top",plot_dist=plt):
    bx = xs[0]
    ex = xs[1]
    plot_dist.plot([bx,ex],[y,y],style)
    x = bx if left else ex
    plot_dist.text(x,y,label,horizontalalignment=ha,va=va)

