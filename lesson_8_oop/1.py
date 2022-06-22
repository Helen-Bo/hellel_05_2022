from abc import ABC, abstractmethod


class User:
    def __init__(self, name, surname, age) -> None:
        self.name = name
        self.surname = surname
        self.age = age


class PaymentSystem(ABC):
    @abstractmethod
    def autorize(self, user: User):
        pass

    @abstractmethod
    def checkout(self):
        pass


class PayPal(PaymentSystem):
    def autorize(self, user: User):
        print(f"Autorize with PayPal. {user}")

    def checkout(self):
        print("checkout with PayPal")


class Stripe(PaymentSystem):
    def autorize(self, user: User):
        print(f"Autorize with Stripe. {user}")

    def checkout(self):
        print("checkout with Stripe")


class PaymentProcessor:
    def __init__(self, payment_system: PaymentSystem, user: User) -> None:
        self._payment_system = payment_system
        self._payment_system.autorize(user)

    def checkout(self):
        self._payment_system.checkout()


def quick_order(payment_processor: PaymentProcessor):
    payment_processor.checkout()


def shopping(payment_processor: PaymentProcessor):
    payment_processor.checkout()


def main():
    user = User(name="Jon", surname="Doe", age="20")
    paypal = PayPal()
    # stripe = Stripe()
    payment_processor = PaymentProcessor(paypal, user)

    shopping(payment_processor)
    quick_order(payment_processor)


if __name__ == "__main__":
    main()


class BaseUnit:
    pass


class Unit(BaseUnit):
    pass


class BaseAttackProcess(ABC):
    pass


class AttackProcess(BaseAttackProcess):
    def __init__(self, unit: Unit) -> None:
        self._unit = unit


class Protection:
    def __init__(self) -> None:
        self.config = ""


class Damage:
    def __init__(self) -> None:
        self.config = ""


class DamageProcessor:
    def __init__(self, attacker: Unit, protector: Unit, protection: Protection, damage: Damage) -> None:
        self.attacker: Unit = attacker
        self.protector: Unit = protector
        self.protection = protection
        self.damage = protection

    def calculate(self):
        print("...")


class HealthProcessor:
    def __init__(self, unit, reduce_protocol) -> None:
        self.unit = unit
        self.reduce_protocol = reduce_protocol

    def reduce_health(self):
        self.reduce_protocol.calculate()
