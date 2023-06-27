'''Функции'''
import json

from .veriables import MAX_PACKAGE_LENGTH, ENCODING


def get_message(sock):
    '''
    Утилита приема и декодирования сообщения,
    принимает БАЙТЫ - выдает СЛОВАРЬ, если принято что-то другое, то выдает ошибку значения
    :param sock;
    :return:
    '''

    encoded_response = sock.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_message(sock, message):
    '''
    Утилита кодирования и отправки сообщения
    принимает СЛОВАРЬ и отправляет его
    :param sock:
    :param message:
    :return:
    '''

    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)