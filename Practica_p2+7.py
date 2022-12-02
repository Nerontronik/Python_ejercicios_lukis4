def http_error(status):
    print("*")
    match status:
        case 400:
            return "Solicitud incorrecta"
            print("*+")
        case 404:
            return "No encontrado"
            print("*++")
        case 418:
            return "Soy una tetera"
            print("*+++")
        case _:
            return "Algo anda mal en internet"
            print("*++++")
print(http_error(500))
            