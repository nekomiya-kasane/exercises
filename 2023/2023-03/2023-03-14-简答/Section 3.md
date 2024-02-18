11. AC ([Control Structures (fsu.edu)](https://www.cs.fsu.edu/~myers/c++/notes/control1.html)
12. B
13. A
14. C ([The three basic programming constructs - Programming constructs - OCR - GCSE Computer Science Revision - OCR - BBC Bitesize](https://www.bbc.co.uk/bitesize/guides/znh6pbk/revision/1))
15. ABC

### Section 3

1. (a) 

   | A    | B    | C    | A AND B | A OR C | NOT B | (A AND B) OR (NOT B) |
   | ---- | ---- | ---- | ------- | ------ | ----- | -------------------- |
   | 0    | 0    | 0    | 0       | 0      | 1     | 1                    |
   | 0    | 0    | 1    | 0       | 1      | 1     | 1                    |
   | 0    | 1    | 0    | 0       | 0      | 0     | 0                    |
   | 0    | 1    | 1    | 0       | 1      | 0     | 0                    |
   | 1    | 0    | 0    | 0       | 1      | 1     | 1                    |
   | 1    | 0    | 1    | 0       | 1      | 1     | 1                    |
   | 1    | 1    | 0    | 1       | 1      | 0     | 1                    |
   | 1    | 1    | 1    | 1       | 1      | 0     | 1                    |

   (b) ==Static RAM== uses transistor to implement, maintains data without refreshment, is faster, and is usually used in CPU's speed-sensitive cache memory, for example the L2 and L3 cache

   ==dynamic RAM== uses capacitor to implement, needs refreshment to maintain data, is a bit slower, and is usually used in the main memory.

2. (a) ==Address bus==:  Unidirectional bus. It carries memory addresses from the processor to other components such as primary storage and input/output devices as well as it also contains a few control lines to carry control commands. It allows the CPU to reference memory locations within the device, and it connects the CPU and other peripherals and carries only memory addresses.

   ==data bus==: Bidirectional bus, it carries the data between the processor and other components. It is an electrical path that connects the CPU, memory, and other hardware devices on the motherboard.

   ==Control bus==: Unidirectional bus. It carries control signals from the processor to other components, and  also carries the clock's pulses. The control signal, which is generated from the control unit within the CPU, is used for controlling and coordinating the various activities across the computer.

   (b) A non-maskable interrupt (NMI) is a hardware interrupt that standard interrupt-masking in the system cannot ignore. It is often used 

   - to handle non-recoverable errors which need immediate attention. i.e. when response time is critical or when an interrupt should never be disabled during normal system operation (including reporting non-recoverable hardware errors, system debugging and profiling, and handling of special cases like system resets)
   - to diagnose and fix faulty code.

3. 5 sections to write technical manual:

   - requirements specification - specify the function and feature of the program. what to implement.
   - detailed design - the details of the program, including data dictionaries, descriptions of each function, top level design information, etc.
   - code listing - the format and requirement of coding, including formatting, basic information, internal comments, and meaningful naming of variables and functions etc.
   - test strategy - illustrating how to test, including the contents & items of blackbox/whitebox tests, unit tests, and testing as a whole etc. It covers necessary aspects such as security tests, input tests etc.
   - completed test log - the data collected in tests following the strategy. The results and proofs (screen shot etc.) of executing tests.

4. (a) Python: `len` (length of a container),   `id` (the memory id of an object or value)

   (b) Functions encapsulate a block of code that can be repeatedly called and executed. Through this code block, a large amount of code can be reused. A typical function can usually takes a few arguments to handle different inputs and usually has some return values to return information to the outer procedures.

   (c) Floating point number is appropriate since 52.345 is a real number.

   A person's surname should be a String since it contains a bunch of space, characters or letters.

   (d) ==Global variables== can be used everywhere in a piece of program, it is destructed or destroyed by the OS or VM only when the program terminated.

   ==Local variables== can be used only in a code block or a function (scope), when the statement is executed, its space is initialized, after exiting its scope, it is destroyed. This saves memory space.

5. (a) A company must take a number of steps to ensure that it collects, processes, and stores personal data in a responsible and secure way. Including

   - Obtain Consent: obtain explicit and informed consent from individuals before collecting, processing, and storing their personal data; clearly state the purpose for which the data will be used, how long it will be retained, and any other relevant details.
   - Maintain Accuracy: ensure that the personal data it collects and processes is accurate, up to date, and relevant to the purpose for which it was collected.
   - Protect Data: take measures to protect personal data from unauthorized access, disclosure, alteration, destruction, or other forms of misuse. 
   - Allow Access: allow individuals to access their personal data and to correct any inaccuracies or errors in their data.
   - Secure Transfer: ensure that any transfers of personal data are lawful and secure.
   - Notify Authorities: report any data breaches to the relevant data protection authorities within some hours.
   - Appoint a Data Protection Officer: A company must appoint a Data Protection Officer (DPO) if it processes large amounts of personal data or carries out high-risk processing activities.

   (b) A company must take steps to ensure that it treats its customers fairly and provides them with accurate and truthful information. Including

   - Provide Accurate Information
   - Avoid Deceptive Practices
   - Honor Promises Made
   - Protect Privacy
   - Provide Access to Personal Information
   - Offer Fair Terms
   - Respond to Complaints

6.  (a) four services or benefits:

   - Professional Development: Professional institutes in computing often offer professional development opportunities such as training courses, seminars, and workshops.
   - Networking: Professional institutes in computing provide a valuable opportunity for Ali to network with other professionals in his field.
   - Certification: Some professional institutes in computing offer certification programs that can help Ali to demonstrate his expertise and credibility to potential employers.
   - Advocacy: Professional institutes in computing often play an advocacy role, representing the interests of their members to government, industry, and other stakeholders.

   (b) Job role: Cybersecurity analyst, and a professional body that would be appropriate for this role is the International Association of Computer Science and Information Technology (IACSIT), which  is a global professional organization that promotes research and development in the fields of computer science and information technology, including cybersecurity

7. ==Investigation Stage Documentation:== Including

   - Problem statement: A description of the problem that needs to be solved, including any error messages or symptoms observed.
   - Investigation plan: A plan for how the investigation will be conducted, including the tools or methods that will be used to diagnose the problem.
   - Testing results: A record of any testing that was conducted to identify the cause of the problem, including the outcomes of these tests and any errors or anomalies observed.
   - Analysis of results: An analysis of the testing results, including any hypotheses or theories about the cause of the problem, and any potential solutions that were identified.

   ==Solution Stage Documentation:== Including

   - Solution statement: A description of the solution that was implemented to resolve the problem, including any changes that were made to the system or software.
   - Implementation plan: A plan for how the solution will be implemented, including any steps that need to be taken to ensure that the solution is effective and does not cause any new problems.
   - Testing results: A record of any testing that was conducted to ensure that the solution is effective and does not cause any new problems, including the outcomes of these tests and any errors or anomalies observed.
   - Verification of solution: Verification that the solution is successful, including any additional testing or validation that was conducted to confirm that the problem has been resolved.

8. 5 reasons:

   - Lack of memory. When the physical memory is ran out by the user, and the OS cannot allocate more space in it, modern OS usually provide a feature called virtual memory or swap partition to store less-used data to the disk, as the speed disk is much lower than the main memory, the computer will become slow.

     You could append more memory (of a appropriate frequency and slot) to the computer to improve this.

   - Lack of disk space: the OS and software need some space to cache things. When the disk is nearly full, caches cannot be allocated. 

     You could append more disks to the computer and leave more space for each partition.

   - Overheating: Overheating can cause your computer to slow down or even shut down unexpectedly. 

     You could ensure your computer is properly ventilated and free of dust, ensure that your computer's fans are functioning correctly, or use a cooling pad or stand.

   - Outdated or conflicting drivers: Outdated or conflicting drivers can cause various performance issues, such as slow startup or shutdown, freezes, and crashes. You could update your drivers manually or use a driver update tool to automatically detect and install the latest drivers for your hardware.

   - Malware or virus infections: Malware or virus infections can significantly slow down your computer's performance. You could run a full system scan with a reputable antivirus or antimalware program to remove any infections. Additionally, you could install an ad blocker or a browser extension that blocks pop-ups and malicious ads.