# -*- coding: utf-8 -*-

# Script Mapping for Devanagari

VowelMap =  [
            '\U00011183',
            '\U00011184',
            '\U00011185',
            '\U00011186',
            '\U00011187',
            '\U00011188',
            '\U00011189',
            '\U0001118A',
            '\U0001118B',
            '\U0001118C',
            '\U0001118D',
            '\U0001118E',
            '\U0001118F',
            '\U00011190',
            ]

SouthVowelMap = [
                '\U0001118D\U000111CC',
                '\U0001118F\U000111CC',
                ]

ModernVowelMap = [
                 '𑆃\U000111BE\U000111CB',
                  '𑆃\U000111BE\U000111CB\U000111B3'
                 ]

SinhalaVowelMap = [
                 '𑆃\U000111BE\U000111CB\u02BD',
                  ]

VowelSignMap =  [
                '\U000111B3',
                '\U000111B4',
                '\U000111B5',
                '\U000111B6',
                '\U000111B7',
                '\U000111B8',
                '\U000111B9',
                '\U000111BA',
                '\U000111BB',
                '\U000111BC',
                '\U000111BD',
                '\U000111BE',
                '\U000111BF',
                ]

SouthVowelSignMap = [
                '\U000111BC\U000111CC',
                '\U000111BE\U000111CC',
                    ]

ModernVowelSignMap =[
                 '\U000111BE\U000111CB',
                  '\U000111BE\U000111CB\U000111B3'
                    ]

SinhalaVowelSignMap = [
                 '\U000111BE\U000111CB\u02BD',
                      ]

AyogavahaMap = [
               '\U00011180',
               '\U00011181',
               '\U00011182'
               ]

ViramaMap =  [
             '\U000111C0'
             ]

ConsonantMap =  [
                '\U00011191',
                '\U00011192',
                '\U00011193',
                '\U00011194',
                '\U00011195',

                '\U00011196',
                '\U00011197',
                '\U00011198',
                '\U00011199',
                '\U0001119A',

                '\U0001119B',
                '\U0001119C',
                '\U0001119D',
                '\U0001119E',
                '\U0001119F',

                '\U000111A0',
                '\U000111A1',
                '\U000111A2',
                '\U000111A3',
                '\U000111A4',

                '\U000111A5',
                '\U000111A6',
                '\U000111A7',
                '\U000111A8',
                '\U000111A9',

                '\U000111AA',
                '\U000111AB',
                '\U000111AC',
                '\U000111AE',

                '\U000111AF',
                '\U000111B0',
                '\U000111B1',
                '\U000111B2'
                ]

SouthConsonantMap = [
                    '\U000111AD',
                    '\U000111AD\U000111CA',
                    '\U000111AB\U000111CA',
                    '\U000111A4\U000111CA'
                    ]

NuktaConsonantMap =  [
                     '\U00011191\U000111CA',
                     '\U00011192\U000111CA',
                     '\U00011193\U000111CA',
                     '\U00011198\U000111CA',
                     '\U0001119D\U000111CA',
                     '\U0001119E\U000111CA',
                     '\U000111A6\U000111CA',
                     '\U000111AA\U000111CA'
                     ]

SinhalaConsonantMap =[
                     '\U00011180\u02BD\U00011193',
                     '\U00011180\u02BD\U00011198',
                     '\U00011180\u02BD\U0001119D',
                     '\U00011180\u02BD\U000111A2',
                     '\U00011180\u02BD\U000111A7',
                      ]

NuktaMap = [
           '\U000111CA'
           ]

OmMap = [
        '𑆏𑆀'
        ]

SignMap =[
         '\U000111C1',
         '\U000111C5',
         '\U000111C6'
         ]

Aytham =[AyogavahaMap[2]+'\u02BD']

NumeralMap = [
             '\U000111D0',
             '\U000111D1',
             '\U000111D2',
             '\U000111D3',
             '\U000111D4',
             '\U000111D5',
             '\U000111D6',
             '\U000111D7',
             '\U000111D8',
             '\U000111D9'
             ]

from ... import GeneralMap as GM

GM.add_additional_chars(dict([(charlist, globals()[charlist]) for charlist in GM.CharmapLists]),
                        __file__.split('.')[0].split('\\')[-1])