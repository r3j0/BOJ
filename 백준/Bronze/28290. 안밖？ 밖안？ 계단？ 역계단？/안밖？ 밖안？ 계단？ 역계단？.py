oh = {
"fdsajkl;":"in-out",
"jkl;fdsa":"in-out",
"asdf;lkj":"out-in",
";lkjasdf":"out-in",
"asdfjkl;":"stairs",
";lkjfdsa":"reverse"
}

string = input().rstrip()
if oh.get(string): print(oh[string])
else: print('molu')