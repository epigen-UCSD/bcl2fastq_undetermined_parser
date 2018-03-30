#!/bin/python2
from HTMLParser import HTMLParser
import sys
import argparse

def read_barcodes(barcode_file):
    """ 
    input: i5/i7 barcode file
    return: a n dic  {index name:seq}
    """

    with open(barcode_file, "r") as fin:
        l = [row.strip("\n").split(" ") for row  in fin.readlines() if row.strip() != '']
    lf=filter(None,[i for j in l for i in j ]) #2d to 1d

    barcode_dic = {lf[i]:lf[i+1] for i in xrange(0,len(lf),2)}
    barcode_dic_rev={v:k for k,v in barcode_dic.items()}
    
    return barcode_dic, barcode_dic_rev


class BarcodeParser(HTMLParser):
    """
    html parser for the unknown barcode reports:
    1. find <h2>Top Unknown Barcodes</h2>
    2. parse the next table 
    3. Save barcode:number of reads into dictionary and return 
    """
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.found = False # found the correct h2 
        self.start = False # start recording  
        self.data=[]

    def handle_starttag(self,tag,attributes):
        if tag == 'td' and self.found :
            self.start = True
        if tag != 'td':
            self.start = False

    def handle_data(self,data):
        if data=="Top Unknown Barcodes":
            #print data
            self.found=True
        if self.start:
            self.data.append(data)
            

def parse_html(undetermined_html_file):
    """ 
    input: the undetermined barcode report html(eg../Reports/html/HVHWTAFXX/default/Undetermined/unknown/laneBarcode.html)
    output: a dic whose key is the unknow barcode seq and value is the number of reads
    """
    with open(undetermined_html_file, "r") as fin:
        html_doc  = fin.read().replace("\n","")

    # parse html 
    myParser= BarcodeParser()
    myParser.feed(html_doc)
    if len(myParser.data)%2!=0: sys.exit("error in the html file: unmatched barcode and count")

    # convert to dic barcode:cnt
    un_barcode_dic={key_to_tuple(k):0 for k in set(myParser.data[1::2])}
    
    for i in xrange(0,len(myParser.data),2):
        un_barcode_dic[key_to_tuple(myParser.data[i+1])]+=int(myParser.data[i].replace(",",""))
    
    return un_barcode_dic 

def key_to_tuple(k):
    return tuple(k.split('+'))

    return [(barcode_dic_rev[k[0]], barcode_dic_rev[k[1]], v) for k,v in un_barcode_dic.items()]


def parse_args():

    parser = argparse.ArgumentParser(description="Reveal Bcl2fastq's unmatched barcode ")

    parser.add_argument('-l','--barcode_lib',
                        help="barcode library file")

    parser.add_argument('-r','--report_html_file',
                        help="bcl2fastq output report")
    args = parser.parse_args()
    return args.barcode_lib,args.report_html_file

def main():

     # parse args
     lib,html = parse_args()

     # get the dic
     b_dic,b_dic_rev = read_barcodes(lib)

     # parse the html
     un_dic = parse_html(html)

     for k,v in  un_dic.items():
         if len(k)==1:
             print '{}:{}'.format(k[0],v)
             print '{}:{}'.format(b_dic_rev[k[0]],v)             
         else:
             print '{},{}:{}'.format(k[0],k[1],v)
             print '{},{}:{}'.format(b_dic_rev[k[0]],b_dic_rev[k[1]],v)             



if __name__ == '__main__':
        main()
