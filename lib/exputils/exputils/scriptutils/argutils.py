#coding: utf-8
import argparse
import os

class PathPredicate:
    def __init__(self, pred, message):
        self.pred = pred
        self.message = message

def argparse_action(name,*preds):
    def checkargs(s_preds, values,):
        for p in s_preds :
            if not p.pred(values):
                raise argparse.ArgumentTypeError(p.message.format(values))
        return values
    return type("Check"+name, (argparse.Action,), {
        "preds" : preds,
        "__call__" : (lambda self, parser, namespace, values, option_string=None : setattr(namespace, self.dest, checkargs(self.preds, values)))
        })

def OR(p1,p2):
    return PathPredicate(
        (lambda p : (p1.pred(p) or p2.pred(p))),
        p1.message + " or " + p2.message )

IS_PATH = PathPredicate(
        (lambda p : os.path.exists(p)), 
        "is_path :{0} is not a exist path")

IS_DIR = PathPredicate(
        (lambda p : os.path.isdir(p)), 
        "is_dir :{0} is not a valid dir")

IS_FILE = PathPredicate(
        (lambda p : os.path.isfile(p)), 
        "is_file :{0} is not a valid file")

IS_READABLE = PathPredicate(
        (lambda p : os.access(p, os.R_OK)), 
        "is_readable :{0} is not readable")

IS_WRITEABLE = PathPredicate(
        (lambda p : os.access(p, os.W_OK)), 
        "is_writeable :{0} is not writeable")

def get_argparse_parser(desc=""):
    return argparse.ArgumentParser(description=desc)

class PathArg:
    def __init__(self,name,preds):
        self.name = name
        self.preds = preds

# path_args ...[PathArg("name1", (pred1, pred2, ...)), PathArg("name2", (pred1, ...))]
def set_simple_path_args(desc, *path_args,**args):
    args = args["args"] if "args" in args.keys() else None
    parser=get_argparse_parser(desc)
    for p in path_args :
        argp_action = argparse_action(p.name,*(p.preds))
        parser.add_argument(p.name,action=argp_action)
    args = parser.parse_args(args)
    keys = [p.name for p in path_args ]
    return dict(zip(keys,[getattr(args,k) for k in keys]))

