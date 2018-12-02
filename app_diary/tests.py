# from django.test import TestCase

# Create your tests here.
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "diary.settings")
django.setup()
from app_diary.models import student

def test_one():
    path = 'C:/Users/CyanZoy/Desktop/1/'
    dirs = os.listdir(path)
    for i in dirs:
        print(path+i[:-3])
        # newname = path + i[:-3]
        os.rename(path+i, path + i[:-3])


def test_two():
    import xlrd

    ExcelFile = xlrd.open_workbook('C:/Users/CyanZoy/Desktop/summary.xls')
    sheet = ExcelFile.sheet_by_name('Sheet 1')
    # print(sheet.name,sheet.nrows,sheet.ncols)
    rows = sheet.row_values(2)#第三行内容
    cols = sheet.col_values(1)#第二列内容
    stu = student()
    for i in range(2, sheet.nrows):
        stu.number, stu.name, stu.room, stu.politic_statue, stu.gpa_three, stu.sum_scores, stu.volunteer, \
        stu.behavoir_scores, stu.eng_scores, stu.phy_scores, stu.apply_type, stu.apply_grant_type \
            = [sheet.cell(i, j).value for j in range(1, sheet.ncols)]
        stu.save()


if __name__ == "__main__":
    test_two()