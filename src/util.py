from xml.dom.minidom import parse
import numpy as np
from PIL import Image
import os
import threading

import util


def read_color():
    dom_tree = parse("../resources/REFcolortable.xml")
    collection = dom_tree.documentElement
    colors_tag = collection.getElementsByTagName("entry")
    color_dict = {}
    for tag in colors_tag:
        value = tag.getAttribute("value").strip()
        rgba = np.asanyarray(tag.getAttribute("rgba").strip().split(','), np.int)
        color_dict[int(float(value)*2)] = rgba
    return color_dict

def echo2dbz(origin_dir, target_dir):
    print(origin_dir)
    print(target_dir)
    # if ~os.path.exists(target_dir):
    #     print( ~os.path.exists(target_dir) == True)
    #     os.makedirs(target_dir)
    seqs_fname = os.listdir(origin_dir)

    threads = []

    for fname in seqs_fname:
        in_seq_dir = os.path.join(origin_dir, fname)
        out_seq_dir = os.path.join(target_dir, fname)
        thread = threading.Thread(target=_echo2dbz, args=(in_seq_dir, out_seq_dir))
        threads.append(thread)
        # _echo2dbz(in_seq_dir, out_seq_dir)

    for thread in threads:
        ## thread.setDaemon(True)
        thread.start()




def _echo2dbz(in_seq_dir, out_seq_dir):
    print(in_seq_dir)
    color_dict = util.read_color()
    # origin_dir = os.path.join('data', directory)
    # target_dir = os.path.join('result', directory)
    if ~os.path.exists(out_seq_dir):
        os.makedirs(out_seq_dir)
    filenames = os.listdir(in_seq_dir)
    for filename in filenames:
        path = os.path.join(in_seq_dir, filename)
        img = Image.open(path)
        img = np.asarray(img, np.int)
        img_rgba = np.zeros((img.shape[0], img.shape[1], 4))
        img_dbz_value = (img - 20) * 1.0 / 2
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                key = min(int(img_dbz_value[i][j] * 2), 160)
                key = max(key , 0)
                img_rgba[i][j] = color_dict[key]
        path = os.path.join(out_seq_dir, filename)
        Image.fromarray(np.uint8(img_rgba)).save(path)