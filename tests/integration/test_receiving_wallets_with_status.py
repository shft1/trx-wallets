import pytest

URL_WALLET = "/wallet/"


@pytest.mark.usefixtures("create_wallet")
def test_receiving_wallets_with_status(client):
    response = client.get(URL_WALLET)
    data_json = response.json()
    expect_keys = {"items", "total", "page", "size", "pages"}
    missing_keys = expect_keys - set(data_json.keys())
    assert not missing_keys, (
        f"В ответе на корректный GET-запрос к эндпоинту `{URL_WALLET}` не "
        f"хватает следующих ключей: `{'`, `'.join(missing_keys)}`"
    )
