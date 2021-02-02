def solution(phone_book):
    phone_len = len(phone_book)

    phone_book.sort(key=lambda x: len(x))

    for i in range(phone_len - 1):
        for j in range(i + 1, phone_len):
            if (phone_book[j].startswith(phone_book[i])):
                return False

        return True