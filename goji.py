#!/usr/bin/env python
# -*- coding: shift_jis -*-
import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import subprocess

st.title("�N�ł��r�W�l�X�}��")
list_number = 0
list_data_before = []
list_data_aftar = []
sentence = ""

def main():
    ### SpradSheets����ǂݍ��� ###
    get_data = DataLoad()
    list_data_before = get_data[0]
    list_data_aftar = get_data[1]

    ### �Z���f�[�^�̌����擾 ###
    list_number = list_data_before.index(list_data_before[-1])

    ### text input ###
    sentence = st.text_area(label='���͓��͗�', value='�����ɕϊ����������͂����Ă�������')

    ### ���͏C�� ###
    sentence = TextConvert(list_data_before, list_data_aftar, list_number, sentence)

    ### text output ###
    st.write('�o�͗�\n\n', sentence)

def DataLoad():
    # �����܂�̕���
    # 2��API���L�q���Ȃ��ƃ��t���b�V���g�[�N����3600�b���ɔ��s�������Ȃ���΂Ȃ�Ȃ�
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    # �_�E�����[�h����json�t�@�C�������N���f���V�����ϐ��ɐݒ�B
    credentials = Credentials.from_service_account_file(
        R"C:\Users\jouza\Downloads\macro-mender-370900-a3fd26f71ed1.json", scopes=scope)
    # OAuth2�̎��i�����g�p����Google API�Ƀ��O�C���B
    gc = gspread.authorize(credentials)
    # �X�v���b�h�V�[�gID��ϐ��Ɋi�[����B
    SPREADSHEET_KEY = '1bI2obwUhSoJsm66YVTR481jYgOAFi7z5vVyvlr0hgUI'
    # �X�v���b�h�V�[�g�i�u�b�N�j���J��
    workbook = gc.open_by_key(SPREADSHEET_KEY)
    # �V�[�g�̈ꗗ���擾����B�i���X�g�`���j
    worksheets = workbook.worksheets()
    print(worksheets)
    # �V�[�g���J��
    worksheet = workbook.worksheet('�V�[�g1')

    ### �Z���f�[�^�ǂݍ��� ###
    list_data_before = worksheet.col_values(2)
    list_data_aftar = worksheet.col_values(3)

    ### �Z���̐擪���폜 ###
    list_data_before.pop(0)
    list_data_aftar.pop(0)

    return list_data_before, list_data_aftar

def TextConvert(list_data_before, list_data_aftar, list_number, sentence):
    ### ���������͖����� ###
    ### �甲�����t�̃`�F�b�N�͂ł��Ă��C�����ł��Ȃ�(�g�p���Ă���p�b�P�[�W�̎d�l��) ###

    ### sentence save to txt file ###
    f = open(R'C:\Users\jouza\textlint-demo\sentence.txt', 'w')
    f.write(sentence)
    f.close()
    ### �甲�����t ###
    ### �����݁A�`�F�b�N�̂ݏC���Ȃ� ###
    subprocess.run(["npx", "textlint", R"C:\Users\jouza\textlint-demo\sentence.txt", R"C:\Users\jouza\textlint-demo\.textlintrc"], shell=True)
    subprocess.Popen(["npx", "textlint", "--fix", R"C:\Users\jouza\textlint-demo\sentence.txt", R"C:\Users\jouza\textlint-demo\.textlintrc"], shell=True)

    ### text convert ###
    ### �Z���f�[�^�̌����J�E���^���񂵂� ###
    ### �Z�����X�g�̕ϊ��O���܂܂�Ăā@���@�ϊ��オ�܂܂�Ă��Ȃ���΁@�u���@ ###
    for count_list in range(list_number+1):
        if list_data_aftar[count_list] not in sentence and list_data_before[count_list] in sentence:
            sentence = sentence.replace(list_data_before[count_list], list_data_aftar[count_list])
    return sentence

if __name__ == '__main__':
    main()