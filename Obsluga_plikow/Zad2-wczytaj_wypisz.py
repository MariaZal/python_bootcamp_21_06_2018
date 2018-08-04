# import sys
#
# file = sys.argv[1]

# try:
with open("logs.txt", encoding='utf8') as f:

    last_login = {}
    total_time = {}
    for line in f:
        line2 = line.split(';')
        id = line2[0]
        action = line2[1]
        time = int(line2[2])

        if action == 'LOGIN':
            last_login[id] = time
        elif action == 'LOGOUT':
            session_time = time - last_login[id]
            total_time[id] = total_time.get(id, 0) + session_time
        else:
            continue


    print(total_time)


##ŁADNIE WYŚWIETL DANE


