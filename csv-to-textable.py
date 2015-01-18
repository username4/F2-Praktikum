#!/usr/bin/python2

# author: Michael Eliachevitch
import re # module for regular expressions, substitutions...

def csv_to_tex (filepath, newfilepath, seperator, use_commas=True):
    filestring = "\\begin{table}\n\\caption{}\n\\label{}\n\\begin{tabular}"
    filestring += "\\toprule \n"
    filestring += "% insert headerline here\n"
    filestring += "\\midrule \n"
    
    with open(filepath, "r") as infile:
        for line in infile:
            if (line.strip()[0] != "#"):
                if use_commas:
                    filestring += re.sub("\.", ",", re.sub("\n", r" \\\\"+"\n", re.sub(seperator, " & ", line)))
                else:
                    filestring += re.sub(",", ".", re.sub("\n", r" \\\\"+"\n", re.sub(seperator, " & ", line)))
    filestring +="\\bottomrule\n"
    filestring +="\\end{tabular}\n\\end{table}"
    with open(newfilepath, "w") as outfile:
        outfile.write(filestring)
        
csv_to_tex("FieldInhomogenities.txt","FieldInhomogenities.tex", " ")

    
