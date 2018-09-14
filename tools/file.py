import yaml,os
import xlwt
from my_framework.file_processing import file_process
class file_process():
    """封装操作excel的方法"""

    # 获取某一页sheet对象
    def create_excel_file(self):
        book = xlwt.Workbook(encoding = 'utf-8')
        self.sheet1 = book.add_sheet('Sheet1',cell_overwrite_ok = True)
        self.title = ['caseId','caseManageId','caseCode','id']
        file_path = os.path.dirname(os.path.abspath('.')) + '\config_file\est.yaml'
        excel_path = os.path.dirname(os.path.abspath('.')) + '\config_file\case_import'
        self.ecl = os.path.join(excel_path, "2.xls")
        i=0
        j=0
        k=0
        l=0
        fs = open(file_path, 'r', encoding="utf-8")
        lins = fs.readlines()
        for st in lins:
            if "caseId" in st:
                print(type(st))
                a=st.split(':')[1]
                b = a.rstrip(',')
                i=i+1

                self.sheet1.write(i,0,b)
            if "caseManageId"  in st:
                a = st.split(':')[1]
                b=a.rstrip(',')
                j = j + 1
                self.sheet1.write(i,1,b)
            if "caseCode" in st:
                a = st.split(':')[1]
                b = a.rstrip(',')
                k = k + 1
                self.sheet1.write(i,2,b)
            if "id_detail" in st:
                a = st.split(':')[1]
                b = a.rstrip(',')
                l = l + 1
                self.sheet1.write(i,3, b)
            if "id_more" in st:
                a = st.split(':')[1]
                b = a.rstrip(',')
                l = l + 1
                self.sheet1.write(i,4, b)
            else:
                pass
        book.save(self.ecl)
        fs.close()
if __name__ == '__main__':
    a=file_process()
    a.create_excel_file()

