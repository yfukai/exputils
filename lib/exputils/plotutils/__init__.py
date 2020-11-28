import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import ticker
from . import cm

#https://stackoverflow.com/questions/31940285/plot-a-polar-color-wheel-based-on-a-colormap-using-python-matplotlib
def color_wheel(cmap,fig=plt.figure(),figsize=(4,4)):
    #Generate a figure with a polar projection
    fg = plt.figure(figsize=figsize)
    ax = fg.add_axes([0.1,0.1,0.8,0.8], projection='polar')

    #define colormap normalization for 0 to 2*pi
    norm = mpl.colors.Normalize(0, 2*np.pi) 

    #Plot a color mesh on the polar plot
    #with the color set by the angle

    n = 200  #the number of secants for the mesh
    t = np.linspace(0,2*np.pi,n)   #theta values
    r = np.linspace(0,1,2)        #raidus values change 0.6 to 0 for full circle
    rg, tg = np.meshgrid(r,t)      #create a r,theta meshgrid
    c = tg                         #define color values as theta value
    im = ax.pcolormesh(t, r, c.T,norm=norm,cmap=cmap)  #plot the colormesh on axis with colormap
    ax.set_yticklabels([])                   #turn of radial tick labels (yticks)
    ax.tick_params(pad=15,labelsize=24)      #cosmetic changes to tick labels
    ax.spines['polar'].set_visible(False)    #turn off the axis spine.
    
def legend_reverse(ax=None,**kwargs):
    if ax is None: ax=plt.gca()
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1],**kwargs)
def errorbar_arg_to_plot_arg(args):
    args_plot=args.copy()
    fmt=args_plot.pop("fmt",".")
    args_plot.pop("capsize",None)
    args_plot.pop("ecolor",None)
    args_plot.pop("capthick",None)
    return fmt, args_plot
def errorbar_limited(err_indices,x,y,yerr=None,xerr=None,ax=None,last_params={},**args):
    indices=np.argsort(x)
    x=x[indices]
    y=y[indices]
    if ax is None: ax=plt.gca()
    wo_err_indices=np.setdiff1d(np.arange(len(x)),err_indices)
    fmt,args_plot=errorbar_arg_to_plot_arg(args)
    args_plot.pop("label",None)
    ax.plot(x[wo_err_indices],y[wo_err_indices],fmt,**args_plot)
    yerr2=None if yerr is None else yerr[err_indices]
    xerr2=None if xerr is None else xerr[err_indices]
    args.update({"zorder":args_plot.get("zorder",3)+2})
    args.update(last_params)
    ax.errorbar(x[err_indices],y[err_indices],yerr2,xerr2,**args)

def get_all_data(ax=None):
    if not ax:
        ax=plt.gca()
    if len(ax.lines)>0:
        xss,yss=zip(*[l.get_data() for l in ax.lines])
        return xss,yss
    else:
        return None

def get_data_lim(ax=None,xlims=(-np.inf,np.inf),ylims=(-np.inf,np.inf)):
    if ax is None: ax=plt.gca()
    data=[np.concatenate(datum) for datum in get_all_data(ax)] #all xs, ys
    data=[datum[np.logical_and(vmin<datum,datum<vmax)] 
          for datum,vmin,vmax in zip(data,*zip(xlims,ylims))]
    return [(np.min(datum),np.max(datum)) for datum in data]

def calc_lim(vmin,vmax,margin,islog=False):
    if islog:
        vr=vmax/vmin
        if vr>0:
            vm=np.exp(np.log(vr)*margin)
            vmin=vmin/vm ; vmax=vmax*vm
    else:
        vr=vmax-vmin
        vm=vr*margin
        vmin=vmin-vm ; vmax=vmax+vm
    return vmin,vmax

def fit_data_lim(ax=None,which="both",
                 margin=0,xlog=True,ylog=True,
                 xlims=[-np.inf,np.inf],ylims=[-np.inf,np.inf]):
    if ax is None: ax=plt.gca()
    if xlog and xlims[0]<0: xlims[0]=0
    if ylog and ylims[0]<0: ylims[0]=0
    limss=get_data_lim(ax,xlims,ylims)
    xlim,ylim=[calc_lim(*lims,margin,islog) 
           for lims,islog in zip(limss,(xlog,ylog))]
    if which=="both" or which=="x":
        ax.set_xlim(xlim)
    if which=="both" or which=="y":
        ax.set_ylim(ylim)

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
        fontsize=10,plotargs={},textargs={},ax=None,xoffset=0,yoffset=0):
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
    x = (bx if left else ex)+xoffset
    y = (by if left else ey)+yoffset
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
