import seaborn as sns

metro_color=sns.color_palette(["#9caeb7","#e60012","#622886","#f39700","#00a7db","#bb641d","#009944","#a9cc51","#e85298","#0079c2","#d7c447"])
warm_color=sns.color_palette(["#c83b36","#df6a37","#cca044","#b14dbe","#ae366a","#74246b"])
cold_color=sns.color_palette(["#38279e","#3a66ba","#33a3a5","#71c458","#37a032","#2a865f"])
def get_darker(cmap,r=0.5):
    return sns.color_palette([[c*r for c in cc] for cc in cmap])
