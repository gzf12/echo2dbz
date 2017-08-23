import util
import os

cwd = os.getcwd()
pro_dir = os.path.abspath(os.path.join(cwd,'..'))
directory = 'data'
origin_dir = 'input/grey_echo'
target_dir = 'output/dbz_echo'
# seq_name = '320_2layer'
util.echo2dbz(os.path.join(pro_dir, directory, origin_dir), os.path.join(pro_dir, directory, target_dir))