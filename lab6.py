# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 08:16:40 2017

@author: palkjaku
"""

def whiteLower(string):
    string = string.lower()
    string = string.replace(' ','')
    out = ""
    for i in string:
        if(ord(i) >= 97 and ord(i) <= 122): out += i

    return out
    
    
def cezar(text, move):
    text = whiteLower(text)
    out = ""
    for i in text:
        if((ord(i)+move) > 122):
            out += chr(97+(26-move))
        else:
            out += chr(ord(i)+move)
    return out.upper()
    
    
def deCezar(text, move):
    text = whiteLower(text)
    out = ""
    for i in text:
        if((ord(i)-move) < 97):
            out += chr(122-(26-move))
        else:
            out += chr(ord(i)-move)
    return out.upper()



def podstawieniowy(tekst, alfabet):
    tekst = whiteLower(tekst)
    print("wprowadzony: " + tekst)
    coded = ""
    for i in tekst:
        coded += alfabet[ord(i)-97]
    return coded

def dePodstawieniowy(kod, alfabet):
    kod = whiteLower(kod)
    normalAlpha = "abcdefghijklmnopqrstuvwxyz"
    decoded = ""
    for i in kod:
        index = 0
        for j in range(len(alfabet)-1):
            if(i == alfabet[j]):
                index = j
                break
            j += 1
        decoded += normalAlpha[j]
    return decoded


def zKluczem(tekst, klucz):



def main():
    
    #print(cezar("AGH",2))
    #print(deCezar(cezar("AGH",2),2))
    
    #print(podstawieniowy("ADV", "abqfszghljkimnovcretupwxyf"))
    #print(dePodstawieniowy("afp", "abqfszghljkimnovcretupwxyf"))
    
main()
            