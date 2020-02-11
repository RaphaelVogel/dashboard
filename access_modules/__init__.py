import configparser
from pathlib import Path


root_dir = Path(__file__).resolve().parent.parent
cfg = configparser.ConfigParser()
cfg.read(Path(root_dir, 'tools/config.txt'))
