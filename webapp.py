#!/usr/bin/python
#-*- coding: utf-8 -*-


#webapp for software design

import cgi

def main():
    parameter = getCgiParameter()
    displayHomePage(parameter['year'],'homepage.html')
    
def displayHomePage(year, homepage_filename):
    try:
        f = open(homepage_filename)
        homepage = f.read()
        f.close()
    except Exception, e:
        hoempage = "Cannot read template file <tt>%s</tt>." % (homepage_filename)
    
    page_content = {}
    year_report = ""
    if year:
        year_report = "<p>The year you chose was %s.</p>\n" % (year)
        year_report += "<p>That was %s years ago.</p>\n" % (str(2015 - int(year)))
    year_report = indent(year_report, 1)
    page_content["results"] = year_report
    output_html = homepage.format(**page_content)
    print "Content-type: text/html\r\n\r\n",
    print output_html
    
def getCgiParameter():
    data = cgi.FieldStorage()
    parameter = {'year' : ''}
    if 'year' in form:
        parameter['year'] = form['year'].value
    return parameter

#Because the input that the user gives is predefined by the developers, there is no need to 
#sanitize inputs

def indent(s, k):
    return "\n".join([" "*(4*k) + line for line in s.splitlines()])

if __name__ == '__main__':
    main()