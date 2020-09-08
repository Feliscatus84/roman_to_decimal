import i_o

mode = input("would you like to convert a file? Y/[N]: ")
if mode.upper() == "Y":
    i_o.read_from_file()
i_o.read_from_console()
