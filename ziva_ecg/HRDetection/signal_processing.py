"""
signal_processing.py

Modularized signal processing commands for dealing with HR data
"""


def load_CSV(filename):
    """ Load CSV file from disk

    :param filename: Path to csv file location on disk
    :return data: (n x 2) Numpy array with time and voltage data
    """
    import numpy as np

    with open(filename) as filein:
        data = np.loadtxt(filein, delimiter=",", skiprows=1)
    t = data[:, 0]
    v = data[:, 1]
    return [t, v]


def BP_filter(t, v, f_low, f_high, order):
    """ Apply bandpass filter to the second column of input data
    Uses butterworth filter of the chosen order

    :param t: Time numpy array
    :param v: Voltage numpy array
    :param f_low: Low cutoff for filter
    :param f_high: High cutoff for filter
    :param order: Order of filter

    :return filt_v: Filtered data
    """
    from scipy.signal import butter, filtfilt

    fs = 1.0 / (t[1] - t[0])
    nyq = 0.5 * fs
    low = f_low / nyq
    high = f_high / nyq
    b, a = butter(order, [low, high], btype="bandpass")

    filt_v = filtfilt(b, a, v)
    return filt_v


def HP_filter(t, v, f_c, order):
    """ Apply highpass filter to the second column of input data
    Uses butterworth filter of the chosen order

    :param t: Time numpy array
    :param v: Voltage numpy array
    :param f_c: Cutoff for filter
    :param order: Order of filter

    :return filt_v: Filtered data
    """
    from scipy.signal import butter, filtfilt

    fs = 1.0 / (t[1] - t[0])
    nyq = 0.5 * fs
    cutoff = f_c / nyq
    b, a = butter(order, cutoff, btype="highpass")

    filt_v = filtfilt(b, a, v)
    return filt_v


def threshold_find_peaks(t, v, percentile=.9):
    """ Use a percentile-based threshold to find peaks

    :param t: Time numpy array
    :param v: Voltage numpy array
    :param percentile: (optional) Percentile 0-1 of data to use as the i
        threshold, default 0.9

    :return mask: Mask of peaks
    """
    import numpy as np
    import math

    sorted = np.sort(v)
    threshold = sorted[math.floor(percentile*len(sorted))]

    mask = v > threshold

    start = 0
    is_one = False
    for i, val in enumerate(mask):
        if val and (not is_one):
            start = i
            is_one = True
        elif is_one and (not val):
            for j in range(start, i + 1):
                mask[j] = False
            avg = math.floor((start + i)/2)
            mask[avg] = True
            is_one = False

    return mask


def display_trace(t, v, xlim=None, ylim=None, useMarkers=False, mask=None):
    """ Display time/voltage trace

    :param t: Time array
    :param v: Voltage array
    :param xlim: (optional) X limit of graph
    :param ylim: (optional) Y limit of graph
    :param useMarkers: (optional) Place markers on some data points (true/false)
    :param mask: (optional) Used with useMarkers to place points
    """
    import matplotlib.pyplot as plt
    import numpy as np

    if not xlim:
        xlim = t[[0, -1]]
    if not ylim:
        ylim = [np.min(v), np.max(v)]

    plt.plot(t, v)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (mV)')

    if useMarkers:
        plt.hold(True)
        plt.scatter(t[mask], v[mask])

    plt.show()


def calc_bpm(t, mask):
    """ Find beats per minute using average difference in peak times

    :param t: Time numpy array
    :param mask: Mask showing individual beats

    :return bpm: Beats per minute
    """
    import numpy as np

    bpm = 60/np.median(np.diff(t[mask]))
    return bpm


def calc_average_beat(t, v, mask, bpm):
    """ Average beats together

    :param t: Time numpy array
    :param v: Voltage numpy array
    :param mask: Mask showing individual beats
    :param bpm: Beats per minute

    :return avg_beat: Averaged heartbeat
    """
    import numpy as np
    import math

    fs = 1.0 / (t[1] - t[0])
    samples = int(math.floor(60 / bpm * fs / 2))

    avg_beat = np.zeros((2 * samples + 1, 1))
    count = 0
    for i in [i for i, val in enumerate(mask) if val == True]:
        cur = v[i - samples:i + samples + 1]
        if len(cur) == 2 * samples + 1:
            avg_beat[:, 0] += cur
            count += 1

    t_beat = range(0, 2 * samples + 1) / fs
    avg_beat /= count
    return [t_beat, avg_beat]


def verify_peaks_ncc(v, mask, template, thresh=0.9):
    """ Reject peaks with low NCC values based on a template

    :param v: Voltage numpy array
    :param mask: Mask showing individual beats
    :param template: Template to match using NCC
    :param thresh (optional): Threshold 0-1 for NCC, default 0.9

    :return mask_corrected: Averaged heartbeat
    """
    import numpy as np
    import math

    mask_corrected = np.copy(mask)
    samples = math.floor(len(template)/2)

    template = np.transpose((template - np.mean(template)) /
                            (np.std(template) * len(template)))

    for i in [i for i, val in enumerate(mask) if val == True]:
        cur = v[i-samples:i+samples+1]
        if len(cur) == 2 * samples + 1:
            cur = (cur - np.mean(cur)) / np.std(cur)
            ncc = np.sum(template * cur)
            if ncc < thresh:
                mask_corrected[i] = 0

    return mask_corrected
