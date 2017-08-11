def read_mat(infile):
    """read Matlab input

    :param infile: input file (str)
    :return: mat_dict
    """
    from scipy.io import loadmat
    d = loadmat(infile)

    return d

def read_hdf5(infile):
    """read HDF5 input

    :param infile: input file (str)
    :return: mat_file_ref
    """
    import h5py

    f = h5py.File(infile)

    return f
