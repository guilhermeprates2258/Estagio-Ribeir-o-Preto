def proximo_elemento():
    sequencias = {
        "a": "1, 3, 5, 7, ___ => 9",
        "b": "2, 4, 8, 16, 32, 64, ____ => 128",
        "c": "0, 1, 4, 9, 16, 25, 36, ____ => 49",
        "d": "4, 16, 36, 64, ____ => 100",
        "e": "1, 1, 2, 3, 5, 8, ____ => 13",
        "f": "2,10, 12, 16, 17, 18, 19, ____ => 20"
    }
    for key, value in sequencias.items():
        print(f"Sequência {key}: {value}")

proximo_elemento()
