from dataclasses import dataclass


@dataclass(frozen =True)
class player:
    name = str
    sign = str

    # def __int__(self, name: str, sign: str) -> None:
    #     self.name = name
    #     self.sign = sign



if __name__ == '__main__':
    player1 = "tobi",