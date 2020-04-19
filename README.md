# Compilers-HW2
Creates parse trees for declarative and assignment statements

### Authors
Gabriel Clark, Sassan Estrada

### Dependency Installation 
```
pip3 install pptree
```
### Execution
- Parse and print file(s) (for multiple files, separate file paths by spaces) to standard out:
  
  If no files are given, `exec()` will run on `input2.txt`.
  
  Must be using linux / macOS
```
  python3 main.py {{file(s)}} > outPutFileOfYourChoosing
``` 


# Documentation
### The Node Class
Each node class has a `grammarType` variable. For non-terminals, this `grammartype` specifies the rule being applied. For terminals, 
the `grammarType` becomes the token and lexeme. 

### The Parser Class
Uses the Recursive Descent method of parsing.

### pptree
Pretty prints a tree :)



   
