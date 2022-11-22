from menu import products

def get_product_by_id(id_product: int) -> dict:
    for product in products:
        product_key = [value for key, value in product.items() if key == "_id"]
        if product_key == [id_product]:
            return product
    
    return {}


def get_products_by_type(type_product: str) -> list[dict]:
    list_type = []

    for product in products:
        product_key = [value for key, value in product.items() if key == "type"]
        if product_key == [type_product]:
            list_type.append(product)

    if(len(list_type) == 0):
        return []

    return list_type

    

def menu_report() -> str:
    #CONTAGEM DE PRODUTOS
    contagem_de_produtos = len(products)


    #MÉDIA DOS PREÇOS
    valores_product = 0

    for product in products:
        for key, value in product.items():
            if key == 'price':
                valores_product += value

    preco_medio = round((valores_product / contagem_de_produtos), 2)


    #CONTAGEM DE TIPO MAIS COMUM
    list_type = []
    count_max = []
    tipo_mais_comum = ''
    
    ##RECRUTANDO TODOS OS TYPES
    for product in products:
        for key, value in product.items():
            if key == 'type':
                list_type.append(value)
    
    list_type_set = set(list_type)
    list_type_tuple = tuple(list_type)
    
    ##VERIFICANDO VALOR MÁXIMO
    for typer_count in list_type_set:
        count_max.append(list_type_tuple.count(typer_count))
    
    ##VERIFICANDO QUAL TYPE COM O COUNT MÁXIMO
    for typer in list_type_set:
        if list_type_tuple.count(typer) == max(count_max):
            tipo_mais_comum = typer


    return f'Products Count: {contagem_de_produtos} - Average Price: {preco_medio} - Most Common Type: {tipo_mais_comum}'


def add_product(menu: str, product: dict) -> dict:
    count_product_menu = len(menu)

    if count_product_menu > 0:
        product.update({"_id": count_product_menu + 1})
    else:
        product.update({"_id": 1 })
    
    menu.append(product)

    return product
