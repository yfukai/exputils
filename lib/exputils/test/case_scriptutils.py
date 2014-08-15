# -*- coding:utf-8 -*-
# using konira

import os
import sys
import konira

LIB_DIR = os.path.realpath('../')

if not LIB_DIR in sys.path:
	sys.path.insert(0, LIB_DIR)
#
import exputils.scriptutils.arguments as arg

describe "add_pred_argument readable dir":
	before each:
		self.parser = arg.get_argparse_parser("test parser")
		self.parser.add_argument("path",
			action=arg.argparse_action(arg.IS_DIR,arg.IS_READABLE))
	it "should parse readable dir argments":
		self.parser.parse_args('exist_dir'.split())
		assert True
	it "should raise error on not exist dir argments":
		raises Exception: self.parser.parse_args('not_exist_dir'.split())
	it "should raise error on file argments":
		raises Exception: self.parser.parse_args('exist_file'.split())

describe "add_pred_argument readable file":
	before each:
		self.parser = arg.get_argparse_parser("test parser")
		self.parser.add_argument("path",
			action=arg.argparse_action(arg.IS_FILE,arg.IS_READABLE))
	it "should parse readable file argments":
		self.parser.parse_args('exist_file'.split())
		assert True
	it "should raise error on not exist file argments":
		raises Exception: self.parser.parse_args('not_exist_file'.split())
	it "should raise error on file argments":
		raises Exception: self.parser.parse_args('exist_dir'.split())

describe "add_pred_argument readable path":
	before each:
		self.parser = arg.get_argparse_parser("test parser")
		self.parser.add_argument("path",
			action=arg.argparse_action(arg.IS_PATH,arg.IS_READABLE))
	it "should parse readable file argments":
		self.parser.parse_args('exist_file'.split())
		assert True
	it "should parse readable dir argments":
		self.parser.parse_args('exist_dir'.split())
		assert True
	it "should raise error on not exist dir argments":
		raises Exception: self.parser.parse_args('not_exist_dir'.split())

