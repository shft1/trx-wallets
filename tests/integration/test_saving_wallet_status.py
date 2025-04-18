import pytest

URL_WALLET = "/wallet/"


@pytest.mark.parametrize(
    "send_data, expect_data",
    [
        (
            {"address": "TYD4pB7wGzrBTV3KdfEb9nvNDXh"},
            "Value error, Неккоректный адрес кошелька!",
        ),
        (
            {"address": "V1kWGXJES9m8bnFpMSQ88eq3zUSpQ67AP"},
            "Value error, Адрес кошелька должен начинаться с 'T'!",
        ),
    ],
)
def test_saving_wallet_status_validation(client, send_data, expect_data):
    response = client.post(URL_WALLET, json=send_data)
    assert response.status_code == 422, (
        "Проверьте, что в адресе проверяется наличие заглавной буквы T в начале и "
        "что длина адреса равна 34 символам."
    )
    msg_data = response.json()["detail"][0]["msg"]
    assert msg_data == expect_data, (
        "Проверьте, что выводится корректное сообщение об ошибке: "
        f"'{expect_data}'"
    )


@pytest.mark.parametrize(
    "send_data, expect_data",
    [
        (
            {"address": "TV1kWGXJES9m8bnFpMSQ88eq3zUSpQ67AP"},
            {"bandwidth", "energy", "balance", "datetime"},
        ),
    ],
)
def test_saving_wallet_status(client, send_data, expect_data):
    response = client.post(URL_WALLET, json=send_data)
    assert response.status_code == 200, (
        "Проверьте, что POST запрос с валидным адресом возвращает 200 статус-код"
    )
    data = response.json()
    missing_keys = expect_data - set(data.keys())
    assert not missing_keys, (
        f"В ответе на корректный POST-запрос к эндпоинту `{URL_WALLET}` не "
        f"хватает следующих ключей: `{'`, `'.join(missing_keys)}`"
    )
