import uuid

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def generate_unique_sku():
    """Generate a unique SKU for testing to avoid conflicts between test runs."""
    return f"SKU-{str(uuid.uuid4())[:8]}"


def test_create_product():
    """Test POST /products creates a product."""
    sku = generate_unique_sku()
    response = client.post(
        "/products",
        json={
            "name": "Test Product",
            "sku": sku,
            "quantity": 10,
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Product"
    assert data["sku"] == sku
    assert data["quantity"] == 10
    assert "id" in data
    assert "created_at" in data


def test_list_products():
    """Test GET /products returns a list of products."""
    response = client.get("/products")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_product():
    """Test GET /products/{product_id} returns a single product."""
    sku = generate_unique_sku()
    create_response = client.post(
        "/products",
        json={
            "name": "Laptop",
            "sku": sku,
            "quantity": 5,
        }
    )
    product_id = create_response.json()["id"]

    get_response = client.get(f"/products/{product_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == product_id
    assert data["name"] == "Laptop"
    assert data["sku"] == sku
    assert data["quantity"] == 5


def test_get_product_not_found():
    """Test GET /products/{product_id} returns 404 for non-existent product."""
    response = client.get("/products/99999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Product not found"}


def test_update_product():
    """Test PATCH /products/{product_id} updates a product."""
    sku = generate_unique_sku()
    create_response = client.post(
        "/products",
        json={
            "name": "Original Name",
            "sku": sku,
            "quantity": 10,
        }
    )
    product_id = create_response.json()["id"]

    update_response = client.patch(
        f"/products/{product_id}",
        json={
            "name": "Updated Name",
            "quantity": 20,
        }
    )
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["id"] == product_id
    assert data["name"] == "Updated Name"
    assert data["sku"] == sku
    assert data["quantity"] == 20


def test_update_product_not_found():
    """Test PATCH /products/{product_id} returns 404 for non-existent product."""
    response = client.patch(
        "/products/99999",
        json={"name": "Updated"}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Product not found"}


def test_delete_product():
    """Test DELETE /products/{product_id} deletes a product."""
    sku = generate_unique_sku()
    create_response = client.post(
        "/products",
        json={
            "name": "To Delete",
            "sku": sku,
            "quantity": 1,
        }
    )
    product_id = create_response.json()["id"]

    delete_response = client.delete(f"/products/{product_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "Product deleted successfully"}

    get_response = client.get(f"/products/{product_id}")
    assert get_response.status_code == 404


def test_delete_product_not_found():
    """Test DELETE /products/{product_id} returns 404 for non-existent product."""
    response = client.delete("/products/99999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Product not found"}


def test_duplicate_sku_on_create():
    """Test POST /products returns 400 for duplicate SKU."""
    sku = generate_unique_sku()

    client.post(
        "/products",
        json={
            "name": "Product 1",
            "sku": sku,
            "quantity": 5,
        }
    )

    response = client.post(
        "/products",
        json={
            "name": "Product 2",
            "sku": sku,
            "quantity": 10,
        }
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "SKU already exists"}


def test_duplicate_sku_on_update():
    """Test PATCH /products/{product_id} returns 400 if new SKU already exists."""
    sku1 = generate_unique_sku()
    sku2 = generate_unique_sku()

    response1 = client.post(
        "/products",
        json={
            "name": "Product 1",
            "sku": sku1,
            "quantity": 5,
        }
    )
    product_id_1 = response1.json()["id"]

    client.post(
        "/products",
        json={
            "name": "Product 2",
            "sku": sku2,
            "quantity": 10,
        }
    )

    update_response = client.patch(
        f"/products/{product_id_1}",
        json={"sku": sku2}
    )
    assert update_response.status_code == 400
    assert update_response.json() == {"detail": "SKU already exists"}
