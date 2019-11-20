import os
import pdfrw
import csv

from pdf_populator.commons.logger import Logger
from pdf_populator.commons.util import transpose_csv

TEMPLATE_DIR = os.path.join(os.getcwd(), "templates")
OUTPUT_DIR = os.path.join(os.getcwd(), "outputs")

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'


class Populator():
    """
    https://dzone.com/articles/creating-and-manipulating-pdfs-with-pdfrw
    http://www.blog.pythonlibrary.org/2018/06/06/creating-and-manipulating-pdfs-with-pdfrw/
    """

    def __init__(self) -> None:
        self.logger = Logger(__name__)

    def execute(self, input_file, template_path, output_dir_path):
        self.logger.info("Start populating pdf file ...")

        tmp_file = os.path.join(os.getcwd(), '.tmp.csv')
        transpose_csv(input_file, tmp_file)
        files = []
        with open(tmp_file, 'rt', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            # skip first row
            next(reader)

            for row in reader:
                file = dict()
                for key in row:
                    file[key] = row[key]
                files.append(file)

            for file in files:
                filename = file.get('Key value')
                if not filename:
                    self.logger.warn("File name not found. Skip")
                    continue

                self.logger.info('Generating file {}'.format(filename))
                output_path = os.path.join(output_dir_path, '{}.pdf'.format(filename))

                self._write_pdf(template_path, output_path, file)

    def _write_pdf(self, input_pdf_path, output_pdf_path, data_dict):
        template_pdf = pdfrw.PdfReader(input_pdf_path)
        annotations = []
        for page in template_pdf.pages:
            annotations.extend(page[ANNOT_KEY] or [])

        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    if key in data_dict.keys():
                        annotation.update(
                            pdfrw.PdfDict(AP=data_dict[key], V=data_dict[key])
                        )
        pdfrw.PdfWriter().write(output_pdf_path, template_pdf)