import pytest
from gasoline.gasoline import(
    Gasoline,
    GasPortion,
    UnwantedGasolineMix,
)


class Benzine(Gasoline):
    pass


class Diesel(Gasoline):
    pass

class TestCreateBenzine:
    def test_create_benzine(self)->None:
        benzine = Benzine(octane=95)
        diesel = Diesel(octane=70)
        assert isinstance(benzine, Gasoline)
        assert isinstance(benzine, Benzine)
        assert isinstance(diesel, Gasoline)
        assert isinstance(diesel, Diesel)

def test_create_a_portion(self)->None:
    benzine95 = Benzine(octane=95)
    benzine98 = Benzine(octane=98)
    protion1 = GasPortion(
        gasoline = benine98,
        volume_liters=3.5,
    )

