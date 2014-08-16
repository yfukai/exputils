from scipy.interpolate import interp1d

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

