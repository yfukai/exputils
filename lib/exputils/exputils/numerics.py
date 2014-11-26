from scipy.interpolate import interp1d
import numpy as np
import math

def interpolate_array(arr, is_appropreate, circle=False, **interp_args):
    length = len(arr)
    xs = [i for i,v in enumerate(arr) if is_appropreate(v)]
    hs = [arr[i] for i in xs]
    if circle:
        xs = [x-length for x in xs ] + xs + [x+length for x in xs ] 
        hs = hs + hs + hs
    else:
        min_x = min(xs) ; max_x = max(xs)
        min_h = hs[0] ; max_h = hs[-1]
        xs = [x for x in range(min_x)] + xs + [x for x in range(max_x,length)]
        hs = min_x*[min_h] + hs + (length-max_x)*[max_h]

    interp = interp1d(xs,hs,**interp_args)
    int_indices=[i for i,v in enumerate(arr) if not is_appropreate(v)]
    interp_results = interp(int_indices)
    
    for i in range(len(int_indices)):
        arr[int_indices[i]] = interp_results[i]
    
    return arr

def get_log_separated_array(begin, end, count):
    return np.logspace(np.log10(begin),np.log10(end),count)

# returns  fmod(a,b) + b if a is negative
def fmod_positive(a,b):
    return np.fmod(a,b) + (a<0)*b 

def calc_linear_fitting_consts(xs,ys):
    mean_x = np.mean(xs)
    mean_x_times_2 = np.mean(xs**2)
    mean_y = np.mean(ys)
    var_x = mean_x_times_2-mean_x**2
    covar = np.mean(xs*ys) - mean_x*mean_y
    a = var_x / covar
    b = mean_y - a * mean_x
    return a, b

def linear_fitting(xs,ys,dxs=None,dys=None,xmin=None,xmax=None):
    xs = np.array(xs); ys = np.array(ys)
    indices = np.where(np.logical_and(xs >= xmin,  xs <= xmax))
    xs = xs[indices] ; ys = ys[indices]
    dxs = dxs[indices] ; dys = dys[indices]
    a,b = calc_linear_fitting_consts(xs,ys)
    
    if dxs == None:
        dxs = np.zeros(len(indices))
    if dys == None:
        dys = ys - a * xs - b
        std = np.std(dys)
        dys = np.array([std]*len(indices))

    das = np.empty([len(indices),2])
    dbs = np.empty([len(indices),2])

    for i in indices:
        xs2 = np.copy(xs)
        xs3 = np.copy(xs)
        xs2[i] = xs[i]+dxs[i]
        xs3[i] = xs[i]-dxs[i]
        a2, b2 = calc_linear_fitting_consts(xs2,ys)
        a3, b3 = calc_linear_fitting_consts(xs2,ys)
        das[i,0] = max(abs(a2-a),abs(a3-a))
        dbs[i,0] = max(abs(b2-b),abs(b3-b))
        ys2 = np.copy(ys)
        ys3 = np.copy(ys)
        ys2[i] = ys[i]+dys[i]
        ys3[i] = ys[i]-dys[i]
        a2, b2 = calc_linear_fitting_consts(xs,ys2)
        a3, b3 = calc_linear_fitting_consts(xs,ys3)
        das[i,1] = max(abs(a2-a),abs(a3-a))
        dbs[i,1] = max(abs(b2-b),abs(b3-b))

    da = np.sqrt(np.sum(np.flatten(das)**2))
    db = np.sqrt(np.sum(np.flatten(dbs)**2))
    return a,da,b,db
