# <a name="topp">Cyber Power Capstone</a>
### C1C Brett Martin
---
## Introduction

There are many purposes for constructing a journal like this on Github for my Capstone project.  For one, it offers me a way to neatly organize and document my progress so that anyone, myself included, can read it at any time and have a thorough understanding of where I'm and and all the places I've been in my search for answers.

Cyber Power, at least how I understand it, is an Industrial Control System (ICS) that emulates the USAFA power grid. The goal is to provide a means to holistically protect the power grid system from both physical and cyber threats to ensure a more robust, resilient, and flexible system overall. The hardware must be made safer and more reliable for consumers while the software must be hardened to ensure data integrity. At the time of writing this introduction, I've only had one full lab day to do actual work, so my knowledge about the project is severely limited. I'll make journal entries every lesson and will add information related to each aspect of the project to their own respective categories.

---
### Contents

- [**Fall Semester Journal**](#journal)
  - [M07 - Research Expectations](#m7)
  - [M08 - Hashgraph Algorithm Overview](#m8)
  - [M09 - Hashgraph Algorithm Research](#m9)
  - [M10 - Hashgraph Algorithm Programming](#m10)
  - [M11 - Hashgraph Hardware Implementation Considerations](#m11)
  - [M12 - Hashgraph Network Research](#m12)
  - [M13 - Hashgraph Network Research](#m13)
  - [M14 - Interfacing and Data Abstraction with Relays](#m14)
  - [M15 - Interfacing and Data Abstraction with Relays](#m15)
  - [M16 - Hashgraph Algorithm Simulation / Relay Data](#m16)
  - [M17 - Obtaining ASCII Data from Relays](#m17)
  - [M18 - Obtaining ASCII Data from Relays](#m18)
  - [M21 - Obtaining ASCII Data from Relays](#m21)
  - [M22 - Obtaining ASCII Data from Relays](#m22)
  - [M23 - Interfacing with Relays via Telnet and Python](#m23)
  - [M24 - Interfacing with Relays via Telnet and Python](#m24)
  - [M25 - Interfacing with Relays via Telnet and Python](#m25)
  - [M27 - Python-Relay Interfacing / New Hardware](#m27)
  - [M29 - New Hardware](#m29)
  - [M30 - Chairs](#m30)
  - [M32 - Comms Between Relay Nodes with Python Sockets](#m32)
  - [M33 - Comms Between Relay Nodes with Python Sockets](#m33)
  - [M35 - Comms Between >2 Nodes with Python Sockets](#m35)
  - [M36 - Comms Between >2 Nodes with Python Sockets](#m36)
  - [M37 - Plans to Implement Hashgraph](#m37)
- [**Spring Semester Journal**](#journal2)
  - [M01 - Creating Standard Image for Rasp Pis](#mm1)
  - [M02 - Creating Standard Image for Rasp Pis](#mm2)
  - [M03 - Defining the HG Algorithm](#mm3)
  - [M04 - Defining the HG Algorithm](#mm4)
  - [M05 - Defining the HG Algorithm](#mm5)
  - [M06 - Defining the HG Algorithm](#mm6)
  - [M07 - HG Algorithm Simulation V2](#mm7)
  - [M08 - HG Algorithm Simulation V2](#mm8)
  - [M09 - HG Algorithm Simulation V2](#mm9)
  - [M10 - HG Algorithm Simulation V2](#mm10)
  - [M11 - HG Algorithm Simulation V2](#mm11)
  - [M12 - HG Algorithm Simulation V2](#mm12)
  - [M13 - HG Algorithm Simulation V2](#mm13)
  - [M14 - HG Algorithm Simulation V2](#mm14)
  - [M17 - HG Algorithm Simulation V2](#mm17)
  - [M19 - HG Algorithm Simulation V2](#mm19)
- [**Overview/Terminology**](#overview)
- [**Hashgraph Algorithm**](#hg)
- [**Issue Tracker**](#issues)
- [**Other**](#other)

---
## <a name="journal">Fall Semester Journal</a>

#### 26 AUGUST 2019 (<a name="m7">M7</a>) :
Spent a great deal of time today researching the hashgraph algorithm, reading examples of how it works and seeing the different applications that it could be used for (which was mostly just for cryptocurrencies). I found an interesting article that explains virtually everything you need to know about the data structure and algorithms, to which I've included a link to below in the ["other"](#other) section. Also in the section is a link to a github repo in which someone created a working python implementation of the data structure and algorithms as well as a link to a Swirlds (company that owns Hashgraph) paper with tons of examples for how to use Hashgraph.

Additionally, Dr. Dudevoir had tasked me with three major things:
- **Research Hashgraph.** This includes contacting the company to find out how to use their SDK and searching for viable alternative solutions to the algorithm (like IBM Hyperledger fabric).
- **Research OpenPDC and MySQL.** Right now, there's only one computer (operating on Microsoft Windows 7) with control of the entire power system. The second computer, located in the left-most server rack and loaded with Windows 10, is not properly configured with OpenPDC and MySQL and cannot operate the power system at the present time. Set this up and consider ways to improve performance such as sampling on more relays and increasing the sample rate on each.
- **Figure out a good internet protocol for the data on each machine.** Excuse my lack of understanding of the terminology here. Ideally, Dr. Dudevoir would like for us to include other institutions such as ARL (Army Research Lab) and West Point in our Hashgraph algorithm (and to verify that they can remotely connect to and operate on our workstations from their locations).

Other things to consider would be connection issues with the Raspberry Pi and some sort of computer (Gimme a break, I don't know *all* of the terminology yet) and creating some sort of man-in-the-middle attack simulator on an FPGA using ethernet cables as the medium for data transfer.  Bring it on.  I aced ECE 383, after all.

Until then, continue to research!

*Quote of the day: "If you want to grant your own wish, then you should clear your own path to it."*

<br />

#### 28 AUGUST 2019 (<a name="m8">M8</a>) :
More Hashgraph research.  Going to try and program a hashgraph simulation in python to get a better understanding of it since I'm still a little shaky as to how it's actually supposed to work.  I think I get it for the most part, though.  I'll use the whitepaper from Swirlds and the one python implementation that I found last lesson as a starting point.  I'm not sure how much help the python implementation that I found will be, though, since it was designed for cryptocurrency applications.  We'll see!

After a TON of research on implementation of the hashgraph algorithm in a network, I was able to construct a program that will eventually become a hashgraph algorithm simulator. Currently, the program *hashgraph_sim.py* is set up with the following components:
- **HashGraphStruct**, an object that emulates the network or graph in which the algorithm takes place. It contains a list of all members or nodes within the network.
- **Member**, an object that emulated a user or member on the network. The Member object stores the name of the member, the list of event objects, and the signing key unique to each member. The functions contained in the Member class are **sign_event_func**, which hashes the byte-type event object; **verify_key_func**, which verifies that the event was signed by the appropriate owner; and **debug_member**, which outputs information about the Member object with the option of performing key verification tests.
- **Event**, an object containing information about each event in the graph to include the owner of the event, the list of transactions (which, in our case will probably involve database information from the relays such as current and voltage), a timestamp at which the event was created, and a list of hashes from each member that has created or received the event.
- **Transaction**, an object containing all transaction information as an array of values.

When the program executes, a network is created from the HashGraphStruct class and four unique Member objects are added to the network's *members* array. The program, at the current moment, will simply iterate through each member in the array and output it's debug information.  My next order of business will be to emulate events and randomize who each member sends the event to.

Lots of work ahead!

*Quote of the day: "Be yourself; everybody else is already taken." - Oscar Wilde*

<br />

#### 30 AUGUST 2019 (<a name="m9">M9</a>) :
Gonna start adding to the HashGraphStruct class today. I've already started on two functions titled *sampling_simulation_safe* and *sampling_simulation_corrupt* where events in the hashgraph will be generated, sent to other members, and verified with both safe and corrupt data, respectively. This will simply serve to verify that the hashed data in each event can be successfully verified by other members in the network.

After reading a bit further in Swirld's white paper for Hashgraph, I realized that I may have improperly implemented a few of the classes in my simulation program. Going to write some pseudocode so I can go back and re-implement everything properly.

Also, I need to talk to Dr. Dudevoir and Dr. Ciezki a little more in-depth about how the algorithm is expected to be implemented on the Phasor Data Concentrators. I think I have a pretty good idea, but a thorough conversation about it should yield some valuable information that will surely help me to implement the algorithm more effectively. Specifically, I need to know for sure what information will be going in/out of each PDC and what role each PDC has in verifying the integrity of data across the network (or the internet, for later on).

I'm done for the day, but I ran into an issue. I've made a note of the issue in the [**Issue Tracker**](#issues) section of the journal (which I *just* added now). I may have a fix for it, but it's about time for me to head out for the weekend. Will try and fix later. OH! And I fixed the issue with each member's keys so that they each produce their own unique keys. The previous method was a class attribute and not an instance one, so they key was the same for all members. It's a good thing I caught that--thank God for my debugging script!

Happy Parent's Weekend-- Oh, and Labor Day, too!

*Quote of the day: "If you’re in a war, instead of throwing a hand grenade at the enemy, throw one of those small pumpkins. Maybe it’ll make everyone think how stupid war is, and while they are thinking, you can throw a real grenade at them." - Jack Handey*

<br />

#### 04 September 2019 (<a name="m10">M10</a>) :
More hashgraph work. So far, I've added a new method to my *HashGraphStruct* class called *event_dump* that, as the name suggests, clears the entire event list for all members in a network.  I figured this would be especially useful for when my powershell console gets so cluttered with a plethora of events for each member that it makes it difficult to discern the data I'm looking for. From here, I plan on testing verification and hashing for events within the network before moving on to the actual gossip protocol and everything else that goes along with the Hashgraph algorithm.

Also, I seemed to have run into an issue with simulating corrupt events. I'll get into the nitty-gritty in the issue tracker below, but I've essentially ran into an issue where a byte-type string of characters is being appended to the corrupt member's event list instead of an Event-type object. Easy fix (hopefully).

Yup, easy fix. Now that I'm able to create and manipulate events in a graph, I'll consider possible next steps in the Hashgraph algorithm simulation next lesson.

*Quote of the day: "I don't trust anybody like I trust myself." - Donald Anderson*

<br />

#### 06 September 2019 (<a name="m11">M11</a>) :
Today was a huge learning day.  Spoke a great deal with Dr Dudevoir and LtCol Brieding about the power system layout (mostly the physical layout) and how the hashgraph algorithm would be implemented.

Had a bit of a crisis at the start of 3rd period, however.  I sat down with C1C Priaulx to talk about the layout of the relays, PDCs, and other networking equipment in our system to get a better understanding of how to implement the Hashgraph algorithm I've been working on. My understanding was a bit skewed.  I thought that each PDC would be equipped with an algorithm that would run on the overarching data structure, but apparently the idea is to have individual computers (RaspPis or virtual servers) for each relay that would operate on it's own private network, accesible by some sort of admin console. This is good. This makes things loads easier. With an individual node for each relay, implementing the algorithm will be as simple as installing openPDC on each computer attached to a relay (which I'll henceforth call a relay-node to clear up any future terminology mis-matches that might occur) and connecting each of them to a switch. This will require some engineering design processes that I learned about in the first few lessons of capstone.

I'll put my hashgraph simulation program on the backburner for the time being while I try and figure out how the hardware implementation will be created. If the hardware layout becomes clear, then creating the simulation should prove much easier.

My first step will be to create some decision matrices and parts lists for multiple variations and solutions to setting up the hashgraph network.  One such solution would involve using Raspberry Pis, a KVM, and a plethora of adapters to connect everything. Another would involve having one or two larger computers installed with VSphere or Microsoft Hyper-V to host virtual servers that would each act as a relay-node. Either way, another switch will likely have to be purchased (unless the old EdgeIron switch is still available for use).

Will continue to do more research in my engineering decision plan.

*Quote of the day: "Using quotes in an official email is actually poor etiquette." - TSgt Eric Williams, a quote attached to every single non-official email I've ever sent since I was an E-2*

<br />

#### 10 September 2019 (<a name="m12">M12</a>) :
Continuing with my engineering decision plan. I think I'll try to figure out exactly what hardware and software I need in orderto actually implement this. I spoke to Mr. Harris about VSphere licensing and he told me to email him so that he can find out whether or not the VSphere licenses are available for the Cyber Power capstone, as well. He also showed me all of the resources in the ACCR and in the Comm Squad cage that I have available to use if I need it, to include servers, switches, raspberry pi boards, and cables.

Spoke to C1C Seazzu about possible setup approaches for the hardware implementation.  After determining that the computers connected to the relays will be attached to a switch separate from the current one, a few good questions were raised.  Before I get to those, however, let's first list out the characteristics of the hashgraph algorithm:

- Several computers exist on a network and are able to create transactions.
- The transaction information is sent to random other nodes through a **gossip protocol**
- Other nodes can create transactions, too, and those are sent randomly through the network

This is where it gets interesting:
- The times for all of the transactions are recorded prior to being sent out via the gossip protocol
- A virtual voting algorithm will then determine when each transaction reached most of the network by averaging times for each transaction across all of the nodes. The consensus algorithm will determine if this order is correct.
- This is done by creating a graph structure that keeps track of who sends events to other members. Every member on the network has a copy of this graph.
- Each event contains a list of transactions, the time that the member claims that it was created, and a signature. The event also has two hashes: a cryptographic hash of the last event you made and the last one you received.

So, to sum it all up: In a hashgraph consensus algorithm, transactions are ordered by events, which are ordered by the consensus timestamp, which is the median time at which active members *received* an event.

Here's where I'm having difficulty understanding this:
- From my research, it's clear that the hashgraph algorithm cares a great deal about timestamps and the order in which events occur. Why does event order matter in a ICS environment?  Is it necessary or even worth investing time and money into?
- All computers in a decentralized network can maintain a ledger of all transactions that occur on each computer in copies of a graph structure. How does one prevent a MITM attack, then? I guess a better question would be: What does the network look like on a map of, say, a city? Would each relay connect to one switch? If that's the case, then who's to stop someone from intercepting data between that relay and the switch and altering it? 

It seems that normal encryption methods would work just as well in this case and that a hashgraph consensus algorithm might not be the proper application. Will continue to search for answers.

*Quote of the day: "All it takes for evil to triumph is for good men to do nothing." - Edmund Burke*

<br />

#### 12 September 2019 (<a name="m13">M13</a>) :
I've started the day with a series of questions from LtCol Breiding:
- What is the purpose of hashgraph? Is encryption required? Additionally, would a normal encryption method work instead of hashgraph?
- Can we do location-finding with hashgraph in the event of a man-in-the-middle attack?

Good questions, ma'am.

I think I've *finally* figured it all out, for the most part. Hashgraph will be used in this context not for event ordering like in a cryptocurrency application to avoid Sybil attacks, but rather to ensure that other relays in the network have the data that they need from a graph that's held by at least two-thirds of the rest of the network (Byzantine Fault Tolerance). This operates under the assumption that less than one-third of the nodes on the network can be influenced by an attacker at any given time. 

Encryption *is* required for digital signatures and hashing, but it won't be enough by itself if we want data redundancy, where the downed node will be provided with a graph of data containing correct data after it recovers. Though the Hashgraph whitepaper does not specify a certain method for signatures or hashing, I'll look into methods such as PGP or MD5 for each.

Location finding would, in fact be possible with this method, though it would be imperfect.  We would be able to discern which node is corrupt, but finding the exact channel through which an attacker was present would be extremely difficult.

Lastly, the topographical representation of the network here in the lab--which had given me a great deal of headache in trying to figure out as it applies to hashgraph--is much different than I had assumed.  Previously, I was under the assumption that all of the relays were connected by a single switch.  If that was the case, then the hashgraph algorithm would be pointless. Data would be sent from one relay, get intercepted before the switch, and disbatch incorrect data throughout the network. Rather, the switch is supposed to emulate a huge network with various connections and routers in such a way that multiple random routes can be taken from one node to another. This makes hashgraph possible.

My next step, I'd imagine, would be to determine exactly how to retrieve the data from each relay so that I can discern, sign, and send it with the hashgraph algorithm as part of a transaction.

*Quote of the day: "I don't have a favorite quote." - C1C Sears Schulz*

<br />

#### 16 September 2019 (<a name="m14">M14</a>) :
Tried to figure out how I'm going to interface with the relays to collect data from them.  Of course, using their ethernet ports is probably the best option, but when I attempted to access the OpenPDC console from the 2nd PDC, I was unable to authenticate and every possible combination of usernames and passwords I could find were incorrect. If I can find a way to interface with the relays without using OpenPDC, that would be ideal.  Right now, I can't access them at all.  While the RTAC is easily accessible through a web console, the relays don't seem to have such an interface.  A quick *netstat* revealed that the PDC I was working on was communicating with 192.168.20.11 (one of the relays) on port 4000-something--not one of the standard ports for any protocol I recognize.  I'll continue to investigate this.

Top priority right now is figuring out how to get data from the relays in a form that I can manipulate for implementation in the hashgraph struct.

*Quote of the day: ""You miss 100% of the shots you don't take." - Wayne Gretzky" - Michael Scott*

<br />

#### 18 September 2019 (<a name="m15">M15</a>) :
I started trying to figure out how openPDC and SQL Server are configured on our primary PDC, but with little success.  The number of applications that do seemingly nothing, like the openPDC console, make figuring out the configuration details super difficult. To make things worse, the PMU connection tester does not work on either PDC (Even after performing a clean install of openPDC on the second PDC).  I've submitted a trouble ticket with the Grid Protection Alliance in hopes that they might have a fix action.  Will continue to research fix actions until I hear back.

My primary goal is still to be able to collect data from the relays that I will be able to manipulate in python later on when I finally implement the hashgraph algorithm.

*Quote of the day: "No connection could be made because the target machine actively refused it." - openPDC*

<br />

#### 20 September 2019 (<a name="m16">M16</a>) :
Julian and Dustin were able to get me in contact with someone from SEL who should be able to point me in the right direction as far as data collection from the relays goes.  Ideally, I'd like to be able to collect raw data from the relays that I can easily manipulate in python.  From there, I should be able to implement the hashgraph algorithm on one of the relays to test its operability. Additionally, I heard back from the Grid Protection Alliance, whom I had contacted two days ago for help with setting up openPDC.  They seemed very open to helping me with my installation issue, but I'll wait to hear back from SEL about alternate methods for aggregating data from relays before I settle with configuring the computer with openPDC. Raw data would be ideal, but if I have to use openPDC in conjunction with a SQL database, that's fine--it'll just be more work.

It's a waiting game right now. Until I hear back from SEL, I'll continue to work on some of the paperwork for the project as well as the hashgraph simulation program I've been writing in Python.

Speaking of the algorithm, I may have to restructure it a little.  The graph will show which members sent what data at what time, but the overall idea of the algorithm is that each computer will store a copy of the graph in memory to reference with other computers.  I have a class for Members, but might have to create a separate class for the computer that the graph will be stored on.

I think I might need to take to the whiteboard for this.

Also, last thing: Since Dr. D isn't here today, I need to remember to ask what parts of the hasgraph algorithm created for cryptocurrency applications should be applied to our microgrid.  This will already be a heavily modified version of the algorithm, so I need to determine which aspects can be changed or removed entirely.  For instance, does this algorithm care what time the transactions took place?  How is this graph constructed given the sample data? 

It should be noted that the simulation program does not emulate the hashgraph algorithm in its current state.  The program--as it stands right now--only really accomplishes the goal of being able to successfully generate data, add it to an event list, encrypt it, send it, and decrypt it.  It also allows for data to be manipulated to see whether or not it will go undetected by the receivers.

*Quote of the day: "It may interest you to know that most Canadians in (the year) 2036 are some of the most efficient, ruthless and dangerous people I know. God help Quebec." - John Titor*

<br />

#### 24 September 2019 (<a name="m17">M17</a>) :
Finally heard back from someone at SEL (Sam Womack) about how to pull raw data from the relays.  Apparently, you can telnet into the relay through port 23 using PuTTY and scrape the raw ascii data from it using Python.  This will be my approach.  I've received permission from Mr Harris to use the CanaKits in the ACCR (raspberry pi kits), along with any of the adapters/hardware in there.  I've already set up one of the pi's behind the server rack and have replaced the PDC connection to the KVM with the Pi.  All I have to do is install Raspbian to the computer and connect the pi to the second ethernet port on the relay and I'll be able to interface with it, hopefully.

Just waiting on installs for now!

*Quote of the day: "Any officer who goes into action without his sword is improperly dressed." - Mad Jack Churchill*

<br />

#### 26 September 2019 (<a name="m18">M18</a>) :
Worked mostly on slides today for our presentation on Monday. All the while, I began installing dependencies on the Raspberry Pi and connected it to relay 451-A (IP 192.168.20.14).  GDK apparently takes an enormous amount of time to download, so I'll probably have to wait until next week before I can actually do anything useful on the machine.

Okay, so the dependencies are mostly installed (CAIRO, ATK, GDK, GLIB, Pango, and gdk-pixbuf).  After that, I'll try configuring PuTTY so I can test my connection to the relay.  A quick ping, however, revealed that I was, in fact, able to talk to the relay.  I ran a quick traceroute to see whether the connection was being made from the router or directly via the ethernet cable and it appears that the connection is being made over ethernet--ideal!

Next lesson is the presentation day.  If I have time after the presentation, I'll try to finish installing those dependencies so I can finally PuTTY into the relay via Telnet.

*Quote of the day: "I am the master of my fate. I am the captain of my soul." - William Ernest Henley*

<br />

#### 04 October 2019 (<a name="m21">M21</a>) :
Spent M19 and M20 presenting and working on the technical document.  Will upload the doc to this repo after finishing this entry.

After installing all of the required dependencies, I was finally able to run PuTTY on the RaspPi I connected to relay 451-A. With PuTTY, I was able to establish a connection to the relay via Telnet over port 23. After doing so, I came up with a prompt screen that I had never seen before. I tried a few common shell commands, but none of them worked. I then scoured the [*user manual*](/451-5_400_IM_20190731-20181115.pdf) for instructions on how to interact with the relay and found a few pages worth of commands.  None of the commands worked, however, because I kept receiving the error *"invalid access level"*. I proceeded to search through the manual once more and found a series of commands to elevate my access level (since they can only be elevated one level at a time). After a bunch more troubleshooting, I was then able to display the relay information using the *target* command.

The steps for accessing and viewing data on a relay from the RaspPi is as follows:
 - Launch the terminal and enter the command *putty* and press **ENTER**
 - From the PuTTY Configuration console, enter the relay IP address into the **Host Name** field, select *Telnet* for **Connection Type**, and click the **Open** button
 - A separate terminal window should appear with the prompt 
    *TERMINAL SERVER*
    *=*
 - Type *ACCESS* and press **ENTER**
    When prompted for a password, use **OTTER**
 - Type *2AC* and press **ENTER**
    When prompted for a password, use **TAIL**
 - Use the command *TARGET* to view the current and voltage values for the relay
   
From here, I will continue to try and pull the data from the relay somehow.  If I can extract this ASCII data into a file, that would be ideal.  There already appears to be a command called *FILE* in the 451 manual, so I'll try to figure out how to get that working next time.

*Quote of the day: "Save the whales. Collect the whole set." - Colonel David Caswell*

<br />

#### 08 October 2019 (<a name="m22">M22</a>) :
Today was the ethics lesson, so I had less time than usual to work in the lab. I spent a great deal of time testing the *TRIGGER* function on the relay over Telnet.  Additionally, I discovered thet the *HELP* function will spit out all the information related to certain commands, much like the *man* function in UNIX.  With this, I was able to derive a bunch of information related to the *FILE* command, which I believe I will have to use in order to pipe the information from the *TRIGGER* command to the RaspPi in ascii form so I can store it in the Hashgraph algorithm.

Will continue to figure out how to export this data.

*Quote of the day: "Don't take counsel of your fears or naysayers!" - Colin Powell*

<br />

#### 10 October 2019 (<a name="m23">M23</a>) :
Someone from SEL just informed me that using the *TRIGGER* command writes data to flash memory and should not be used frequently. Oops.  Good to know, I guess. He also informed me that there's another command called *MET* which takes metering data from the relay--pretty much exactly what I need for the hashgraph algorithm--and outputs it to the screen without writing it to a file. How ideal.  

Oh, and there's more good news: There's a python library called [*telnetlib*](https://docs.python.org/3/library/telnetlib.html) which allows for easy manipulation of data from telnet sessions.  You know what that means? You guessed it--another python script. Woo. I'm brimming with excitement.  I'll use the script to connect to the relay, prompt the relay for meter data, and display the sampled data to the screen in intervals of a few seconds to test its operability.  Will begin work on the script next lesson.

*Quote of the day: "It is not the critic who counts; not the man who points out how the strong man stumbles, or where the doer of deeds could have done them better. The credit belongs to the man who is actually in the arena, whose face is marred by dust and sweat and blood; who strives valiantly; who errs, who comes short again and again, because there is no effort without error and shortcoming; but who does actually strive to do the deeds; who knows great enthusiasms, the great devotions; who spends himself in a worthy cause; who at the best knows in the end the triumph of high achievement, and who at the worst, if he fails, at least fails while daring greatly, so that his place shall never be with those cold and timid souls who neither know victory nor defeat." - Theodore Roosevelt*

<br />

#### 15 October 2019 (<a name="m24">M24</a>) :
Spent most of the time trying to learn how the *telnetlib* works.  After a long period of frustration, I was finally able to queue the relay for metered data using *MET* and print it to the console from the debuggeras shown in the image below.  My next step will be to collect this data in the form of a string so that I can manipulate it.

![](/Images/Telnet_Test_0.png)

*Quote of the day: "A pelican that is wet walks with a gaited limp, and the dry fish swims alone." - Bill Cosby*

<br />

#### 17 October 2019 (<a name="m25">M25</a>) :
I ran into a problem where--after disabling the debugger--I was unable to display anything to the console--output data or otherwise. After a bit of help from the *telnetlib* documentation page, I was able to deduce that the *read_all()* function I was using was keeping the program locked in a read state, thus making the print statement unreachable.  To remedy this, I instead used the *read_until()* function to wait until the relay's terminal interface displayed the prompt *=>>*, signalling that the meter command had finished executing. The code is as follows:

```
tn.write("MET".encode('ascii') + b"\r\n")
relay_met_data = tn.read_until(b"=>>").decode('ascii')
```

where *relay_met_data* is a string containing the decoded metered output data, which contains all of the information for one single sample of the relay.

After discovering how to aggregate and display the metering information, I added to the script the ability to append these samples to a list and print the sample rate of the relay.  After several tests between 10 and 1000 cycles of metering, I was able to deduce that the sample rate that the hashgraph algorithm will use is somewhere between 320 and 640 samples/second, which should be fine for the purpose of the algorithm.

Next time, I'll try and switch gears to establishing connectivity between one relay and another.  That way, I'll be able to integrate the telnet test script with the networking script to test sending and receiving data between relays.  I could also test sample send/receive rates after that.

*Quote of the day: "There is nothing better than being shot at and missed.  It's really great." - General James Mattis*

<br />

#### 24 October 2019 (<a name="m27">M27</a>) :
Worked on the ethics paper last lesson and resumed prepping this lesson for what I call "Phase 2." Phase 1 involved creating the python script that collected sample data from the relays. Phase 2 will involve hooking up multiple RaspPis and have them communicate with each other via *sockets*. Once that's complete, I'll move on to Phase 3, where I'll sample data on each of the Pis from their respective relays and attempt to send and receive that information between each Pi in the network. The final phase will involve implementing the Hashgraph algorithm on each of the Pis. This will involve the most troubleshooting, I'd imagine, since I'll be dealing with multiple factors at once to include telnet, sockets, public key encryption, and the overall hashgraph consensus algorithm.

Once I set up the initial Hashgraph network, I'll collect data to determine the effective sample rate. The consensus algorithm will probably require the most overhead and will likely be the bottleneck for sample speeds. I'll also do some research into the time complexity of the algorithm to see if I can at least get an accurate prediction as to what it might be.

Today, I spent most of my time trying to connect a second RaspPi to relay **421-D**, with IP address *192.168.20.15*. I tried connecting a KVM switch so that I would be able to access both Pis from the same display, but neither the ECE or the CompSci departments have the hardware. I eventually opted to setting up another workstation beside one of the empty rack cages with a NVideo variant of the RaspPi that I acquired from Col Neff. After setting up the second relay workstation, I was able to verify that a connection to the relay could be established by checking the link lights and performing a traceroute from the Pi to the relay. Next time, I'll try creating a script using *sockets* to make the two computers communicate with each other. If possible, I'd like to see if I can connect my laptop as well to see if I can get reliable three-way communication established. 

*Quote of the day: "When something is important enough, you do it even if the odds are not in your favor." - Elon Musk*

<br />

#### 31 October 2019 (<a name="m29">M29</a>) :
Finally found a KVM switch that works with all of the hardware, including the HP Proliant server, thanks to Dr. D. I've gone ahead and set everything up and returned all of the borrowed hardware back to the ACCR.  In addition, I've also labelled the RaspPis with their respective relay names and last two octets of their IP addresses (451A (20.14) and 421C (20.12)).

Will begin testing the aforementioned connectivity between RaspPis next lesson!

*Quote of the day: "Be good to people for no reason." - Anonymous*

<br />

#### 01 November 2019 (<a name="m30">M30</a>) :
Moved some chairs around today!

*Quote of the day: "Cyber Power is my new favorite capstone." - Col Brian Neff*

<br />

#### 07 November 2019 (<a name="m32">M32</a>) :
Got sockets working! ...sort of. As a simple test, I used the following code (modified from GeeksForGeeks) to establish connectivity between the RaspPi at relay 451A and my personal computer.

   ```
   import socket
   
   s = socket.socket()
   print("Socket successfully created")
   
   port = 6969
   
   s.bind(('', port))
   print("socket binded to ", port)
   
   s.listen(5)
   print("socket is listening")
   
   while True:
    c, addr = s.accept()	 
    print('Got connection from', addr)
   
    c.send('Thank you for connecting') 
    c.close() 
   ```

The connection seems to be established from the client side (451A), but this connection does not reflect from the powershell session on the server side (personal computer) when I attempt to telnet in. Will attempt to send data to confirm whether or not the socket connection has actually been established. I'll run the following code from the client to test this:

   ```
   import socket
   
   s = socket.socket()
   
   port = 6969
   
   s.connect(('192.168.20.249', port))
   
   print(s.recv(1024))
   s.close()	 
   ```

Update: It's working now. So, I'm able to send data at least from the server to the client.  I'll try to send data from the client to the server next.  After that, I'll get the other RaspPi ready so I can attempt to make multiple connections between these computers.  The information in [**this article at RealPython.com**](https://realpython.com/python-sockets/) seems super useful for this purpose.  I'll spend a few hours researching sockets and the many ways to implement it.

Also, another super-important point that I should probably document before it slips my mind again: the IP addresses for the RaspPis that I'll be using in these scripts should be the IP addresses for the actual Pis and not their respective relays.  For instance, the IP address for establishing a TCP connection between my computer and the RaspPi at 451A should be 192.169.20.230, not 192.168.20.14. When in doubt, just run a quick *ifconfig* from the terminal to determine the IP address to use.  That gives me an idea, actually: I ought to create a spreadsheet or a network diagram of all of the new equipment I've connected to the relays (to include the relays and all of the pre-existing hardware).

*Quote of the day: "Python is executable pseudocode. Perl is executable line noise." - Bruce Eckel*

<br />

#### 12 November 2019 (<a name="m33">M33</a>) :
Moved around a server rack and a desk so I can use the KVM without having to worry about whether or not Julian or Dr Ciezki will be using whatever hardware is sitting on the desk. So, I have room to work now--nice!

I went ahead and took the better version of the echo server script I used last time (named *sockets_echo_client.py* and *sockets_echo_server.py*) and ran them both on the Pis in the server rack to test their operability. The new script has a few upsides to the old ones.  For one, the following line (because the socket object supports the context manager type) will automatically close the socket connection, thus removing the need to use the *close()* function.

   ```
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   ```

Additionally, the *sendall()* function will ensure that all of the data, and not just the first byte, will be sent to the server.

The following are screenshots of the server, client, and server, respectively, that demonstrate how these basic scripts works.

![](/Images/server_1.png)
 
![](/Images/client_1.png)
 
![](/Images/server_2.png)

I've also spent some time researching the implementation of multiple connections, which I didn't have enough time to implement today, but will try to get working next time using the [**aforementioned article at RealPython.com**](https://realpython.com/python-sockets/). 

Also, it's probably worth mentioning that the IP address used in the client and server scripts **both** need to be the IP of the server. In this case, that IP is *192.168.20.183*.

*Quote of the day: "Look... Why take a chance?" - Casino (1995)*

<br />

#### 18 November 2019 (<a name="m35">M35</a>) :
Finally back on the grind. I'll be running a few more tests involving connections between multiple computers via sockets today. I'll try making a script that will automatically connect three computers and allow me to send data to each of them from the terminal. It might work better having two separate scripts running on each machine--one for receiving and one for sending. Otherwise, I'll just end up in a wait lock when any of the machines prompt the user for input. Multi-threading is always another option, but that might be a bit too complicated for something so simple. 

So I'm able to get multiple connections working with two separate scripts, yay! I only configured one of my Pis as a server successfully, however. The second Pi (at IP 20.230) appears to throw an error when I run the script *multi_receive.py*, which works fine on the other Pi. Will add to the issue tracker.

One this issue is resolved, however, I should be able to move on to implementing a series of tests to try and break the scripts and harden them a bit more. Then, it'll be on to the actual hashgraph implementation.

*Quote of the day: 
   "To see a world in a grain of sand,
   And a heaven in a wild flower,
   Hold infinity in the palm of your hand,
   And eternity in an hour.." 
    - William Blake, Auguries of Innocence*

<br />

#### 20 November 2019 (<a name="m36">M36</a>) :
Back to work trying to get *multi_receive.py* to work on the one Pi. Trying to upgrade python is proving to be the most difficult challenge as every method of installing results in some sort of error. These errors didn't exist on the brand new Pi that I set up for the other relay, which leads me to believe that there's an issue with the image on this one. However, I've started manually installing python3.8, which takes a long time. I might have to come in on the weekend to account for the lost time I've spent installing this.

Ran into issue after issue just trying to get python updated from 3.4, so I'm just going to do a clean reimage of the Raspbian OS on the Pis SD card.

*Quote of the day: "If you want to build a ship, don’t drum up the men to gather wood, divide the work and give orders. Instead, teach them to yearn for the vast and endless sea." - Antoine de Saint-Exupéry*

*"But also, drum up the men to gather wood, divide the work and give orders." - Management 101*

<br />

#### 02 December 2019 (<a name="m37">M37</a>) :
Worked on the slides for the end-of-semester presentation.  It was mostly just a recap, but I was also able to go back through and update the overall pricing for the hardware implementation of the hashgraph network.  It should be somewhere around $560 now.  Also, so I don't forget later, here are the computers that will need to be purchased for the implementation: https://www.amazon.com/CanaKit-Raspberry-Premium-Clear-Supply/dp/B07BC7BMHY/ref=asc_df_B07BC7BMHY/?tag=hyprod-20&linkCode=df0&hvadid=312824707815&hvpos=1o1&hvnetw=g&hvrand=3055069548742498157&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9029003&hvtargid=aud-802037562948:pla-570414545643&psc=1. 

More on Hashgraph.  Spend a solid 10 minutes drafting up implementation ideas for the algorithm with C1C Sears Shulz, a Cyber Science major whose capstone is right down the hall from ours. What perplexes me the most is how the algorithm is explained in the Swirlds Whitepaper on the subject.  The graphics they use don't seem to make much sense to me.  I think the best thing I can do before proceeding is to absorb as much knowledge about the algorithm as I can and do more research into how it operates on a network so that when I actually implement it, it will work efficiently and exactly the way it's supposed to.

*Quote of the day: "The less you apologize, the more it means when you actually do." - Me*

<br />


[*Go to top*](#topp)

---
## <a name="journal2">Spring Semester Journal</a>

#### 07 January 2020 (<a name="mm1">M01</a>) :
First day back from break! I was able to get a second RaspPi 3 B+ from Col Neff and will use it to create a standard image that I can write to all of the other Pis. Currently, I'm just waiting on the OS install and will have to wait on software updates after that. From there, it will just be a matter of testing connectivity to the other 3 B+ I have set up in the rack. Additionally, the older model RaspPi has been removed and has been placed on the shelf near the door--its purpose will not be served in this project due to too many issues that can be resolved by updating to a newer hardware model.

*Quote of the day: "This chapter of my life is creeping closer to the end and the authors missing and chance to finish gracefully." - A Fighting Chance*

<br />

#### 09 January 2020 (<a name="mm2">M02</a>) :
Finished installing the software updates on the new Pi. I went ahead and tested connectivity between both of the nodes using basic multi-send and multi-receive telnet scripts and everything works perfectly. The scripts are titled *multi_send.py* and *multi_receive.py*. Will move on to writing the full algorithm from here. This is going to require a great deal more research, but I'm hoping that I can have something working within the next few weeks. We'll see, I suppose!

Also, I sent an email to Dr. Fagin from the CompSci department in hopes that he could help with some clarification.

*Quote of the day: "Here I are, the Dyberry Star." - Harold Martin Sr.*

<br />

#### 13 January 2020 (<a name="mm3">M03</a>) :
Got an email back from Dr. Fagin. He said he's too busy to help and suggested that I just do a bunch of research on my own.  He also mentioned that I don't exactly need a Hashgraph algorithm, but something similar that utilizes BFT.  Good, that's exactly what I thought!

With the standard Pi image created, I've moved on to creating the actual algorithm.  The demo I created last semester was more to demonstrate the ability of individual users in the graph to send and receive events while also being able to verify the authenticity of tha data being sent. Data aquisition from the relays, manipulation of plaintext data from relays, and communication between multiple nodes were all achieved and served as the only other requirements that the simulator did not cover. Thus, once I'm able to fully grasp the algorithm, implementing it should be relatively easy. 

Since the algorithm has proven to be a little too over my head at first glance, I've created a separate section in this README titled [*Hashgraph*](#hg) where I'll outline every single part of the algorithm and how it will eventually be implemented.

Also, I found a few useful links with simple HG implementations:
  - https://github.com/conanwu777/hashgraph
  - https://github.com/Lapin0t/py-swirld

We'll see how helpful these actually prove to be.

*Quote of the day: "It is the privilege of the gods to want nothing, and of godlike men to want little." - Diogenes*

<br />

#### 15 January 2020 (<a name="mm4">M04</a>) :
Did some more research involving the two HG repositories I mentioned last lesson. More specifically, I began deconstructing the code for the conanwu777 repo.  So far, it seems to make sense. There are a few C++ syntax things that I have either forgotten or simply do not know at the moment, but I'm figuring it out as I go along fairly well. I've taken to an actual notebook to write out the pseudocode, which I'll later transcribe to this electronic journal, and it seems to be effective so far. Will continue to examine this code.

So far, I've deconstructed the main loop. There were a few function calls that I'll have to delve a little into, and I'll get to those next time, but I think I'm making progress. We'll see!

*Quote of the day: "Never, ever underestimate the importance of having fun." - Randy Pausch*

<br />

#### 17 January 2020 (<a name="mm5">M05</a>) :
More hashgraph research! After running into multiple issues trying to run both of the aforementioned python and C++ implementations, I've decided to just write down the whitepaper details much the same way I did with the other repos.  I'll just use those other repos as a reference for now in case I get stuck on the technical jargon in the whitepaper, but I think it should be fairly straightforward--there's just a *lot* to read. The algorithm is super detailed, but I've decided to divide it up into a few main parts: Gossip Protocol, Divide Rounds, Decide Fame, and Order. Of course, there will be a main loop that runs all of these in some order, but I'll detail that more in the [*Hashgraph*](#hg) section of this journal.

*Quote of the day: "Everybody in this country should learn to program a computer... because it teaches you how to think." - Steve Jobs*

<br />

#### 22 January 2020 (<a name="mm6">M06</a>) :
Added pseudocode to the [*Hashgraph*](#hg) section of the journal. After going through the whitepaper and the example code I found earlier, I'm getting closer and closer to understanding how the algorithm works. I'm still a little shaky on how **rounds** are determined, however. Will continue to research.

*Quote of the day: "A pint of sweat will save a gallon of blood." - General George Patton*

<br />

#### 24 January 2020 (<a name="mm7">M07</a>) :
Created a version 2 of the simulation script and pushed it to the repo. Will continue constructing this.

*Quote of the day: "There is a difference between knowing the path and walking the path." - Morpheus*

<br />

#### 28 January 2020 (<a name="mm8">M08</a>) :
More work on the simulation script. I've determined that I need to figure out first how to handle multiple nodes trying to communicate with each other at the same time without causing a wait lock. A few ideas include a priority system (which should be randomized to some degree) and interrupts. I'll probably go with the first one because it makes more sense to me. This might require multithreading, though. Will work on that for the remainder of class.

Also, another important thing to note: The simulation currently uses code that will only with with python 3.8 and above. Any previous versions will cause and error.

As far as progress made, I completed the random number generator for the node to sync with. I've implemented this with the following code:
  ```
  while(current_node == (rand_node := random.randrange(N))):		# Pick random node != current node
				pass
  ```
  
I was also able to create the multithreading implementation to call two functions within the Node object: *begin_sync* and *wait_sync*. These have been tested and work the way they should as far as the actual multithreading goes. I just have to write the actual functions that are called now.  This will be the tricky part.

*Quote of the day: "Space isn't remote at all. It's only an hour's drive away if your car could go straight upwards." - Fred Hoyle*

<br />

#### 30 January 2020 (<a name="mm9">M09</a>) :
Working more on determining which nodes go first in the algorithm based on randomly generated priority.

*Quote of the day: "There is nothing impossible to him who will try." - Alexander the Great*

<br />

#### 03 February 2020 (<a name="mm10">M10</a>) :
Still trying to figure out this algorithm. Gonna try a suggestion that Sears Schulz gave me: using different port numbers for each connection. Perhaps also selecting a different pool of ports for each node. We'll see how it works!

*Quote of the day: "Every failure is a step to success." - William Whewell*

<br />

#### 05 February 2020 (<a name="mm11">M11</a>) :
Just finished creating a simulated version of the sync process! As opposed to the other ideas I had, I used two flags in the *Node* class to simulate the *sync_request* and *sync_active* states as Boolean variable. I also used multithreading to call the *begin_sync()* function from the starting node and the *wait_sync()* function from the randomly chosen node where the random node != the starting node. Since the simulation will run on one machine--and not run on several individual Pis--it made sense to remove threading from the main function of the *Node* class altogether. These will be restored in the final version. 

Starting on the Divide Rounds subroutine next.

*Quote of the day: "This suspense is terrible. I hope it will last." - Oscar Wilde*

<br />

#### 07 February 2020 (<a name="mm12">M12</a>) :
I think I jumped the gun a little in my last entry. Before I can move to the Divide Rounds subroutine, I need to update the sync routine to actually create an event and compare graphs between nodes.

I just updated the Hashgraph structure for each node. The variable *hg* will be a dictionary, using the node names as keys, and will contain a list of *Events* for each node key. I also updated the *node_set_network()* function in the *Network* class to create these structs for each node and also *create_event()* in the *Node* class to create an event and add it to the hashgraph.

Next, I need to build a function to compare hashgraphs when a sync is made and only send the nodes that are not in the receiver's graph. Easy money.

*Quote of the day: "As for me, I am tormented with an everlasting itch for things remote. I love to sail forbidden seas, and land on barbarous coasts." - Herman Melville*

<br />

#### 11 February 2020 (<a name="mm13">M13</a>) :
I'll start working on the sync that I mentioned last lesson.

*Quote of the day: "Man is so made that when anything fires his soul, impossibilities vanish." - Jean se La Fontaine*

<br />

#### 13 February 2020 (<a name="mm14">M14</a>) :
So here's my plan of attack:
  - Iterate through the hg dict of the receiver
  - Iterate through each node and compare the contents to those of the sending node's hg
  - Copy over the missing items
  - Order them by time
  
I'll start programming this today.

*Quote of the day: "Nothing is as obnoxious as other people's luck." - F. Scott Fitzgerald*

<br />

#### 25 February 2020 (<a name="mm17">M17</a>) :
Created a test script last weekend that was able to compare and combine lists pretty much exactly how I outlined it in the Lesson 14 journal entry. Now it's just a matter of implementing it in the simulation script. Easy money.

Will continue on with the simulation. This would be so much easier with a Cyber Science major in the capstone.

*Quote of the day: "Ideas shape the course of History." - John Maynard Keynes*

<br />

#### 02 March 2020 (<a name="mm19">M19</a>) :
Added more functionality to the *create_event* function within the *Node* class. From there, I was able to complete the *sign_event* and *verify_event* functions in the same class from the previous version of the algorithm, which essentially just uses **NACL** to encrypt and verify byte-type event data. The *create_event* function was then updated to check to see if the event is the first for it's respective node. If so, no signing is necessary. Otherwise, the *sign_event* function is called for both the self-parent event and the other-parent event.

Also, the **Sync** portion of the algorithm is complete, I think. I'll begin testing that now to verify that it works as intended.

*Quote of the day: "Just DO IT." - Shia LaBeouf (Also, Nike)*

<br />


[*Go to top*](#topp)

---
## <a name="overview">Overview/Technology</a>

#### *What is Cyber Power?*
Cyber Power is an Industrial Control System (ICS) that emulates the USAFA power grid. The goal is to provide a means to holistically protect the power grid system from both physical and cyber threats to ensure a more robust, resilient, and flexible system overall. The hardware must be made safer and more reliable for consumers while the software must be hardened to ensure data integrity. 

#### Terminology
Relays
<br />
From Wikipedia: *"A relay is an electrically operated switch. It consists of a set of input terminals for a single or multiple control signals, and a set of operating contact terminals. The switch may have any number of contacts in multiple contact forms, such as make contacts, break contacts, or combinations thereof."*

Industrial Control System (ICS)
<br />
From Wikipedia: *"Industrial control system (ICS) is a general term that encompasses several types of control systems and associated instrumentation used for industrial process control. Such systems can range from a few modular panel-mounted controllers to large interconnected and interactive distributed control systems with many thousands of field connections. All systems receive data received from remote sensors measuring process variables (PVs), compare these with desired set points (SPs) and derive command functions which are used to control a process through the final control elements (FCEs), such as control valves."*

Phasor Data Concentrator (PDC)
<br />
From OpenEI: *"Receives and time-synchronizes phasor data from multiple phasor measurement units (PMUs) to produce a real-time, time-aligned output data stream. A PDC can exchange phasor data with PDCs at other locations. Through use of multiple PDCs, multiple layers of concentration can be implemented within an individual synchrophasor data system."*

#### Technology
- The relays and networking equipment are mostly manufactured by Schweitzer Engineering Laboratories. The computers that are used to interface with the relays and store information from them are rackmounted servers. More computers are available for use later on in the capstone if need be.

- Hashgraph: From Wikipedia: *"Hashgraph is a distributed ledger technology developed by Leemon Baird, the co-founder and CTO of Swirlds, in 2016. It is an asynchronous Byzantine Fault Tolerance (aBFT) consensus algorithm capable of securing the platform against attacks. It does not need miners to validate transactions and uses directed acyclic graphs for time-sequencing transactions without bundling them into blocks."*

   Essentially, Hashgraph will be implemented to ensure the integrity of data throughout our ICS. Though the algorithm is largely used for cryptocurrency purposes as a replacement for blockchain, it should theoretically work well with relay information integrity as well.

[*Go to top*](#topp)

---
## <a name="hg">Hashgraph</a>

#### *Hashgraph Algorithm in a Nutshell*
Like Blockchain, but way, way better.

#### Gossip Protocol (Sending/Receiving and Syncing)
Each *member* is represented by a single, vertical line in the graph.

  - Member A chooses another member at random
  - Member A sends that member (Member B) all of the data it has so far
  - Member A does the same with another random member
  - Member B does the same
  - All consecutive members do the same
    - If a single member is given new data, it sends their information to another member immediately after
    - HG struct depicts this gossiping in a directed graph with respect to time
    
  Here's the pseudocode for the consensus algorithm loop, taken from the Swirlds Hashgraph Whitepaper:
  ```
  // This loop runs on each member's computer concurrently
  N = number of members
  
  while(1) {
    sync_member = random() % N
    gossip(sync_member)   // Sends random member all data in their graph
    create_event()
    divide_rounds()
    decide_fame()
    find_order()
  }
  ```
  
  The appropriate function calls are detailed in their respective subsections below.

#### Divide Rounds (Witnesses)

Divide Rounds pesudocode:
  ```
  func divide_rounds() {
    for x in events {
      if x is the first event {
        x.round = 1
        x.witness = True
      } else {
        x.round += 1    // IFF at least one event is able to connect 2/3 of the events in the current round
        x.witness = True    // IFF x.round is greater than the round number of any parent nodes
      }
    }
  }
  ```

#### Decide Fame (Voting)

Decide Fame pesudocode:
  ```
  func decide_fame() {
    for x in events {
      for y in events {
        if x.witness && y.witness && y.round > x.round {
          d = y.round = x.round
          s = []
          s.append(events in y.round-1 that y can strongly see)
          if (majority vote in set s or if there is a tie) {
            v = True
          } else {
            v = False
          }
          t = (num events in s with a positive vote)
          if d = 1 {
            y.vote = can y see x?
          } elif d mod c > 0 {
            if t > 2*n/3 {
              x.famous = v
              // break from y loop
            } else {
              y.vote < v
            }
          } else {
            if t > 2*n/3 {
              y.vote = v
            } else {
              y.vote = middle bit of y.signature    // Coin flip
            }
          }
        }
      }
    }
  }
  ```

#### Find Order (Update Graph)

Find Order pesudocode (and this one is mostly copy-pasted):
  ```
  func find_order() {
    for x in events {
      if (there is a round r such that there is no event y in or before round r that has y . witness = TRUE and y . famous = UNDECIDED) && ( x is an ancestor of every round r unique famous witness) && (this is not true of any round earlier than r) {
        x.roundReceived = r
        s = set of each event z such that z is a self - ancestor of a round r unique famous witness , and x is an ancestor of z but not of the self - parent of z
        x.consensus_timestamp = median of timestamps of all events in s
      }
    }
    
    return (all events that have round_received UNDECIDED, sorted by round_received, then ties sorted by consensus_timestamp, then by whitened signature)
  }
  ```

[*Go to top*](#topp)

---
## <a name="issues">Issue Tracker</a>

I'll use this section of the journal to keep track of any issues I have or have had along with the steps and fix actions taken to resolve them.

- **Problem:**

   Python returning error on line 80 when signing an object string: *AttributeError: type object 'Member' has no attribute 'signing_key'*. I believe this might have something to do with the fact that I'm using *type(self)* instead of *self* when calling for the *signing_key* attribute. I believe that creating a temp variable for *self* and using that instead would solve the issue. Will verify later.

   **Solution:**

   Solved by replacing this code from lines 80-81:
   ```
   signed = type(self).signing_key.sign(obj_string)
   verify_key = type(self).signing_key.verify_key
   ```
   
   With *this* code:
   ```
   signed = self.signing_key.sign(obj_string)
   verify_key = self.signing_key.verify_key
   ```
   
   Removing the *type()* call made the reference point to the member object, not the overall class attribute.
   
   **STATUS: *Resolved***
   
- **Problem:**

   When executing the *sampling_simulation_corrupt* method in my hashgraph object, all members except for the corrupt member (*corr_member*) have their event list populated with an Event-type object. Instead, the corrupt member is given a byte-type string that is appended to it's event list, making key verification impossible (although it's still caught by an exception handler).

   *The following screenshot compares Alice's event list to Bob's after calling **sampling_simulation_corrupt(alice, bob)** followed by **debug_member()***
   ![](/Images/Issues/Issue2Console.png)

   I believe the issue is that I passed the value of the corrupt hash to the *corr_event* variable instead of an actual Event with the corrupt hash.
   
   **Solution:**
   
   The value for the signed hash was being appended to the corrupt member's event list as opposed to an actual Event-type object. Solved by replacing this code from lines 178-179:
   
   ```
   corrupt = new_event.hash[0]
   corr_event = corrupt[:-1] + bytes([int(corrupt[-1]) ^ 1])
   ```
   
   With *this* code:
   ```
   corr_sample = [{"IA":random.randint(30,50), "IB":random.randint(30,50), "IC":random.randint(30,50)}, {"VA":random.randint(20,40), "VB":random.randint(20,40), "VC":random.randint(20,40)}]
   corr_event = Event(member, event_time, corr_sample)
   corr_event.hash = corr_member.sign_event_func(corr_event)
   ```
   
   Creating an entirely new event resolved the issue and is reflected in the console where all members have properly populated event lists and all members except for the corrupt member have the correct signature.
   
   ![](/Images/Issues/Issue2Resolved.png)
   
   **STATUS: *Resolved***
   
- **Problem:**

   When running *multi_receive.py* on the Pi at **20.230**, I get the following error in the console: 
   
   ```
   Traceback (most recent call last):
   File "multi_receive.py", line 10, in <module>
   s.listen()
   TypeError: listen() takes exactly one argument (0 given)
   ```
   
   The issue does not occur on the Pi at **20.183**, which leads me to believe that I might have to update and/or upgrade the versions of either the OS, Raspbian, or python. Will try upgrading and see if that works. Also, I think it's strange that the *listen()* function requires one argument on one machine and not the other. 
   
   Turns out the Pis were both using different versions of python. I've upgraded the one on **20.230** to see if that resolves the issue. If it does, I'll go ahead and upgrade the Pi at **20.183** as well.
   
   **Solution:**
   
   Figured out that the Raspberry Pis were two different versions. Replaced the RaspPi 2 with another RaspPi 3 and the issue was resolved.
   
   **STATUS: *Resolved***
   
<br />

#### Stack Exchange Posts

The following are posts I've made on various Stack Exchange boards related to cyber power:
  - [Decentralized communication between multiple computers in a network](https://stackoverflow.com/questions/59954817/is-decentralized-communication-between-3-computers-in-a-network-possible-in-pyt)
  - [Full comms between multiple Raspberry Pis](https://stackoverflow.com/questions/58665473/whats-the-best-way-to-implement-full-communication-between-many-rasppis-over-a)
   
<br />

[*Go to top*](#topp)

---
## <a name="other">Other</a>

Helpful Links:
- [Hashgraph Python Implementation](https://github.com/prakashcc/HashPay)
- [Everything you need to know about Hashgraph](https://101blockchains.com/hashgraph/)
- [Hashgraph whitepaper examples](https://www.swirlds.com/downloads/SWIRLDS-TR-2016-02.pdf)
- [Ukraine Cyber-Introduced Power Outage](https://doi.org/10.1109/CPRE.2017.8090056)
- [Securing Comms for SCADA and ICSs](https://doi.org/10.1109/CPRE.2016.7914914)
- [Cybersecurity Best Practices for ICSs](http://dx.doi.org/10.1109/RWEEK.2016.7573308)
- [Digital Signatures with NACL](https://pynacl.readthedocs.io/en/stable/signing/)

[*Go to top*](#topp)

---

Documentation: Referenced "Securing Critical Industrial Systems With SEL Solutions" whitepaper and "Defense-in-Depth Security for Industrial Control Systems" by Schweitzer Engineering Laboratories, Inc. for information related to SEL-specific ICS cybersecurity solutions. Additionally, all other resources referenced have been included in the [**"other"**](#other) section with hyperlinks.
