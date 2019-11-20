import argparse

from .populator import Populator


def main():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('--input', type=str, help='input file path')
    my_parser.add_argument('--template', type=str, help='template file path')
    my_parser.add_argument('--output-dir', type=str, help='output directory path')

    args = my_parser.parse_args()

    print('input= {}'.format(args.input))
    print('template = {}'.format(args.template))
    print('output_dir = {}'.format(args.output_dir))

    Populator().execute(input_file=args.input, template_path=args.template, output_dir_path=args.output_dir)


if __name__ == '__main__':
    main()