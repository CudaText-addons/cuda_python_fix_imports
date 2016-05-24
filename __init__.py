from cudatext import *
import sys
import os

from . import format_proc
from .fiximports import FixImports

format_proc.INI = 'cuda_python_fix_imports.ini'
format_proc.MSG = '[Python Fix Imports] '


def do_format(text):
    fn = format_proc.ini_filename()
    section = 'op'
    op_split = ini_read(fn, section, 'split_import_statements', '1')=='1'
    op_sort = ini_read(fn, section, 'sort_import_statements', '1')=='1'
    
    res, textout = FixImports().sortImportGroups(
        ed.get_filename(), 
        text,
        splitImportStatements=op_split,
        sortImportStatements=op_sort)      
    if res:
        if textout!=text:
            return textout


class Command:
    def config_global(self):
        format_proc.config_global()

    def config_local(self):
        format_proc.config_local()

    def run(self):
        format_proc.run(do_format)
