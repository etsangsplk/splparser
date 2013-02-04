
from splparser.parsetree import *

def p_hostname_id(p):
    """hostname : wordid PERIOD id
                | id PERIOD wordid
                | id PERIOD id"""
    r = ".".join([p[1].raw, p[3].raw])
    p[0] = ParseTreeNode('HOSTNAME', raw=r)

def p_hostname_wordid(p):
    """hostname : hostname PERIOD id"""
    r = ".".join([p[1].raw, p[3].raw])
    p[0] = ParseTreeNode('HOSTNAME', raw=r)