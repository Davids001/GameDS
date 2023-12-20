
def game_core_v3(number: int = 1) -> int:
# сделал по умолчанию, если цифру не ввели, компьютер сам рандомно закидывает число.
    if number == 1:
        import numpy as np
        number = np.random.randint(1, 101) 
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
# изначально количество попыток равно 0   
    count = 1
# создаем список контрольных точек.
    control_points= [0,25,50,75,100]
# длина необходима для определения отрезка, в котором находится наше загаданное число.
    length = range(len(control_points))
# запускаем цикл для определения крайних контрольных точек.
    for i in length:
        count += 1
        if control_points[i] < number:
            continue
# если контрольная точка меньше числа, то едем дальше по циклу и перешагиваем на след. точку.
        else:
            point_1 = control_points[i-1]
            point_2 = control_points[i]
            break
#зафиксировали контрольные точки, где находится наше число.
    point_0 = point_2
# крайнюю большую контрольную точку мы и берем за старт предположения загаданного числа.
# цикл, пока наша точка не будет равна загаданному число.
    while point_0 != number:        
        count += 1
#если загаданное число будет меньше чем наше предположение, то переменная n = нашей точке. необходимо для новой контрольной точки.      
        if number < point_0:
            n = point_0
#и наше новое предположение  уже будет равна половине отрезка между старым нашем предположением и крайней левой контрольной точки.
            point_0 -= abs((point_0 - point_1) // 2)
#иначе если загаданное число будет больше, чем наше предположение, то крайняя правая точка будет равна нашему предположению ранее.
        else:
            point_2 = n
            point_1 = point_0
# при этом наше новое предположение будет точка, которая находится посредине нового отрезка.            
            point_0 += abs((point_2 - point_0) // 2)
    print(count)        
    return count
# возвращаем результат и запускаем программу.
if __name__ == "__main__":
    # RUN
    game_core_v3()