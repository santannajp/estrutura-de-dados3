from loguru import logger

#print -> logger

logger.add("meu_app.log")

def soma(x, y):
    try:
        soma = x+y
        logger.info(f"voce digitou os valores corretos, parabens {soma}")
        return soma
    except:
        logger.critical("voce tem que digitar valores corretos")

soma(2, 3)
soma(2, 7)
soma(2, "3")
