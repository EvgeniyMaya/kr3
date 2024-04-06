import os.path

from config import ROOT_DIR
from srs.utils import open_json_file, file_list, filter_operations, sort_operration, mask_operation_info, format_date,operation_to

TEST_PATH_OPERATIONS = os.path.join(ROOT_DIR, "tests", "file.json")


def test_filter_operations(list_with_dict):
    assert filter_operations(list_with_dict)[0] == {
        "id": 522357576,
        "state": "EXECUTED",
        "date": "2019-07-12T20:41:47.882230",
        "operationAmount": {
            "amount": "51463.70",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 48894435694657014368",
        "to": "Счет 38976430693692818358"
    }


def test_open_json_file(list_with_dict):
    assert open_json_file(TEST_PATH_OPERATIONS) == list_with_dict


def test_sort_operration(list_with_dict):
    assert sort_operration(filter_operations(list_with_dict))[0] == {'date': '2019-12-08T22:46:21.935582',
                                                                     'description': 'Открытие вклада',                                                                'id': 863064926,
                                                                     'operationAmount': {'amount': '41096.24',
                                                                                         'currency': {'code': 'USD',
                                                                                                      'name': 'USD'}},
                                                                     'state': 'EXECUTED',
                                                                     'to': 'Счет 90424923579946435907'}

def test_mask_operation_info(list_with_dict):
    assert mask_operation_info(list_with_dict[1]) == 'Visa Classic 683198** **** 7658 ->'
    assert mask_operation_info(list_with_dict[4]) == '->'
    assert mask_operation_info(list_with_dict[0]) == 'Счет **4368 '

def test_operation_to(list_with_dict):
    assert operation_to(list_with_dict[1]) == 'Счет **5229'

def test_format_date(list_with_dict):
    assert format_date(list_with_dict[1])== '19.08.2018'