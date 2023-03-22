# Игра на клеточном поле
Задано квадратное поле размером (2n+1)*(2n+1) в клетках которой стоят целые числа от 
0 до 9, расставленные случайным образом.

Играют два игрока 1 и 2.
Ходы делаются по очереди. При очередном ходе выбирается клетка, примыкающая к 
последней выбранной (предыдущий ход соперника) по вертикали или горизонтали и 
число стоящее в этой клетке плюсуется к сумме уже набранной этим участником.
Игра заканчивается, когда при очередном ходе попали на границу поля или соперник не 
может сделать очередной ход. Победителем считается тот у которого сумма больше.
Первый ход делается в квадрат, ограниченный горизонталями от n-1 до n +1 и 
вертикалями от n-1 до n+1.

Задача: написать программу, которая играет в эту игру.
