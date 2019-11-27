from .models import Word
from . import db

import xlrd


def cet4():
    book = xlrd.open_workbook('cet4.xls')
    sheet = book.sheet_by_index(0)

    columns = sheet.ncols
    rows = sheet.nrows

    for i in range(rows):
        for j in range(0, columns, 2):
            word = Word(word=sheet.cell(i, j).value,
                        translation=sheet.cell(i, j+1).value,
                        tag='cet4')
            db.session.add()
            try:
                db.session.commit()
            except:
                db.session.rollback()