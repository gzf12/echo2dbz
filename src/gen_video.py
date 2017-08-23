import cv2
import os


def read_img(img_path, color):
    img12 = cv2.imread(img_path)
    img12 = cv2.resize(img12, (1164, 964))
    img12[0:5, 0:-200] = color
    img12[959:964, 0:-200] = color
    img12[:, 0:5] = color
    img12[:, 959:964] = color
    return img12


def gen_video():
    seq_idx = '441'
    pre0 = '/Users/GZF/OneDrive/workspace/echo2dbz/data/output/echo_map/' + seq_idx + '_gt'
    pre1 = '/Users/GZF/OneDrive/workspace/echo2dbz/data/output/echo_map/' + seq_idx + '_2layer'
    pre2 = '/Users/GZF/OneDrive/workspace/echo2dbz/data/output/echo_map/' + seq_idx + '_convlstm'
    pre3 = '/Users/GZF/OneDrive/workspace/echo2dbz/data/output/echo_map/' + seq_idx + '_highway'
    pre4 = '/Users/GZF/OneDrive/workspace/echo2dbz/data/output/echo_map/' + seq_idx + '_gt'

    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    video = cv2.VideoWriter()
    video_path = '/Users/GZF/OneDrive/workspace/echo2dbz/data/output/seq_' + seq_idx + '.avi'
    fps = 2

    video.open(video_path, fourcc, fps, (964 * 2 + 200, 964 * 2), True)

    g = [0, 255, 0]
    r = [0, 0, 255]

    for i in range(1, 11):
        img_path = os.path.join(pre0, 'gt' + str(i) + '.png')

        img12 = read_img(img_path, g)
        ims = cv2.resize(img12, (964 * 2 + 200, 964 * 2))

        ims[0:964, 0:964] = img12[0:964, 0:964]
        ims[0 + 964:964 + 964, 0:964] = img12[0:964, 0:964]
        ims[0:964, 0 + 964:964 + 964] = img12[0:964, 0:964]
        ims[0 + 964:964 + 964, 0 + 964:964 + 964] = img12[0:964, 0:964]
        ims[:, 964 * 2:] = cv2.resize(img12[:, 964:], (200, 964 * 2))

        video.write(ims)
    for i in range(11, 21):
        img_path = os.path.join(pre1, 'pd' + str(i) + '.png')

        img12 = read_img(img_path, r)
        ims = cv2.resize(img12, (964 * 2 + 200, 964 * 2))
        ims[0:964, 0:964] = img12[0:964, 0:964]

        img_path = os.path.join(pre2, 'pd' + str(i) + '.png')
        img12 = read_img(img_path, r)
        ims[0 + 964:964 + 964, 0:964] = img12[0:964, 0:964]

        img_path = os.path.join(pre3, 'pd' + str(i) + '.png')
        img12 = read_img(img_path, r)
        ims[0:964, 0 + 964:964 + 964] = img12[0:964, 0:964]

        img_path = os.path.join(pre4, 'gt' + str(i) + '.png')
        img12 = read_img(img_path, g)
        ims[0 + 964:964 + 964, 0 + 964:964 + 964] = img12[0:964, 0:964]

        ims[:, 964 * 2:] = cv2.resize(img12[:, 964:], (200, 964 * 2))
        video.write(ims)
    video.release()

if __name__ == '__main__':
    gen_video()
