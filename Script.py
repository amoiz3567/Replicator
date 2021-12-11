import main


statements = {
    ""
}

NMcommands = {
    ""
}


def scripts(read):

    commands = {
        "print": "print",
    }
    cmds     = ""
    
    for i in commands.values():
        cmds += i

    #region [ rgba(80, 50 ,10, 0.2) ]
    def syncCode(path):
        Code     = ""
        Finish   = ""
        filepath = path
    #endregion

        #region [ rgba(50, 50 ,10, 0.2) ]
        with open(filepath) as fp:
            line = fp.readline()
            cnt  = 1
            while line:
                if "//" in line:
                    line  = fp.readline()
                    cnt  += 1
                    pass
                else:
                    codeadd = ("{}:  {}\n".format(cnt, line.strip()))
                    print(codeadd)
                    
                    line     = fp.readline()
                    Code     = codeadd
                    Finish  += codeadd
                    cnt     += 1
                    Interpreter_Error_CodeTest(Code)
                    Language_Given_Instructions(Code)
                    Code_TypeAnalysis_Fundementalscmd(Code)
                    pass
            Error_Analysis(Finish)
            #endregion



    def Interpreter_Error_CodeTest(Code):
        Code
        #str(print(" returned code 0\n "))
        pass

    def Language_Given_Instructions(Code):
        if cmds in Code:
            if "(" in Code:
                if ")" in Code:
                    print("command: " + Code)
            else:
                print("Error: Print with no definition")
        pass

    def Code_TypeAnalysis_Fundementalscmd(Code):
        if '"' in Code:
            print("string : " + Code)
            print("string : " + Code.replace("\"", ""))
        else:
            return
        if "'" in Code:
            print("string : " + Code)
            print("string : " + Code.replace("\'", ""))
        else:
            return
        pass
    
    
    def Error_Analysis(Code):
        if cmds in Code:
            if not cmds in Code:
                print(" returned code 1\n  Looks like and Error occured: \n   " + Code)
            pass

    syncCode(read)
