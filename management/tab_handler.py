# from menu import products
from .product_handler import get_product_by_id


def calculate_tab(command_table: list) -> dict:
    list_product_command = []
    sub_total = 0
    command_total = 0
    
    for command in command_table:
        for key, value in command.items():
            if key == "_id":
                # print(get_product_by_id(value))
                for key, value in get_product_by_id(value).items():
                    if key == "price":
                        sub_total = value
                        # print(sub_total)
            if key == "amount":
                list_product_command.append(round((sub_total * value), 2))
    
    for product_value in list_product_command:
        command_total = round((command_total + product_value), 2)
    
    return {"subtotal": f'${command_total}'}
