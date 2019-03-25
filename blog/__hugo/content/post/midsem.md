---
title: "Mid-Semester  Exam"
date: 2019-03-22T14:00:00+11:00
categories: ["Assessments"]
hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# Multiple Choice

|1. Which of the following statements pertaining to actors in use cases is FALSE?|
|:--|
|**In presence of generalization a more general actor can always replace the specialized one.**|
|One user might be represented by multiple actors in the same use case.|
|Actor is a class of entities (human or computer), falling beyond the system boundaries and interacting with the system.|
|One use case might involve multiple actors.|

|2. After you initialise a new Git repository and create a file named hello.py, which of the following commands will not work if issued?|
|:--|
|git add hello.py|
|**git commit -m "created a simple python program"**|
|git status|
|git add .|


|3. What is the major benefit of the incremental and iterative software development model?|
|:--|
|It is easier to test and debug|
|It is used when there is a need to release a product to the market early|
|**Customers can provide feedback to each increment, and product can be adapted**|
|Less Project Management Overhead|


|4. Read the following description.<br>"Customers of the garage can buy cars. Customers with a bad credit should pay an extra down payment".<br>Which of the following diagrams represent this description?|
|:--|
|![](Picture1.png)|
|![](Picture2.png)|
|![](Picture3.png)|
|> ![](Picture4.png)|

|5. Which of the following is not true in the context of object-oriented design principles?|
|:--|
|Encapsulation ensures that changes to the internal implementation of the class does not affect other parts of the application or clients accessing the class|
|Abstraction helps to focus on the common properties and behaviors of objects|
|**Association is a mechanism to accurately represent the knowledge about the problem domain and discard irrelevant details**|
|Encapsulation hides the object state so that it can only be accessed through its public interface (methods)|
|By abstracting the implementation, encapsulation reduces the dependencies so that a change to a class does not cause a rippling effect on the system|

|6. What one of the following is not a responsibility of the product owner?|
|:--|
|The product owner is responsible for ensuring that the product backlog always has the right set of user-stories needed|
|The product owner can change the priority of the user-stories implemented|
|**The product owner provides an estimate in story points of the effort required to develop a user-story**|
|The product owner decides which user-stories are pulled into an iteration|

|7. Which of the following statements is NOT true?<br>![](Picture5.png)|
|:--|
|The diamond near A is called composition|
|B is part of A|
|**If an instance of B is deleted, all contained object instances of A are also deleted**|
|If an instance of A is deleted, all contained object instances of B are also deleted|

|8. A travel agency offers many trips <i>e.g. 7-day Japan trip, 14-day Japan trip</i>.<br>Each trip comprises of a number of tours <i>e.g., 7-day Japan trip includes 3 tours (tour to Hiroshima, tour to Mt Fuji, Tokyo city tour)</i>.<br>The same tour can be joined by members from different trips <i>e.g. the tour to Hiroshima can be part of both 7-day Japan trip and 14-day Japan trip</i>.<br>To model the above scenario, you decide that a trip can be made up of multiple tours and a single tour can be included in several trips.<br>This situation is best modelled with a UML class diagram as:|
|:--|
|![](Picture6.png)|
|> ![](Picture7.png)|
|![](Picture8.png)|
|![](Picture9.png)|

|9. An illustration of a one-to-many relationship would be:|
|:--|
|A museum displays a list of art works|
|A branch location has an internal Branch_ID code|
|**A balance field is totalled for all accounts for each person**|
|A person changes his/her primary address|
|A student can enrol in several courses and each course has several students|


|10. Which one of these represents a functional requirement?|
|:--|
|All pages on a website must load in less than 2 seconds regardless of location of the customer|
|The UI for the web application must adhere to HTML 5 guidelines and standards to ensure cross-platform portability|
|**Employees shall be forced to change their password the next time they log in if they have not changed it within the length of time established as "password expiration duration"**|
|The rate of failure occurrence of the Automated Teller Machine shall be 1 / 365 (1 failure in 365 days)|

# Case Study
> You are analysing requirements for an online developer's forum.  
To use the forum, a regular user must register providing a valid user-name and password.  
Once registered, a user will be able to log into the system with their registered user-name and password and view the list of current discussion threads.  
Discussion threads are grouped by topics _e.g. python string functions, OO analysis, inheritance with Java._  
User can click on any discussion thread and view or post messages under that thread.  
Users can also search for relevant threads of discussion belonging to particular topic by doing a keyword search _e.g. "inheritance java"_.  
A list of relevant discussion threads categorised under that topic will be displayed. Users can click on a search result and view or post messages under that thread.  
Users can also create a new thread of discussion, under a particular topic but users can only post under existing topics.  
Administrators can perform additional tasks such as delete or update messages posted by any user, close a discussion thread, create new topics and view statistics.

**(a) Draw a use-case diagram that contains actors, use cases and their relationship from the scenario described above (5 marks)**
<div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom lightbox&quot;,&quot;xml&quot;:&quot;&lt;mxfile modified=\&quot;2019-03-22T15:58:02.767Z\&quot; host=\&quot;pebppomjfocnoigkeepgbmcifnnlndla\&quot; agent=\&quot;Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36\&quot; version=\&quot;10.5.0\&quot; etag=\&quot;-0cuwbffDbe1SrfcQJlw\&quot; type=\&quot;device\&quot;&gt;&lt;diagram id=\&quot;MyqEeeji2L7RtrTl9s_R\&quot; name=\&quot;Page-1\&quot;&gt;7V1Lc6M4EP41PtqFXjyOec3uIVOV2uzsVs1NBtlmBiMXyJNkfv0KA8YgwM4GgbGTS4wAGbr7+7rVUssTdLd+/SOim9VX7rFgAg3vdYLuJxBCDCz5L2l5S1uAgUnasox8L2srGp793yy/MGvd+h6LSxcKzgPhb8qNLg9D5opSG40i/lK+bMGD8rdu6JIpDc8uDdTWf31PrNJWmxhF+5/MX67ybwZGdmZN84uzhnhFPf5y0IQeJugu4lykn9avdyxIpJfLJb3vS8PZ/YNFLBSn3PDwY/5GbgFdzA3r+4vzbf77++3UctJuftFgm71x9rTiLRdBxLehx5JejAm6fVn5gj1vqJucfZFal20rsQ7kEZAfAzpnwS11fy53t93xgEfyVMhDef3twg+CSlP2/SwS7LXxzcBeXtLSGF8zEb3JS173Qk9vyYwMZ4cvhcKIlbWtDpWF8itpZiXLfd+FIOWHTJbvkKsJFDEyTxpWdpi9e1myPBIrvuQhDR4532Ty/MGEeMtgQbeCl6Xt0Xi1uz85YKF3k1i8PHQDGse+mzZ+8YP8+vShkidpF7V8cL6NXNbyhsjO0EijJRNtoqjXXcQCKvxf5QfpXg+wxr5Nuk6sNhA7iRwesVchBbZvW5auyI4qapVmK8pKiVjs/6bz3QWJXjfcD8XuxcjthNzLFhr4yzBRk5Q6k1i4Tczfl6Rzk51Y+56X3H8EThEXUoY8uYOYbVjK2DF7qIKTDhXfYseNyDNmwHSy7zhZoVlvT4lYiq5MUsKwjcod8MUilmZWtYf9I/1/EyFHCG9csMx95DFUwiFRSax3odIP3WDrsTHCEgItsCStqJwaMwxxGU/TblAKwKzSL+kLp0Cxmb/Y0o8TTUHjxnWlIoTqdINARorseNxC400aPi781wS6XcQl0CjHJUSNS+yasMTWFZSovvAp4r/8BFnGXcQ8+Vo+DeLzEiIyy0LcB3tDSRFr9hddxmijcAbmtTiDKXC0eAN83BtUSBt24gysqi8AcNabO0CK1TzypR/u8gNjcQjAGpjLLKQK6LKGqdaJFJgOZ4fiQAtfDQdaWigwNeQ2DkQkz8nkbIU7IcEpxFUadPriQHUY9cTj5Nm+sjhOEptnzX6WOTD7OYYqoMtiv1Hk6Bx1ZHcR5DeBaLH7KzOgY2hhQMeo12HBgATlOduPJgHKOJ5C2Bfh2YqlPDMauatJMrOT5AH+XkWMeufNe3joqE+d85GjfyrYSORHhvYb1sVP7uQIP/ewWc1oXYTnqAmbCdQTN7dDT3oNE+bZ+gx+qBMfgsouBFSwqjGNbKjsF/B4LOQHDHtg9jOdi2e/UyfRBmY/1ZIvlf0w0sJ+qSm3sR8guY/5aJqAwEqaAPWWJgDqAOsr9/zF21gyBY4zMOcBNdtchMx8I+norOUHBk80AzXB+Y/PXmTLc4LyWBLEmc07KjKEQw87oKVI6MNe9sCxZrRbeNUiT9GNVyUnetVBk1F2rVPdOdB4Q0P5eam61qqj9YW/44Y2T2tmd34pd3umDljT8rLUpFvT9hYqDxW6WceiJu2x3d/cJbSvA8kN2u0JyarP/kTyPcZ6gNwwEjpYg2A4jgYgoyqQC2T3gGN1KHyROB50mGvXTg9dO46nSM/KUnh0SIwNVEZcN0DG5XB7inrLCCINK8DPEcUNmu0JxfATxTUo1hNWo/b14cYMOHm5xQdRWwmi7b4w60BFpTqS0OcI42GTzk5tVP1BzJ4nOIEecKam2zrmtYGW9bpTrIx6YY8rdvOXOjCdm61YJVUHrjQRT576FifVHBVziFd0k3zcroMbV/BD5T4munzisZ+pbM6F4OtmJR8uyakaiOCVrCLfisAP2d2+srh14c7pmcVKpENqktuoJq9oasvNtk/oFbT5ULR2Sq3zgLs/tXLrR1OKDc6vDCazmvlNqTy7ScPoU/WBo3J45okODzSs7e0pcFXXnH0GrvdQUz74qG8k0DRLqOvGNeJqLUtunT0kkdQajMuEcYNue4KxGnx8wvh+qisdfLQcAwNcKcfoKB9sl3vFvQ1JoYbC0LPEcUN02xOOa6tFrx7Huvzx8dJSYlUQ11E6GFWHqv0lhKF5JUhu0G5PSK7beurqkYyJHiA3jIAPAmtsVIDcUWSNS70WReP6cYxVjzz2JPHJ0G6oBusJ2rX7+1w7tPXU/eHjLtrCUAuyq46/vxoONQi88dbJ5g/XlToGxtC5Y6SWwo2JT3NZHefTIemUvHd3iPHOuU01Tbqho3Vu0HbKfNZRPgLNsG3byVajwEHYLEdD8nV73DEHXgdWB50uILV5xovEKtRTkooa8sQHRVm2UQloOloUTmaOjUwECbQwAQ6BvUFTrTr4FtLPyfHa3f56DXCwSpqXVu0KT+XVQRce4fcuPBpvtSvSU+2KjxIrJqSb6v79ZEi+NKIvIs2N+cBK7lnAdoWa4yh1NVTC63d7U3VTrC6jxCZC07YF6qlbYA1Kbub7yG2829RrKuTH7ZtfGTNkWJUdR7rJgVnVdSP5Dw70sPmfWrZwYZHJydgdtLLBet/+xePFrqaKI+tYsQK0UDfju/zHbvINOPrMvairCLP9D85x0yFsl4MSCw4clKgQq0jPePTjM9/sGemL7ORh8TtSqckWP8eFHv4D&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div>

**(b) Draw a class diagram for the above problem domain. The class diagram must clearly identify all necessary classes (with attributes and methods) and relationships (with cardinalities) (10 marks)**
<div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers lightbox&quot;,&quot;xml&quot;:&quot;&lt;mxfile modified=\&quot;2019-03-22T16:50:13.974Z\&quot; host=\&quot;pebppomjfocnoigkeepgbmcifnnlndla\&quot; agent=\&quot;Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36\&quot; version=\&quot;10.5.0\&quot; etag=\&quot;dK9MNLnqaCrH2aKb_w_f\&quot; type=\&quot;device\&quot;&gt;&lt;diagram id=\&quot;dw2oBZI5BR601whYxw6C\&quot; name=\&quot;Page-1\&quot;&gt;7V1rj+K2Gv41SHsqUeVKyMcZ6LaVds/Zs7NVL1+qLPFAOiFGiekM/fW1E5uQ2LkMYHtavBppiXFC4ufxe7czcRfbl+/zaLf5CGOQThwrfpm4y4nj2P4swP+RlgNtsTy/alnnSUzb6oaH5C/AOtLWfRKDotERQZiiZNdsXMEsAyvUaIvyHD43uz3CtPmru2gNuIaHVZTyrT8nMdpUrXPfqtt/AMl6w37Ztug324h1pg3FJorh80mT+93EXeQQourT9mUBUjJ6bFyq8953fHu8sRxkaMwJn5e/vv/t8///2N89O6v1/55+/g3lU3qVP6N0Tx+Y3iw6sBFY53C/o91AjsCLaNyjr6y7xd+XfXxazBMAtwDlB9yFXsjz6CmUIu6cHj/X422zts3JWM9nFGYK8fp46XoU8Ac6EK8YFIcblJ8KkHMDUzwn2zTK8NH9I8zQA/3GxsdRmqwz/HmFxwCf6d6TkUswq+7oFwjucOtqk6Txh+gA9+SRChStntjR/QbmyV/4slFKr4m/zhGdIM6s0eOBnImbLdyagwL3+cSG3241fYxeGh0/RAWiDSuYptGuSL4eH2Mb5esku4cIwS3t1EmEU8C7qcazQBvKLofyFB/uMdI/Ljms8dOiEoMcPoEFTCEGdZnBCvwkTVtNDP8UPKJO9ItdtEqy9Yeyz9KrWz7TpydNEJ/7mJZyY5PEMcgIchBFbMYRTHYwyVA5PP49/sODuLC+9Sc+vvEFPrbrY/xHuudoATP8LFFSIgYwB54B4UGDyNb5WDtirOkMd2bjJrgjC/og6MQ+i7bAoC8Tfd/RjL43rPPSpASyApzpffsstLcYtxTU8H4h6C+nNkcBl6eAK4A7jb6C9BMsEpRAcv286tuiwZtAOpiPVOSSgJ69PePG93QbN7zou4u3SZYQmiBorJwLrZzZeVbOzJIE91yo6ZLi94igbjTdZfIveNt2Tmg0nRqkx9o0sjSdbXPAgngN2HPj4dnANcyi9Lu6FY/3PotBTEe77vMBlsAR3P4ACB2oNI72CBJ5jLZMVoMsviMhFnz4NYVENpOm9wm59xMxSu6kc7DZjcN9vgLDagtrhzU4wyLJQRqh5M/mfVwfBj5yoNzisJ150+TQbnHYvKeNRUOyMqbGhQGVDq4PAW2HsowNm3etpmXAFqNtgiqXqqBqHr1da8PjpR9B30RUpEOvP6Tiiyf+JgdRXBj0paI/NswiDX2bR9/4GXKwti1Ps6chCqphI8bCZvmPy3f/MXNdLv62dlHPW/NHAvwXq3pDAdkUcHXLe0+UQaEU+FKpfMMC2SyYjVQE8rQ+n0ngMJce7LCsZrDDsdyR+lHasPAR92pOcINjwh2vmxAdIdghpN1Qmi3Ex9drr4fEOzDHXLt+aiMMz8Z+3isM9Yc+xGk2lCD85IYGimigPQzi8s7RMf5ZNHhgKKGGEtpjI75YRyTF76sUFiA2rNDAitFRFHmSQlyBuAVFEa2BkRVaWOGOzJRKYwVzgEwgVT7Y/kibUZbz4JlAqlb8tcdPPFF1FouiEcfBcEA2B0LdAt8TxdAYB0qvwZBAduzA1h08YE8iIsFHahAaGsimAate0UaDWRcNjr6iIYH0OKL2cIHIAyAkKBlQJRIMDWTTINRtG866aAB3IDMsUMIC19FtHfpdGmGFCYAAtQ3e0aCR4YNkPni6DUWW3+D4EIMU1HxIYkMFyVQIdBuLjogKLcxlF18ELF56XGgydr2vtFHha9PopOAGxxRfvGpCVPQ6o/jCk4a1eK0JVYZmtcnFS/vf+GoTt6PkwhTfKGaC/qoLsSSI9ggLWSMIJMOvvcIi7E2lG/Slov8GKil4S5jAH2MH2WAvF3v99RJm4ZkysHXXS7girE29hDL8tddL+D0E+EKtfkMD2TTQXjLh99RN3VGT39BAtvevvWgi5N3/dtGEYYFsFmivmfB76qeW2AMwFJAeBtTt/vtdi5H3u9gkSZXzQXvphN+1P0EzSWqIIJcI+qsnHF43PBwKBLYc8iYX2IX8wObGgxsNHttOEfcCaZB35IT49Zdm7l8091+9762QCPLK58Qx4eN2ZIYIaoggSA2qJUIgJoJwmaVhgkQmCLKEikVC9ys/DA2U0UCULlTLA8fsia4MbEF+UAi2tJRRVxW9WV2njgPaBX9X2qgqoi958I7sUWyoIJkKggyiYir0bF1p9i1UxAJBAlExC0bsXvkEDs8wN+soZAcKBGlExQ7iYFGBWU4jnwaCPKJimdBVVECNhIoJ1ZsMFnUAwRBDdiBRu/XYU2ZAXgpsDAbpHBBkFBVzoGejHsIBoyGkk0CUTVRsKPT4DmaTFlU0ECzBVkyDHufBrL9WxgPB+mvFPOgyGMmqM/xsGC0ESuVQv1R8UT55URjPUgFDQt2WY9C5k0/pUhhuaOOG5+i2KIOeHd8e8OgmBTLJCQVE8HVblW7IQaz2vb2UKM3X9uJBzQ+/nB78Sg4wdvRw+XL65fLAjl4S9Av7Dfz55Cx8VJ9EDtg51fNf5RXB1EIffEVwtV6cZ4WadwTPHW7u8y9vpvP8BLOyyK9zsi0nI0oVj7noMol8H62e1iWVmNCYOO5j+W/SUx04ZtuYHqp31hJa386pVD40fm80KPTKn8i41Jf1G9ectjLN8PGxwFRpQ3q8uwtQ5t1FgzIGAMMcWmETlOsgPSWSpnldRxXaTGdoE+NxEm1hFjckuX2mRD5X+l9RkjMDbViUdyh4NaI85M24m5jkFd37RPnMdSUI8+Y1p3brAvLmd8jr7G8M0JU0Zz9yVaR5YT5nDQqkOT+JVUjzs0R1rwZ4I9KcvSZvUJpXbxHXJs1v1GTz+hf5EGkeXlWaH+W3pUx+81H725Df/dCW8ttvul2XWuPqwWVLC/SIa+tV4prKYvuVcZVhQ/+a4nqs8e10bJKrKI7CL+i4CXEddIz6UVyH85ZJxgJjF9pkvH+tTn7z2babkN8DWE8J2Gyt4z9VNwd6QuBnie/heMuZEv6a4nustV0R5wLx3eGkM+ocl3y1HLfqxuhZNZ/w0EaHk250snb+Tjhr/g4rIn0/sj+7r5rO1R1cNwzMC67bUFJDwf5w5jaVlHMVHTVtqyhPlRib80WCt6GiBgP+YeDJCAby5oirDGs94f5/rccxOtwfXEVlvVbTBFZrnxP61sYuTdPub1NRJ1fT8AtZbkLTzIdyEWHQShtcSdNw8idUJn74NQk3oWoGoCaqhr1W/bqpZbsVIlOYi5hrzUX8+1TN2Bqh2aWJ5bM0jdfynTzqzHVpmnZ/2w9aJJShafhg+m1omqE8Seg3XRppdS3q4m68UXEbmmYwbxLOPLuFymVoXxNcfJhDiE6759Fu8xHGgPT4Gw==&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div>
<script type="text/javascript" src="https://www.draw.io/js/viewer.min.js"></script>