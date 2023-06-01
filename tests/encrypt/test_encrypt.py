from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    expected = encrypt_message("testes", 3)
    assert expected == "set_set"

    expected = encrypt_message("testes", 4)
    assert expected == "se_tset"

    expected = encrypt_message("testes", 9)
    assert expected == "setset"

    with pytest.raises(TypeError):
        encrypt_message(1, 1)

    with pytest.raises(TypeError):
        encrypt_message("erro", "error")
