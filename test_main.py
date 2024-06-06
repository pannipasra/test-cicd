# ======================================================
# Test
# ======================================================
import os
import io
import pytest
from .main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}



def test_read_pong():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == "pong"


@pytest.fixture
def sample_files():
    with open("test_file1.txt", "w") as f:
        f.write("This is a test file 1")
    # Always yield the list of filenames
    filenames = ["test_file1.txt"]
    yield filenames
    # Cleanup after the test execution (optional)
    for f in filenames:
        os.remove(f)  # Import os if needed

def _file():
    name = "test_file1.txt"
    with open(name, "w") as f:
        f.write("This is a test file 1")
    yield [name]
    os.remove(name)  # Uncomment to delete the file


def test_upload_files():
    # Create an empty dictionary to store file data
    data = {}
    
    # Get filenames from _file()
    for filenames in _file():
        # Assuming each yield returns a list with one filename
        filename = filenames[0]
        # Simulate creating file content (replace with your actual content creation logic)
        file_content = f"Content for {filename}"
        # Prepare file data for upload (adjust filename/content type as needed)
        data["files"] = (filename, io.BytesIO(file_content.encode()), "text/plain")

    # Simulate API call with prepared file data
    response = client.post("/uploadfiles/", files=data)
    # Assertions
    assert response.status_code == 200
    data = response.json()
    print("_file()")
    print(_file())
    assert data == {"filenames": filenames}
