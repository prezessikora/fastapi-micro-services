from fastapi.testclient import TestClient
from app.main import app, db, MusicRecordsService
from app.warehouse.domain.MusicRecord import MusicRecord

client = TestClient(app)

# E2E
# Service
# Unit

# Products service tests

def test_products_version():
    response = client.get("/products/version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0"}


def test_products_get_by_sku():
    collection = db.movie
    inserted = collection.insert_one({
        "title": "Smash",
        "artist": "Nrivana",
        "stock": 100,
        "location": "43,13"
    })
    response = client.get(f'/products/sku/{str(inserted.inserted_id)}')
    assert response.status_code == 200

class MusicRecordsServiceMock:
    def find_music_record_by_id(self, product_id):
        return MusicRecord('','','','','')

# Unit - insert for real mongo instance we mock the data layer service
def test_products_get_by_sku_mock():
    app.dependency_overrides[MusicRecordsService] = MusicRecordsServiceMock

    response = client.get(f'/products/sku/012345678901234567891234')
    assert response.status_code == 200
    assert response.json() ==  {'artist': '', 'id': '', 'location': '', 'stock': '', 'title': ''}