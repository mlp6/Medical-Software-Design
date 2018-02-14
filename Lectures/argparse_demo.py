def main():
    """main demonstration function

    :returns: shoutout (string), p (float)
    """

    args = parse_cli()

    x = args.x
    y = args.y
    p = x*y

    if not args.noshoutout:
        shoutout = args.shoutout
    else:
        shoutout = ""

    return (shoutout, p)


def parse_cli():
    """parse CLI

    :returns: args
    """
    import argparse as ap

    par = ap.ArgumentParser(description="multiple 2 numbers and include in a shoutout",
                            formatter_class=ap.ArgumentDefaultsHelpFormatter)

    par.add_argument("--x",
                     dest="x",
                     help="first number",
                     type=float,
                     default=5.0)

    par.add_argument("--y",
                     dest="y",
                     help="second number",
                     type=float,
                     default=3.2)

    # note that type isn't specified since argparse will default to a str
    par.add_argument("--shoutout",
                     dest="shoutout",
                     help="shoutout message",
                     default="The product of your two numbers is")


    par.add_argument("--noshoutout",
                     dest="noshoutout",
                     help="suppress shoutout message printing",
                     action="store_true")

    args = par.parse_args()

    return args



if __name__ == "__main__":
    (shoutout, p) = main()
    print(shoutout + " %.2f." % p)
