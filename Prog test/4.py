class Name:
    def __init__(self, name) -> None:
        if name not in ["Богдан", "Volodia"]:
            raise ValueError("Дозволені імена: Богдан,Volodia")
        self.name = name

a = Name("Ладик")