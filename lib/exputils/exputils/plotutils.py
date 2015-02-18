import matplotlib.pyplot as plt

def plt_guideline_log(b,e,exponent,label="",style="-b",ha="right",plot_dist=plt):
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
    plt.loglog([bx,ex],[by,ey],style)
    plt.text(ex,ey,label,horizontalalignment=ha)

def plt_line(bx,y,ex,label="",style="--",left=False,ha="right",va = "top",plot_dist=plt):
    plt.plot([bx,ex],[y,y],style)
    x = bx if left else ex
    plt.text(x,y,label,horizontalalignment=ha,va=va)

