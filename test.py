#работает, но только с линухой
from sh import ping

res = ping("-c", 1, 'yandex.ru')
print('res:\n',res)