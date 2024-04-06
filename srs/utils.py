import json, os
import datetime as dt

a = os.path.abspath('operations.json')
file_list = os.path.join(a)


def open_json_file(file_path):
    with open(file_path, encoding="utf8") as file:
        return json.load(file)


def filter_operations(operation_data):
    filtered_list = []
    for operation in operation_data:
        if operation.get("state") == "EXECUTED":
            filtered_list.append(operation)
    return filtered_list


def sort_operration(operation_data: list[dict]) -> list[dict]:
    sor_list = sorted(operation_data, key=lambda x: x["date"], reverse=True)
    return sor_list


def mask_operation_info(operation):
    operation_from = operation.get("from")

    if operation_from:
        parts = operation_from.split()
        numbers = parts[-1]
        if len(numbers) == 16:
            masked_numbers = f"{numbers[:4]}{numbers[4:6]}** **** {numbers[-4:]}"
            return f"{" ".join(parts[:-1])} {masked_numbers} ->"
        else:
            return f"Счет **{numbers[-4:]} ->"

    return "->"


def operation_to(operation):
    operation_to = operation.get("to")
    if operation_to:
        parts = operation_to.split()
        numbers = parts[-1]
        return f"Счет **{numbers[-4:]}"


def format_date(operation):
    date: str = operation["date"]
    dt_time: dt.datetime = dt.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return dt_time.strftime("%d.%m.%Y")
