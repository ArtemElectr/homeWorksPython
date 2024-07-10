from time import sleep


class UrTube:
    def __init__(self):
        self.current_user = None
        self.users = []
        self.videos = []

    def log_in(self, nickname, password):
        for user in self.users:
            if user == nickname and hash(password) == user.password:
                self.current_user = user
                break

    def register(self, nickname, password, age):
        is_exist = False
        for user in self.users:
            if user == nickname:
                print(f'Пользователь {user.nickname} уже существует')
                is_exist = True

        if not is_exist:
            self.users.append(User(nickname, password, age))

        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        for vid_ in video:
            if not self.__contains__(vid_):
                self.videos.append(vid_)

    def get_videos(self, row):
        list_ = []
        for video in self.videos:
            if video.__contains__(row):
                list_.append(video.title)
        return list_

    def __contains__(self, item):
        for video in self.videos:
            if video.title == item.title:
                return True
        return False

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for video in self.videos:
            if video.__eq__(title):
                if video.adult_mode and self.current_user < 18:
                    return print(f'Вам нет 18 лет, пожалуйста покиньте страницу')

                print(video.time_now)
                while video.time_now < video.duration:
                    sleep(1)
                    video.time_now += 1
                    print(video.time_now)
                print('Конец видео')
                video.time_now = 0


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __contains__(self, item):
        if self.title.lower().count(item.lower()):
            return True
        return False

    def __eq__(self, row):
        if self.title == row:
            return True
        return False


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, nick):
        if self.nickname is nick:
            return True
        else:
            return False

    def __lt__(self, age_limit):
        if self.age < age_limit:
            return  True
        else:
            return False

    def __str__(self):
        return f'{self.nickname}'


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')