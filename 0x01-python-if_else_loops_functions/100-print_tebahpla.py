#!/usr/bin/python3
case_flag = False
for i in range(122, 96, -1):
if case_flag:
	print(chr(i).upper(), end=" ")
else:
	print(chr(i), end=" ")

case_flag = not case_flag                  
