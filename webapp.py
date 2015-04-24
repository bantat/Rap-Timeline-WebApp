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
    wiki_link = ""
    year_options = ""
    year_list = [2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002, \
    2001,2000,1999,1998,1997,1996,1995,1994,1993,1992,1991,1990,1989,1988]
    
    if year:
    	int_year = int(year)
    	difference = 2015 - int_year
    	string_difference = str(difference)
        year_report = "<p>The year you chose was %s.</p>\n" % (year)
        year_report += "<p>That was %s years ago.</p>\n" % (string_difference)
        wiki_link = '<p>Interested in learning more about the year %s?\n' % (year)
    	wiki_link += 'Here is a link to the wikipedia page for %s:\n' % (year)
    	wiki_link += '<a href="http://en.wikipedia.org/wiki/%s"> Wikipedia </a></p>\n' \
    	% (year)
    	
    for item in year_list:
    	year_value = item
    	year_options += '<option value="%i">%i</option>\n' % (year_value, year_value)
    
    year_options = indent(year_options, 3)	
    wiki_link = indent(wiki_link, 1)
    year_report = indent(year_report, 1)
    
    page_content["options"] = year_options
    page_content["results"] = year_report
    page_content["links"] = wiki_link
    
    output_html = homepage.format(**page_content)
    print "Content-type: text/html\r\n\r\n",
    print output_html
    
def getCgiParameter():
    data = cgi.FieldStorage()
    parameter = {'year' : ''}
    if 'year' in data:
        parameter['year'] = sanitizeUserInput(data['year'].value)
    return parameter

def sanitizeUserInput(input):
    """Strips out scary characters from s and returns the sanitized version.
    """
    illegal_chars = ";,\\/:'\"<>@"
    for ch in illegal_chars:
        input = input.replace(ch, '')
    return input

def indent(s, k):
    return "\n".join([" "*(4*k) + line for line in s.splitlines()])

if __name__ == '__main__':
    main()