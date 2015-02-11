import matplotlib.pyplot as plt

def plt_guideline(bx,by,ex,exponent,label="",style="-b",ha="right",plot_dist=plt):
    ey = by*((ex/bx)**exponent)
    plt.loglog([bx,ex],[by,ey],style)
    plt.text(ex,ey,label,horizontalalignment=ha)

def plt_line(bx,y,ex,label="",style="--",left=False,ha="right",va = "top",plot_dist=plt):
    plt.plot([bx,ex],[y,y],style)
    x = bx if left else ex
    plt.text(x,y,label,horizontalalignment=ha,va=va)

