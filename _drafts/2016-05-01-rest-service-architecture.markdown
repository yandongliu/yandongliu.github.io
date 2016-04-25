---
layout: post
title:  "Write a REST service"
date:   2016-04-18 17:12:22 -0800
categories: python go rest architecture
---

In today's collaborative work environment there could be many people working at the same thing. How to achieve both `speed` and `deveoper productivity`? For example if you choose `micro-service` architecture locally developer can move really fast, but it seems to hurt developer productivity in the long term as you'll soon find teams make the same mistakes again and again, duplicate the same effort debugging the same error, and spend a lot of time fixing the same libs... And I feel like people learn less this way as they don't benefit from the rest of the community (you learn more from your immediate team). On the other hand, `monorepo` guarantees that if problem is fixed it's fixed for the whole company, I can learn what went wrong and how it got fixed, and most of the time I probably don't have to worry about it as they might get fixed even before I know, so that I can spend most of the time churning out code for my own business. The flip side of it is, managing a large repo will become a problem one day, editing same files across teams will cause troubles, and deploy is definitely an issue sometimes. There is no perfect solution.

Anyway this is too broad a topic and I am not experienced enough to give a complete answer. Many companies tried a number of different approaches, and they same to apply to teams of certain size and stage, and people always iterate on them. On the outside the service seems to be running fine, but in-house people might need fight fire all the time.

`Frontend (React) - Web server - REST Backend (Go/Python)`

This seems to be a typical way of isolating layers, and, as long as contracts are agreed on, developers should be able to focus on their own work.

### Backend structure:

 - *Handlers*: for various endpoints (HTTP, or other protocols)
 - *Repositories*: read/write objects from data storage
 - *Services*: where business logic happen
 - *Task Scheduler*: for long-running jobs
 - etc

There is no view/controller components. All such work should happen on frontend.

### An example Python backend structure:

#### Handler
aa
