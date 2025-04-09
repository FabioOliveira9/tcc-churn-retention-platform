
def definir_acao_recomendacao(dados_cliente, probabilidade):
    contrato_anual = dados_cliente.get("Contract_One_Year", 0) == 1 or dados_cliente.get("Contract_Two_Year", 0) == 1
    contrato_mensal = dados_cliente.get("Contract_One_Year", 0) == 0 and dados_cliente.get("Contract_Two_Year", 0) == 0
    meses = dados_cliente.get("Tenure_in_Months", 0)
    satisfacao = dados_cliente.get("Satisfaction_Score", 3)
    num_servicos = sum([
        dados_cliente.get("Streaming_Music", 0),
        dados_cliente.get("Streaming_TV", 0),
        dados_cliente.get("Premium_Tech_Support", 0),
        dados_cliente.get("Online_Backup", 0),
        dados_cliente.get("Device_Protection_Plan", 0),
        dados_cliente.get("Online_Security", 0)
    ])

    if contrato_anual and meses >= 10 and probabilidade >= 0.75:
        return "Oferecer 3 meses de desconto para renovação"
    elif contrato_mensal and meses >= 3:
        if satisfacao <= 2 and num_servicos <= 2:
            return "Sugerir readequação de plano ou produtos complementares"
        elif satisfacao >= 4 and num_servicos >= 4:
            return "Oferecer upgrade de plano com benefício"
        else:
            return "Enviar pesquisa para entender insatisfação"
    elif contrato_mensal and meses < 3:
        return "Não realizar ação de retenção — cliente ainda em fase inicial"
    else:
        return "Acompanhar comportamento — nenhuma ação imediata"
