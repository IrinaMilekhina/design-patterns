import os
from os.path import join

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATES_DIR = join(BASE_DIR, "pages", "templates")
OUT_FILES_DIR = join(BASE_DIR, "out")
