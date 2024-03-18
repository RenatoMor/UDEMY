
#@ \r\n -> CRLF
#@ \n -> LF (Line Feed - Avança o cursor para a próxima linha)
#@ \r -> CR - (Carriage Return - Retorna o cursor para o início da linha)
#@ \t -> TAB - (Tabulação - Avança o cursor para a próxima tabulação)
#@ sep -> separador de valores - Padrão é o espaço, mas posso inserir o que eu quiser
#@ end -> finalizador - Padrão é o \n, mas posso inserir o que eu quiser

print(12, 34, 1011, sep=" ", end='#') 
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')
