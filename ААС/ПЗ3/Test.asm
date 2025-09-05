.model tiny
.code
org 100h
Begin:
mov ah, 9
mov dx, offset message
int 21h
ret
message db "Konstantin", 00h, 0Ah, '$'
end Begin