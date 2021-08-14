import pytest
from app.controllers.functions import *


def test_validations_inside_mkad():
    assert validations_mkad('Moscow Ring Road') == 1

def test_get_location_destiny():
    assert get_location_destiny('Moscow Ring Road')
