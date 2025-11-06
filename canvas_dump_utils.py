#!/usr/bin/env python3
import os
import logging

logging.basicConfig(level=logging.INFO)

def mkdir(p: str):
    # recursive and idempotent
    os.makedirs(p, exist_ok=True)

def mk_and_cd(p: str):
    """Create directory p if needed, then chdir into it. Return previous cwd."""
    cwd = os.getcwd()
    mkdir(p)
    os.chdir(p)
    return cwd
