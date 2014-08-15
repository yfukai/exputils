#coding: utf-8
import argparse
import os

class PathPredicate:
	def __init__(self, pred, message):
		self.pred = pred
		self.message = message

def argparse_action(*preds):
	class CheckDir(argparse.Action):
		def __call__(self, parser, namespace, values, option_string=None):
			for p in preds :
				if not p.pred(values):
					raise argparse.ArgumentTypeError(p.message.format(values))
			setattr(namespace,self.dest,values)
	return CheckDir

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

# path_args ... {"name1": (pred1, pred2, ...), "name2": (pred1,...)}
def set_simple_path_args(desc, path_args,args=None):
	parser=get_argparse_parser(desc)
	for name, path_arg in path_args.items() :
		parser.add_argument(name,action=argparse_action(*path_arg))
	args = parser.parse_args(args)
	keys = path_args.keys()
	return dict(zip(keys,[getattr(args,k) for k in keys]))

