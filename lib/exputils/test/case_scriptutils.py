# -*- coding:utf-8 -*-
# using konira

import os
import sys
import konira

LIB_DIR = os.path.realpath('../')

if not LIB_DIR in sys.path:
    sys.path.insert(0, LIB_DIR)
#
import exputils.scriptutils.argutils as arg

describe "add_pred_argument readable dir":
    before each:
        self.parser = arg.get_argparse_parser("test parser")
        self.parser.add_argument("path",
            action=arg.argparse_action("path",arg.IS_DIR,arg.IS_READABLE))
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
            action=arg.argparse_action("path",arg.IS_FILE,arg.IS_READABLE))
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
            action=arg.argparse_action("path",arg.IS_PATH,arg.IS_READABLE))
    it "should parse readable file argments":
        self.parser.parse_args('exist_file'.split())
        assert True
    it "should parse readable dir argments":
        self.parser.parse_args('exist_dir'.split())
        assert True
    it "should raise error on not exist dir argments":
        raises Exception: self.parser.parse_args('not_exist_dir'.split())

describe "set_simple_path_args":
    it "should parse readable dir argments":
        parsed_args = arg.set_simple_path_args(
            "test dir path",
            arg.PathArg("dir",(arg.IS_DIR,arg.IS_READABLE)),
            args='exist_dir'.split())
        assert parsed_args["dir"] == "exist_dir"
    it "should parse readable file argments":
        parsed_args = arg.set_simple_path_args(
            "test dir path",
            arg.PathArg("file",(arg.IS_FILE,arg.IS_READABLE)),
            args='exist_file'.split())
        assert parsed_args["file"] == "exist_file"
    it "should parse multiple argments":
        parsed_args = arg.set_simple_path_args(
            "test dir path",
            arg.PathArg("file",(arg.IS_FILE,arg.IS_READABLE)),
            arg.PathArg("dir",(arg.IS_DIR,arg.IS_READABLE)),
            args='exist_file exist_dir'.split())
        assert parsed_args["file"] == "exist_file"
        assert parsed_args["dir"] == "exist_dir"
    it "should parse or argments":
        parsed_args = arg.set_simple_path_args(
            "test dir path",
            arg.PathArg("file_or_dir",(arg.OR(arg.IS_FILE,arg.IS_DIR),arg.IS_READABLE)),
            args='exist_file'.split())
        assert parsed_args["file_or_dir"] == "exist_file"
        parsed_args = arg.set_simple_path_args(
            "test dir path",
            arg.PathArg("file_or_dir",(arg.OR(arg.IS_FILE,arg.IS_DIR),arg.IS_READABLE)),
            args='exist_dir'.split())
        assert parsed_args["file_or_dir"] == "exist_dir"
    it "should rais error on not appropreate args":
        raises Exception: arg.set_simple_path_args(
            "test dir path",{"dir":(arg.IS_DIR,arg.IS_READABLE)},
            args='exist_file'.split())

describe "set_args":
    it "should parse ordinary argments":
        parsed_args = arg.set_args(
            "test dir path",
            arg.PathArg("dir",(arg.IS_DIR,arg.IS_READABLE)),
            arg.Arg("N", type=int),
            args='exist_dir 10'.split())
        assert parsed_args["dir"] == "exist_dir"
        assert parsed_args["N"] == 10
 
import exputils.scriptutils.pathutils as pathu

describe "getfiles":
    it "should get file list":
        f = pathu.getfiles("exist_dir","tsv")
        assert len(f) == 2
        f = pathu.getfiles("exist_dir")
        assert len(f) == 4

describe "get_abs_path":
    it "should get abstract path":
        p = pathu.get_abs_path("exist_dir")
        assert p.endswith("exist_dir")
        assert p.startswith("/")
        p = pathu.get_abs_path("/tmp")
        assert p == "/tmp"

import exputils.scriptutils.iterutils as iteru
describe "iget":
    it "should get iter element by index":
        assert iteru.iget([1,2,-1,4],2) == -1

describe "csv_skip_row":
    it "shold skip comment line":
        data = ["#comment","data"]
        result = list(iteru.csv_skip_row(data))
        assert len(result) == 1
        assert result[0] == "data"
 
