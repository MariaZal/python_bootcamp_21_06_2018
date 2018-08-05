import re

text = """ 21 May 1995 Lorem ipsum dolor sit amet, consectetur adipiscing elit, 24 Oct 2003 sed 15 Jun 1991 do eiusmod tempor incididunt ut labore user-44@email.pl et dolore magna aliqua. Ut enim 02 Sep 2008 ad 09 Feb 1990 minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 24 Feb 2007 commodo consequat. Duis aute irure dolor in 59-996 reprehenderit in voluptate velit user-12@email.com esse cillum dolore eu user-19@email.gov.uk fugiat nulla pariatur. 15 Aug 1993 Excepteur sint occaecat 04 Dec 1990 cupidatat 58-950 non proident, sunt in culpa qui officia deserunt mollit 26 Feb 1996 anim id est 30-666 laborum.
Lorem ipsum dolor sit 14-113 amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad 22 Jan 1995 minim veniam, quis 02 Jun 1993 nostrud exercitation user-32@email.com ullamco user-78@email.pl laboris user-72@email.gov.uk nisi 84-979 ut aliquip ex 11 Apr 2001 ea user-46@email.pl commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse user-38@email.edu.pl cillum dolore user-88@email.gov.uk eu fugiat nulla 12 Nov 1994 pariatur. Excepteur sint occaecat cupidatat 75-254 non proident, sunt in culpa qui officia deserunt 34-738 mollit user-13@email.pl anim id est laborum.
30-579 Lorem ipsum 50-621 dolor sit amet, 28 Mar 1994 consectetur adipiscing elit, sed do eiusmod tempor 56-582 incididunt ut labore et dolore magna aliqua. Ut enim user-75@email.gov.uk ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip 31-335 ex ea commodo consequat. Duis aute irure 23-810 dolor in 04 Feb 2006 reprehenderit 25 Sep 1992 in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 12-157 occaecat cupidatat non proident, 92-961 sunt in 08 Aug 1990 culpa qui officia deserunt mollit anim id est user-92@email.gov.uk laborum.
Lorem ipsum dolor user-100@email.com sit amet, consectetur adipiscing user-58@email.pl elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 37-883 nisi ut aliquip ex user-99@email.edu.pl ea commodo consequat. 19 Feb 1995 Duis aute irure 73-149 dolor in reprehenderit in voluptate velit 28 Mar 1997 esse cillum dolore eu fugiat nulla pariatur. Excepteur 73-457 sint occaecat cupidatat non proident, sunt in culpa qui 12 May 1998 officia deserunt 11 Dec 1996 mollit anim 07 Oct 2004 id est laborum.
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed 31 Jul 2006 do eiusmod 05 Apr 1997 tempor incididunt ut labore et dolore magna aliqua. Ut 91-765 enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi 13 May 1993 ut user-14@email.gov.uk aliquip ex ea 51-314 commodo consequat. Duis aute irure dolor in reprehenderit 67-544 in user-54@email.com voluptate user-75@email.pl velit esse cillum dolore eu fugiat nulla pariatur. 26 Aug 2007 Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt user-65@email.pl mollit user-72@email.pl anim id 48-221 est laborum.
Lorem ipsum dolor sit user-22@email.edu.pl amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt 26 May 1994 ut labore et 28 Jul 1992 dolore magna aliqua. Ut enim ad minim veniam, 21-186 quis nostrud exercitation ullamco laboris nisi user-39@email.pl ut aliquip 18 Sep 1994 ex ea commodo consequat. Duis aute irure dolor 64-574 in reprehenderit in voluptate velit esse user-91@email.edu.pl cillum dolore eu fugiat nulla pariatur. Excepteur sint 65-842 occaecat cupidatat non user-49@email.pl proident, sunt in culpa qui officia 27 May 1993 deserunt mollit anim 45-639 id 63-244 est laborum.
Lorem ipsum dolor sit amet, 22 May 2003 consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 95-234 labore 13-859 et dolore magna aliqua. Ut enim 26-441 ad minim veniam, quis nostrud exercitation 15-240 ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure user-64@email.pl dolor in reprehenderit 55-131 in voluptate velit esse 51-921 cillum 75-708 dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 40-350 nisi ut aliquip ex ea commodo 16-646 consequat. Duis aute irure dolor in reprehenderit in voluptate velit 27 Oct 2003 esse cillum dolore 62-259 eu user-31@email.com fugiat nulla pariatur. Excepteur 36-776 sint 37-553 occaecat cupidatat 03 Sep 1998 non proident, sunt in user-62@email.gov.uk culpa qui officia deserunt mollit anim id est laborum.
Lorem ipsum dolor sit amet, consectetur adipiscing 08 Feb 2005 elit, sed do eiusmod tempor incididunt ut user-24@email.edu.pl labore et dolore magna aliqua. 01 Jun 2001 Ut enim ad minim 61-847 veniam, quis nostrud 30 Jul 2007 exercitation ullamco 19 Jun 1993 laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 14 Aug 2009 in reprehenderit in user-36@email.com voluptate velit esse cillum dolore eu user-69@email.pl fugiat nulla 19-830 pariatur. user-92@email.pl Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia 46-486 deserunt 12 Jan 2001 mollit 14-928 anim id 38-277 est laborum.
Lorem ipsum dolor sit amet, 14 Sep 1995 consectetur adipiscing elit, sed do eiusmod tempor 40-434 incididunt ut labore et user-92@email.pl dolore magna aliqua. user-31@email.com Ut enim 10-967 ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute 31-185 irure dolor 04 Jun 1995 in reprehenderit in voluptate velit 30 Dec 2003 esse cillum dolore user-20@email.pl eu fugiat 52-715 nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa user-14@email.edu.pl qui officia deserunt mollit anim id est laborum.
 """


sit_pattern = re.compile("\d{2} \w{3} \d{4}")
sit_pattern2 = re.compile("\d{2}\-\d{3}")
sit_pattern3 = re.compile("[\w\-._]+@[\w\-._]+\w+")
print(sit_pattern.findall(text))
print(sit_pattern2.findall(text))
print(sit_pattern3.findall(text))