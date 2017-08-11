def read_json(infile):
    """read class groups from JSON file

    :param infile: input file (str)
    :return: class_groups (dict)
    """
    import json
    with open(infile, 'r') as f:
        class_groups = json.load(f)

    return class_groups


def read_csv(infile):
    """read class groups from CSV file

    :param infile: input file (str)
    :return: class_groups (dict)
    """
    import csv
    with open(infile, 'r') as f:
        c = csv.reader(infile)
        # FIX ME!!
        class_groups = ????

    return class_groups


def read_csv_numpy(infile):
    """read class groups from CSV file

    :param infile: input file (str)
    :return: class_groups (dict)
    """
    from numpy import loadtxt
    # COMPLETE ME!!

    return class_groups
