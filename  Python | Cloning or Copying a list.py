{\rtf1\ansi\ansicpg1252\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Python program to copy or clone a list\
# Using the Slice Operator\
def Cloning(li1):\
	li_copy = li1[:]\
	return li_copy\
\
\
# Driver Code\
li1 = [4, 8, 2, 10, 15, 18]\
li2 = Cloning(li1)\
print("Original List:", li1)\
print("After Cloning:", li2)\
}