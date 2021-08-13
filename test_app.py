import pytest
from app.controllers.functions import *


def test_validations_inside_mkad():
    assert validations_mkad('Rua são fidelis, recreio, rio das ostras, brasil') == 0


def test_validations_inside_mkad():
    assert validations_mkad('Rua são fidelis, recreio, rio das ostras, brasil') == 1