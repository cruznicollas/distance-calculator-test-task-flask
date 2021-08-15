import pytest
from application.controllers.functions import *


def test_get_location_destiny():
    assert get_location_destiny('Moscow Ring Road')

def test_invalid_characteres():
    assert get_location_destiny('Mos@ow R!ng Road')

def test_invalid():
    assert get_location_destiny('d54a6s5d1a32sd1a3da')