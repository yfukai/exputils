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

def calc_linear_fitting_consts(xs,ys,ws = None):
    average_x = np.average(xs, weights=ws)
    average_x_times_2 = np.average(xs**2, weights=ws)
    average_y = np.average(ys, weights=ws)
    var_x = average_x_times_2-average_x**2
    covar = np.average(xs*ys, weights=ws) - average_x*average_y
    a = covar / var_x
    b = average_y - a * average_x
    return a, b

def linear_fitting(xs,ys,dxs=None,dys=None,xmin=np.finfo(float).min,xmax=np.finfo(float).max,independent=True):
    xs = np.array(xs,dtype=float); ys = np.array(ys,dtype=float)
    indices = np.where(np.logical_and(xs >= xmin,  xs <= xmax))[0]
    xs = xs[indices] ; ys = ys[indices]

    if dxs != None:
        dxs = np.array(dxs)[indices]
    else:
        dxs = np.zeros(len(indices))
    if dys != None:
        dys = np.array(dys)[indices]
 
    if dxs != None and dys != None:
        ws = 1.0 / np.sqrt(dxs**2 + dys**2)
    elif dys != None:
        ws = 1.0 / np.sqrt(dys**2)
    else:
        ws = None

    a,b = calc_linear_fitting_consts(xs,ys,ws)
    
    if dys == None:
        dys = ys - a * xs - b
        std = np.std(dys)
        dys = np.array([std]*len(indices))

    das = np.empty([len(indices),2])
    dbs = np.empty([len(indices),2])

    for i in range(len(indices)):
        xs2 = np.copy(xs)
        xs3 = np.copy(xs)
        dx = dxs[i]
        xs2[i] = xs[i]+dx
        xs3[i] = xs[i]-dx
        a2, b2 = calc_linear_fitting_consts(xs2,ys,ws)
        a3, b3 = calc_linear_fitting_consts(xs2,ys,ws)
        das[i,0] = max(abs(a2-a),abs(a3-a))
        dbs[i,0] = max(abs(b2-b),abs(b3-b))

        ys2 = np.copy(ys)
        ys3 = np.copy(ys)
        dy = dys[i]
        ys2[i] = ys[i]+dy
        ys3[i] = ys[i]-dy
        a2, b2 = calc_linear_fitting_consts(xs,ys2,ws)
        a3, b3 = calc_linear_fitting_consts(xs,ys3,ws)
        das[i,1] = max(abs(a2-a),abs(a3-a))
        dbs[i,1] = max(abs(b2-b),abs(b3-b))

    if independent:
        da = np.sqrt(np.sum(das.flatten()**2))
        db = np.sqrt(np.sum(dbs.flatten()**2))
    else:
        da = np.sum(das.flatten())
        db = np.sum(dbs.flatten())
    return a,b,da,db
