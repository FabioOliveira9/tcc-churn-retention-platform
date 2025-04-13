
def definir_acao_recomendacao(contrato, probabilidade_churn, possui_servicos, tenure):
    '''
    Define uma ação de retenção com base nas regras de negócio.
    '''
    if contrato in ['One year', 'Two year'] and tenure >= 10:
        if probabilidade_churn > 0.6:
            return "Oferecer 3 meses de desconto para renovação antecipada."
        else:
            return "Cliente com contrato longo e risco moderado. Manter acompanhamento."

    if contrato == 'Monthly':
        if tenure < 3:
            return "Não oferecer desconto. Monitorar engajamento nos próximos meses."
        elif probabilidade_churn > 0.6 and possui_servicos <= 2:
            return "Oferecer plano personalizado ou produtos complementares."
        elif probabilidade_churn > 0.6:
            return "Oferecer upgrade de plano com benefícios extras."
        else:
            return "Cliente mensal com baixo risco. Manter comunicação padrão."

    return "Manter estratégia atual e monitorar periodicamente."
