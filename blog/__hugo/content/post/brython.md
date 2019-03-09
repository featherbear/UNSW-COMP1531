---
title: "Brython"
description: "Python via Javascript!"
date: 2019-02-12T21:14:42+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams:
  enable: false
  options: ""
---

**This page is my [Brython](https://brython.info/) playground!**

---

{{% brython %}}

{{< python show="true">}}
from browser import document, alert

def echo():
  alert("hello")

echo()

{{< /python >}}