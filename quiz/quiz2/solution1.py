print '\n'.join(map(str, map(lambda i: "FuzzBuzz" if i % 15 == 0 else "Fuzz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i, range(1, 101))))

