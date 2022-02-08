# Objetos Próprios

class ContaCorrente:

  def __init__(self, codigo):
    self.codigo = codigo
    self.saldo = 0
  
  def deposita(self, valor):
    self.saldo += valor
  
  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)


conta_do_gab = ContaCorrente(15)
print(conta_do_gab)
conta_do_gab.deposita(500)
print(conta_do_gab)
conta_da_dani = ContaCorrente(32424)
conta_da_dani.deposita(1000)
print(conta_da_dani)
contas = [conta_do_gab, conta_da_dani]
for conta in contas:
  print(contas)

contas = [conta_do_gab, conta_da_dani, conta_do_gab]
print(contas[0])
conta_do_gab.deposita(100)
print(contas[0])
print(contas[2])

def deposita_para_todas(contas):
  for conta in contas:
    conta.deposita(100)
contas = [conta_do_gab, conta_da_dani]
print(contas[0], contas[1])
deposita_para_todas(contas)
print(contas[0], contas[1])

contas.insert(0,76)
print(contas[0], contas[1], contas[2])

#deposita_para_todas(contas)
#print(contas[0], contas[1], contas[2])
