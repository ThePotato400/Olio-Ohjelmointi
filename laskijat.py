class Laskija:
    """Luokka, joka toteuttaa eri laskutoimituksia.

    Julkiset metodit:
        summaa(Union[int, float], Union[int, float])
        kerro(Union[int, float], Union[int, float])
    """

    def summaa(self, *args):
        """Palauttaa annettujen lukujen summan.

        :param args: summan luvut
        :type args: Union[int, float]
        :return: annettujen lukujen summa
        :rtype: Union[int, float]
        """
        return sum(args)

    def kerro(self, *args):
        """Palauttaa annettujen lukujen tulon.

        :param args: tulon luvut
        :type args: Union[int, float]
        :return: annettujen lukujen tulo
        :rtype: Union[int, float]
        """
        tulo = 1
        for luku in args:
            tulo *= luku
        return tulo

class MonenLaskija(Laskija):
    """Luokka, joka perii luokan Laskija ja toteuttaa laskutoimituksia useammalle luvulle."""

    def summaa(self, *args):
        """Palauttaa annettujen lukujen summan.

        :param args: summan luvut
        :type args: Union[int, float]
        :return: annettujen lukujen summa
        :rtype: Union[int, float]
        """
        return super().summaa(*args)

    def kerro(self, *args):
        """Palauttaa annettujen lukujen tulon.

        :param args: tulon luvut
        :type args: Union[int, float]
        :return: annettujen lukujen tulo
        :rtype: Union[int, float]
        """
        return super().kerro(*args)

def argumenttien_tulostaja(**kwargs):
    """Tulostaa annetut avainsana-argumentit.

    :param kwargs: avainsana-argumentit
    """
    for avainsana, arvo in kwargs.items():
        print(f'Argumentin "{avainsana}" arvo on {arvo}.')

# Testaus
l = Laskija()
ml = MonenLaskija()

print(l.summaa(11, 31))
print(l.kerro(3, 12))
print()
print(ml.summaa(1, 2, 3, 4, 5))
print(ml.kerro(1, 2, 3, 4, 5))
print()
print(ml.summaa(1, 2, 3, 4, 5, 6, 7))
print(ml.kerro(1, 2, 3, 4, 5, 6 ,7))
print()
argumenttien_tulostaja(eka=42, toka='foo', kolmas=[0, 1, 2])
print()
argumenttien_tulostaja(nimi='Tero', ika=41, kaupunki='Turku', oppilaitos='TAI')
