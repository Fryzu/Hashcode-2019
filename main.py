if __name__ == '__main__':
    import argparse
    import importlib
    import logging

    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser(description="Google Hashcode 2k19 - Pizza")
    parser.add_argument("--input", help='input file', default='a_example.in')
    parser.add_argument("--output", help='output file', default='a_example.out')
    parser.add_argument("--solver", type=str, default="simple")
    args = parser.parse_args()

    logging.debug("Program arguments: %s", args)
    solver = None

    try:
        solver = importlib.import_module('.'.join(["src", args.solver]))
    except ImportError:
        logging.error('Cant import solver')
        exit(1)

    solver = solver.Solver(args.input)
    solver.read_input(args.input)
    solver.solve()

    #solver.write(args.output)
