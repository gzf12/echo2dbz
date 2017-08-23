from PIL import Image
import numpy as np
import threading

color_map_path = '../resources/guangzhou20170103065000_map_color.png'
vector_map_path = '../resources/guangzhou20170103065000_map_vector.png'
echo_path = '../data/output/320_2layer/gt1.png'

radar_map_path = '../data/output/radar_map.png'

def _img_map_echo2map(echo_path,
                 radar_map_path,
                 color_map_path=color_map_path,
                 vector_map_path=vector_map_path):

    color_map = Image.open(color_map_path)
    vector_map = Image.open(vector_map_path)
    echo = Image.open(echo_path)

    echo_1000 = echo.resize((964,964))

    color_a = np.array(color_map, dtype=np.uint8)
    vector_a = np.array(vector_map, dtype=np.uint8)
    echo_a = np.array(echo_1000, dtype=np.uint8)

    for i in range(echo_a.shape[0]):
        for j in range(echo_a.shape[1]):
            if echo_a[i][j][3] > 254:
                color_a[i][j] = echo_a[i][j]

            if vector_a[i][j][3] > 254:
                color_a[i][j] = vector_a[i][j]

    radar_map = Image.fromarray(color_a)
    radar_map.save(radar_map_path)

def _seq_map_echo2map(in_seq_dir, out_seq_dir):
    threads = []
    print(in_seq_dir)
    if ~os.path.exists(out_seq_dir):
        os.makedirs(out_seq_dir)

    filenames = os.listdir(in_seq_dir)
    for filename in filenames:
        # _img_map_echo2map(os.path.join(in_seq_dir, filename), os.path.join(out_seq_dir, filename))
        thread = threading.Thread(target=_img_map_echo2map, args=(os.path.join(in_seq_dir, filename), os.path.join(out_seq_dir, filename)))
        threads.append(thread)


    for thread in threads:
        ## thread.setDaemon(True)
        thread.start()


def map_echo2map(origin_dir, target_dir):
    print(origin_dir)
    print(target_dir)
    seqs_fname = os.listdir(origin_dir)
    for fname in seqs_fname:
        in_seq_dir = os.path.join(origin_dir, fname)
        out_seq_dir = os.path.join(target_dir, fname)
        _seq_map_echo2map(in_seq_dir, out_seq_dir)

import os

cwd = os.getcwd()
pro_dir = os.path.abspath(os.path.join(cwd,'..'))
directory = 'data'
origin_dir = 'input/dbz_echo'
target_dir = 'output/echo_map'
# seq_name = '320_2layer'
map_echo2map(os.path.join(pro_dir, directory, origin_dir), os.path.join(pro_dir, directory, target_dir))

# _map_echo2map(echo_path, radar_map_path)