# Ping para Unix

def pingUnix(ip="8.8.8.8"):
    '''
    Faz ping no linux e captura resposta
    :param ip: endereço de ip para enviar ping
    :return: True ou False, caso consiga conexão
    '''
    import os
    response = os.popen(f"ping -c 5 {ip}").read()
    print(response)
    if "5 pacotes transmitidos, 5 recebidos" in response:
        return True
    else:
        return False

def pingWindows(ip="8.8.8.8"):
    """
    Faz ping no Windows e captura resposta
    :param ip: endereço de ip para enviar ping
    :return: True ou False, caso consiga conexão
    """
    import os
    ip = "8.8.8.8"
    response = os.popen(f"ping {ip}").read()
    print(response)
    if "Recebidos = 5" in response:
        return True
    else:
        return False