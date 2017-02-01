---
layout: page
title: "Research"
description: "Research"
group: navigation
order: 1
---
{% include JB/setup %}

I am a founding member of the new UC Berkeley RISE Lab

## [RISE Lab](https://rise.cs.berkeley.edu) Research Vision

A long-standing grand challenge in computing is to enable machines to behave intelligently: to rapidly and repeatedly take appropriate actions based on information in the world around them. 
This challenge has been addressed in specific applications such as online advertising and high-frequency trading, and has been a focus in specialized physical systems like self-driving cars and drones. 
While the progress has been encouraging, the general challenge of intelligent real-time decision-making has not yet been addressed. 
There are three broad trends that frame the challenge:

1. **Timely Data:** Networked sensors have become ubiquitous, carried in our pockets and embedded in our vehicles, buildings, streets, and appliances. These devices allow continuous monitoring of the world around us in ways that have never been possible before and are highly vulnerable to privacy and security breaches. *While many experiments are underway, we have yet to see a wide range of applications that harness data with the degree of recency, granularity, and security that is enabled by networked sensing and control.*

1. **Practical Artificial Intelligence:** In recent years, AI has graduated from research labs into a surprising breadth of complex applications. 
Much of the recent practical success of AI has come from a convergence of massive training sets and new programmable systems for learning at scale. *Systems for offline learning have fueled widespread experimentation with AI; real-time decision-making is the natural next step.*

1. **Programmable Actuation:** The devices around us are increasingly programmable. 
Our vehicles, houses, and workplaces are heavily networked and controlled by malleable software. Robots, drones, and embedded medical devices will extend the programmable world to our homes, airspace, and bloodstreams. *The first generation of pervasive programmable actuation is already here, and significant disruption is on the horizon.*


Today, we are at an inflection point, poised for a wave of applications that close the loop between computational intelligence and the physical world. 
The critical missing catalysts are secure, general-purpose systems that can learn and act in real time on large-scale streams of live data. 
To this end, we are studying the design of new algorithms and systems for *Real-time Intelligent Secure Execution* (**RISE**) that will enable the next decade of innovation centered around widespread, intelligent, and trustworthy computing.  

In the RISE Lab we are pursuing research challenges in the following three areas:

1. **Systems:** We are designing responsive software and hardware that provide orders-of-magnitude lower latency and higher throughput than existing platforms. These systems support a diversity of real-time, intelligent and secure applications, much like Hadoop and Spark powered big data analytics over the past decade. These systems are designed to respond in real time and at scale, closing the loop between data, models, and decisions. 

1. **Machine Learning:** We are developing robust online learning techniques that rapidly explore massive solution spaces and adapt to feedback in real time. We are exploring the design of systems for reinforcement learning, to close the loop between data and decisions. We are also pursuing mechanisms that incentivize data and model sharing across organizations to promote collaboration. 

1. **Security:** We are studying the design of systems and algorithms that  are able to process sensitive data in an untrusted infrastructure, while preserving data confidentiality and building mechanisms to guarantee post-hoc auditability for social and legal requirements.  

The [UC Berkeley RISE Lab](https://rise.cs.berkeley.edu) is a joint effort with faculty spanning systems, machine learning, databases, and security and is funded by a consortium of world class sponsors who are actively participating in the ongoing research.



---

## Other Research Directions 


### Real-time Interactive Machine Learning

Machine learning and systems research have largely focused on the design of algorithms and systems to train models at scale on static datasets.
However, training models is only a small part of the greater _life-cycle of machine learning_ which spans training, model serving, performance evaluation, exploration, and eventually re-training.
Furthermore, in many real-world applications there are often many models and modeling tasks which may share common data and incorporate user level personalization (e.g., spam prediction and content filtering).
This bigger picture introduces a wide range of exciting new challenges in both the design of models and algorithms as well as the systems needed to support each of these stages.

* <b>Low-Latency Model Serving:</b> Serving predictions can be costly, requiring the evaluation of complex feature functions, retrieval of user personalization information, and potentially slow mathematical operations.
Existing systems resort to pre-materialized predictions or specialized bespoke prediction services limiting their scalability and broader adoption.
I believe that we can leverage advances in distributed query processing, caching, partial materialization, and model approximations to enable more general purpose low-latency prediction serving.

* <b>Hybrid Online/Offline Learning:</b> Typically models are trained offline at fixed intervals (e.g., every night) resulting in stale models.
While online learning algorithms exist, there is limited systems support and offline re-training can often be more efficient and improve estimation quality (e.g., by iterating multiple times).
I believe that by splitting models into online and offline components we can achieve a compromise by enabling fast updates to rapidly changing parameters (e.g., personalization parameters) while leveraging existing offline training systems for slowly evolving parameters.

* <b>Managing Multiple Models:</b> Often there will be multiple models for the same task (e.g., models built by different employees).
Choosing the right model and sharing training and prediction computation across models can improve accuracy and system performance.
Model selection is often accomplished using A/B testing, however this approach is deficient as model performance can vary across user groups and time.
I believe that by applying active learning techniques we can adaptively select the best models for different groups at different times.
This will require the development of new systems to support active learning in a low-latency serving environment.

### Graph Systems and Analytics

The GraphX project was initial created to address the need to unify tables and graphs support entire graph analytics pipelines which combines tabular pre-processing and post-processing with complex graph algorithms.
GraphX recast the essential patterns and optimizations in graph-processing systems as new distributed join strategies and new techniques for incremental materialized view maintenance.
Through this alternative perspective, GraphX integrates graph computation into a general purpose distributed data-flow system, enabling users to view data as tables or graphs without data movement or duplication and efficiently execute graph algorithms at performance parity with specialized graph-processing systems.
GraphX is now part of Apache Spark and has been put into production at major technology companies (e.g., Alibaba Taobao).  The next steps in the GraphX project are to be able to support graph structure queries like those found in graph databases, streaming graph modifications, and achieve consistent scale-out and scale-up performance.



### Hybrid Synchronous and Asynchronous Systems

Much of my early work on graph processing systems, the parameter servers, and even transactional models for machine learning leveraged nondeterminism and asynchrony to improve performance.
Meanwhile, many contemporary data processing systems have abandoned asynchrony, in favor of the simpler Bulk Synchronous Parallel (BSP) execution model and the determinism it affords.
This leads to the question: can we combine the benefits of asynchronous systems and the simplicity and determinism of synchronous systems?
In my lab, we have already begun to explore a hybrid approach to algorithm and system design that provides more frequent, fine-grained communication, while retaining determinism at different levels of granularity.
Building on the concept of mini-batch algorithms in machine learning, I believe their is a pattern and corresponding abstraction that can interpolate between the extremes enabling users to choose the level of coordination that leads to the optimal trade-off between algorithm convergence rates and system performance.
Understanding how and when to exploit non-determinism while preserving  guarantees on algorithm correctness will be a key part of managing the machine learning life-cycle and exploiting the high-performance systems of the future.





