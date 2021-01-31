# encoding: GBK
from chat import chat
from public import variables
from system110 import system_1_1_0
from system120 import system_1_2_0
from chat import friend
n_z = variables.n_z


def judge():
    if variables.n_s[0] == 110:
        system_1_1_0.main_page()
    elif variables.n_s[0] == 120:
        system_1_2_0.main_page()


def chatroom_helper():
    h1 = input(
        '\n\n---------------------------------------------------------------------------------------------------------'
        '--------\n                                              �����Ұ�������                                         ����{}����'
        'Ϣδ��\n������1.����0�鿴δ����Ϣ(δ����)                                                              '
        '  ====\n     2.����1��'
        '��������������                                                                ====      ====\n     3.����2�鿴������'
        'Ϣ(δ����)        '
        '                                                ====  {}  ====\n     4.����3������ѽ���                        '
        '          '
        '                                 ====      ====\n     5.����4����system��ҳ��                                      '
        '         '
        '                     ====\n-----------------------------------------------------------------------------------'
        '------------------------------\n������:'.format(0, n_z[0]))
    if h1 == '0':
        print('\n��Чѡ��!')
        chatroom_helper()
        pass
    elif h1 == '1':
        variables.if_on = True
        chat.chat()
    elif h1 == '2':
        print('\n��Чѡ��!')
        chatroom_helper()
        pass
    elif h1 == '3':
        if n_z[0] == '  visitor ':
            print('\n��⵽���ο��˺�,�޷���Ӻ���!')
            chatroom_helper()
        else:
            print('Welcome!')
            friend_helper()
    elif h1 == '4':
        judge()
    else:
        print('\n��Чѡ��!')
        chatroom_helper()


def friend_helper():
    a = input('\n\n----------------------------------------------------------------------------------------------------'
              '----'
              '---------\n                                              friend����\n������1.����0���������Ұ�������                   '
              '                                                ====\n     2.����1������Ӻ��ѽ���                               '
              '                                 ====     ====\n     3.����2�鿴�ҵĺ���                                  '
              '       '
              '                      ==== {}  ====\n     4.����3ɾ������                                           '
              '                           ====     ====\n     5.����4����system��ҳ��                                        '
              '                           ====\n-----------------------------------------------------------------------'
              '------------------------------------------\n������:'.format(n_z[0]))
    if a == '0':
        chatroom_helper()
    elif a == '1':
        friend.find_friend()
    elif a == '2':
        friend.get_friend(2)
    elif a == '3':
        friend.delete_friend()
    elif a == '4':
        judge()
    else:
        print('\n��Чѡ��!')
    friend_helper()


if __name__ == '__main__':
    variables.n_z.append('  visitor ')
    chatroom_helper()
