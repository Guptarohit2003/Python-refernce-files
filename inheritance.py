'''Scenario
Your task is to build a multifunction device (MFD) class consisting of methods responsible for document scanning, printing, and sending via fax.
The methods are delivered by the following classes:
scan(), delivered by the Scanner class;
print(), delivered by the Printer class;
send() and print(), delivered by the Fax class.
Each method should print a message indicating its purpose and origin, like:
'print() method from Printer class'
'send() method from Fax class'
create an MFD_SPF class ('SPF' means 'Scanner', 'Printer', 'Fax'), then instantiate it;
create an MFD_SFP class ('SFP' means 'Scanner', 'Fax', 'Printer'), then instantiate it;
on each object call the methods: scan(), print(), send();
observe the output differences. Was the Printer class utilized each time?'''


class Scanner:
    def scan(self):
        print('scanning')


class Printer:
    def print(self):
        print('printing')

class Fax():
    def send(self):
        print('sending')

    def print(self):
        print('printing from fax')

class MFD_SPF(Scanner, Printer, Fax):
    pass

class MFD_SFP(Scanner, Fax ,Printer):
    pass

print('Creating device following the order: Scanner, Fax, Printer')
mfd_sfp = MFD_SFP()
print('Device capabilities:')
mfd_sfp.scan()
mfd_sfp.print()
mfd_sfp.send()

print()
print('Creating device following the order: Scanner, Printer, Fax')
mfd_spf = MFD_SPF()
print('Device capabilities:')
mfd_spf.scan()
mfd_spf.print()
mfd_spf.send()
