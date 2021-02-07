from abc import ABCMeta, abstractmethod


class Beer(metaclass=ABCMeta):
    pass


class Snack(metaclass=ABCMeta):

    @abstractmethod
    def interact(self, beer: Beer) -> None:
        pass


class AbstractShop(metaclass=ABCMeta):

    @abstractmethod
    def buy_beer(self) -> Beer:
        pass

    @abstractmethod
    def buy_snack(self) -> Snack:
        pass


class Tuborg(Beer):
    pass


class Staropramen(Beer):
    pass


class Peanuts(Snack):

    def interact(self, beer: Beer) -> None:
        print('Мы выпили по бутылке пива {} и закусили его арахисом'.format(
            beer.__class__.__name__))


class Chips(Snack):

    def interact(self, beer: Beer) -> None:
        print('Мы выпили несколько банок пива {} и съели пачку чипсов'.format(
            beer.__class__.__name__))


class ExpensiveShop(AbstractShop):

    def buy_beer(self) -> Beer:
        return Tuborg()

    def buy_snack(self) -> Snack:
        return Peanuts()


class CheapShop(AbstractShop):

    def buy_beer(self) -> Beer:
        return Staropramen()

    def buy_snack(self) -> Snack:
        return Chips()


if __name__ == '__main__':
    expensive_shop = ExpensiveShop()
    cheap_shop = CheapShop()
    print('OUTPUT:')
    beer = expensive_shop.buy_beer()
    snack = cheap_shop.buy_snack()
    snack.interact(beer)
    beer = cheap_shop.buy_beer()
    snack = expensive_shop.buy_snack()
    snack.interact(beer)
