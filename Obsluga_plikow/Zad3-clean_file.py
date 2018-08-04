# lower count
# strip
with open('cleaned_emails.txt', 'w') as clean:
    with open("emails.txt", encoding='utf8') as f:

        for line in f:
            line = str(line).lower().strip()
            print(line)
            x = line.count('@')

            if x == 1:
                clean.write(line)
                clean.write('\n')
