# A tool to parse the bcl2fastq demultiplex output 

## Usage 

``` shell
$python ./parseUnknow.py -h 

>usage: parseUnknow.py [-h] [-l BARCODE_LIB] [-r REPORT_HTML_FILE]

>Reveal Bcl2fastq's unmatched barcode

>optional arguments:
>  -h, --help            show this help message and exit
>  -l BARCODE_LIB, --barcode_lib BARCODE_LIB
>                        barcode library file
>  -r REPORT_HTML_FILE, --report_html_file REPORT_HTML_FILE
>                        bcl2fastq output report
```

Example 1: 

``` shell
$python ./parseUnknow.py -l ./nexteraXT_v2.txt -r ../OnePrimer/Reports/html/HVHWTAFXX/default/Undetermined/unknown/laneBarcode.html

CGAGGCTG:7022340
N710:7022340
CGTACTAG:7970660
N702:7970660
GGACTCCT:7869400
N705:7869400
CTCTCTAC:4766800
N707:4766800
TAGGCATG:3557540
N706:3557540
AAGAGGCA:6818900
N711:6818900
GTAGAGGA:3782020
N712:3782020
TAAGGCGA:13637920
N701:13637920
AGGCAGAA:13120040
N703:13120040
TCCTGAGC:3109220
N704:3109220

```

Example 2:

``` shell
$python ./parseUnknow.py -l ./nexteraXT_v2.txt -r ./Reports/html/HVHWTAFXX/default/Undetermined/unknown/laneBarcode.html 

GGACTCCT,TACTCCTT:4365580
N705,S507:4365580
AGGCAGAA,CTCCTTAC:3730220
N703,S505:3730220
TAAGGCGA,AGAGGATA:4408860
N701,S503:4408860
TAAGGCGA,TATGCAGT:4371140
N701,S506:4371140
GGACTCCT,AGGCTTAG:3418720
N705,S508:3418720
AAGAGGCA,AGAGGATA:4267560
N711,S503:4267560
TAAGGCGA,CTCCTTAC:4039780
N701,S505:4039780
CGTACTAG,TATGCAGT:3205340
N702,S506:3205340
CGAGGCTG,ATAGAGAG:3898940
N710,S502:3898940
AGGCAGAA,TACTCCTT:5230540
N703,S507:5230540
```
