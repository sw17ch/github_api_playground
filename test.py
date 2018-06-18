#!/usr/bin/python

glist_a = []
glist_b = []

def call_branch_a(a,b):
    glist_a.append(1)
    glist_b.append(-1)

def call_branch_b(a,b):
    pass

def call_branch_c(a,b):
    pass

call_branch_a(glist_a,glist_b)
call_branch_b(glist_a,glist_b)
call_branch_c(glist_a,glist_b)

exit(sum(glist_a) + sum(glist_b))
