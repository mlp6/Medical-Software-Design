def rectify(signal):
    """rectify signal to be all positive

    :param signal: input signal from read_data()
    :returns: rectified_signal (np.array)
    """
    from numpy import abs

    signal = removeNans(signal)
    signal = removeInfs(signal)
    rectified_signal = abs(signal)


    return rectified_signal


def read_data(filename="test.asc"):
    """read in raw data from binary file

    :param filename: default = "test.dat"
    :returns: signal (np.array)
    """

    import numpy as np

    # from scipy.io import loadmat # v5 MAT files
    #import h5py # MAT v7.3 -> gzip compressed HDF5



    return signal


def find_peaks(rectified_signal):
    """

    """

if __name__ == "__main__":
    # DO SOMETHING
    pass
    find_peaks()
    rectify(signal)
    students_want_to_lpf()
    read_data()
    output_env()

def test_rectify_nan():
    from env_detect import rectify
    import numpy as np

    insig=np.array([50,150,NaN,300])
    rect_out=rectify(insig)
    assert np.array_equal([50,150,2,300])

    insig=np.array([50,150,2,NaN])
    rect_out=rectify(insig)
    assert np.array_equal([50,150,2,300])

    insig=np.array([NaN,150,2,300])
    rect_out=rectify(insig)
    assert np.array_equal([50,150,2,300])

    insig=np.array([NaN,NaN,NaN,NaN])
    rect_out=rectify(insig)
    assert np.array_equal([50,150,2,300])