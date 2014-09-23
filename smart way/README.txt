Description:                General Information about EDGAR Data 

WWW/FTP Problems E-mail:    webmaster@sec.gov

Anonymous FTP:              ftp.sec.gov 

Document Revision Date:     April 5, 2007


     Introduction
     ------------

Welcome to the Securities & Exchange Commission's FTP server for EDGAR
filings. The data in this system consists of electronic filings by
corporations and individual filers to the SEC. These filings are
disseminated to the public through the EDGAR Dissemination Service,
currently operated under contract to Keane Federal Systems, which
markets data directly to subscribers. See
http://www.sec.gov/info/edgar/ednews/dissemin.htm for more details and
contact information.

After early testing in 1992-93 beginning with 450 voluntary filers,
companies began filing through EDGAR in 1994-95 with various phase-in
periods for different form types. See Electronic Filing and the EDGAR
System: A Regulatory Overview
(http://www.sec.gov/info/edgar/regoverview.htm) for more details. 

For filings not available through EDGAR, paper versions are available
through the SEC Branch of Public Reference (email, publicinfo@sec.gov;
phone (202) 551-8090; fax, (202) 777-1030). See
http://www.sec.gov/info/edgar/ofis.shtml#access for more information.

To use anonymous FTP to access the EDGAR FTP server, use your File
Transfer Protocol software to connect to ftp.sec.gov and log in as
user "anonymous" with a password of your electronic mail address.  

To preserve equitable server access, we ask that bulk FTP transfer
requests are performed between 9 PM and 6 AM Eastern time.


     Using the EDGAR Index Files
     ---------------------------

The EDGAR indices are a helpful resource for FTP retrieval, listing
the following information for each filing: Company Name, Form
Type, CIK, Date Filed, and File Name (including folder path). 

Three types of indexes are sorted by these different data fields:

     company - sorted by company name
     form - sorted by form type
     master - sorted by CIK number

Indexes are located in the following folders according to time period
indexed:

     /edgar/daily-index - daily index files through the current year;
     previous year folders are available through 1994Q3

     /edgar/full-index - year folders contain quarterly indexes; other
     company, form, and master full indexes are compilations for the
     previous business day through the beginning of the current
     quarter.

The following archive formats are available:

     PKZIP compatible  - .zip extension (e.g., master.zip) 
     Macintosh StuffIt - .sit extension (e.g., master.sit) 
     UNIX compress     - .Z extension   (e.g., master.Z) 


     Notes on Directory Structure
     ----------------------------

Raw text filings can be accessed via the paths indicated in the
indexes, for example:

   /edgar/data/CIK/0123456789-AB-CDEFGH.txt 

Post-EDGAR 7.0 filings (after May 26, 2000) are also accessible via an
alternative symbolic path incorporating an intermediate folder named
by the accession number without dashes. All the documents submitted
for a given filing will be in this folder:

   /edgar/data/CIK/0123456789ABCDEFGH/0123456789-AB-CDEFGH.txt

Other documents that may be of interest:

   /edgar/data/CIK/0123456789ABCDEFGH/0123456789-AB-CDEFGH-index.htm
        (The HTML version includes hyperlinked table of submitted documents.)

   /edgar/data/CIK/0123456789ABCDEFGH/0123456789-AB-CDEFGH.hdr.sgml
        (The SGML header contents)

* Data folder -- Note that the /edgar/data folder will show as empty.
There are so many (tens of thousands) folders and files in this
directory that access is not allowed. You'll need to "leapfrog" over
the /data folder to include the subsequent CIK folder(s) (see below for
more).


     Getting the Actual Text Files
     -----------------------------

The following instructions relate to command-line ftp programs. Many
FTP users will use programs that have a graphical interface, but the
approach is similar and leapfrogging over the /data folder may still require
manual entry of a full folder path as indicated in the indexes. To start
with the indexes indicated above:

ftp> cd edgar/full-index
ftp> get company.idx 

If you are downloading compressed files, remember to switch to binary mode.

The indexes indicate the paths and names of the text files. For example, 
the index might contain the following file name and path:

/edgar/data/100334/0000100334-06-000121.txt

To retrive this file: 

ftp> cd edgar
ftp> cd data/100334/
ftp> get 0000100334-06-000121.txt


     Notes on Filings
     ----------------

Indexes are updated each evening for the current business day's
filings. Filing submissions that begin after 5:30 pm Eastern Time (10
pm for Ownership forms 3, 4, 5), will be disseminated the next
business day, showing up in the following day's index.

Filings are sometimes removed or corrected for a variety of reasons
at the filer's request including, but not limited to, the document was
submitted for the wrong filer, the document was a duplcate of a
previously filed document, the document in its current form was
unreadable, or the document contained sensitive information.
Corrections processed during a given business day will show up in the
index processed that evening. However, removals processed on
subsequent business days will not be reflected in any previous
indexes, hence a few filings will no longer be accessible at the
locations indicated in these indexes. 

Corrections are noted in the Feed directory - see below. 


     Feed and Oldloads Folders
     -------------------------

Feed - The Feed directory contains a tar'ed and gzip'ed archive file
(e.g., 20061207.nc.tar.gz; nc stands for non-cooked) for each filing
day. Each filing compressed in the tar is a separate filing submission
(without the binary feed header).

In addition, the Feed archive contains any corrections to previous
submissions. Each file is labeled with the SEC's unique accession
number and a label with the correction number. For example, the first
correction received that day for a particular file is labeled:

    0000950168-93-000089.corr01

Oldloads - Contains a concatenated copy of all filing submissions for
that day (e.g., 20061207.gz) complete with the binary filing header.
This is one single file with all the submissions concatenated
together.


     Documentation and Helpful Resources
     -----------------------------------------------

Descriptions of EDGAR Form Types:
http://www.sec.gov/info/edgar/forms/edgform.pdf. 

Content of specific forms:
http://www.sec.gov/about/forms/secforms.htm. 

Current EDGAR Filer Manual, XFDL and XML specs, and other
materials for EDGAR filers: http://www.sec.gov/info/edgar.shtml.

XBRL Interactive Data initiative:
http://www.sec.gov/spotlight/xbrl.htm.


    Contact
    -------

Questions? Send your query to webmaster@sec.gov. Note that we do not
offer technical support for developing or debugging scripted downloading
processes.
