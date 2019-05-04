---
title: "Software Architecture"
date: 2019-04-23T16:00:00+10:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# Architectural Style

1) Components  
2) Connectors - (ie RPC, broadcast, protocols)  
3) Constraints  

ie Client/Server, Peer-to-Peer, Pipe-Filter, Centralised, Layered

## Client Server Architecture
One component functions as a server, which provides services to other componenets  
One component functions as a client, which requests services provided by a server

Connector -> Request-response model

**Pros**  
Straightforward, Scalable, Easy to maintain

**Cons**  
Single point of failure, congestion

## Peer to Peer
Each peer functions as both a server and a client.  
No middleman server (although possibly a a relay (Hybrid P2P))

**Pros**  
Efficiency, scalability, robustness

**Cons**  
Complexity, resource availability


# Pipe and Filter Architecture
ie `ls . | grep -v ... | more`  

A filter component which reads input streams, and transforms data.  
A pipe connector which transfers data from one filter to another.

Output can start beginning before all input is read.  
Stateless

**Pros**
Easy to understand, flexible, concurrent

**Cons**
Order dependent, error handling, not interactive

# Repository Architecture
Central data repository component  
Data accessor components

Read/Write connector

**Pros**  
Centralisation -> concurrency, integrity, security, backup

**Cons**  
eh.

# Event Based Architecture
Publisher and subscriber

