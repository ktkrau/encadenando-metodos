from Usuario import Usuario

elena = Usuario("Elena", "elena@detroya.com")
juana = Usuario("Juana", "juana@dearco.com")
ana = Usuario("Ana", "ana@bolena.com")

#Haz que el primer usuario haga 3 depósitos y 1 giro

elena.hacer_deposito(20).hacer_deposito(130).hacer_deposito(45).hacer_retiro(32).mostrar_balance_usuario()




#Haz que el segundo usuario haga 2 depósitos y 2 giros, y luego muestra sus balances
juana.hacer_deposito(134).hacer_deposito(23).hacer_retiro(21).hacer_retiro(57).mostrar_balance_usuario()




#Haz que el tercer usuario haga 1 deposito y 3 giros
ana.hacer_deposito(187).hacer_retiro(64).hacer_retiro(12).hacer_retiro(38).mostrar_balance_usuario()




#transferir

elena.transferir_dinero(12, ana)
print(elena.balance_cuenta)
print(ana.balance_cuenta)