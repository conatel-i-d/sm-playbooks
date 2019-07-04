import re
#texto = "Cisco IOS Software, C3560CX Software (C3560CX-UNIVERSALK9-M), Version 15.2(4)E2, RELEASE SOFTWARE (fc2)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2016 by Cisco Systems, Inc.\nCompiled Mon 27-Jun-16 09:08 by prod_rel_team\n\nROM: Bootstrap program is C3560CX boot loader\nBOOTLDR: C3560CX Boot Loader (C3560CX-HBOOT-M) Version 15.2(3r)E2, RELEASE SOFTWARE (fc2)\n\nSW_clienteDemo uptime is 6 days, 20 hours, 23 minutes\nSystem returned to ROM by power-on\nSystem restarted at 16:56:22 UTC Mon Jun 17 2019\nSystem image file is \"flash:/c3560cx-universalk9-mz.152-4.E2/c3560cx-universalk9-mz.152-4.E2.bin\"\nLast reload reason: power-on\n\n\n\nThis product contains cryptographic features and is subject to United\nStates and local country laws governing import, export, transfer and\nuse. Delivery of Cisco cryptographic products does not imply\nthird-party authority to import, export, distribute or use encryption.\nImporters, exporters, distributors and users are responsible for\ncompliance with U.S. and local country laws. By using this product you\nagree to comply with applicable laws and regulations. If you are unable\nto comply with U.S. and local laws, return this product immediately.\n\nA summary of U.S. laws governing Cisco cryptographic products may be found at:\nhttp://www.cisco.com/wwl/export/crypto/tool/stqrg.html\n\nIf you require further assistance please contact us by sending email to\nexport@cisco.com.\n\nLicense Level: ipbase\nLicense Type: Default. No valid license found.\nNext reload license Level: ipbase\n\ncisco WS-C3560CX-8PC-S (APM86XXX) processor (revision G0) with 524288K bytes of memory.\nProcessor board ID FOC2043Z3EA\nLast reset from power-on\n5 Virtual Ethernet interfaces\n12 Gigabit Ethernet interfaces\nThe password-recovery mechanism is enabled.\n\n512K bytes of flash-simulated non-volatile configuration memory.\nBase ethernet MAC Address       : 28:52:61:10:B1:00\nMotherboard assembly number     : 73-16471-05\nPower supply part number        : 341-0675-02\nMotherboard serial number       : FOC20433BVY\nPower supply serial number      : DCC203650S1\nModel revision number           : G0\nMotherboard revision number     : A0\nModel number                    : WS-C3560CX-8PC-S\nSystem serial number            : FOC2043Z3EA\nTop Assembly Part Number        : 68-5359-02\nTop Assembly Revision Number    : E0\nVersion ID                      : V02\nCLEI Code Number                : CMM1S10DRA\nHardware Board Revision Number  : 0x02\n\n\nSwitch Ports Model                     SW Version            SW Image                 \n------ ----- -----                     ----------            ----------               \n*    1 12    WS-C3560CX-8PC-S          15.2(4)E2             C3560CX-UNIVERSALK9-M    \n\n\nConfiguration register is 0xF"
texto = "Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE7, RELEASE SOFTWARE (fc1)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2013 by Cisco Systems, Inc.\nCompiled Mon 28-Jan-13 10:22 by prod_rel_team\nImage text-base: 0x00003000, data-base: 0x01900000\n\nROM: Bootstrap program is C2960 boot loader\nBOOTLDR: C2960 Boot Loader (C2960-HBOOT-M) Version 12.2(53r)SEY3, RELEASE SOFTWARE (fc1)\n\nSW-CDP-POE uptime is 1 week, 1 day, 39 minutes\nSystem returned to ROM by power-on\nSystem image file is \"flash:/c2960-lanbasek9-mz.122-55.SE7/c2960-lanbasek9-mz.122-55.SE7.bin\"\n\n\nThis product contains cryptographic features and is subject to United\nStates and local country laws governing import, export, transfer and\nuse. Delivery of Cisco cryptographic products does not imply\nthird-party authority to import, export, distribute or use encryption.\nImporters, exporters, distributors and users are responsible for\ncompliance with U.S. and local country laws. By using this product you\nagree to comply with applicable laws and regulations. If you are unable\nto comply with U.S. and local laws, return this product immediately.\n\nA summary of U.S. laws governing Cisco cryptographic products may be found at:\nhttp://www.cisco.com/wwl/export/crypto/tool/stqrg.html\n\nIf you require further assistance please contact us by sending email to\nexport@cisco.com.\n\ncisco WS-C2960-24LT-L (PowerPC405) processor (revision F0) with 65536K bytes of memory.\nProcessor board ID FOC1516W3S4\nLast reset from power-on\n2 Virtual Ethernet interfaces\n24 FastEthernet interfaces\n2 Gigabit Ethernet interfaces\nThe password-recovery mechanism is enabled.\n\n64K bytes of flash-simulated non-volatile configuration memory.\nBase ethernet MAC Address       : 88:F0:77:87:47:00\nMotherboard assembly number     : 73-12620-06\nPower supply part number        : 341-0267-02\nMotherboard serial number       : FOC15161731\nPower supply serial number      : DCA1512J03Y\nModel revision number           : F0\nMotherboard revision number     : A0\nModel number                    : WS-C2960-24LT-L\nSystem serial number            : FOC1516W3S4\nTop Assembly Part Number        : 800-32809-03\nTop Assembly Revision Number    : A0\nVersion ID                      : V08\nCLEI Code Number                : COMCT00ARE\nHardware Board Revision Number  : 0x02\n\n\nSwitch Ports Model              SW Version            SW Image                 \n------ ----- -----              ----------            ----------               \n*    1 26    WS-C2960-24LT-L    12.2(55)SE7           C2960-LANBASEK9-M        \n\n\nConfiguration register is 0xF"
exp = '^Cisco (.+) Software, (.+) Software.+?Version (\d\d\.\d[^,.]+).+$'
result = re.search(exp, texto, flags=re.DOTALL)
print('Plataforma:', result.group(2))
print('Sistema operativo:', result.group(1))
print('Version:', result.group(3))