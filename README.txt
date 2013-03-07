Author: Nguyen Tran, nguyent_92@wpi.edu
Language: Python 2.5, 2.6, 2.7
Operating System: Ubuntu



--- DESCRIPTION ---
SMTP-SAUCE [Command line]: Base on SMTP-SOURCE, it sends emails through servers. The program add these following options:
- Emails can be a random size
- Attach a random file to email
- Create a log file 
- Measure the time to connect to the server, send emails, and disconnect.

SMTPCONF [Bash script]: Without having to edit the root files multiple times, it automatically logs in to the provided DynECT Email Delivery account and send emails using SMTP-SAUCE.



--- MANUALS ---
SMTP-SOURCE manual	: http://www.postfix.org/smtp-source.1.html
STMP-SAUCE manual 	: ./docs/Manual_smtp-sauce.txt
SMTPCONF manual		: ./docs/manual_smtpcof.txt



--- INSTALL / UNINSTALL ---

- Install SMTP-SAUCE. 
Run file <smtpadd/install>
$ sudo path-to-file/install

- Uninstall SMTP-SAUCE.
Run file <smtpadd/uninstall>
$ sudo path-to-file/uninstall



----------------------
The SMTP-SAUCE 's syntax is similar to SMTP-SOURCE

- When testing without attachments, it is recommended to use SMTP-SOURCE since it is faster than SMTP-SAUCE.
- SMTP-SAUCE should be use only when testing with attachments.
(see ./docs/comparison_chart.doc for more speed test information)

- You need to install SMTP-SAUCE to run SMTPCONF
- You can move SMTPCONF anywhere without harming any other files.



-------- EXAMPLES ------------
[Inside terminal]

- Man page
$ man smtp-sauce

- Send 10 emails to the destination, with random attachments in side "folder", record all actions in "log.txt" 
$ smtp-sauce -f fromaddress -t toaddress -m 10 -ra folder -log localhost:25

- Login to DynECT account "johnsmith", send 3 messages from "john@dyn.com" to "abcd@dyn.com" with a random attachment in the ~/music folder 
$ ./smtpconf johnsmith mypassword -m 3 -t abcd@dyn.com -f john@dyn.com localhost:25	
