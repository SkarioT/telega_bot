#работает, но только с линухой
from sh import ping

res = ping("-c", 3, 'yandex.ru')
print('res:\n',res)

