#! /usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
def checkdist():
        #���������ź�
        GPIO.output(2,GPIO.HIGH)
        #����10us����
        time.sleep(0.000015)
        GPIO.output(2,GPIO.LOW)
        while not GPIO.input(3):
                pass
        #���ָߵ�ƽʱ��ʱ��ʱ
        t1 = time.time()
        while GPIO.input(3):
                pass
        #�ߵ�ƽ����ֹͣ��ʱ
        t2 = time.time()
        #���ؾ��룬��λΪ��
        return (t2-t1)*340/2
def setup():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(2,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(3,GPIO.IN)
        time.sleep(2)
