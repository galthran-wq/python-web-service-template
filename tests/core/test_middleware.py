from httpx import AsyncClient


async def test_request_id_generated(client: AsyncClient) -> None:
    response = await client.get("/health")
    assert "x-request-id" in response.headers
    assert len(response.headers["x-request-id"]) > 0


async def test_request_id_preserved(client: AsyncClient) -> None:
    request_id = "test-request-id-123"
    response = await client.get("/health", headers={"x-request-id": request_id})
    assert response.headers["x-request-id"] == request_id
