diskette_mb = 1.44
KB_in_bytes = 1024
MB_in_KB = 1024
diskette_bytes = diskette_mb * MB_in_KB * KB_in_bytes
pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4
total_chars = pages * lines_per_page * chars_per_line
book_size_bytes = total_chars * bytes_per_char
books_fit = int(diskette_bytes // book_size_bytes)

# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", books_fit)
