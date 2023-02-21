

buffer_len = 1
work_buffer = ''
nums = []


def words(n):
    s = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
         6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    return s.get(n)


with open('test.txt', 'r') as f:
    buffer = f.read(buffer_len)
    if not buffer:
        print('Файл пуст, пожалуйста выберите другой файл')
    while buffer:
        while '0' <= buffer <= '9':
            if '0' <= buffer <= '9':
                work_buffer += buffer
            buffer = f.read(buffer_len)
        if len(work_buffer) > 0:
            try:
                if int(work_buffer) % 2 != 0:
                    if int(work_buffer, 4) < 4096:
                        if work_buffer[len(work_buffer) - 3] == '2':
                            nums.append(int(work_buffer))
            except ValueError:
                work_buffer = ''
                buffer = f.read(buffer_len)
        work_buffer = ''
        buffer = f.read(buffer_len)
    if not nums:
        print('Нет подходящих цифр')
    else:
        print(nums)
        p = []
        for i in nums:
            a = ''
            for j in str(i):
                if j != '2':
                    a += j
            p.append(a)
        print('Цифры чисел без двоек:', *p)
        a = ''
        for i in str((max(nums) + min(nums)) // 2):
            a += words(int(i)) + ' '
        print('Среднее число между максимальным и минимальным:', (max(nums) + min(nums)) // 2, a)



