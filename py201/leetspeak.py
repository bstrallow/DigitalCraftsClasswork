def soLeet(para):
    para = para.upper()
    para = para.replace("A", "4")
    para = para.replace("E", "3")
    para = para.replace("G", "6")
    para = para.replace("I", "1")
    para = para.replace("O", "0")
    para = para.replace("S", "5")
    para = para.replace("T", "7")
    print para
para = raw_input('Enter a paragraph of text here: ')
soLeet(para)
