from config import ROOT_DIR
from utils import open_json_file,filter_operations,format_date,mask_operation_info,operation_to,sort_operration
import os.path

PATH_OPERATIONS = os.path.join(ROOT_DIR,"srs", "operations.json")
def main():
    data=open_json_file(PATH_OPERATIONS)
    operations = filter_operations(data)
    operations = sort_operration(operations)[:5]

    for i in operations:
        print(format_date(i),i["description"])
        print(mask_operation_info(i),operation_to(i))
        print(i["operationAmount"]["amount"],i["operationAmount"]["currency"]["name"])
        print()
main()
