#!/usr/bin/python

glist_a = []
glist_b = []

def call_branch_a(a,b):
    pass

def call_branch_b(a,b):
    pass

def call_branch_c(a,b):
    del a[:]
    b.append(1)
    b.append(-1)

call_branch_a(glist_a,glist_b)
call_branch_b(glist_a,glist_b)
call_branch_c(glist_a,glist_b)

exit(sum(glist_a) + sum(glist_b))
