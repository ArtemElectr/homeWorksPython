def info_competition(team1_num, team2_num, score1, score2, team1_time, team2_time):
    print('В команде Мастера кода участников %d!' % team1_num)
    print('Итого сегодня в командах участников: %d и %d!' % (team1_num, team2_num))

    print('Команда Волшебники данных решила задач: {}!'.format(score2))
    print("Волшебники данных решили задачи за {} c!".format(team1_time))

    print(f'Команды решили {score1} и {score2} задач.')

    if score1 >= score2 and team1_time < team2_time:
        challenge_result = 'Победа команды Мастера кода!'
    elif score1 <= score2 and team1_time > team2_time:
        challenge_result = 'Победа команды Волшебники данных!'
    else:
        challenge_result = 'Ничья!'

    print(f'Результат битвы: {challenge_result}')

    tasks_total = score1 + score2
    time_avg = round((team1_time + team2_time) / tasks_total, 1)

    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')


info_competition(6, 6, 40, 42, 1552.512, 2153.31451)






