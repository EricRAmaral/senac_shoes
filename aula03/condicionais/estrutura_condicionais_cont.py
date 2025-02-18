# P I Z Z A R I A   S A B O R E S
# Calabresa, 4 queijos, Frango com Requeijão
# Se o cliente pedir uma pizza de calabresa, na sexta feira o refri é gratis
# Se o cliente pedr qualquer pizza no sábado, o frete é gratis
# Senão, informe ao cliente apenas que a pizza solicitada está sendo preparada

sabor_pizza = int(input(f"""
                    ========= 🍕 PIZZARIA SABORES 🍕 =========
                    Informe o sabor da sua pizza: 
                    1 - Calabresa
                    2 - 4 Queijos
                    3 - Frango com Requeijão
                    :  """))

dia_semana = "sexta"

if sabor_pizza == 1 and dia_semana == "sexta":
    print("✅ Parabéns, o refri hoje é por nossa conta.")
elif (sabor_pizza == 1 or sabor_pizza == 2 or sabor_pizza == 3) and dia_semana == "sabado":
    print("✅ Parabéns, o frete hoje é por nossa conta.")
else:
    print("🍕 A sua pizza está sendo preparada.")