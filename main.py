from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Данные о продуктах для примера
sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99
}

# Список всех продуктов
sample_products = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]

@app.get("/product/{product_id}")
async def get_product(product_id: int):
    # Поиск продукта по ID
    product = next((p for p in sample_products if p["product_id"] == product_id), None)
    
    # Если продукт не найден, возвращаем ошибку
    if product is None:
        return {"error": "Product not found"}
    
    return product

@app.get("/products/search")
async def search_products(keyword: str, category: Optional[str] = None, limit: Optional[int] = 10):
    # Фильтрация продуктов по ключевому слову и категории
    filtered_products = [p for p in sample_products 
                        if keyword.lower() in p["name"].lower() 
                        and (category is None or p["category"] == category)]
    
    # Возвращаем ограниченное количество результатов
    return filtered_products[:limit]