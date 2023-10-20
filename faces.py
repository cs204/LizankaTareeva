def main ():
    s = input()
    sN = convert(s)
    print (sN)

def convert(s):
    """функция заменяет символ :) на эмодзи"""
    s = s.replace(":)", "\N{Slightly Smiling Face}")
    s = s.replace(":(", "\N{Slightly Frowning Face}")
    return s

main()