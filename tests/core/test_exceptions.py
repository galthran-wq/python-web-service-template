from httpx import ASGITransport, AsyncClient
from pydantic import BaseModel
from src.main import app


class _DummyBody(BaseModel):
    value: int


@app.post("/_validate")
async def _validation_endpoint(body: _DummyBody) -> _DummyBody:
    return body


async def test_validation_error_format() -> None:
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post("/_validate", json={"value": "not_an_int"})
    assert response.status_code == 422
    data = response.json()
    assert "detail" in data
    assert isinstance(data["detail"], list)
    error = data["detail"][0]
    assert "loc" in error
    assert "msg" in error
    assert "type" in error
    assert "url" not in error
