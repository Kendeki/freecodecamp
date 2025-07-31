from random import sample
from copy import deepcopy

class Hat:
    def __init__(self, **balls):
        
        # Não preciso me preocupar com memória alocada sem necessidade,
        # pois Hat sempre é instanciada com pelo menos um elemento.

        self.contents: list[str] = []
        
        for color, quantity in balls.items():

            # Checagens no input para evitar problemas no código.
            # Não é necessário para esse projeto em si, apenas
            # cluí por apresentar boa prática.

            if type(quantity) != int:
                raise TypeError("Quantity must be an int.")
            elif color.startswith("__"):
                raise ValueError("Variable may not start with '__'.")
            elif not color.isidentifier():
                raise ValueError(f"Invalid syntax for attribute: {color}")
            elif hasattr(self.__class__, color):
                raise ValueError(f"Class {self.__class__.__name__} already contains attribute {color}")

            self.contents += [color for _ in range(quantity)]    

    def draw(self, num: int) -> list[str]:
        if len(self.contents) < num:
            removed_balls: list[str] = self.contents[:]

            for i in removed_balls:
                self.contents.remove(i)
            return removed_balls
        
        removed_balls: list[str] = sample(self.contents, num)
        
        for i in removed_balls:
            self.contents.remove(i)
        return removed_balls

def experiment(hat: Hat, expected_balls: dict[str, int], num_balls_drawn: int, num_experiments: int) -> float:
    num_successful = 0
    
    for _ in range(num_experiments):
        new_hat = deepcopy(hat)
        removed_balls = new_hat.draw(num_balls_drawn)
        removed_balls = {ball: removed_balls.count(ball) for ball in removed_balls}

        for ball in expected_balls.keys():
            success = True
            try:
                if removed_balls[ball] < expected_balls[ball]:
                    success = False
                    break
            except KeyError:
                success = False
                break

        if success:
            num_successful += 1

    return num_successful/num_experiments 