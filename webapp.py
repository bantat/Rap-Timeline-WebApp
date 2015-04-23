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
        homepage = "Cannot read template file <tt>%s</tt>." % (homepage_filename)
    
    page_content = {}
    year_report = ""
    
    if year:
    	int_year = int(year)
    	difference = 2015 - int_year
    	string_difference = str(difference)
        year_report = "<p>The year you chose was %s.</p>\n" % (year)
        year_report += "<p>That was %s years ago.</p>\n" % (string_difference)
    year_report = indent(year_report, 1)
    page_content["results"] = year_report
    wiki_link = '<p>Interested in learning more about the year %s?\n' % (year)
    wiki_link += 'Follow this link to visit the wikipedia page for %s.\n' % (year)
    wiki_link += '<p><a href="en.wikipedia.org/wiki/%s"> %s </a></p>\n' % (year, year)
    wiki_link = indent(wiki_link, 1)
    page_content["links"] = wiki_link
    output_html = homepage.format(**page_content)
    print "Content-type: text/html\r\n\r\n",
    print output_html
    
def getCgiParameter():
    data = cgi.FieldStorage()
    parameter = {'year' : ''}
    if 'year' in data:
        parameter['year'] = data['year'].value
    return parameter

#Because the input that the user gives is predefined by the developers, there is no need to 
#sanitize inputs

def indent(s, k):
    return "\n".join([" "*(4*k) + line for line in s.splitlines()])

if __name__ == '__main__':
    main()