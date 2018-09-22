from pprint import pprint as pp


class Aircraft:
    def __init__(self, registration: str, model: str, num_rows: int, num_seats_per_row: int):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJK"[:self._num_seats_per_row])


class Flight:
    def __init__(self, number: str, aircraft: Aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))
        self._number = number
        self._aircraft = aircraft

        rows, seats = aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()


a = Aircraft("G-EUPT", "Airbus A380", num_rows=22, num_seats_per_row=6)

print(a.model())
print(a.registration())
print(a.seating_plan())

f = Flight("SN060", a)
print(type(f))
print(f.number())
print(f.aircraft_model())

pp(f._seating)
