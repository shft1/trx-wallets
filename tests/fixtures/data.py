from datetime import datetime

import pytest


@pytest.fixture
def create_wallet(mixer):
    mixer.blend(
        "app.models.WalletAddress",
        address="TV1kWGXJES9m8bnFpMSQ88eq3zUSpQ67AP",
    )
    mixer.blend(
        "app.models.WalletInfo",
        bandwidth=0,
        energy=0,
        balance=100.0,
        datetime=datetime.now(),
        address=1,
    )
