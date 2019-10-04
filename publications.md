---
layout: default
title: "Publications"
description: "Recent Publications"
group: navigation
order: 2
---

# ArXiv Preprints

<div id="WangICCV19" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Zuxuan Wu and
Xin Wang and
Joseph E. Gonzalez and
Tom Goldstein and
Larry S. Davis</li>
</ul>
</div>
<div class="title">ACE: Adapting to Changing Environments for Semantic Segmentation</div><div class="venue">CoRR</div>
<div class="year">2019</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#WangICCV19_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#WangICCV19_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://arxiv.org/abs/1904.06268">paper</a></li>
</ul>
</div>
<div class="cards"><div id="WangICCV19_abs" class="collapse abstract"><div class="card card-body">Deep neural networks exhibit exceptional accuracy when they are trained and tested on the same data distributions. However, neural classifiers are often extremely brittle when confronted with domain shift---changes in the input distribution that occur over time. We present ACE, a framework for semantic segmentation that dynamically adapts to changing environments over the time. By aligning the distribution of labeled training data from the original source domain with the distribution of incoming data in a shifted domain, ACE synthesizes labeled training data for environments as it sees them. This stylized data is then used to update a segmentation model so that it performs well in new environments. To avoid forgetting knowledge from past environments, we introduce a memory that stores feature statistics from previously seen domains. These statistics can be used to replay images in any of the previously observed domains, thus preventing catastrophic forgetting. In addition to standard batch training using stochastic gradient decent (SGD), we also experiment with fast adaptation methods based on adaptive meta-learning. Extensive experiments are conducted on two datasets from SYNTHIA, the results demonstrate the effectiveness of the proposed approach when adapting to a number of tasks.</div></div><div id="WangICCV19_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@article{WangICCV19,
 abstract = {Deep neural networks exhibit exceptional accuracy when they are trained and tested on the same data distributions. However, neural classifiers are often extremely brittle when confronted with domain shift---changes in the input distribution that occur over time. We present ACE, a framework for semantic segmentation that dynamically adapts to changing environments over the time. By aligning the distribution of labeled training data from the original source domain with the distribution of incoming data in a shifted domain, ACE synthesizes labeled training data for environments as it sees them. This stylized data is then used to update a segmentation model so that it performs well in new environments. To avoid forgetting knowledge from past environments, we introduce a memory that stores feature statistics from previously seen domains. These statistics can be used to replay images in any of the previously observed domains, thus preventing catastrophic forgetting. In addition to standard batch training using stochastic gradient decent (SGD), we also experiment with fast adaptation methods based on adaptive meta-learning. Extensive experiments are conducted on two datasets from SYNTHIA, the results demonstrate the effectiveness of the proposed approach when adapting to a number of tasks.},
 archiveprefix = {arXiv},
 author = {Zuxuan Wu and
Xin Wang and
Joseph E. Gonzalez and
Tom Goldstein and
Larry S. Davis},
 bibsource = {dblp computer science bibliography, https://dblp.org},
 biburl = {https://dblp.org/rec/bib/journals/corr/abs-1904-06268},
 eprint = {1904.06268},
 journal = {CoRR},
 keywords = {arxivpre},
 timestamp = {Thu, 25 Apr 2019 13:55:01 +0200},
 title = { {ACE:} Adapting to Changing Environments for Semantic Segmentation},
 url = {http://arxiv.org/abs/1904.06268},
 volume = {abs/1904.06268},
 year = {2019}
}
</code></pre></div></div>
</div></div>

<div id="Balakrishna19" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Ashwin Balakrishna</li>
	<li>Brijen Thananjeyan</li>
	<li>Jonathan Lee</li>
	<li>Arsh Zahed</li>
	<li>Felix Li</li>
	<li>Joseph E. Gonzalez</li>
	<li>Ken Goldberg</li>
</ul>
</div>
<div class="title">On-Policy Robot Imitation Learning from a Converging Supervisor</div><div class="venue">CoRR</div>
<div class="year">2019</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Balakrishna19_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Balakrishna19_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://arxiv.org/abs/1907.03423">paper</a></li>
</ul>
</div>
<div class="cards"><div id="Balakrishna19_abs" class="collapse abstract"><div class="card card-body">Existing on-policy imitation learning algorithms, such as DAgger, assume access to a fixed supervisor. However, there are many settings where the supervisor may evolve during policy learning, such as a human performing a novel task or an improving algorithmic controller. We formalize imitation learning from a "converging supervisor" and provide sublinear static and dynamic regret guarantees against the best policy in hindsight with labels from the converged supervisor, even when labels during learning are only from intermediate supervisors. We then show that this framework is closely connected to a class of reinforcement learning (RL) algorithms known as dual policy iteration (DPI), which alternate between training a reactive learner with imitation learning and a model-based supervisor with data from the learner. Experiments suggest that when this framework is applied with the state-of-the-art deep model-based RL algorithm PETS as an improving supervisor, it outperforms deep RL baselines on continuous control tasks and provides up to an 80-fold speedup in policy evaluation.</div></div><div id="Balakrishna19_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@article{Balakrishna19,
 abstract = {Existing on-policy imitation learning algorithms, such as DAgger, assume access to a fixed supervisor. However, there are many settings where the supervisor may evolve during policy learning, such as a human performing a novel task or an improving algorithmic controller. We formalize imitation learning from a "converging supervisor" and provide sublinear static and dynamic regret guarantees against the best policy in hindsight with labels from the converged supervisor, even when labels during learning are only from intermediate supervisors. We then show that this framework is closely connected to a class of reinforcement learning (RL) algorithms known as dual policy iteration (DPI), which alternate between training a reactive learner with imitation learning and a model-based supervisor with data from the learner. Experiments suggest that when this framework is applied with the state-of-the-art deep model-based RL algorithm PETS as an improving supervisor, it outperforms deep RL baselines on continuous control tasks and provides up to an 80-fold speedup in policy evaluation.},
 archiveprefix = {arxivpre},
 author = {Ashwin Balakrishna and Brijen Thananjeyan and Jonathan Lee and Arsh Zahed and Felix Li and Joseph E. Gonzalez and Ken Goldberg},
 bdsk-url-1 = {http://arxiv.org/abs/1907.03423},
 bibsource = {dblp computer science bibliography, https://dblp.org},
 biburl = {https://dblp.org/rec/bib/journals/corr/abs-1907-03423},
 eprint = {1907.03423},
 journal = {CoRR},
 keywords = {arxivpre},
 timestamp = {Wed, 17 Jul 2019 10:27:36 +0200},
 title = {On-Policy Robot Imitation Learning from a Converging Supervisor},
 url = {http://arxiv.org/abs/1907.03423},
 volume = {abs/1907.03423},
 year = {2019}
}
</code></pre></div></div>
</div></div>

<div id="Zhao2018" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Sicheng Zhao</li>
	<li>Bichen Wu</li>
	<li>Joseph Gonzalez</li>
	<li>Sanjit A. Seshia</li>
	<li>Kurt Keutzer</li>
</ul>
</div>
<div class="title">Unsupervised Domain Adaptation: from Simulation Engine to the RealWorld</div><div class="venue">CoRR</div>
<div class="year">2018</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Zhao2018_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Zhao2018_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://arxiv.org/abs/1803.09180">paper</a></li>
</ul>
</div>
<div class="cards"><div id="Zhao2018_abs" class="collapse abstract"><div class="card card-body">Large-scale labeled training datasets have enabled deep neural networks to excel on a wide range of benchmark vision tasks. However, in many applications it is prohibitively expensive or time-consuming to obtain large quantities of labeled data. To cope with limited labeled training data, many have attempted to directly apply models trained on a large-scale labeled source domain to another sparsely labeled target domain. Unfortunately, direct transfer across domains often performs poorly due to domain shift and dataset bias. Domain adaptation is the machine learning paradigm that aims to learn a model from a source domain that can perform well on a different (but related) target domain. In this paper, we summarize and compare the latest unsupervised domain adaptation methods in computer vision applications. We classify the non-deep approaches into sample re-weighting and intermediate subspace transformation categories, while the deep strategy includes discrepancy-based methods, adversarial generative models, adversarial discriminative models and reconstruction-based methods. We also discuss some potential directions.</div></div><div id="Zhao2018_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@article{Zhao2018,
 abstract = {Large-scale labeled training datasets have enabled deep neural networks to excel on a wide range of benchmark vision tasks. However, in many applications it is prohibitively expensive or time-consuming to obtain large quantities of labeled data. To cope with limited labeled training data, many have attempted to directly apply models trained on a large-scale labeled source domain to another sparsely labeled target domain. Unfortunately, direct transfer across domains often performs poorly due to domain shift and dataset bias. Domain adaptation is the machine learning paradigm that aims to learn a model from a source domain that can perform well on a different (but related) target domain. In this paper, we summarize and compare the latest unsupervised domain adaptation methods in computer vision applications. We classify the non-deep approaches into sample re-weighting and intermediate subspace transformation categories, while the deep strategy includes discrepancy-based methods, adversarial generative models, adversarial discriminative models and reconstruction-based methods. We also discuss some potential directions.},
 archiveprefix = {arXiv},
 author = {Sicheng Zhao and Bichen Wu and Joseph Gonzalez and Sanjit A. Seshia and Kurt Keutzer},
 bdsk-url-1 = {http://arxiv.org/abs/1803.09180},
 bibsource = {dblp computer science bibliography, https://dblp.org},
 biburl = {https://dblp.org/rec/bib/journals/corr/abs-1803-09180},
 eprint = {1803.09180},
 journal = {CoRR},
 keywords = {arxivpre},
 month = {3},
 title = {Unsupervised Domain Adaptation: from Simulation Engine to the RealWorld},
 url = {http://arxiv.org/abs/1803.09180},
 volume = {abs/1803.09180},
 year = {2018}
}
</code></pre></div></div>
</div></div>

<div id="Feinberg2018" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Vladimir Feinberg</li>
	<li>Alvin Wan</li>
	<li>Ion Stoica</li>
	<li>Michael I. Jordan</li>
	<li>Joseph E. Gonzalez</li>
	<li>Sergey Levine</li>
</ul>
</div>
<div class="title">Model-Based Value Estimation for Efficient Model-Free Reinforcement Learning</div><div class="venue">CoRR</div>
<div class="year">2018</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Feinberg2018_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Feinberg2018_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://arxiv.org/abs/1803.00101">paper</a></li>
</ul>
</div>
<div class="cards"><div id="Feinberg2018_abs" class="collapse abstract"><div class="card card-body">Recent model-free reinforcement learning algorithms have proposed incorporating learned dynamics models as a source of additional data with the intention of reducing sample complexity. Such methods hold the promise of incorporating imagined data coupled with a notion of model uncertainty to accelerate the learning of continuous control tasks. Unfortunately, they rely on heuristics that limit usage of the dynamics model. We present model-based value expansion, which controls for uncertainty in the model by only allowing imagination to fixed depth. By enabling wider use of learned dynamics models within a model-free reinforcement learning algorithm, we improve value estimation, which, in turn, reduces the sample complexity of learning.</div></div><div id="Feinberg2018_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@article{Feinberg2018,
 abstract = {Recent model-free reinforcement learning algorithms have proposed incorporating learned dynamics models as a source of additional data with the intention of reducing sample complexity. Such methods hold the promise of incorporating imagined data coupled with a notion of model uncertainty to accelerate the learning of continuous control tasks. Unfortunately, they rely on heuristics that limit usage of the dynamics model. We present model-based value expansion, which controls for uncertainty in the model by only allowing imagination to fixed depth. By enabling wider use of learned dynamics models within a model-free reinforcement learning algorithm, we improve value estimation, which, in turn, reduces the sample complexity of learning.},
 archiveprefix = {arXiv},
 author = {Vladimir Feinberg and Alvin Wan and Ion Stoica and Michael I. Jordan and Joseph E. Gonzalez and Sergey Levine},
 bdsk-url-1 = {http://arxiv.org/abs/1803.00101},
 bibsource = {dblp computer science bibliography, https://dblp.org},
 biburl = {https://dblp.org/rec/bib/journals/corr/abs-1803-00101},
 eprint = {1803.00101},
 journal = {CoRR},
 keywords = {arxivpre},
 month = {2},
 title = {Model-Based Value Estimation for Efficient Model-Free Reinforcement Learning},
 url = {http://arxiv.org/abs/1803.00101},
 volume = {abs/1803.00101},
 year = {2018}
}
</code></pre></div></div>
</div></div>

<div id="Hughes18" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>J. Weston Hughes</li>
	<li>Taylor Sittler</li>
	<li>Anthony D. Joseph</li>
	<li>Jeffrey E. Olgin</li>
	<li>Joseph E. Gonzalez</li>
	<li>Geoffrey H. Tison</li>
</ul>
</div>
<div class="title">Using Multitask Learning to Improve 12-Lead Electrocardiogram Classification</div><div class="venue">CoRR</div>
<div class="year">2018</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Hughes18_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Hughes18_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://arxiv.org/abs/1812.00497">paper</a></li>
</ul>
</div>
<div class="cards"><div id="Hughes18_abs" class="collapse abstract"><div class="card card-body">We develop a multi-task convolutional neural network (CNN) to classify multiple diagnoses from 12-lead electrocardiograms (ECGs) using a dataset comprised of over 40,000 ECGs, with labels derived from cardiologist clinical interpretations. Since many clinically important classes can occur in low frequencies, approaches are needed to improve performance on rare classes. We compare the performance of several single-class classifiers on rare classes to a multi-headed classifier across all available classes. We demonstrate that the addition of common classes can significantly improve CNN performance on rarer classes when compared to a model trained on the rarer class in isolation. Using this method, we develop a model with high performance as measured by F1 score on multiple clinically relevant classes compared against the gold-standard cardiologist interpretation.</div></div><div id="Hughes18_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@article{Hughes18,
 abstract = {We develop a multi-task convolutional neural network (CNN) to classify multiple diagnoses from 12-lead electrocardiograms (ECGs) using a dataset comprised of over 40,000 ECGs, with labels derived from cardiologist clinical interpretations. Since many clinically important classes can occur in low frequencies, approaches are needed to improve performance on rare classes. We compare the performance of several single-class classifiers on rare classes to a multi-headed classifier across all available classes. We demonstrate that the addition of common classes can significantly improve CNN performance on rarer classes when compared to a model trained on the rarer class in isolation. Using this method, we develop a model with high performance as measured by F1 score on multiple clinically relevant classes compared against the gold-standard cardiologist interpretation.},
 archiveprefix = {arXiv},
 author = {J. Weston Hughes and Taylor Sittler and Anthony D. Joseph and Jeffrey E. Olgin and Joseph E. Gonzalez and Geoffrey H. Tison},
 bdsk-url-1 = {http://arxiv.org/abs/1812.00497},
 bibsource = {dblp computer science bibliography, https://dblp.org},
 biburl = {https://dblp.org/rec/bib/journals/corr/abs-1812-00497},
 eprint = {1812.00497},
 journal = {CoRR},
 keywords = {arxivpre},
 month = {12},
 title = {Using Multitask Learning to Improve 12-Lead Electrocardiogram Classification},
 url = {http://arxiv.org/abs/1812.00497},
 volume = {abs/1812.00497},
 year = {2018}
}
</code></pre></div></div>
</div></div>

<div id="Crankshaw18" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Daniel Crankshaw</li>
	<li>Gur-Eyal Sela</li>
	<li>Corey Zumar</li>
	<li>Xiangxi Mo</li>
	<li>Joseph E. Gonzalez</li>
	<li>Ion Stoica</li>
	<li>Alexey Tumanov</li>
</ul>
</div>
<div class="title">InferLine: ML Inference Pipeline Composition Framework</div><div class="venue">CoRR</div>
<div class="year">2018</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Crankshaw18_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Crankshaw18_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://arxiv.org/abs/1812.01776">paper</a></li>
</ul>
</div>
<div class="cards"><div id="Crankshaw18_abs" class="collapse abstract"><div class="card card-body">The dominant cost in production machine learning workloads is not training individual models but serving predictions from increasingly complex prediction pipelines spanning multiple models, machine learning frameworks, and parallel hardware accelerators. Due to the complex interaction between model configurations and parallel hardware, prediction pipelines are challenging to provision and costly to execute when serving interactive latency-sensitive applications. This challenge is exacerbated by the unpredictable dynamics of bursty workloads. 

In this paper we introduce InferLine, a system which efficiently provisions and executes ML inference pipelines subject to end-to-end latency constraints by proactively optimizing and reactively controlling per-model configuration in a fine-grained fashion. Unpredictable changes in the serving workload are dynamically and cost-optimally accommodated with minimal service level degradation. InferLine introduces (1) automated model profiling and pipeline lineage extraction, (2) a fine-grain, cost-minimizing pipeline configuration planner, and (3) a fine-grain reactive controller. InferLine is able to configure and deploy prediction pipelines across a wide range of workload patterns and latency goals. It outperforms coarse-grained configuration alternatives by up 7.6x in cost while achieving up to 32x lower SLO miss rate on real workloads and generalizes across state-of-the-art model serving frameworks.</div></div><div id="Crankshaw18_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@article{Crankshaw18,
 abstract = {The dominant cost in production machine learning workloads is not training individual models but serving predictions from increasingly complex prediction pipelines spanning multiple models, machine learning frameworks, and parallel hardware accelerators. Due to the complex interaction between model configurations and parallel hardware, prediction pipelines are challenging to provision and costly to execute when serving interactive latency-sensitive applications. This challenge is exacerbated by the unpredictable dynamics of bursty workloads. 

In this paper we introduce InferLine, a system which efficiently provisions and executes ML inference pipelines subject to end-to-end latency constraints by proactively optimizing and reactively controlling per-model configuration in a fine-grained fashion. Unpredictable changes in the serving workload are dynamically and cost-optimally accommodated with minimal service level degradation. InferLine introduces (1) automated model profiling and pipeline lineage extraction, (2) a fine-grain, cost-minimizing pipeline configuration planner, and (3) a fine-grain reactive controller. InferLine is able to configure and deploy prediction pipelines across a wide range of workload patterns and latency goals. It outperforms coarse-grained configuration alternatives by up 7.6x in cost while achieving up to 32x lower SLO miss rate on real workloads and generalizes across state-of-the-art model serving frameworks.},
 archiveprefix = {arXiv},
 author = {Daniel Crankshaw and Gur{-}Eyal Sela and Corey Zumar and Xiangxi Mo and Joseph E. Gonzalez and Ion Stoica and Alexey Tumanov},
 bdsk-url-1 = {http://arxiv.org/abs/1812.01776},
 bibsource = {dblp computer science bibliography, https://dblp.org},
 biburl = {https://dblp.org/rec/bib/journals/corr/abs-1812-01776},
 eprint = {1812.01776},
 journal = {CoRR},
 keywords = {arxivpre},
 month = {11},
 title = {InferLine: {ML} Inference Pipeline Composition Framework},
 url = {http://arxiv.org/abs/1812.01776},
 volume = {abs/1812.01776},
 year = {2018}
}
</code></pre></div></div>
</div></div>

<div id="Golmant18" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Noah Golmant</li>
	<li>Nikita Vemuri</li>
	<li>Zhewei Yao</li>
	<li>Vladimir Feinberg</li>
	<li>Amir Gholami</li>
	<li>Kai Rothauge</li>
	<li>Michael W. Mahoney</li>
	<li>Joseph Gonzalez</li>
</ul>
</div>
<div class="title">On the Computational Inefficiency of Large Batch Sizes for Stochastic Gradient Descent</div><div class="venue">CoRR</div>
<div class="year">2018</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Golmant18_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Golmant18_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://arxiv.org/abs/1811.12941">paper</a></li>
</ul>
</div>
<div class="cards"><div id="Golmant18_abs" class="collapse abstract"><div class="card card-body">Increasing the mini-batch size for stochastic gradient descent offers significant opportunities to reduce wall-clock training time, but there are a variety of theoretical and systems challenges that impede the widespread success of this technique. We investigate these issues, with an emphasis on time to convergence and total computational cost, through an extensive empirical analysis of network training across several architectures and problem domains, including image classification, image segmentation, and language modeling. Although it is common practice to increase the batch size in order to fully exploit available computational resources, we find a substantially more nuanced picture. Our main finding is that across a wide range of network architectures and problem domains, increasing the batch size beyond a certain point yields no decrease in wall-clock time to convergence for \emph{either} train or test loss. This batch size is usually substantially below the capacity of current systems. We show that popular training strategies for large batch size optimization begin to fail before we can populate all available compute resources, and we show that the point at which these methods break down depends more on attributes like model architecture and data complexity than it does directly on the size of the dataset.</div></div><div id="Golmant18_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@article{Golmant18,
 abstract = {Increasing the mini-batch size for stochastic gradient descent offers significant opportunities to reduce wall-clock training time, but there are a variety of theoretical and systems challenges that impede the widespread success of this technique. We investigate these issues, with an emphasis on time to convergence and total computational cost, through an extensive empirical analysis of network training across several architectures and problem domains, including image classification, image segmentation, and language modeling. Although it is common practice to increase the batch size in order to fully exploit available computational resources, we find a substantially more nuanced picture. Our main finding is that across a wide range of network architectures and problem domains, increasing the batch size beyond a certain point yields no decrease in wall-clock time to convergence for \emph{either} train or test loss. This batch size is usually substantially below the capacity of current systems. We show that popular training strategies for large batch size optimization begin to fail before we can populate all available compute resources, and we show that the point at which these methods break down depends more on attributes like model architecture and data complexity than it does directly on the size of the dataset.},
 archiveprefix = {arXiv},
 author = {Noah Golmant and Nikita Vemuri and Zhewei Yao and Vladimir Feinberg and Amir Gholami and Kai Rothauge and Michael W. Mahoney and Joseph Gonzalez},
 bdsk-url-1 = {http://arxiv.org/abs/1811.12941},
 bibsource = {dblp computer science bibliography, https://dblp.org},
 biburl = {https://dblp.org/rec/bib/journals/corr/abs-1811-12941},
 eprint = {1811.12941},
 journal = {CoRR},
 keywords = {arxivpre},
 month = {11},
 title = {On the Computational Inefficiency of Large Batch Sizes for Stochastic Gradient Descent},
 url = {http://arxiv.org/abs/1811.12941},
 volume = {abs/1811.12941},
 year = {2018}
}
</code></pre></div></div>
</div></div>

<div id="Liaw2017" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Richard Liaw</li>
	<li>Sanjay Krishnan</li>
	<li>Animesh Garg</li>
	<li>Daniel Crankshaw</li>
	<li>Joseph E. Gonzalez</li>
	<li>Ken Goldberg</li>
</ul>
</div>
<div class="title">Composing Meta-Policies for Autonomous Driving Using Hierarchical Deep Reinforcement Learning</div><div class="venue">CoRR</div>
<div class="year">2017</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Liaw2017_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Liaw2017_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://arxiv.org/abs/1711.01503">paper</a></li>
</ul>
</div>
<div class="cards"><div id="Liaw2017_abs" class="collapse abstract"><div class="card card-body">Rather than learning new control policies for each new task, it is possible, when tasks share some structure, to compose a "meta-policy" from previously learned policies. This paper reports results from experiments using Deep Reinforcement Learning on a continuous-state, discrete-action autonomous driving simulator. We explore how Deep Neural Networks can represent meta-policies that switch among a set of previously learned policies, specifically in settings where the dynamics of a new scenario are composed of a mixture of previously learned dynamics and where the state observation is possibly corrupted by sensing noise. We also report the results of experiments varying dynamics mixes, distractor policies, magnitudes/distributions of sensing noise, and obstacles. In a fully observed experiment, the meta-policy learning algorithm achieves 2.6x the reward achieved by the next best policy composition technique with 80% less exploration. In a partially observed experiment, the meta-policy learning algorithm converges after 50 iterations while a direct application of RL fails to converge even after 200 iterations.</div></div><div id="Liaw2017_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@article{Liaw2017,
 abstract = {Rather than learning new control policies for each new task, it is possible, when tasks share some structure, to compose a "meta-policy" from previously learned policies. This paper reports results from experiments using Deep Reinforcement Learning on a continuous-state, discrete-action autonomous driving simulator. We explore how Deep Neural Networks can represent meta-policies that switch among a set of previously learned policies, specifically in settings where the dynamics of a new scenario are composed of a mixture of previously learned dynamics and where the state observation is possibly corrupted by sensing noise. We also report the results of experiments varying dynamics mixes, distractor policies, magnitudes/distributions of sensing noise, and obstacles. In a fully observed experiment, the meta-policy learning algorithm achieves 2.6x the reward achieved by the next best policy composition technique with 80% less exploration. In a partially observed experiment, the meta-policy learning algorithm converges after 50 iterations while a direct application of RL fails to converge even after 200 iterations.},
 archiveprefix = {arXiv},
 author = {Richard Liaw and Sanjay Krishnan and Animesh Garg and Daniel Crankshaw and Joseph E. Gonzalez and Ken Goldberg},
 bdsk-url-1 = {http://arxiv.org/abs/1711.01503},
 bibsource = {dblp computer science bibliography, https://dblp.org},
 biburl = {https://dblp.org/rec/bib/journals/corr/abs-1711-01503},
 eprint = {1711.01503},
 journal = {CoRR},
 keywords = {arxivpre},
 month = {11},
 title = {Composing Meta-Policies for Autonomous Driving Using Hierarchical Deep Reinforcement Learning},
 url = {http://arxiv.org/abs/1711.01503},
 volume = {abs/1711.01503},
 year = {2017}
}
</code></pre></div></div>
</div></div>

<div id="BellettiSFBG16" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Francois W. Belletti</li>
	<li>Evan R. Sparks</li>
	<li>Michael J. Franklin</li>
	<li>Alexandre M. Bayen</li>
	<li>Joseph E. Gonzalez</li>
</ul>
</div>
<div class="title">Scalable Linear Causal Inference for Irregularly Sampled Time Series with Long Range Dependencies</div><div class="venue">CoRR</div>
<div class="year">2016</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#BellettiSFBG16_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://arxiv.org/abs/1603.03336">paper</a></li>
</ul>
</div>
<div class="cards"><div id="BellettiSFBG16_abs" class="collapse abstract"><div class="card card-body"></div></div><div id="BellettiSFBG16_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@article{BellettiSFBG16,
 archiveprefix = {arXiv},
 author = {Francois W. Belletti and Evan R. Sparks and Michael J. Franklin and Alexandre M. Bayen and Joseph E. Gonzalez},
 bdsk-url-1 = {http://arxiv.org/abs/1603.03336},
 bibsource = {dblp computer science bibliography, https://dblp.org},
 biburl = {https://dblp.org/rec/bib/journals/corr/BellettiSFBG16},
 eprint = {1603.03336},
 journal = {CoRR},
 keywords = {arxivpre},
 timestamp = {Mon, 13 Aug 2018 16:48:40 +0200},
 title = {Scalable Linear Causal Inference for Irregularly Sampled Time Series with Long Range Dependencies},
 url = {http://arxiv.org/abs/1603.03336},
 volume = {abs/1603.03336},
 year = {2016}
}
</code></pre></div></div>
</div></div>

<div id="Gonzalez15" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Joseph E. Gonzalez</li>
	<li>Peter Bailis</li>
	<li>Michael I. Jordan</li>
	<li>Michael J. Franklin</li>
	<li>Joseph M. Hellerstein</li>
	<li>Ali Ghodsi</li>
	<li>Ion Stoica</li>
</ul>
</div>
<div class="title">Asynchronous Complex Analytics in a Distributed Dataflow Architecture</div><div class="venue">CoRR</div>
<div class="year">2015</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Gonzalez15_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://arxiv.org/abs/1510.07092">paper</a></li>
</ul>
</div>
<div class="cards"><div id="Gonzalez15_abs" class="collapse abstract"><div class="card card-body"></div></div><div id="Gonzalez15_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@article{Gonzalez15,
 archiveprefix = {arXiv},
 author = {Joseph E. Gonzalez and Peter Bailis and Michael I. Jordan and Michael J. Franklin and Joseph M. Hellerstein and Ali Ghodsi and Ion Stoica},
 bdsk-url-1 = {http://arxiv.org/abs/1510.07092},
 bibsource = {dblp computer science bibliography, https://dblp.org},
 biburl = {https://dblp.org/rec/bib/journals/corr/GonzalezBJFHGS15},
 eprint = {1510.07092},
 journal = {CoRR},
 keywords = {arxivpre},
 timestamp = {Mon, 13 Aug 2018 16:46:22 +0200},
 title = {Asynchronous Complex Analytics in a Distributed Dataflow Architecture},
 url = {http://arxiv.org/abs/1510.07092},
 volume = {abs/1510.07092},
 year = {2015}
}
</code></pre></div></div>
</div></div>



<br/><br/>

---

# Publications


<div id="Jain19" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Samvit Jain</li>
	<li>Xin Wang</li>
	<li>Joseph Gonzalez</li>
</ul>
</div>
<div class="title">Accel: A Corrective Fusion Network for Efficient Semantic Segmentation on Video</div><div class="venue">The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)</div>
<div class="year">2019</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Jain19_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Jain19_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://arxiv.org/abs/1807.06667">paper</a></li>
</ul>
</div>
<div class="cards"><div id="Jain19_abs" class="collapse abstract"><div class="card card-body">We present Accel, a novel semantic video segmentation system that achieves high accuracy at low inference cost by combining the predictions of two network branches: (1) a reference branch that extracts high-detail features on a reference keyframe, and warps these features forward using frame-to-frame optical flow estimates, and (2) an update branch that computes features of adjustable quality on the current frame, performing a temporal update at each video frame. The modularity of the update branch, where feature subnetworks of varying layer depth can be inserted (e.g. ResNet-18 to ResNet-101), enables operation over a new, state-of-the-art accuracy-throughput trade-off spectrum. Over this curve, Accel models achieve both higher accuracy and faster inference times than the closest comparable single-frame segmentation networks. In general, Accel significantly outperforms previous work on efficient semantic video segmentation, correcting warping-related error that compounds on datasets with complex dynamics. Accel is end-to-end trainable and highly modular: the reference network, the optical flow network, and the update network can each be selected independently, depending on application requirements, and then jointly fine-tuned. The result is a robust, general system for fast, high-accuracy semantic segmentation on video.</div></div><div id="Jain19_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{Jain19,
 abstract = {We present Accel, a novel semantic video segmentation system that achieves high accuracy at low inference cost by combining the predictions of two network branches: (1) a reference branch that extracts high-detail features on a reference keyframe, and warps these features forward using frame-to-frame optical flow estimates, and (2) an update branch that computes features of adjustable quality on the current frame, performing a temporal update at each video frame. The modularity of the update branch, where feature subnetworks of varying layer depth can be inserted (e.g. ResNet-18 to ResNet-101), enables operation over a new, state-of-the-art accuracy-throughput trade-off spectrum. Over this curve, Accel models achieve both higher accuracy and faster inference times than the closest comparable single-frame segmentation networks. In general, Accel significantly outperforms previous work on efficient semantic video segmentation, correcting warping-related error that compounds on datasets with complex dynamics. Accel is end-to-end trainable and highly modular: the reference network, the optical flow network, and the update network can each be selected independently, depending on application requirements, and then jointly fine-tuned. The result is a robust, general system for fast, high-accuracy semantic segmentation on video.},
 author = {Samvit Jain and Xin Wang and Joseph Gonzalez},
 bdsk-url-1 = {http://arxiv.org/abs/1807.06667},
 booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
 keywords = {peerrev},
 month = {June},
 title = {Accel: {A} Corrective Fusion Network for Efficient Semantic Segmentation on Video},
 url = {http://arxiv.org/abs/1807.06667},
 year = {2019}
}
</code></pre></div></div>
</div></div>

<div id="WangCVPR19" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Xin Wang</li>
	<li>Fisher Yu</li>
	<li>Ruth Wang</li>
	<li>Trevor Darrell</li>
	<li>Joseph E. Gonzalez</li>
</ul>
</div>
<div class="title">TAFE-Net: Task-Aware Feature Embeddings for Low Shot Learning</div><div class="venue">The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)</div>
<div class="year">2019</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#WangCVPR19_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#WangCVPR19_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://arxiv.org/abs/1904.05967">paper</a></li>
</ul>
</div>
<div class="cards"><div id="WangCVPR19_abs" class="collapse abstract"><div class="card card-body">Learning good feature embeddings for images often requires substantial training data. As a consequence, in settings where training data is limited (e.g., few-shot and zero-shot learning), we are typically forced to use a generic feature embedding across various tasks. Ideally, we want to construct feature embeddings that are tuned for the given task. In this work, we propose Task-Aware Feature Embedding Networks (TAFE-Nets) to learn how to adapt the image representation to a new task in a meta learning fashion. Our network is composed of a meta learner and a prediction network. Based on a task input, the meta learner generates parameters for the feature layers in the prediction network so that the feature embedding can be accurately adjusted for that task. We show that TAFE-Net is highly effective in generalizing to new tasks or concepts and evaluate the TAFE-Net on a range of benchmarks in zero-shot and few-shot learning. Our model matches or exceeds the state-of-the-art on all tasks. In particular, our approach improves the prediction accuracy of unseen attribute-object pairs by 4 to 15 points on the challenging visual attribute-object composition task.</div></div><div id="WangCVPR19_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{WangCVPR19,
 abstract = {Learning good feature embeddings for images often requires substantial training data. As a consequence, in settings where training data is limited (e.g., few-shot and zero-shot learning), we are typically forced to use a generic feature embedding across various tasks. Ideally, we want to construct feature embeddings that are tuned for the given task. In this work, we propose Task-Aware Feature Embedding Networks (TAFE-Nets) to learn how to adapt the image representation to a new task in a meta learning fashion. Our network is composed of a meta learner and a prediction network. Based on a task input, the meta learner generates parameters for the feature layers in the prediction network so that the feature embedding can be accurately adjusted for that task. We show that TAFE-Net is highly effective in generalizing to new tasks or concepts and evaluate the TAFE-Net on a range of benchmarks in zero-shot and few-shot learning. Our model matches or exceeds the state-of-the-art on all tasks. In particular, our approach improves the prediction accuracy of unseen attribute-object pairs by 4 to 15 points on the challenging visual attribute-object composition task.},
 author = {Xin Wang and Fisher Yu and Ruth Wang and Trevor Darrell and Joseph E. Gonzalez},
 bdsk-url-1 = {https://arxiv.org/abs/1904.05967},
 booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
 keywords = {peerrev},
 month = {June},
 title = { {TAFE-Net}: Task-Aware Feature Embeddings for Low Shot Learning},
 url = {https://arxiv.org/abs/1904.05967},
 year = {2019}
}
</code></pre></div></div>
</div></div>

<div id="Jonas2019" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Eric Jonas</li>
	<li>Johann Schleier-Smith</li>
	<li>Vikram Sreekanti</li>
	<li>Chia-Che Tsai</li>
	<li>Anurag Khandelwal</li>
	<li>Qifan Pu</li>
	<li>Vaishaal Shankar</li>
	<li>Joao Menezes Carreira</li>
	<li>Karl Krauth</li>
	<li>Neeraja Yadwadkar</li>
	<li>Joseph E. Gonzalez</li>
	<li>Raluca Ada Popa</li>
	<li>Ion Stoica</li>
	<li>David A. Patterson</li>
</ul>
</div>
<div class="title">Cloud Programming Simplified: A Berkeley View on Serverless Computing</div><div class="venue">EECS Department, University of California, Berkeley Technical Report</div>
<div class="year">2019</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Jonas2019_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Jonas2019_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://www2.eecs.berkeley.edu/Pubs/TechRpts/2019/EECS-2019-3.html">paper</a></li>
</ul>
</div>
<div class="cards"><div id="Jonas2019_abs" class="collapse abstract"><div class="card card-body">Serverless cloud computing handles virtually all the system administration operations needed to make it easier for programmers to use the cloud. It provides an interface that greatly simplifies cloud programming, and represents an evolution that parallels the transition from assembly language to high-level programming languages. This paper gives a quick history of cloud computing, including an accounting of the predictions of the 2009 Berkeley View of Cloud Computing paper, explains the motivation for serverless computing, describes applications that stretch the current limits of serverless, and then lists obstacles and research opportunities required for serverless computing to fulfill its full potential. Just as the 2009 paper identified challenges for the cloud and predicted they would be addressed and that cloud use would accelerate, we predict these issues are solvable and that serverless computing will grow to dominate the future of cloud computing.</div></div><div id="Jonas2019_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@techreport{Jonas2019,
 abstract = {Serverless cloud computing handles virtually all the system administration operations needed to make it easier for programmers to use the cloud. It provides an interface that greatly simplifies cloud programming, and represents an evolution that parallels the transition from assembly language to high-level programming languages. This paper gives a quick history of cloud computing, including an accounting of the predictions of the 2009 Berkeley View of Cloud Computing paper, explains the motivation for serverless computing, describes applications that stretch the current limits of serverless, and then lists obstacles and research opportunities required for serverless computing to fulfill its full potential. Just as the 2009 paper identified challenges for the cloud and predicted they would be addressed and that cloud use would accelerate, we predict these issues are solvable and that serverless computing will grow to dominate the future of cloud computing.},
 author = {Eric Jonas and Johann Schleier-Smith and Vikram Sreekanti and Chia-Che Tsai and Anurag Khandelwal and Qifan Pu and Vaishaal Shankar and Joao Menezes Carreira and Karl Krauth and Neeraja Yadwadkar and Joseph E. Gonzalez and Raluca Ada Popa and Ion Stoica and David A. Patterson},
 bdsk-url-1 = {http://www2.eecs.berkeley.edu/Pubs/TechRpts/2019/EECS-2019-3.html},
 institution = {EECS Department, University of California, Berkeley},
 keywords = {techreport},
 month = {2},
 number = {UCB/EECS-2019-3},
 title = {Cloud Programming Simplified: A Berkeley View on Serverless Computing},
 url = {http://www2.eecs.berkeley.edu/Pubs/TechRpts/2019/EECS-2019-3.html},
 year = {2019}
}
</code></pre></div></div>
</div></div>

<div id="Hotmobil2019" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Samvit Jain</li>
	<li>Ganesh Ananthanarayanan</li>
	<li>Junchen Jiang</li>
	<li>Yuanchao Shu</li>
	<li>Joseph E. Gonzalez</li>
</ul>
</div>
<div class="title">Scaling Video Analytics Systems to Large Camera Deployments</div><div class="venue">HotMobile `19, Proceedings of the 20th International Workshop on Mobile Computing Systems and Applications</div>
<div class="year">2019</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Hotmobil2019_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Hotmobil2019_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://arxiv.org/abs/1809.02318">paper</a></li>
</ul>
</div>
<div class="cards"><div id="Hotmobil2019_abs" class="collapse abstract"><div class="card card-body">Driven by advances in computer vision and the falling costs of camera hardware, organizations are deploying video cameras en masse for the spatial monitoring of their physical premises. Scaling video analytics to massive camera deployments, however, presents a new and mounting challenge, as compute cost grows proportionally to the number of camera feeds. This paper is driven by a simple question: can we scale video analytics in such a way that cost grows sublinearly, or even remains constant, as we deploy more cameras, while inference accuracy remains stable, or even improves. We believe the answer is yes. Our key observation is that video feeds from wide-area camera deployments demonstrate significant content correlations (e.g. to other geographically proximate feeds), both in space and over time. These spatio-temporal correlations can be harnessed to dramatically reduce the size of the inference search space, decreasing both workload and false positive rates in multi-camera video analytics. By discussing use-cases and technical challenges, we propose a roadmap for scaling video analytics to large camera networks, and outline a plan for its realization.</div></div><div id="Hotmobil2019_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{Hotmobil2019,
 abstract = {Driven by advances in computer vision and the falling costs of camera hardware, organizations are deploying video cameras en masse for the spatial monitoring of their physical premises. Scaling video analytics to massive camera deployments, however, presents a new and mounting challenge, as compute cost grows proportionally to the number of camera feeds. This paper is driven by a simple question: can we scale video analytics in such a way that cost grows sublinearly, or even remains constant, as we deploy more cameras, while inference accuracy remains stable, or even improves. We believe the answer is yes. Our key observation is that video feeds from wide-area camera deployments demonstrate significant content correlations (e.g. to other geographically proximate feeds), both in space and over time. These spatio-temporal correlations can be harnessed to dramatically reduce the size of the inference search space, decreasing both workload and false positive rates in multi-camera video analytics. By discussing use-cases and technical challenges, we propose a roadmap for scaling video analytics to large camera networks, and outline a plan for its realization.},
 author = {Samvit Jain and Ganesh Ananthanarayanan and Junchen Jiang and Yuanchao Shu and Joseph E. Gonzalez},
 bdsk-url-1 = {https://arxiv.org/abs/1809.02318},
 booktitle = {HotMobile `19, Proceedings of the 20th International Workshop on Mobile Computing Systems and Applications},
 keywords = {peerrev},
 month = {2},
 title = {Scaling Video Analytics Systems to Large Camera Deployments},
 url = {https://arxiv.org/abs/1809.02318},
 year = {2019}
}
</code></pre></div></div>
</div></div>

<div id="cidr19" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Joseph M. Hellerstein</li>
	<li>Jose M. Faleiro</li>
	<li>Joseph E. Gonzalez</li>
	<li>Johann Schleier-Smith</li>
	<li>Vikram Sreekanti</li>
	<li>Alexey Tumanov</li>
	<li>Chenggang Wu</li>
</ul>
</div>
<div class="title">Serverless Computing: One Step Forward, Two Steps Back</div><div class="venue">Conference on Innovative Data Systems Research (CIDR '19)</div>
<div class="year">2019</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#cidr19_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#cidr19_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://arxiv.org/abs/1812.03651">paper</a></li>
</ul>
</div>
<div class="cards"><div id="cidr19_abs" class="collapse abstract"><div class="card card-body">Serverless computing offers the potential to program the cloud in an autoscaling, pay-as-you go manner. In this paper we address critical gaps in first-generation serverless computing, which place its autoscaling potential at odds with dominant trends in modern computing: notably data-centric and distributed computing, but also open source and custom hardware. Put together, these gaps make current serverless offerings a bad fit for cloud innovation and particularly bad for data systems innovation. In addition to pinpointing some of the main shortfalls of current serverless architectures, we raise a set of challenges we believe must be met to unlock the radical potential that the cloud---with its exabytes of storage and millions of cores---should offer to innovative developers.</div></div><div id="cidr19_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{cidr19,
 abstract = {Serverless computing offers the potential to program the cloud in an autoscaling, pay-as-you go manner. In this paper we address critical gaps in first-generation serverless computing, which place its autoscaling potential at odds with dominant trends in modern computing: notably data-centric and distributed computing, but also open source and custom hardware. Put together, these gaps make current serverless offerings a bad fit for cloud innovation and particularly bad for data systems innovation. In addition to pinpointing some of the main shortfalls of current serverless architectures, we raise a set of challenges we believe must be met to unlock the radical potential that the cloud---with its exabytes of storage and millions of cores---should offer to innovative developers.},
 author = {Joseph M. Hellerstein and Jose M. Faleiro and Joseph E. Gonzalez and Johann Schleier{-}Smith and Vikram Sreekanti and Alexey Tumanov and Chenggang Wu},
 bdsk-url-1 = {https://arxiv.org/abs/1812.03651},
 booktitle = {Conference on Innovative Data Systems Research ({CIDR} '19)},
 keywords = {peerrev},
 month = {1},
 title = {Serverless Computing: One Step Forward, Two Steps Back},
 url = {https://arxiv.org/abs/1812.03651},
 year = {2019}
}
</code></pre></div></div>
</div></div>

<div id="Tanwani19" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Ajay Kumar Tanwani</li>
	<li>Nitesh Mor</li>
	<li>John Kubiatowicz</li>
	<li>Joseph E. Gonzalez</li>
	<li>Ken Goldberg</li>
</ul>
</div>
<div class="title">A Fog Robotics Approach to Deep Robot Learning: Application to Object Recognition and Grasp Planning in Surface Decluttering</div><div class="venue">International Conference on Robotics and Automation, ICRA 2019, Montreal, QC, Canada, May 20-24, 2019</div>
<div class="year">2019</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Tanwani19_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Tanwani19_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://doi.org/10.1109/ICRA.2019.8793690">paper</a></li>
</ul>
</div>
<div class="cards"><div id="Tanwani19_abs" class="collapse abstract"><div class="card card-body">The growing demand of industrial, automotive and service robots presents a challenge to the centralized Cloud Robotics model in terms of privacy, security, latency, bandwidth, and reliability. In this paper, we present a `Fog Robotics' approach to deep robot learning that distributes compute, storage and networking resources between the Cloud and the Edge in a federated manner. Deep models are trained on non-private (public) synthetic images in the Cloud; the models are adapted to the private real images of the environment at the Edge within a trusted network and subsequently, deployed as a service for low-latency and secure inference/prediction for other robots in the network. We apply this approach to surface decluttering, where a mobile robot picks and sorts objects from a cluttered floor by learning a deep object recognition and a grasp planning model. Experiments suggest that Fog Robotics can improve performance by sim-to-real domain adaptation in comparison to exclusively using Cloud or Edge resources, while reducing the inference cycle time by 4\times to successfully declutter 86% of objects over 213 attempts.</div></div><div id="Tanwani19_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{Tanwani19,
 abstract = {The growing demand of industrial, automotive and service robots presents a challenge to the centralized Cloud Robotics model in terms of privacy, security, latency, bandwidth, and reliability. In this paper, we present a `Fog Robotics' approach to deep robot learning that distributes compute, storage and networking resources between the Cloud and the Edge in a federated manner. Deep models are trained on non-private (public) synthetic images in the Cloud; the models are adapted to the private real images of the environment at the Edge within a trusted network and subsequently, deployed as a service for low-latency and secure inference/prediction for other robots in the network. We apply this approach to surface decluttering, where a mobile robot picks and sorts objects from a cluttered floor by learning a deep object recognition and a grasp planning model. Experiments suggest that Fog Robotics can improve performance by sim-to-real domain adaptation in comparison to exclusively using Cloud or Edge resources, while reducing the inference cycle time by 4\times to successfully declutter 86% of objects over 213 attempts.},
 author = {Ajay Kumar Tanwani and Nitesh Mor and John Kubiatowicz and Joseph E. Gonzalez and Ken Goldberg},
 bdsk-url-1 = {https://doi.org/10.1109/ICRA.2019.8793690},
 bibsource = {dblp computer science bibliography, https://dblp.org},
 biburl = {https://dblp.org/rec/bib/conf/icra/TanwaniMKGG19},
 booktitle = {International Conference on Robotics and Automation, {ICRA} 2019, Montreal, QC, Canada, May 20-24, 2019},
 doi = {10.1109/ICRA.2019.8793690},
 keywords = {peerrev},
 pages = {4559--4566},
 timestamp = {Tue, 13 Aug 2019 20:25:20 +0200},
 title = {A Fog Robotics Approach to Deep Robot Learning: Application to Object Recognition and Grasp Planning in Surface Decluttering},
 url = {https://doi.org/10.1109/ICRA.2019.8793690},
 year = {2019}
}
</code></pre></div></div>
</div></div>

<div id="Zhang19" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Tianjun Zhang</li>
	<li>Zhewei Yao</li>
	<li>Amir Gholami</li>
	<li>Kurt Keutzer</li>
	<li>Joseph E. Gonzalez</li>
	<li>George Biros</li>
	<li>Michael W. Mahoney</li>
</ul>
</div>
<div class="title">ANODEV2: A Coupled Neural ODE Evolution Framework</div><div class="venue">Neural Information Processing Systems (NeurIPS '19)</div>
<div class="year">2019</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Zhang19_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Zhang19_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://arxiv.org/abs/1906.04596">paper</a></li>
</ul>
</div>
<div class="cards"><div id="Zhang19_abs" class="collapse abstract"><div class="card card-body">It has been observed that residual networks can be viewed as the explicit Euler discretization of an Ordinary Differential Equation (ODE). This observation motivated the introduction of so-called Neural ODEs, which allow more general discretization schemes with adaptive time stepping. Here, we propose ANODEV2, which is an extension of this approach that also allows evolution of the neural network parameters, in a coupled ODE-based formulation. The Neural ODE method introduced earlier is in fact a special case of this new more general framework. We present the formulation of ANODEV2, derive optimality conditions, and implement a coupled reaction-diffusion-advection version of this framework in PyTorch. We present empirical results using several different configurations of ANODEV2, testing them on multiple models on CIFAR-10. We report results showing that this coupled ODE-based framework is indeed trainable, and that it achieves higher accuracy, as compared to the baseline models as well as the recently-proposed Neural ODE approach.</div></div><div id="Zhang19_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@proceedings{Zhang19,
 abstract = {It has been observed that residual networks can be viewed as the explicit Euler discretization of an Ordinary Differential Equation (ODE). This observation motivated the introduction of so-called Neural ODEs, which allow more general discretization schemes with adaptive time stepping. Here, we propose ANODEV2, which is an extension of this approach that also allows evolution of the neural network parameters, in a coupled ODE-based formulation. The Neural ODE method introduced earlier is in fact a special case of this new more general framework. We present the formulation of ANODEV2, derive optimality conditions, and implement a coupled reaction-diffusion-advection version of this framework in PyTorch. We present empirical results using several different configurations of ANODEV2, testing them on multiple models on CIFAR-10. We report results showing that this coupled ODE-based framework is indeed trainable, and that it achieves higher accuracy, as compared to the baseline models as well as the recently-proposed Neural ODE approach.},
 author = {Tianjun Zhang and Zhewei Yao and Amir Gholami and Kurt Keutzer and Joseph E. Gonzalez and George Biros and Michael W. Mahoney},
 booktitle = {Neural Information Processing Systems ({NeurIPS} '19)},
 keywords = {peerrev},
 title = { {ANODEV2:} A Coupled Neural ODE Evolution Framework},
 url = {https://arxiv.org/abs/1906.04596},
 year = {2019}
}
</code></pre></div></div>
</div></div>

<div id="SaxenaSigcommNetAI" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Vidit Saxena</li>
	<li>Joakim Jald\'en</li>
	<li>Joseph E. Gonzalez</li>
	<li>Mats Bengtsson</li>
	<li>Hugo M. Tullberg</li>
	<li>Ion Stoica</li>
</ul>
</div>
<div class="title">Contextual Multi-Armed Bandits for Link Adaptation in Cellular Networks</div><div class="venue">Proceedings of the 2019 Workshop on Network Meets AI \& ML, NetAI at SIGCOMM 2019, Beijing, China, August 23, 2019.</div>
<div class="year">2019</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#SaxenaSigcommNetAI_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#SaxenaSigcommNetAI_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://doi.org/10.1145/3341216.3342212">paper</a></li>
</ul>
</div>
<div class="cards"><div id="SaxenaSigcommNetAI_abs" class="collapse abstract"><div class="card card-body">Cellular networks dynamically adjust the transmission parameters for a wireless link in response to its time-varying channel state. This is known as link adaptation, where the typical goal is to maximize the link throughput. State-of-the-art outer loop link adaptation (OLLA) selects the optimal transmission parameters based on an approximate, offline, model of the wireless link. Further, OLLA refines the offline model by dynamically compensating any deviations from the observed link performance. However, in practice, OLLA suffers from slow convergence and a sub-optimal link throughput. In this paper, we propose a link adaptation approach that overcomes the shortcomings of OLLA through a novel learning scheme. Our approach relies on contextual multi-armed bandits (MAB), where the context vector is composed of the instantaneous wireless channel state along with side information about the link. For a given context, our approach learns the success probability for each of the available transmission parameters, which is then exploited to select the throughput-maximizing parameters. Through numerical experiments, we show that our approach converges faster than OLLA and achieves a higher steady-state link throughput. For frequent and infrequent channel reports respectively, our scheme outperforms OLLA by 15% and 25% in terms of the steady-state link throughput.</div></div><div id="SaxenaSigcommNetAI_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{SaxenaSigcommNetAI,
 abstract = {Cellular networks dynamically adjust the transmission parameters for a wireless link in response to its time-varying channel state. This is known as link adaptation, where the typical goal is to maximize the link throughput. State-of-the-art outer loop link adaptation (OLLA) selects the optimal transmission parameters based on an approximate, offline, model of the wireless link. Further, OLLA refines the offline model by dynamically compensating any deviations from the observed link performance. However, in practice, OLLA suffers from slow convergence and a sub-optimal link throughput. In this paper, we propose a link adaptation approach that overcomes the shortcomings of OLLA through a novel learning scheme. Our approach relies on contextual multi-armed bandits (MAB), where the context vector is composed of the instantaneous wireless channel state along with side information about the link. For a given context, our approach learns the success probability for each of the available transmission parameters, which is then exploited to select the throughput-maximizing parameters. Through numerical experiments, we show that our approach converges faster than OLLA and achieves a higher steady-state link throughput. For frequent and infrequent channel reports respectively, our scheme outperforms OLLA by 15% and 25% in terms of the steady-state link throughput.},
 author = {Vidit Saxena and Joakim Jald{\'{e} }n and Joseph E. Gonzalez and Mats Bengtsson and Hugo M. Tullberg and Ion Stoica},
 bdsk-url-1 = {https://doi.org/10.1145/3341216.3342212},
 bibsource = {dblp computer science bibliography, https://dblp.org},
 biburl = {https://dblp.org/rec/bib/conf/sigcomm/SaxenaJGBTS19},
 booktitle = {Proceedings of the 2019 Workshop on Network Meets {AI} {\&} ML, NetAI at SIGCOMM 2019, Beijing, China, August 23, 2019.},
 crossref = {DBLP:conf/sigcomm/2019netai},
 doi = {10.1145/3341216.3342212},
 keywords = {peerrev},
 pages = {44--49},
 timestamp = {Thu, 15 Aug 2019 09:19:24 +0200},
 title = {Contextual Multi-Armed Bandits for Link Adaptation in Cellular Networks},
 url = {https://doi.org/10.1145/3341216.3342212},
 year = {2019}
}
</code></pre></div></div>
</div></div>

<div id="WangUAI19" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Xin Wang</li>
	<li>Fisher Yu</li>
	<li>Lisa Dunlap</li>
	<li>Yi-An Ma</li>
	<li>Ruth Wang</li>
	<li>Azalia Mirhoseini</li>
	<li>Trevor Darrell</li>
	<li>Joseph E. Gonzalez</li>
</ul>
</div>
<div class="title">Deep Mixture of Experts via Shallow Embedding</div><div class="venue">Proceedings of the Thirty-Fifth Conference on Uncertainty in Artificial Intelligence, UAI 2019, Tel Aviv, Israel, July 22-25, 2019</div>
<div class="year">2019</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#WangUAI19_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#WangUAI19_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://auai.org/uai2019/proceedings/papers/192.pdf">paper</a></li>
</ul>
</div>
<div class="cards"><div id="WangUAI19_abs" class="collapse abstract"><div class="card card-body">Larger networks generally have greater representational power at the cost of increased computational complexity. Sparsifying such networks has been an active area of research but has been generally limited to static regularization or dynamic approaches using reinforcement learning. We explore a mixture of experts (MoE) approach to deep dynamic routing, which activates certain experts in the network on a per-example basis. Our novel DeepMoE architecture increases the representational power of standard convolutional networks by adaptively sparsifying and recalibrating channel-wise features in each convolutional layer. We employ a multi-headed sparse gating network to determine the selection and scaling of channels for each input, leveraging exponential combinations of experts within a single convolutional network. Our proposed architecture is evaluated on four benchmark datasets and tasks, and we show that Deep-MoEs are able to achieve higher accuracy with lower computation than standard convolutional networks.</div></div><div id="WangUAI19_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{WangUAI19,
 abstract = {Larger networks generally have greater representational power at the cost of increased computational complexity. Sparsifying such networks has been an active area of research but has been generally limited to static regularization or dynamic approaches using reinforcement learning. We explore a mixture of experts (MoE) approach to deep dynamic routing, which activates certain experts in the network on a per-example basis. Our novel DeepMoE architecture increases the representational power of standard convolutional networks by adaptively sparsifying and recalibrating channel-wise features in each convolutional layer. We employ a multi-headed sparse gating network to determine the selection and scaling of channels for each input, leveraging exponential combinations of experts within a single convolutional network. Our proposed architecture is evaluated on four benchmark datasets and tasks, and we show that Deep-MoEs are able to achieve higher accuracy with lower computation than standard convolutional networks.},
 author = {Xin Wang and Fisher Yu and Lisa Dunlap and Yi{-}An Ma and Ruth Wang and Azalia Mirhoseini and Trevor Darrell and Joseph E. Gonzalez},
 bdsk-url-1 = {http://auai.org/uai2019/proceedings/papers/192.pdf},
 bibsource = {dblp computer science bibliography, https://dblp.org},
 biburl = {https://dblp.org/rec/bib/conf/uai/WangYDMWMDG19},
 booktitle = {Proceedings of the Thirty-Fifth Conference on Uncertainty in Artificial Intelligence, {UAI} 2019, Tel Aviv, Israel, July 22-25, 2019},
 keywords = {peerrev},
 pages = {192},
 timestamp = {Fri, 19 Jul 2019 13:05:12 +0200},
 title = {Deep Mixture of Experts via Shallow Embedding},
 url = {http://auai.org/uai2019/proceedings/papers/192.pdf},
 year = {2019}
}
</code></pre></div></div>
</div></div>

<div id="Wenting19" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Wenting Zheng</li>
	<li>Raluca Ada Popa</li>
	<li>Joseph E. Gonzalez</li>
	<li>Ion Stoica</li>
</ul>
</div>
<div class="title">Helen: Maliciously Secure Coopetitive Learning for Linear Models.</div><div class="venue">IEEE Symposium on Security and Privacy</div>
<div class="year">2019</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Wenting19_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Wenting19_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://people.eecs.berkeley.edu/~wzheng/helen_ieeesp.pdf">paper</a></li>
</ul>
</div>
<div class="cards"><div id="Wenting19_abs" class="collapse abstract"><div class="card card-body">Many organizations wish to collaboratively train machine learning models on their combined datasets for a common benefit (e.g., better medical research, or fraud detection). However, they often cannot share their plaintext datasets due to privacy concerns and/or business competition. In this paper, we design and build Helen, a system that allows multiple parties to train a linear model without revealing their data, a setting we call coopetitive learning. Compared to prior secure training systems, Helen protects against a much stronger adversary who is malicious and can compromise m−1 out of m parties. Our evaluation shows that Helen can achieve up to five orders of magnitude of performance improvement when compared to training using an existing state-of-the-art secure multi-party computation framework.</div></div><div id="Wenting19_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@proceedings{Wenting19,
 abstract = {Many organizations wish to collaboratively train machine learning models on their combined datasets for a common benefit (e.g., better medical research, or fraud detection). However, they often cannot share their plaintext datasets due to privacy concerns and/or business competition. In this paper, we design and build Helen, a system that allows multiple parties to train a linear model without revealing their data, a setting we call coopetitive learning. Compared to prior secure training systems, Helen protects against a much stronger adversary who is malicious and can compromise m−1 out of m parties. Our evaluation shows that Helen can achieve up to five orders of magnitude of performance improvement when compared to training using an existing state-of-the-art secure multi-party computation framework.},
 author = {Wenting Zheng and Raluca Ada Popa and Joseph E. Gonzalez and Ion Stoica},
 bdsk-url-1 = {https://people.eecs.berkeley.edu/~wzheng/helen_ieeesp.pdf},
 booktitle = { {IEEE} Symposium on Security and Privacy},
 keywords = {peerrev},
 publisher = { {IEEE} Computer Society},
 title = {Helen: Maliciously Secure Coopetitive Learning for Linear Models.},
 url = {https://people.eecs.berkeley.edu/~wzheng/helen_ieeesp.pdf},
 year = {2019}
}
</code></pre></div></div>
</div></div>

<div id="cmi2018" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Rolando Garcia</li>
	<li>Vikram Sreekanti</li>
	<li>Neeraja Yadwadkar</li>
	<li>Daniel Crankshaw</li>
	<li>Joseph E. Gonzalez</li>
	<li>Joseph M. Hellerstein</li>
</ul>
</div>
<div class="title">Context: The Missing Piece in the Machine Learning Lifecycle</div><div class="venue">Proceedings of the KDD Workshop on Common Model Infrastructure (CMI)</div>
<div class="year">2018</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#cmi2018_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#cmi2018_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://www.vikrams.io/papers/flor-cmi18.pdf">paper</a></li>
</ul>
</div>
<div class="cards"><div id="cmi2018_abs" class="collapse abstract"><div class="card card-body">Machine learning models have become ubiquitous in modern applications. The ML Lifecycle describes a three-phase process used by data scientists and data engineers to develop, train, and serve models. Unfortunately, context around the data, code, people, and systems involved in these pipelines is not captured today. In this paper, we first discuss common pitfalls that missing context creates. Some examples where context is missing include tracking the relationships between code and data and capturing experimental processes over time. We then discuss techniques to address these challenges and briefly mention future work around designing and implementing systems in this space.</div></div><div id="cmi2018_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{cmi2018,
 abstract = {Machine learning models have become ubiquitous in modern applications. The ML Lifecycle describes a three-phase process used by data scientists and data engineers to develop, train, and serve models. Unfortunately, context around the data, code, people, and systems involved in these pipelines is not captured today. In this paper, we first discuss common pitfalls that missing context creates. Some examples where context is missing include tracking the relationships between code and data and capturing experimental processes over time. We then discuss techniques to address these challenges and briefly mention future work around designing and implementing systems in this space.},
 author = {Rolando Garcia and Vikram Sreekanti and Neeraja Yadwadkar and Daniel Crankshaw and Joseph E. Gonzalez and Joseph M. Hellerstein},
 bdsk-url-1 = {http://www.vikrams.io/papers/flor-cmi18.pdf},
 booktitle = {Proceedings of the KDD Workshop on Common Model Infrastructure (CMI)},
 keywords = {peerrev},
 month = {8},
 title = {Context: The Missing Piece in the Machine Learning Lifecycle},
 url = {http://www.vikrams.io/papers/flor-cmi18.pdf},
 year = {2018}
}
</code></pre></div></div>
</div></div>

<div id="uai2018" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Xin Wang</li>
	<li>Yujia Luo</li>
	<li>Dan Crankshaw</li>
	<li>Alexey Tumanov</li>
	<li>Fisher Yu</li>
	<li>Joseph E. Gonzalez</li>
</ul>
</div>
<div class="title">IDK Cascades: Fast Deep Learning by Learning not to Overthink</div><div class="venue">Conference on Uncertainty in Artificial Intelligence (UAI)</div>
<div class="year">2018</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#uai2018_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#uai2018_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://arxiv.org/abs/1706.00885">paper</a></li>
</ul>
</div>
<div class="cards"><div id="uai2018_abs" class="collapse abstract"><div class="card card-body">Advances in deep learning have led to substantial increases in prediction accuracy but have been accompanied by increases in the cost of rendering predictions. We conjecture that fora majority of real-world inputs, the recent advances in deep learning have created models that effectively "overthink" on simple inputs. In this paper, we revisit the classic question of building model cascades that primarily leverage class asymmetry to reduce cost. We introduce the "I Don't Know"(IDK) prediction cascades framework, a general framework to systematically compose a set of pre-trained models to accelerate inference without a loss in prediction accuracy. We propose two search based methods for constructing cascades as well as a new cost-aware objective within this framework. The proposed IDK cascade framework can be easily adopted in the existing model serving systems without additional model re-training. We evaluate the proposed techniques on a range of benchmarks to demonstrate the effectiveness of the proposed framework.</div></div><div id="uai2018_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{uai2018,
 abstract = {Advances in deep learning have led to substantial increases in prediction accuracy but have been accompanied by increases in the cost of rendering predictions. We conjecture that fora majority of real-world inputs, the recent advances in deep learning have created models that effectively "overthink" on simple inputs. In this paper, we revisit the classic question of building model cascades that primarily leverage class asymmetry to reduce cost. We introduce the "I Don't Know"(IDK) prediction cascades framework, a general framework to systematically compose a set of pre-trained models to accelerate inference without a loss in prediction accuracy. We propose two search based methods for constructing cascades as well as a new cost-aware objective within this framework. The proposed IDK cascade framework can be easily adopted in the existing model serving systems without additional model re-training. We evaluate the proposed techniques on a range of benchmarks to demonstrate the effectiveness of the proposed framework.},
 author = {Xin Wang and Yujia Luo and Dan Crankshaw and Alexey Tumanov and Fisher Yu and Joseph E. Gonzalez},
 bdsk-url-1 = {https://arxiv.org/abs/1706.00885},
 booktitle = {Conference on Uncertainty in Artificial Intelligence (UAI)},
 keywords = {peerrev},
 month = {7},
 title = { {IDK} Cascades: Fast Deep Learning by Learning not to Overthink},
 url = {https://arxiv.org/abs/1706.00885},
 year = {2018}
}
</code></pre></div></div>
</div></div>

<div id="icml2018" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Eric Liang</li>
	<li>Richard Liaw</li>
	<li>Robert Nishihara</li>
	<li>Philipp Moritz</li>
	<li>Roy Fox</li>
	<li>Joseph Gonzalez</li>
	<li>Ken Goldberg</li>
	<li>Ion Stoica</li>
</ul>
</div>
<div class="title">Ray RLLib: A Composable and Scalable Reinforcement Learning Library</div><div class="venue">Proceedings of the 35th International Conference on Machine Learning</div>
<div class="year">2018</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#icml2018_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#icml2018_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://arxiv.org/abs/1712.09381">paper</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://ray.readthedocs.io/en/latest/rllib.html">code</a></li>
</ul>
</div>
<div class="cards"><div id="icml2018_abs" class="collapse abstract"><div class="card card-body">Reinforcement learning (RL) algorithms involve the deep nesting of highly irregular computation patterns, each of which typically exhibits opportunities for distributed computation. We argue for distributing RL components in a composable way by adapting algorithms for top-down hierarchical control, thereby encapsulating parallelism and resource requirements within short-running compute tasks. We demonstrate the benefits of this principle through RLlib: a library that provides scalable software primitives for RL. These primitives enable a broad range of algorithms to be implemented with high performance, scalability, and substantial code reuse.</div></div><div id="icml2018_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{icml2018,
 abstract = {Reinforcement learning (RL) algorithms involve the deep nesting of highly irregular computation patterns, each of which typically exhibits opportunities for distributed computation. We argue for distributing RL components in a composable way by adapting algorithms for top-down hierarchical control, thereby encapsulating parallelism and resource requirements within short-running compute tasks. We demonstrate the benefits of this principle through RLlib: a library that provides scalable software primitives for RL. These primitives enable a broad range of algorithms to be implemented with high performance, scalability, and substantial code reuse.},
 author = {Eric Liang and Richard Liaw and Robert Nishihara and Philipp Moritz and Roy Fox and Joseph Gonzalez and Ken Goldberg and Ion Stoica},
 bdsk-url-1 = {https://arxiv.org/abs/1712.09381},
 booktitle = {Proceedings of the 35th International Conference on Machine Learning},
 code = {https://ray.readthedocs.io/en/latest/rllib.html},
 keywords = {peerrev},
 month = {7},
 publisher = {ACM},
 series = {ICML '18},
 title = {Ray {RLLib}: {A} Composable and Scalable Reinforcement Learning Library},
 url = {https://arxiv.org/abs/1712.09381},
 year = {2018}
}
</code></pre></div></div>
</div></div>

<div id="acmqueue2018" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Dan Crankshaw</li>
	<li>Joseph E. Gonzalez</li>
	<li>Peter Bailis</li>
</ul>
</div>
<div class="title">Research for Practice: Prediction-Serving Systems</div><div class="venue">Commun. ACM</div>
<div class="year">2018</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#acmqueue2018_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#acmqueue2018_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://doi.acm.org/10.1145/3190574">paper</a></li>
</ul>
</div>
<div class="cards"><div id="acmqueue2018_abs" class="collapse abstract"><div class="card card-body">What happens when we wish to actually deploy a machine learning model to production? This survey examines several recent systems for serving machine learning models as well as some classic papers describing early efforts in prediction serving.</div></div><div id="acmqueue2018_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@article{acmqueue2018,
 abstract = {What happens when we wish to actually deploy a machine learning model to production? This survey examines several recent systems for serving machine learning models as well as some classic papers describing early efforts in prediction serving.},
 acmid = {3190574},
 address = {New York, NY, USA},
 author = {Dan Crankshaw and Joseph E. Gonzalez and Peter Bailis},
 bdsk-url-1 = {http://doi.acm.org/10.1145/3190574},
 bdsk-url-2 = {https://doi.org/10.1145/3190574},
 doi = {10.1145/3190574},
 issn = {0001-0782},
 issue_date = {August 2018},
 journal = {Commun. ACM},
 keywords = {techreport},
 month = {7},
 number = {8},
 numpages = {5},
 pages = {45--49},
 publisher = {ACM},
 title = {Research for Practice: Prediction-Serving Systems},
 url = {http://doi.acm.org/10.1145/3190574},
 volume = {61},
 year = {2018}
}
</code></pre></div></div>
</div></div>

<div id="eccv2018" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Xin Wang</li>
	<li>Fisher Yu</li>
	<li>Zi-Yi Dou</li>
	<li>Joseph E. Gonzalez</li>
</ul>
</div>
<div class="title">SkipNet: Learning Dynamic Routing in Convolutional Networks</div><div class="venue">Proceedings of the European Conference on Computer Vision (ECCV)</div>
<div class="year">2018</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#eccv2018_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#eccv2018_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://arxiv.org/abs/1711.09485">paper</a></li>
</ul>
</div>
<div class="cards"><div id="eccv2018_abs" class="collapse abstract"><div class="card card-body">While deeper convolutional networks are needed to achieve maximum accuracy in visual perception tasks, for many inputs shallower networks are sufficient. We exploit this observation by learning to skip convolutional layers on a per-input basis. We introduce SkipNet, a modified residual network, that uses a gating network to selectively skip convolutional blocks based on the activations of the previous layer. We formulate the dynamic skipping problem in the context of sequential decision making and propose a hybrid learning algorithm that combines supervised learning and reinforcement learning to address the challenges of non-differentiable skipping decisions. We show SkipNet reduces computation by 30-90% while preserving the accuracy of the original model on four benchmark datasets and outperforms the state-of-the-art dynamic networks and static compression methods. We also qualitatively evaluate the gating policy to reveal a relationship between image scale and saliency and the number of layers skipped.</div></div><div id="eccv2018_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{eccv2018,
 abstract = {While deeper convolutional networks are needed to achieve maximum accuracy in visual perception tasks, for many inputs shallower networks are sufficient. We exploit this observation by learning to skip convolutional layers on a per-input basis. We introduce SkipNet, a modified residual network, that uses a gating network to selectively skip convolutional blocks based on the activations of the previous layer. We formulate the dynamic skipping problem in the context of sequential decision making and propose a hybrid learning algorithm that combines supervised learning and reinforcement learning to address the challenges of non-differentiable skipping decisions. We show SkipNet reduces computation by 30-90% while preserving the accuracy of the original model on four benchmark datasets and outperforms the state-of-the-art dynamic networks and static compression methods. We also qualitatively evaluate the gating policy to reveal a relationship between image scale and saliency and the number of layers skipped.},
 author = {Xin Wang and Fisher Yu and Zi{-}Yi Dou and Joseph E. Gonzalez},
 bdsk-url-1 = {https://arxiv.org/abs/1711.09485},
 booktitle = {Proceedings of the European Conference on Computer Vision ({ECCV})},
 keywords = {peerrev},
 month = {7},
 title = { {SkipNet}: Learning Dynamic Routing in Convolutional Networks},
 url = {https://arxiv.org/abs/1711.09485},
 year = {2018}
}
</code></pre></div></div>
</div></div>

<div id="Wu_2018_CVPR" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Bichen Wu</li>
	<li>Alvin Wan</li>
	<li>Xiangyu Yue</li>
	<li>Peter Jin</li>
	<li>Sicheng Zhao</li>
	<li>Noah Golmant</li>
	<li>Amir Gholaminejad</li>
	<li>Joseph E. Gonzalez</li>
	<li>Kurt Keutzer</li>
</ul>
</div>
<div class="title">Shift: A Zero FLOP, Zero Parameter Alternative to Spatial Convolutions</div><div class="venue">The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)</div>
<div class="year">2018</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Wu_2018_CVPR_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Wu_2018_CVPR_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://arxiv.org/abs/1711.08141">paper</a></li>
</ul>
</div>
<div class="cards"><div id="Wu_2018_CVPR_abs" class="collapse abstract"><div class="card card-body">Neural networks rely on convolutions to aggregate spatial information. However, spatial convolutions are expensive in terms of model size and computation, both of which grow quadratically with respect to kernel size. In this paper, we present a parameter-free, FLOP-free "shift" operation as an alternative to spatial convolutions. We fuse shifts and point-wise convolutions to construct end-to-end trainable shift-based modules, with a hyperparameter characterizing the tradeoff between accuracy and efficiency. To demonstrate the operation's efficacy, we replace ResNet's 3x3 convolutions with shift-based modules for improved CIFAR10 and CIFAR100 accuracy using 60% fewer parameters; we additionally demonstrate the operation's resilience to parameter reduction on ImageNet, outperforming ResNet family members. We finally show the shift operation's applicability across domains, achieving strong performance with fewer parameters on classification, face verification and style transfer.</div></div><div id="Wu_2018_CVPR_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{Wu_2018_CVPR,
 abstract = {Neural networks rely on convolutions to aggregate spatial information. However, spatial convolutions are expensive in terms of model size and computation, both of which grow quadratically with respect to kernel size. In this paper, we present a parameter-free, FLOP-free "shift" operation as an alternative to spatial convolutions. We fuse shifts and point-wise convolutions to construct end-to-end trainable shift-based modules, with a hyperparameter characterizing the tradeoff between accuracy and efficiency. To demonstrate the operation's efficacy, we replace ResNet's 3x3 convolutions with shift-based modules for improved CIFAR10 and CIFAR100 accuracy using 60% fewer parameters; we additionally demonstrate the operation's resilience to parameter reduction on ImageNet, outperforming ResNet family members. We finally show the shift operation's applicability across domains, achieving strong performance with fewer parameters on classification, face verification and style transfer.},
 author = {Bichen Wu and Alvin Wan and Xiangyu Yue and Peter Jin and Sicheng Zhao and Noah Golmant and Amir Gholaminejad and Joseph E. Gonzalez and Kurt Keutzer},
 bdsk-url-1 = {https://arxiv.org/abs/1711.08141},
 booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
 keywords = {peerrev},
 month = {6},
 title = {Shift: A Zero {FLOP}, Zero Parameter Alternative to Spatial Convolutions},
 url = {https://arxiv.org/abs/1711.08141},
 year = {2018}
}
</code></pre></div></div>
</div></div>

<div id="Jain18IWVS" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Samvit Jain</li>
	<li>Joseph E. Gonzalez</li>
</ul>
</div>
<div class="title">Fast Semantic Segmentation on Video Using Block Motion-Based Feature Interpolation</div><div class="venue">The Third International Workshop on Video Segmentation (IWVS)</div>
<div class="year">2018</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Jain18IWVS_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Jain18IWVS_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://arxiv.org/abs/1803.07742">paper</a></li>
</ul>
</div>
<div class="cards"><div id="Jain18IWVS_abs" class="collapse abstract"><div class="card card-body">Convolutional networks optimized for accuracy on challenging, dense prediction tasks are prohibitively slow to run on each frame in a video. The spatial similarity of nearby video frames, however, suggests opportunity to reuse computation. Existing work has explored basic feature reuse and feature warping based on optical flow, but has encountered limits to the speedup attainable with these techniques. In this paper, we present a new, two part approach to accelerating inference on video. First, we propose a fast feature propagation technique that utilizes the block motion vectors present in compressed video (e.g. H.264 codecs) to cheaply propagate features from frame to frame. Second, we develop a novel feature estimation scheme, termed feature interpolation, that fuses features propagated from enclosing keyframes to render accurate feature estimates, even at sparse keyframe frequencies. We evaluate our system on the Cityscapes and CamVid datasets, comparing to both a frame-by-frame baseline and related work. We find that we are able to substantially accelerate segmentation on video, achieving near real-time frame rates (20.1 frames per second) on large images (960 x 720 pixels), while maintaining competitive accuracy. This represents an improvement of almost 6x over the single-frame baseline and 2.5x over the fastest prior work.</div></div><div id="Jain18IWVS_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{Jain18IWVS,
 abstract = {Convolutional networks optimized for accuracy on challenging, dense prediction tasks are prohibitively slow to run on each frame in a video. The spatial similarity of nearby video frames, however, suggests opportunity to reuse computation. Existing work has explored basic feature reuse and feature warping based on optical flow, but has encountered limits to the speedup attainable with these techniques. In this paper, we present a new, two part approach to accelerating inference on video. First, we propose a fast feature propagation technique that utilizes the block motion vectors present in compressed video (e.g. H.264 codecs) to cheaply propagate features from frame to frame. Second, we develop a novel feature estimation scheme, termed feature interpolation, that fuses features propagated from enclosing keyframes to render accurate feature estimates, even at sparse keyframe frequencies. We evaluate our system on the Cityscapes and CamVid datasets, comparing to both a frame-by-frame baseline and related work. We find that we are able to substantially accelerate segmentation on video, achieving near real-time frame rates (20.1 frames per second) on large images (960 x 720 pixels), while maintaining competitive accuracy. This represents an improvement of almost 6x over the single-frame baseline and 2.5x over the fastest prior work.},
 author = {Samvit Jain and Joseph E. Gonzalez},
 bdsk-url-1 = {https://arxiv.org/abs/1803.07742},
 booktitle = {The Third International Workshop on Video Segmentation (IWVS)},
 keywords = {peerrev},
 month = {3},
 title = {Fast Semantic Segmentation on Video Using Block Motion-Based Feature Interpolation},
 url = {https://arxiv.org/abs/1803.07742},
 year = {2018}
}
</code></pre></div></div>
</div></div>

<div id="LearningSys2018" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Xiangxi Mo</li>
	<li>Paras Jain</li>
	<li>Ajay Jain</li>
	<li>Alexey Tumanov</li>
	<li>Joseph E. Gonzalez</li>
	<li>Ion Stoica</li>
</ul>
</div>
<div class="title">A Case for Dynamic GPU Inference Multitenancy and Scheduling</div><div class="venue">Proceedings of the Learning Systems Workshop at NIPS 2018</div>
<div class="year">2018</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#LearningSys2018_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#LearningSys2018_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://learningsys.org/nips18/assets/papers/102CameraReadySubmissionGPU_Virtualization%20(8).pdf">paper</a></li>
</ul>
</div>
<div class="cards"><div id="LearningSys2018_abs" class="collapse abstract"><div class="card card-body">Serving deep neural networks in latency critical interactive settings often requires GPU acceleration. However, the small batch sizes typical in online inference results in poor GPU utilization, a potential performance gap which GPU resource sharing can address. In this paper, we explore several techniques to leverage both temporal and spatial multiplexing to improve GPU utilization for deep learning inference workloads. We evaluate the performance trade-offs of each approach with respect to resource-efficiency, latency predictability, and isolation when compared with conventional batched inference. Our experimental analysis suggests at least a 5x potential for improved utilization through the exploration of more advanced spatial and temporal multiplexing strategies. Our preliminary prototype of a dynamic space-time scheduler demonstrates a 3.18x speedup over space-only multiplexing and a 7.76x speedup over time-only multiplexing, while also providing better isolation and latency predictability.</div></div><div id="LearningSys2018_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{LearningSys2018,
 abstract = {Serving deep neural networks in latency critical interactive settings often requires GPU acceleration. However, the small batch sizes typical in online inference results in poor GPU utilization, a potential performance gap which GPU resource sharing can address. In this paper, we explore several techniques to leverage both temporal and spatial multiplexing to improve GPU utilization for deep learning inference workloads. We evaluate the performance trade-offs of each approach with respect to resource-efficiency, latency predictability, and isolation when compared with conventional batched inference. Our experimental analysis suggests at least a 5x potential for improved utilization through the exploration of more advanced spatial and temporal multiplexing strategies. Our preliminary prototype of a dynamic space-time scheduler demonstrates a 3.18x speedup over space-only multiplexing and a 7.76x speedup over time-only multiplexing, while also providing better isolation and latency predictability.},
 author = {Xiangxi Mo and Paras Jain and Ajay Jain and Alexey Tumanov and Joseph E. Gonzalez and Ion Stoica},
 bdsk-url-1 = {http://learningsys.org/nips18/assets/papers/102CameraReadySubmissionGPU_Virtualization%20(8).pdf},
 booktitle = {Proceedings of the Learning Systems Workshop at NIPS 2018},
 keywords = {peerrev},
 month = {12},
 title = {A Case for Dynamic GPU Inference Multitenancy and Scheduling},
 url = {http://learningsys.org/nips18/assets/papers/102CameraReadySubmissionGPU_Virtualization%20(8).pdf},
 year = {2018}
}
</code></pre></div></div>
</div></div>

<div id="icml_automl2018" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Richard Liaw</li>
	<li>Eric Liang</li>
	<li>Robert Nishihara</li>
	<li>Philipp Moritz</li>
	<li>Joseph E. Gonzalez</li>
	<li>Ion Stoica</li>
</ul>
</div>
<div class="title">Tune: A Research Platform for Distributed Model Selection and Training</div><div class="venue">Proceedings of the ICML Workshop on AutoML</div>
<div class="year">2018</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#icml_automl2018_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#icml_automl2018_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://arxiv.org/abs/1807.05118">paper</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://ray.readthedocs.io/en/latest/tune.html">code</a></li>
</ul>
</div>
<div class="cards"><div id="icml_automl2018_abs" class="collapse abstract"><div class="card card-body">Modern machine learning algorithms are increasingly computationally demanding, requiring specialized hardware and distributed computation to achieve high performance in a reasonable time frame. Many hyperparameter search algorithms have been proposed for improving the efficiency of model selection, however their adaptation to the distributed compute environment is often ad-hoc. We propose Tune, a unified framework for model selection and training that provides a narrow-waist interface between training scripts and search algorithms. We show that this interface meets the requirements for a broad range of hyperparameter search algorithms, allows straightforward scaling of search to large clusters, and simplifies algorithm implementation. We demonstrate the implementation of several state-of-the-art hyperparameter search algorithms in Tune.</div></div><div id="icml_automl2018_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{icml_automl2018,
 abstract = {Modern machine learning algorithms are increasingly computationally demanding, requiring specialized hardware and distributed computation to achieve high performance in a reasonable time frame. Many hyperparameter search algorithms have been proposed for improving the efficiency of model selection, however their adaptation to the distributed compute environment is often ad-hoc. We propose Tune, a unified framework for model selection and training that provides a narrow-waist interface between training scripts and search algorithms. We show that this interface meets the requirements for a broad range of hyperparameter search algorithms, allows straightforward scaling of search to large clusters, and simplifies algorithm implementation. We demonstrate the implementation of several state-of-the-art hyperparameter search algorithms in Tune.},
 author = {Richard Liaw and Eric Liang and Robert Nishihara and Philipp Moritz and Joseph E. Gonzalez and Ion Stoica},
 bdsk-url-1 = {https://arxiv.org/abs/1807.05118},
 booktitle = {Proceedings of the ICML Workshop on AutoML},
 code = {https://ray.readthedocs.io/en/latest/tune.html},
 keywords = {peerrev},
 title = {Tune: A Research Platform for Distributed Model Selection and Training},
 url = {https://arxiv.org/abs/1807.05118},
 year = {2018}
}
</code></pre></div></div>
</div></div>

<div id="Stoica17" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Ion Stoica</li>
	<li>Dawn Song</li>
	<li>Raluca Ada Popa</li>
	<li>David A. Patterson</li>
	<li>Michael W. Mahoney</li>
	<li>Randy H. Katz</li>
	<li>Anthony D. Joseph</li>
	<li>Michael Jordan</li>
	<li>Joseph M. Hellerstein</li>
	<li>Joseph E. Gonzalez</li>
	<li>Ken Goldberg</li>
	<li>Ali Ghodsi</li>
	<li>David E. Culler</li>
	<li>Pieter Abbeel</li>
</ul>
</div>
<div class="title">A Berkeley View of Systems Challenges for AI</div><div class="venue">EECS Department, University of California, Berkeley Technical Report</div>
<div class="year">2017</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Stoica17_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Stoica17_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://www2.eecs.berkeley.edu/Pubs/TechRpts/2017/EECS-2017-159.html">paper</a></li>
</ul>
</div>
<div class="cards"><div id="Stoica17_abs" class="collapse abstract"><div class="card card-body">With the increasing commoditization of computer vision, speech recognition and machine translation systems and the widespread deployment of learning-based back-end technologies such as digital advertising and intelligent infrastructures, AI (Artificial Intelligence) has moved from research labs to production. These changes have been made possible by unprecedented levels of data and computation, by methodological advances in machine learning, by innovations in systems software and architectures, and by the broad accessibility of these technologies.

The next generation of AI systems promises to accelerate these developments and increasingly impact our lives via frequent interactions and making (often mission-critical) decisions on our behalf, often in highly personalized contexts. Realizing this promise, however, raises daunting challenges. In particular, we need AI systems that make timely and safe decisions in unpredictable environments, that are robust against sophisticated adversaries, and that can process ever increasing amounts of data across organizations and individuals without compromising confidentiality. These challenges will be exacerbated by the end of the Moore's Law, which will constrain the amount of data these technologies can store and process. In this paper, we propose several open research directions in systems, architectures, and security that can address these challenges and help unlock AI's potential to improve lives and society.</div></div><div id="Stoica17_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@techreport{Stoica17,
 abstract = {With the increasing commoditization of computer vision, speech recognition and machine translation systems and the widespread deployment of learning-based back-end technologies such as digital advertising and intelligent infrastructures, AI (Artificial Intelligence) has moved from research labs to production. These changes have been made possible by unprecedented levels of data and computation, by methodological advances in machine learning, by innovations in systems software and architectures, and by the broad accessibility of these technologies.

The next generation of AI systems promises to accelerate these developments and increasingly impact our lives via frequent interactions and making (often mission-critical) decisions on our behalf, often in highly personalized contexts. Realizing this promise, however, raises daunting challenges. In particular, we need AI systems that make timely and safe decisions in unpredictable environments, that are robust against sophisticated adversaries, and that can process ever increasing amounts of data across organizations and individuals without compromising confidentiality. These challenges will be exacerbated by the end of the Moore's Law, which will constrain the amount of data these technologies can store and process. In this paper, we propose several open research directions in systems, architectures, and security that can address these challenges and help unlock AI's potential to improve lives and society.},
 author = {Ion Stoica and Dawn Song and Raluca Ada Popa and David A. Patterson and Michael W. Mahoney and Randy H. Katz and Anthony D. Joseph and Michael Jordan and Joseph M. Hellerstein and Joseph E. Gonzalez and Ken Goldberg and Ali Ghodsi and David E. Culler and Pieter Abbeel},
 bdsk-url-1 = {http://www2.eecs.berkeley.edu/Pubs/TechRpts/2017/EECS-2017-159.html},
 institution = {EECS Department, University of California, Berkeley},
 keywords = {techreport},
 month = {9},
 number = {UCB/EECS-2017-159},
 title = {A Berkeley View of Systems Challenges for {AI} },
 url = {http://www2.eecs.berkeley.edu/Pubs/TechRpts/2017/EECS-2017-159.html},
 year = {2017}
}
</code></pre></div></div>
</div></div>

<div id="socc17" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Neeraja J. Yadwadkar</li>
	<li>Bharath Hariharan</li>
	<li>Joseph E. Gonzalez</li>
	<li>Burton Smith</li>
	<li>Randy H. Katz</li>
</ul>
</div>
<div class="title">Selecting the Best VM Across Multiple Public Clouds: A Data-driven Performance Modeling Approach</div><div class="venue">Proceedings of the 2017 Symposium on Cloud Computing</div>
<div class="year">2017</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#socc17_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#socc17_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://doi.acm.org/10.1145/3127479.3131614">paper</a></li>
</ul>
</div>
<div class="cards"><div id="socc17_abs" class="collapse abstract"><div class="card card-body">Users of cloud services are presented with a bewildering choice of VM types and the choice of VM can have significant implications on performance and cost. In this paper we address the fundamental problem of accurately and economically choosing the best VM for a given workload and user goals. To address the problem of optimal VM selection, we present PARIS, a data-driven system that uses a novel hybrid offline and online data collection and modeling framework to provide accurate performance estimates with minimal data collection. PARIS is able to predict workload performance for different user-specified metrics, and resulting costs for a wide range of VM types and workloads across multiple cloud providers. When compared to sophisticated baselines, including collaborative filtering and a linear interpolation model using measured workload performance on two VM types, PARIS produces significantly better estimates of performance. For instance, it reduces runtime prediction error by a factor of 4 for some workloads on both AWS and Azure. The increased accuracy translates into a 45% reduction in user cost while maintaining performance.</div></div><div id="socc17_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{socc17,
 abstract = {Users of cloud services are presented with a bewildering choice of VM types and the choice of VM can have significant implications on performance and cost. In this paper we address the fundamental problem of accurately and economically choosing the best VM for a given workload and user goals. To address the problem of optimal VM selection, we present PARIS, a data-driven system that uses a novel hybrid offline and online data collection and modeling framework to provide accurate performance estimates with minimal data collection. PARIS is able to predict workload performance for different user-specified metrics, and resulting costs for a wide range of VM types and workloads across multiple cloud providers. When compared to sophisticated baselines, including collaborative filtering and a linear interpolation model using measured workload performance on two VM types, PARIS produces significantly better estimates of performance. For instance, it reduces runtime prediction error by a factor of 4 for some workloads on both AWS and Azure. The increased accuracy translates into a 45% reduction in user cost while maintaining performance.},
 acmid = {3131614},
 address = {New York, NY, USA},
 author = {Neeraja J. Yadwadkar and Bharath Hariharan and Joseph E. Gonzalez and Burton Smith and Randy H. Katz},
 bdsk-url-1 = {http://doi.acm.org/10.1145/3127479.3131614},
 bdsk-url-2 = {https://doi.org/10.1145/3127479.3131614},
 booktitle = {Proceedings of the 2017 Symposium on Cloud Computing},
 doi = {10.1145/3127479.3131614},
 isbn = {978-1-4503-5028-0},
 keywords = {peerrev},
 location = {Santa Clara, California},
 month = {9},
 numpages = {14},
 pages = {452--465},
 publisher = {ACM},
 series = {SoCC '17},
 title = {Selecting the Best {VM} Across Multiple Public Clouds: A Data-driven Performance Modeling Approach},
 url = {http://doi.acm.org/10.1145/3127479.3131614},
 year = {2017}
}
</code></pre></div></div>
</div></div>

<div id="aistats17" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Francois W. Belletti</li>
	<li>Evan R. Sparks</li>
	<li>Michael J. Franklin</li>
	<li>Alexandre M. Bayen</li>
	<li>Joseph E. Gonzalez</li>
</ul>
</div>
<div class="title">Random Projection Design for Scalable Implicit Smoothing of Randomly Observed Stochastic Processes</div><div class="venue">Artificial Intelligence and Statistics (AIStats '17)</div>
<div class="year">2017</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#aistats17_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#aistats17_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://proceedings.mlr.press/v54/belletti17a/belletti17a.pdf">paper</a></li>
</ul>
</div>
<div class="cards"><div id="aistats17_abs" class="collapse abstract"><div class="card card-body">Sampling at random timestamps, long range dependencies, and scale hamper standard meth- ods for multivariate time series analysis. In this paper we present a novel estimator for cross-covariance of randomly observed time series which unravels the dynamics of an unobserved stochastic process. We analyze the statistical properties of our estimator without needing the assumption that observation timestamps are independent from the process of interest and show that our solution is not hindered by the issues affecting standard estimators for cross-covariance. We implement and evaluate our statistically sound and scalable approach in the distributed setting using Apache Spark and demonstrate its ability to unravel causal dynamics on both simulations and high-frequency financial trading data.</div></div><div id="aistats17_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{aistats17,
 abstract = {Sampling at random timestamps, long range dependencies, and scale hamper standard meth- ods for multivariate time series analysis. In this paper we present a novel estimator for cross-covariance of randomly observed time series which unravels the dynamics of an unobserved stochastic process. We analyze the statistical properties of our estimator without needing the assumption that observation timestamps are independent from the process of interest and show that our solution is not hindered by the issues affecting standard estimators for cross-covariance. We implement and evaluate our statistically sound and scalable approach in the distributed setting using Apache Spark and demonstrate its ability to unravel causal dynamics on both simulations and high-frequency financial trading data.},
 author = {Francois W. Belletti and Evan R. Sparks and Michael J. Franklin and Alexandre M. Bayen and Joseph E. Gonzalez},
 bdsk-url-1 = {http://proceedings.mlr.press/v54/belletti17a/belletti17a.pdf},
 booktitle = {Artificial Intelligence and Statistics ({AIStats} '17)},
 keywords = {peerrev},
 month = {7},
 title = {Random Projection Design for Scalable Implicit Smoothing of Randomly Observed Stochastic Processes},
 url = {http://proceedings.mlr.press/v54/belletti17a/belletti17a.pdf},
 year = {2017}
}
</code></pre></div></div>
</div></div>

<div id="nsdi17a" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Daniel Crankshaw</li>
	<li>Xin Wang</li>
	<li>Guilio Zhou</li>
	<li>Michael J. Franklin</li>
	<li>Joseph E. Gonzalez</li>
	<li>Ion Stoica</li>
</ul>
</div>
<div class="title">Clipper: A Low-Latency Online Prediction Serving System</div><div class="venue">14th USENIX Symposium on Networked Systems Design and Implementation (NSDI 17)</div>
<div class="year">2017</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#nsdi17a_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#nsdi17a_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://www.usenix.org/conference/nsdi17/technical-sessions/presentation/crankshaw">paper</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://clipper.ai">code</a></li>
</ul>
</div>
<div class="cards"><div id="nsdi17a_abs" class="collapse abstract"><div class="card card-body">Machine learning is being deployed in a growing number of applications which demand real-time, accurate, and robust predictions under heavy query load. However, most machine learning frameworks and systems only address model training and not deployment.

In this paper, we introduce Clipper, a general-purpose low-latency prediction serving system. Interposing between end-user applications and a wide range of machine learning frameworks, Clipper introduces a modular architecture to simplify model deployment across frameworks and applications. Furthermore, by introducing caching, batching, and adaptive model selection techniques, Clipper reduces prediction latency and improves prediction throughput, accuracy, and robustness without modifying the underlying machine learning frameworks. We evaluate Clipper on four common machine learning benchmark datasets and demonstrate its ability to meet the latency, accuracy, and throughput demands of online serving applications. Finally, we compare Clipper to the Tensorflow Serving system and demonstrate that we are able to achieve comparable throughput and latency while enabling model composition and online learning to improve accuracy and render more robust predictions.</div></div><div id="nsdi17a_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{nsdi17a,
 abstract = {Machine learning is being deployed in a growing number of applications which demand real-time, accurate, and robust predictions under heavy query load. However, most machine learning frameworks and systems only address model training and not deployment.

In this paper, we introduce Clipper, a general-purpose low-latency prediction serving system. Interposing between end-user applications and a wide range of machine learning frameworks, Clipper introduces a modular architecture to simplify model deployment across frameworks and applications. Furthermore, by introducing caching, batching, and adaptive model selection techniques, Clipper reduces prediction latency and improves prediction throughput, accuracy, and robustness without modifying the underlying machine learning frameworks. We evaluate Clipper on four common machine learning benchmark datasets and demonstrate its ability to meet the latency, accuracy, and throughput demands of online serving applications. Finally, we compare Clipper to the Tensorflow Serving system and demonstrate that we are able to achieve comparable throughput and latency while enabling model composition and online learning to improve accuracy and render more robust predictions.},
 address = {Boston, MA},
 author = {Daniel Crankshaw and Xin Wang and Guilio Zhou and Michael J. Franklin and Joseph E. Gonzalez and Ion Stoica},
 bdsk-url-1 = {https://www.usenix.org/conference/nsdi17/technical-sessions/presentation/crankshaw},
 booktitle = {14th USENIX Symposium on Networked Systems Design and Implementation (NSDI 17)},
 code = {https://clipper.ai},
 isbn = {978-1-931971-37-9},
 keywords = {peerrev},
 pages = {613--627},
 publisher = {USENIX Association},
 title = {Clipper: A Low-Latency Online Prediction Serving System},
 url = {https://www.usenix.org/conference/nsdi17/technical-sessions/presentation/crankshaw},
 year = {2017}
}
</code></pre></div></div>
</div></div>

<div id="cidr17" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Joseph M. Hellerstein</li>
	<li>Vikram Sreekanti</li>
	<li>Joseph E. Gonzalez</li>
	<li>Sudhansku Arora</li>
	<li>Arka Bhattacharyya</li>
	<li>Shirshanka Das</li>
	<li>Akon Dey</li>
	<li>Mark Donsky</li>
	<li>Gabriel Fierro</li>
	<li>Sreyashi Nag</li>
	<li>Krishna Ramachandran</li>
	<li>Chang She</li>
	<li>Eric Sun</li>
	<li>Carl Steinbach</li>
	<li>Venkat Subramanian</li>
</ul>
</div>
<div class="title">Establishing Common Ground with Data Context</div><div class="venue">Conference on Innovative Data Systems Research (CIDR '17)</div>
<div class="year">2017</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#cidr17_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" href="">paper</a></li>
</ul>
</div>
<div class="cards"><div id="cidr17_abs" class="collapse abstract"><div class="card card-body"></div></div><div id="cidr17_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{cidr17,
 author = {Joseph M. Hellerstein and Vikram Sreekanti and Joseph E. Gonzalez and Sudhansku Arora and Arka Bhattacharyya and Shirshanka Das and Akon Dey and Mark Donsky and Gabriel Fierro and Sreyashi Nag and Krishna Ramachandran and Chang She and Eric Sun and Carl Steinbach and Venkat Subramanian},
 booktitle = {Conference on Innovative Data Systems Research ({CIDR} '17)},
 keywords = {peerrev},
 title = {Establishing Common Ground with Data Context},
 year = {2017}
}
</code></pre></div></div>
</div></div>

<div id="nsdi17b" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Wenting Zheng</li>
	<li>Ankur Dave</li>
	<li>Jethro G. Beekman</li>
	<li>Raluca Ada Popa</li>
	<li>Joseph E. Gonzalez</li>
	<li>Ion Stoica</li>
</ul>
</div>
<div class="title">Opaque: An Oblivious and Encrypted Distributed Analytics Platform</div><div class="venue">14th USENIX Symposium on Networked Systems Design and Implementation (NSDI 17)</div>
<div class="year">2017</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#nsdi17b_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://www.usenix.org/conference/nsdi17/technical-sessions/presentation/zheng">paper</a></li>
</ul>
</div>
<div class="cards"><div id="nsdi17b_abs" class="collapse abstract"><div class="card card-body"></div></div><div id="nsdi17b_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{nsdi17b,
 address = {Boston, MA},
 author = {Wenting Zheng and Ankur Dave and Jethro G. Beekman and Raluca Ada Popa and Joseph E. Gonzalez and Ion Stoica},
 bdsk-url-1 = {https://www.usenix.org/conference/nsdi17/technical-sessions/presentation/zheng},
 booktitle = {14th USENIX Symposium on Networked Systems Design and Implementation (NSDI 17)},
 isbn = {978-1-931971-37-9},
 keywords = {peerrev},
 pages = {283--298},
 publisher = {USENIX Association},
 title = {Opaque: An Oblivious and Encrypted Distributed Analytics Platform},
 url = {https://www.usenix.org/conference/nsdi17/technical-sessions/presentation/zheng},
 year = {2017}
}
</code></pre></div></div>
</div></div>

<div id="acmqueu2016" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Matei Zaharia</li>
	<li>Reynold S. Xin</li>
	<li>Patrick Wendell</li>
	<li>Tathagata Das</li>
	<li>Michael Armbrust</li>
	<li>Ankur Dave</li>
	<li>Xiangrui Meng</li>
	<li>Josh Rosen</li>
	<li>Shivaram Venkataraman</li>
	<li>Michael J. Franklin,</li>
	<li>Ali Ghodsi</li>
	<li>Joseph E. Gonzalez</li>
	<li>Scott Shenker</li>
	<li>Ion Stoica</li>
</ul>
</div>
<div class="title">Apache Spark: A Unified Engine for Big Data Processing</div><div class="venue">Commun. ACM</div>
<div class="year">2016</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#acmqueu2016_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://doi.acm.org/10.1145/2934664">paper</a></li>
</ul>
</div>
<div class="cards"><div id="acmqueu2016_abs" class="collapse abstract"><div class="card card-body"></div></div><div id="acmqueu2016_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@article{acmqueu2016,
 acmid = {2934664},
 address = {New York, NY, USA},
 author = {Matei Zaharia and Reynold S. Xin and Patrick Wendell and Tathagata Das and Michael Armbrust and Ankur Dave and Xiangrui Meng and Josh Rosen and Shivaram Venkataraman and Michael J. Franklin, and Ali Ghodsi and Joseph E. Gonzalez and Scott Shenker and Ion Stoica},
 bdsk-url-1 = {http://doi.acm.org/10.1145/2934664},
 bdsk-url-2 = {https://doi.org/10.1145/2934664},
 doi = {10.1145/2934664},
 issn = {0001-0782},
 issue_date = {November 2016},
 journal = {Commun. ACM},
 keywords = {techreport},
 month = {9},
 number = {11},
 numpages = {10},
 pages = {56--65},
 publisher = {ACM},
 title = {Apache Spark: A Unified Engine for Big Data Processing},
 url = {http://doi.acm.org/10.1145/2934664},
 volume = {59},
 year = {2016}
}
</code></pre></div></div>
</div></div>

<div id="Rong2016" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Rong Gu</li>
	<li>Qianhao Dong</li>
	<li>Haoyuan Li</li>
	<li>Joseph E. Gonzalez</li>
	<li>Zhao Zhang</li>
	<li>Shuai Wang</li>
	<li>Yihua Huang</li>
	<li>Scott Shenker</li>
	<li>Ion Stoica</li>
	<li>Patrick P. C. Lee</li>
</ul>
</div>
<div class="title">DFS-Perf: A Scalable and Unified Benchmarking Framework for Distributed File Systems</div><div class="venue">EECS Department, University of California, Berkeley Technical Report</div>
<div class="year">2016</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#Rong2016_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://www2.eecs.berkeley.edu/Pubs/TechRpts/2016/EECS-2016-133.html">paper</a></li>
</ul>
</div>
<div class="cards"><div id="Rong2016_abs" class="collapse abstract"><div class="card card-body"></div></div><div id="Rong2016_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@techreport{Rong2016,
 author = {Rong Gu and Qianhao Dong and Haoyuan Li and Joseph E. Gonzalez and Zhao Zhang and Shuai Wang and Yihua Huang and Scott Shenker and Ion Stoica and Patrick P. C. Lee},
 bdsk-url-1 = {http://www2.eecs.berkeley.edu/Pubs/TechRpts/2016/EECS-2016-133.html},
 institution = {EECS Department, University of California, Berkeley},
 keywords = {techreport},
 month = {7},
 number = {UCB/EECS-2016-133},
 title = {DFS-Perf: A Scalable and Unified Benchmarking Framework for Distributed File Systems},
 url = {http://www2.eecs.berkeley.edu/Pubs/TechRpts/2016/EECS-2016-133.html},
 year = {2016}
}
</code></pre></div></div>
</div></div>

<div id="grades16" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Ankur Dave</li>
	<li>Alekh Jindal</li>
	<li>Li Erran Li</li>
	<li>Reynold Xin</li>
	<li>Joseph E. Gonzalez</li>
	<li>Matei Zaharia</li>
</ul>
</div>
<div class="title">GraphFrames: An Integrated API for Mixing Graph and Relational Queries.</div><div class="venue">SIGMOD Grades Workshop</div>
<div class="year">2016</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#grades16_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" href="">paper</a></li>
</ul>
</div>
<div class="cards"><div id="grades16_abs" class="collapse abstract"><div class="card card-body"></div></div><div id="grades16_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{grades16,
 author = {Ankur Dave and Alekh Jindal and Li Erran Li and Reynold Xin and Joseph E. Gonzalez and Matei Zaharia},
 booktitle = { {SIGMOD} Grades Workshop},
 keywords = {peerrev},
 title = {GraphFrames: An Integrated API for Mixing Graph and Relational Queries.},
 year = {2016}
}
</code></pre></div></div>
</div></div>

<div id="jmlr2016" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Neeraja J. Yadwadkar</li>
	<li>Bharath Hariharan</li>
	<li>Joseph E. Gonzalez</li>
	<li>Randy Katz</li>
</ul>
</div>
<div class="title">Multi-Task Learning for Straggler Avoiding Predictive Job Scheduling</div><div class="venue">Journal of Machine Learning Research (JMLR '16)</div>
<div class="year">2016</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#jmlr2016_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" href="">paper</a></li>
</ul>
</div>
<div class="cards"><div id="jmlr2016_abs" class="collapse abstract"><div class="card card-body"></div></div><div id="jmlr2016_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{jmlr2016,
 author = {Neeraja J. Yadwadkar and Bharath Hariharan and Joseph E. Gonzalez and Randy Katz},
 booktitle = {Journal of Machine Learning Research ({JMLR} '16)},
 keywords = {peerrev},
 title = {Multi-Task Learning for Straggler Avoiding Predictive Job Scheduling},
 year = {2016}
}
</code></pre></div></div>
</div></div>

<div id="bcb2015" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Veronika Strnadova-Neeley</li>
	<li>Aydin Buluc</li>
	<li>Jarrod Chapman</li>
	<li>John Gilbert</li>
	<li>Joseph E. Gonzalez</li>
	<li>Leonid Oliker</li>
</ul>
</div>
<div class="title">Efficient Data Reduction for Large-Scale Genetic Mapping</div><div class="venue">ACM Conference on Bioinformatics, Computational Biology, and Health Informatics (BCB '15)</div>
<div class="year">2015</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#bcb2015_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" href="">paper</a></li>
</ul>
</div>
<div class="cards"><div id="bcb2015_abs" class="collapse abstract"><div class="card card-body"></div></div><div id="bcb2015_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{bcb2015,
 author = {Veronika Strnadova-Neeley and Aydin Buluc and Jarrod Chapman and John Gilbert and Joseph E. Gonzalez and Leonid Oliker},
 booktitle = { {ACM} Conference on Bioinformatics, Computational Biology, and Health Informatics ({BCB} '15)},
 keywords = {peerrev},
 title = {Efficient Data Reduction for Large-Scale Genetic Mapping},
 year = {2015}
}
</code></pre></div></div>
</div></div>

<div id="sdm15" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Neeraja J. Yadwadkar</li>
	<li>Bharath Hariharan</li>
	<li>Joseph E. Gonzalez</li>
	<li>Randy Katz</li>
</ul>
</div>
<div class="title">Faster Jobs in Distributed Data Processing using Multi-Task Learning</div><div class="venue">SIAM International Conference on Data Mining (SDM '15)</div>
<div class="year">2015</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#sdm15_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" href="">paper</a></li>
</ul>
</div>
<div class="cards"><div id="sdm15_abs" class="collapse abstract"><div class="card card-body"></div></div><div id="sdm15_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{sdm15,
 author = {Neeraja J. Yadwadkar and Bharath Hariharan and Joseph E. Gonzalez and Randy Katz},
 booktitle = { {SIAM} International Conference on Data Mining ({SDM} '15)},
 keywords = {peerrev},
 title = {Faster Jobs in Distributed Data Processing using Multi-Task Learning},
 year = {2015}
}
</code></pre></div></div>
</div></div>

<div id="LearningSys2015" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Daniel Crankshaw</li>
	<li>Xin Wang</li>
	<li>Joseph E. Gonzalez</li>
	<li>Michael J. Franklin</li>
</ul>
</div>
<div class="title">Scalable Training and Serving of Personalized Models</div><div class="venue">Proceedings of the Learning Systems Workshop at NIPS 2015</div>
<div class="year">2015</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#LearningSys2015_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" href="">paper</a></li>
</ul>
</div>
<div class="cards"><div id="LearningSys2015_abs" class="collapse abstract"><div class="card card-body"></div></div><div id="LearningSys2015_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{LearningSys2015,
 author = {Daniel Crankshaw and Xin Wang and Joseph E. Gonzalez and Michael J. Franklin},
 booktitle = {Proceedings of the Learning Systems Workshop at NIPS 2015},
 keywords = {peerrev},
 title = {Scalable Training and Serving of Personalized Models},
 year = {2015}
}
</code></pre></div></div>
</div></div>

<div id="cidr15" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Daniel Crankshaw</li>
	<li>Peter Bailis</li>
	<li>Joseph E. Gonzalez</li>
	<li>Haoyuan Li</li>
	<li>Zhao Zhang</li>
	<li>Michael J. Franklin</li>
	<li>Ali Ghodsi</li>
	<li>Michael I. Jordan</li>
</ul>
</div>
<div class="title">The Missing Piece in Complex Analytics: Low Latency, Scalable Model Management and Serving with Velox</div><div class="venue">Conference on Innovative Data Systems Research (CIDR '15)</div>
<div class="year">2015</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#cidr15_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" href="">paper</a></li>
</ul>
</div>
<div class="cards"><div id="cidr15_abs" class="collapse abstract"><div class="card card-body"></div></div><div id="cidr15_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{cidr15,
 author = {Daniel Crankshaw and Peter Bailis and Joseph E. Gonzalez and Haoyuan Li and Zhao Zhang and Michael J. Franklin and Ali Ghodsi and Michael I. Jordan},
 booktitle = {Conference on Innovative Data Systems Research ({CIDR} '15)},
 keywords = {peerrev},
 title = {The Missing Piece in Complex Analytics: Low Latency, Scalable Model Management and Serving with Velox},
 year = {2015}
}
</code></pre></div></div>
</div></div>

<div id="siam14" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Veronika Strnadova</li>
	<li>Aydin Buluc</li>
	<li>Leonid Oliker</li>
	<li>Joseph E. Gonzalez</li>
	<li>Stefanie Jegelka</li>
	<li>Jarrod Chapman</li>
	<li>John Gilbert</li>
</ul>
</div>
<div class="title">Fast Clustering Methods for Genetic Mapping in Plants</div><div class="venue">16th SIAM Conference on Parallel Processing for Scientific Computing</div>
<div class="year">2014</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#siam14_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" href="">paper</a></li>
</ul>
</div>
<div class="cards"><div id="siam14_abs" class="collapse abstract"><div class="card card-body"></div></div><div id="siam14_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{siam14,
 author = {Veronika Strnadova and Aydin Buluc and Leonid Oliker and Joseph E. Gonzalez and Stefanie Jegelka and Jarrod Chapman and John Gilbert},
 booktitle = {16th SIAM Conference on Parallel Processing for Scientific Computing},
 keywords = {peerrev},
 title = {Fast Clustering Methods for Genetic Mapping in Plants},
 year = {2014}
}
</code></pre></div></div>
</div></div>

<div id="WWW2014" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Joseph E. Gonzalez</li>
</ul>
</div>
<div class="title">From Graphs to Tables the Design of Scalable Systems for Graph Analytics</div><div class="venue">Proceedings of the 23rd International Conference on World Wide Web</div>
<div class="year">2014</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#WWW2014_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://doi.acm.org/10.1145/2567948.2580059">paper</a></li>
</ul>
</div>
<div class="cards"><div id="WWW2014_abs" class="collapse abstract"><div class="card card-body"></div></div><div id="WWW2014_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{WWW2014,
 acmid = {2580059},
 address = {New York, NY, USA},
 author = {Joseph E. Gonzalez},
 bdsk-url-1 = {http://doi.acm.org/10.1145/2567948.2580059},
 bdsk-url-2 = {https://doi.org/10.1145/2567948.2580059},
 booktitle = {Proceedings of the 23rd International Conference on World Wide Web},
 doi = {10.1145/2567948.2580059},
 isbn = {978-1-4503-2745-9},
 keywords = {techreport},
 location = {Seoul, Korea},
 numpages = {2},
 pages = {1149--1150},
 publisher = {ACM},
 series = {WWW '14 Companion},
 title = {From Graphs to Tables the Design of Scalable Systems for Graph Analytics},
 url = {http://doi.acm.org/10.1145/2567948.2580059},
 year = {2014}
}
</code></pre></div></div>
</div></div>

<div id="osdi14" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Joseph E. Gonzalez</li>
	<li>Reynold S. Xin</li>
	<li>Ankur Dave</li>
	<li>Daniel Crankshaw</li>
	<li>Michael J. Franklin</li>
	<li>Ion Stoica</li>
</ul>
</div>
<div class="title">GraphX: Graph Processing in a Distributed Dataflow Framework</div><div class="venue">11th USENIX Symposium on Operating Systems Design and Implementation (OSDI 14)</div>
<div class="year">2014</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#osdi14_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" href="">paper</a></li>
</ul>
</div>
<div class="cards"><div id="osdi14_abs" class="collapse abstract"><div class="card card-body"></div></div><div id="osdi14_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{osdi14,
 author = {Joseph E. Gonzalez and Reynold S. Xin and Ankur Dave and Daniel Crankshaw and Michael J. Franklin and Ion Stoica},
 booktitle = {11th USENIX Symposium on Operating Systems Design and Implementation (OSDI 14)},
 keywords = {peerrev},
 pages = {599--613},
 title = {GraphX: Graph Processing in a Distributed Dataflow Framework},
 year = {2014}
}
</code></pre></div></div>
</div></div>

<div id="nips14" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Xinghao Pan</li>
	<li>Stefanie Jegelka</li>
	<li>Joseph E. Gonzalez</li>
	<li>Joseph K. Bradley</li>
	<li>Michael I. Jordan</li>
</ul>
</div>
<div class="title">Parallel Double Greedy Submodular Maximization</div><div class="venue">Neural Information Processing Systems (NIPS '14)</div>
<div class="year">2014</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#nips14_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" href="">paper</a></li>
</ul>
</div>
<div class="cards"><div id="nips14_abs" class="collapse abstract"><div class="card card-body"></div></div><div id="nips14_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{nips14,
 author = {Xinghao Pan and Stefanie Jegelka and Joseph E. Gonzalez and Joseph K. Bradley and Michael I. Jordan},
 booktitle = {Neural Information Processing Systems ({NIPS} '14)},
 keywords = {peerrev},
 title = {Parallel Double Greedy Submodular Maximization},
 year = {2014}
}
</code></pre></div></div>
</div></div>

<div id="gblasex14" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>David Bader</li>
	<li>Ayd\in Bulu\cc</li>
	<li>John Gilbert</li>
	<li>Joseph E. Gonzalez</li>
	<li>Jeremy Kepner</li>
	<li>Timothy Mattson</li>
</ul>
</div>
<div class="title">The Graph BLAS effort and its implications for Exascale</div><div class="venue">SIAM Workshop on Exascale Applied Mathematics Challenges and Opportunities (EX14)</div>
<div class="year">2014</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#gblasex14_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" href="">paper</a></li>
</ul>
</div>
<div class="cards"><div id="gblasex14_abs" class="collapse abstract"><div class="card card-body"></div></div><div id="gblasex14_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{gblasex14,
 author = {David Bader and Ayd{\i}n Bulu\c{c} and John Gilbert and Joseph E. Gonzalez and Jeremy Kepner and Timothy Mattson},
 booktitle = {SIAM Workshop on Exascale Applied Mathematics Challenges and Opportunities (EX14)},
 keywords = {peerrev},
 title = {The Graph BLAS effort and its implications for Exascale},
 year = {2014}
}
</code></pre></div></div>
</div></div>

<div id="IEEE2013" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>T. Mattson</li>
	<li>D. Bader</li>
	<li>J. Berry</li>
	<li>A. Buluc</li>
	<li>J. Dongarra</li>
	<li>C. Faloutsos</li>
	<li>J. Feo</li>
	<li>J. Gilbert</li>
	<li>J. Gonzalez</li>
	<li>B. Hendrickson</li>
	<li>J. Kepner</li>
	<li>C. Leiserson</li>
	<li>A. Lumsdaine</li>
	<li>D. Padua</li>
	<li>S. Poole</li>
	<li>S. Reinhardt</li>
	<li>M. Stonebraker</li>
	<li>S. Wallach</li>
	<li>A. Yoo</li>
</ul>
</div>
<div class="title">Standards for graph algorithm primitives</div><div class="venue">2013 IEEE High Performance Extreme Computing Conference (HPEC)</div>
<div class="year">2013</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#IEEE2013_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#IEEE2013_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://doi.org/10.1109/HPEC.2013.6670338">paper</a></li>
</ul>
</div>
<div class="cards"><div id="IEEE2013_abs" class="collapse abstract"><div class="card card-body">It is our view that the state of the art in constructing a large collection of graph algorithms in terms of linear algebraic operations is mature enough to support the emergence of a standard set of primitive building blocks. This paper is a position paper defining the problem and announcing our intention to launch an open effort to define this standard.</div></div><div id="IEEE2013_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{IEEE2013,
 abstract = {It is our view that the state of the art in constructing a large collection of graph algorithms in terms of linear algebraic operations is mature enough to support the emergence of a standard set of primitive building blocks. This paper is a position paper defining the problem and announcing our intention to launch an open effort to define this standard.},
 author = {T. Mattson and D. Bader and J. Berry and A. Buluc and J. Dongarra and C. Faloutsos and J. Feo and J. Gilbert and J. Gonzalez and B. Hendrickson and J. Kepner and C. Leiserson and A. Lumsdaine and D. Padua and S. Poole and S. Reinhardt and M. Stonebraker and S. Wallach and A. Yoo},
 bdsk-url-1 = {https://doi.org/10.1109/HPEC.2013.6670338},
 booktitle = {2013 IEEE High Performance Extreme Computing Conference (HPEC)},
 doi = {10.1109/HPEC.2013.6670338},
 keywords = {peerrev},
 month = {9},
 pages = {1-2},
 title = {Standards for graph algorithm primitives},
 url = {https://doi.org/10.1109/HPEC.2013.6670338},
 year = {2013}
}
</code></pre></div></div>
</div></div>

<div id="icdm13" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Evan Sparks,</li>
	<li>Ameet Talwalkar</li>
	<li>Virginia Smith</li>
	<li>Xinghao Pan</li>
	<li>Joseph E. Gonzalez</li>
	<li>Tim Kraska</li>
	<li>Michael I. Jordan</li>
	<li>Michael J. Franklin</li>
</ul>
</div>
<div class="title">MLI: An API for Distributed Machine Learning</div><div class="venue">International Conference on Data Mining (ICDM)</div>
<div class="year">2013</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#icdm13_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#icdm13_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://ieeexplore.ieee.org/abstract/document/6729619">paper</a></li>
</ul>
</div>
<div class="cards"><div id="icdm13_abs" class="collapse abstract"><div class="card card-body">MLI is an Application Programming Interface designed to address the challenges of building Machine Learning algorithms in a distributed setting based on data-centric computing. Its primary goal is to simplify the development of high-performance, scalable, distributed algorithms. Our initial results show that, relative to existing systems, this interface can be used to build distributed implementations of a wide variety of common Machine Learning algorithms with minimal complexity and highly competitive performance and scalability.</div></div><div id="icdm13_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{icdm13,
 abstract = {MLI is an Application Programming Interface designed to address the challenges of building Machine Learning algorithms in a distributed setting based on data-centric computing. Its primary goal is to simplify the development of high-performance, scalable, distributed algorithms. Our initial results show that, relative to existing systems, this interface can be used to build distributed implementations of a wide variety of common Machine Learning algorithms with minimal complexity and highly competitive performance and scalability.},
 author = {Evan Sparks, and Ameet Talwalkar and Virginia Smith and Xinghao Pan and Joseph E. Gonzalez and Tim Kraska and Michael I. Jordan and Michael J. Franklin},
 bdsk-url-1 = {https://ieeexplore.ieee.org/abstract/document/6729619},
 booktitle = {International Conference on Data Mining (ICDM)},
 keywords = {peerrev},
 month = {12},
 organization = {IEEE},
 title = { {MLI}: An API for Distributed Machine Learning},
 url = {https://ieeexplore.ieee.org/abstract/document/6729619},
 year = {2013}
}
</code></pre></div></div>
</div></div>

<div id="sigmod13" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Reynold Xin</li>
	<li>Joseph E. Gonzalez</li>
	<li>Michael Franklin</li>
	<li>Ion Stoica</li>
</ul>
</div>
<div class="title">GraphX: A Resilient Distributed Graph System on Spark</div><div class="venue">SIGMOD Grades Workshop</div>
<div class="year">2013</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#sigmod13_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#sigmod13_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://dl.acm.org/citation.cfm?id=2484427">paper</a></li>
</ul>
</div>
<div class="cards"><div id="sigmod13_abs" class="collapse abstract"><div class="card card-body">From social networks to targeted advertising, big graphs capture the structure in data and are central to recent advances in machine learning and data mining. Unfortunately, directly applying existing data-parallel tools to graph computation tasks can be cumbersome and inefficient. The need for intuitive, scalable tools for graph computation has lead to the development of new graph-parallel systems (e.g., Pregel, PowerGraph) which are designed to efficiently execute graph algorithms. Unfortunately, these new graph-parallel systems do not address the challenges of graph construction and transformation which are often just as problematic as the subsequent computation. Furthermore, existing graph-parallel systems provide limited fault-tolerance and support for interactive data mining.

We introduce GraphX, which combines the advantages of both data-parallel and graph-parallel systems by efficiently expressing graph computation within the Spark data-parallel framework. We leverage new ideas in distributed graph representation to efficiently distribute graphs as tabular data-structures. Similarly, we leverage advances in data-flow systems to exploit in-memory computation and fault-tolerance. We provide powerful new operations to simplify graph construction and transformation. Using these primitives we implement the PowerGraph and Pregel abstractions in less than 20 lines of code. Finally, by exploiting the Scala foundation of Spark, we enable users to interactively load, transform, and compute on massive graphs.</div></div><div id="sigmod13_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{sigmod13,
 abstract = {From social networks to targeted advertising, big graphs capture the structure in data and are central to recent advances in machine learning and data mining. Unfortunately, directly applying existing data-parallel tools to graph computation tasks can be cumbersome and inefficient. The need for intuitive, scalable tools for graph computation has lead to the development of new graph-parallel systems (e.g., Pregel, PowerGraph) which are designed to efficiently execute graph algorithms. Unfortunately, these new graph-parallel systems do not address the challenges of graph construction and transformation which are often just as problematic as the subsequent computation. Furthermore, existing graph-parallel systems provide limited fault-tolerance and support for interactive data mining.

We introduce GraphX, which combines the advantages of both data-parallel and graph-parallel systems by efficiently expressing graph computation within the Spark data-parallel framework. We leverage new ideas in distributed graph representation to efficiently distribute graphs as tabular data-structures. Similarly, we leverage advances in data-flow systems to exploit in-memory computation and fault-tolerance. We provide powerful new operations to simplify graph construction and transformation. Using these primitives we implement the PowerGraph and Pregel abstractions in less than 20 lines of code. Finally, by exploiting the Scala foundation of Spark, we enable users to interactively load, transform, and compute on massive graphs.},
 author = {Reynold Xin and Joseph E. Gonzalez and Michael Franklin and Ion Stoica},
 bdsk-url-1 = {https://dl.acm.org/citation.cfm?id=2484427},
 booktitle = { {SIGMOD} Grades Workshop},
 keywords = {peerrev},
 title = {GraphX: A Resilient Distributed Graph System on Spark},
 url = {https://dl.acm.org/citation.cfm?id=2484427},
 year = {2013}
}
</code></pre></div></div>
</div></div>

<div id="nips13" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Xinghao Pan</li>
	<li>Joseph E. Gonzalez</li>
	<li>Stefanie Jegelka</li>
	<li>Tamara Broderick</li>
	<li>Michael I. Jordan</li>
</ul>
</div>
<div class="title">Optimistic Concurrency Control for Distributed Unsupervised Learning</div><div class="venue">NIPS '13</div>
<div class="year">2013</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#nips13_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#nips13_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://arxiv.org/abs/1307.8049">paper</a></li>
</ul>
</div>
<div class="cards"><div id="nips13_abs" class="collapse abstract"><div class="card card-body">Research on distributed machine learning algorithms has focused primarily on one of two extremes - algorithms that obey strict concurrency constraints or algorithms that obey few or no such constraints. We consider an intermediate alternative in which algorithms optimistically assume that conflicts are unlikely and if conflicts do arise a conflict-resolution protocol is invoked. We view this "optimistic concurrency control" paradigm as particularly appropriate for large-scale machine learning algorithms, particularly in the unsupervised setting. We demonstrate our approach in three problem areas: clustering, feature learning and online facility location. We evaluate our methods via large-scale experiments in a cluster computing environment.</div></div><div id="nips13_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{nips13,
 abstract = {Research on distributed machine learning algorithms has focused primarily on one of two extremes - algorithms that obey strict concurrency constraints or algorithms that obey few or no such constraints. We consider an intermediate alternative in which algorithms optimistically assume that conflicts are unlikely and if conflicts do arise a conflict-resolution protocol is invoked. We view this "optimistic concurrency control" paradigm as particularly appropriate for large-scale machine learning algorithms, particularly in the unsupervised setting. We demonstrate our approach in three problem areas: clustering, feature learning and online facility location. We evaluate our methods via large-scale experiments in a cluster computing environment.},
 author = {Xinghao Pan and Joseph E. Gonzalez and Stefanie Jegelka and Tamara Broderick and Michael I. Jordan},
 bdsk-url-1 = {https://arxiv.org/abs/1307.8049},
 booktitle = { {NIPS} '13},
 keywords = {peerrev},
 title = {Optimistic Concurrency Control for Distributed Unsupervised Learning},
 url = {https://arxiv.org/abs/1307.8049},
 year = {2013}
}
</code></pre></div></div>
</div></div>

<div id="vldb2012" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Yucheng Low AND Joseph E. Gonzalez AND Aapo Kyrola AND Danny Bickson AND Carlos Guestrin AND Joseph M. Hellerstein</li>
</ul>
</div>
<div class="title">Distributed GraphLab: A Framework for Machine Learning and Data Mining in the Cloud.</div><div class="venue">Proceedings of Very Large Data Bases (PVLDB)</div>
<div class="year">2012</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#vldb2012_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#vldb2012_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://arxiv.org/abs/1204.6078">paper</a></li>
</ul>
</div>
<div class="cards"><div id="vldb2012_abs" class="collapse abstract"><div class="card card-body">While high-level data parallel frameworks, like MapReduce, simplify the design and implementation of large-scale data processing systems, they do not naturally or efficiently support many important data mining and machine learning algorithms and can lead to inefficient learning systems. To help fill this critical void, we introduced the GraphLab abstraction which naturally expresses asynchronous, dynamic, graph-parallel computation while ensuring data consistency and achieving a high degree of parallel performance in the shared-memory setting. In this paper, we extend the GraphLab framework to the substantially more challenging distributed setting while preserving strong data consistency guarantees. We develop graph based extensions to pipelined locking and data versioning to reduce network congestion and mitigate the effect of network latency. We also introduce fault tolerance to the GraphLab abstraction using the classic Chandy-Lamport snapshot algorithm and demonstrate how it can be easily implemented by exploiting the GraphLab abstraction itself. Finally, we evaluate our distributed implementation of the GraphLab abstraction on a large Amazon EC2 deployment and show 1-2 orders of magnitude performance gains over Hadoop-based implementations.</div></div><div id="vldb2012_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{vldb2012,
 abstract = {While high-level data parallel frameworks, like MapReduce, simplify the design and implementation of large-scale data processing systems, they do not naturally or efficiently support many important data mining and machine learning algorithms and can lead to inefficient learning systems. To help fill this critical void, we introduced the GraphLab abstraction which naturally expresses asynchronous, dynamic, graph-parallel computation while ensuring data consistency and achieving a high degree of parallel performance in the shared-memory setting. In this paper, we extend the GraphLab framework to the substantially more challenging distributed setting while preserving strong data consistency guarantees. We develop graph based extensions to pipelined locking and data versioning to reduce network congestion and mitigate the effect of network latency. We also introduce fault tolerance to the GraphLab abstraction using the classic Chandy-Lamport snapshot algorithm and demonstrate how it can be easily implemented by exploiting the GraphLab abstraction itself. Finally, we evaluate our distributed implementation of the GraphLab abstraction on a large Amazon EC2 deployment and show 1-2 orders of magnitude performance gains over Hadoop-based implementations.},
 author = {Yucheng Low AND Joseph E. Gonzalez AND Aapo Kyrola AND Danny Bickson AND Carlos Guestrin AND Joseph M. Hellerstein},
 bdsk-url-1 = {https://arxiv.org/abs/1204.6078},
 booktitle = {Proceedings of Very Large Data Bases (PVLDB)},
 keywords = {peerrev},
 month = {8},
 title = {Distributed GraphLab: A Framework for Machine Learning and Data Mining in the Cloud.},
 url = {https://arxiv.org/abs/1204.6078},
 year = {2012}
}
</code></pre></div></div>
</div></div>

<div id="osdi12" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Joseph E. Gonzalez</li>
	<li>Yucheng Low</li>
	<li>Haijie Gu</li>
	<li>Danny Bickson</li>
	<li>Carlos Guestrin</li>
</ul>
</div>
<div class="title">PowerGraph: Distributed Graph-Parallel Computation on Natural Graphs</div><div class="venue">OSDI '12</div>
<div class="year">2012</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#osdi12_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#osdi12_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://www.usenix.org/system/files/conference/osdi12/osdi12-final-167.pdf">paper</a></li>
</ul>
</div>
<div class="cards"><div id="osdi12_abs" class="collapse abstract"><div class="card card-body">Large-scale graph-structured computation is central to tasks ranging from targeted advertising to natural language processing and has led to the development of several graph-parallel abstractions including Pregel and GraphLab. However, the natural graphs commonly found in the real-world have highly skewed power-law degree distributions, which challenge the assumptions made by these abstractions, limiting performance and scalability.

In this paper, we characterize the challenges of computation on natural graphs in the context of existing graphparallel abstractions. We then introduce the PowerGraph abstraction which exploits the internal structure of graph programs to address these challenges. Leveraging the PowerGraph abstraction we introduce a new approach to distributed graph placement and representation that exploits the structure of power-law graphs. We provide a detailed analysis and experimental evaluation comparing PowerGraph to two popular graph-parallel systems. Finally, we describe three different implementation strategies for PowerGraph and discuss their relative merits with empirical evaluations on large-scale real-world problems demonstrating order of magnitude gains.
</div></div><div id="osdi12_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{osdi12,
 abstract = {Large-scale graph-structured computation is central to tasks ranging from targeted advertising to natural language processing and has led to the development of several graph-parallel abstractions including Pregel and GraphLab. However, the natural graphs commonly found in the real-world have highly skewed power-law degree distributions, which challenge the assumptions made by these abstractions, limiting performance and scalability.

In this paper, we characterize the challenges of computation on natural graphs in the context of existing graphparallel abstractions. We then introduce the PowerGraph abstraction which exploits the internal structure of graph programs to address these challenges. Leveraging the PowerGraph abstraction we introduce a new approach to distributed graph placement and representation that exploits the structure of power-law graphs. We provide a detailed analysis and experimental evaluation comparing PowerGraph to two popular graph-parallel systems. Finally, we describe three different implementation strategies for PowerGraph and discuss their relative merits with empirical evaluations on large-scale real-world problems demonstrating order of magnitude gains.
},
 author = {Joseph E. Gonzalez and Yucheng Low and Haijie Gu and Danny Bickson and Carlos Guestrin},
 bdsk-url-1 = {https://www.usenix.org/system/files/conference/osdi12/osdi12-final-167.pdf},
 booktitle = { {OSDI} '12},
 keywords = {peerrev},
 title = {PowerGraph: Distributed Graph-Parallel Computation on Natural Graphs},
 url = {https://www.usenix.org/system/files/conference/osdi12/osdi12-final-167.pdf},
 year = {2012}
}
</code></pre></div></div>
</div></div>

<div id="wsdm2012" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Amr Ahmed</li>
	<li>Mohamed Aly</li>
	<li>Joseph Gonzalez</li>
	<li>Shravan Narayanamurthy</li>
	<li>Alex Smola</li>
</ul>
</div>
<div class="title">Scalable Inference in Latent Variable Models</div><div class="venue">Conference on Web Search and Data Mining (WSDM)</div>
<div class="year">2012</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#wsdm2012_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#wsdm2012_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://www.cs.cmu.edu/~jegonzal/papers/ahmed_scalable_inference_in_latent_variable_models.pdf">paper</a></li>
</ul>
</div>
<div class="cards"><div id="wsdm2012_abs" class="collapse abstract"><div class="card card-body">Latent variable techniques are pivotal in tasks ranging from predicting user click patterns and targeting ads to organizing the news and managing user generated content. Latent variable techniques like topic modeling, clustering, and subspace estimation provide substantial insight into the latent structure of complex data with little or no external guidance making them ideal for reasoning about large-scale, rapidly evolving datasets. Unfortunately, due to the data dependencies and global state introduced by latent variables and the iterative nature of latent variable inference, latent-variable techniques are often prohibitively expensive to apply to large-scale, streaming datasets.

In this paper we present a scalable parallel framework for efficient inference in latent variable models over streaming web-scale data. Our framework addresses three key challenges: 1) synchronizing the global state which includes global latent variables (e.g., cluster centers and dictionaries); 2) efficiently storing and retrieving the large local state which includes the data-points and their corresponding latent variables (e.g., cluster membership); and 3) sequentially incorporating streaming data (e.g., the news). We address these challenges by introducing: 1) a novel delta-based aggregation system with a bandwidth-efficient communication protocol; 2) schedule-aware out-of-core storage; and 3) approximate forward sampling to rapidly incorporate new data. We demonstrate state-of-the-art performance of our framework by easily tackling datasets two orders of magnitude larger than those addressed by the current state-of-the-art. Furthermore, we provide an optimized and easily customizable open-source implementation of the framework</div></div><div id="wsdm2012_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{wsdm2012,
 abstract = {Latent variable techniques are pivotal in tasks ranging from predicting user click patterns and targeting ads to organizing the news and managing user generated content. Latent variable techniques like topic modeling, clustering, and subspace estimation provide substantial insight into the latent structure of complex data with little or no external guidance making them ideal for reasoning about large-scale, rapidly evolving datasets. Unfortunately, due to the data dependencies and global state introduced by latent variables and the iterative nature of latent variable inference, latent-variable techniques are often prohibitively expensive to apply to large-scale, streaming datasets.

In this paper we present a scalable parallel framework for efficient inference in latent variable models over streaming web-scale data. Our framework addresses three key challenges: 1) synchronizing the global state which includes global latent variables (e.g., cluster centers and dictionaries); 2) efficiently storing and retrieving the large local state which includes the data-points and their corresponding latent variables (e.g., cluster membership); and 3) sequentially incorporating streaming data (e.g., the news). We address these challenges by introducing: 1) a novel delta-based aggregation system with a bandwidth-efficient communication protocol; 2) schedule-aware out-of-core storage; and 3) approximate forward sampling to rapidly incorporate new data. We demonstrate state-of-the-art performance of our framework by easily tackling datasets two orders of magnitude larger than those addressed by the current state-of-the-art. Furthermore, we provide an optimized and easily customizable open-source implementation of the framework},
 author = {Amr Ahmed and Mohamed Aly and Joseph Gonzalez and Shravan Narayanamurthy and Alex Smola},
 bdsk-url-1 = {http://www.cs.cmu.edu/~jegonzal/papers/ahmed_scalable_inference_in_latent_variable_models.pdf},
 booktitle = {Conference on Web Search and Data Mining (WSDM)},
 keywords = {peerrev},
 title = {Scalable Inference in Latent Variable Models},
 url = {http://www.cs.cmu.edu/~jegonzal/papers/ahmed_scalable_inference_in_latent_variable_models.pdf},
 year = {2012}
}
</code></pre></div></div>
</div></div>

<div id="aistats2011" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Joseph E. Gonzalez</li>
	<li>Yucheng Low</li>
	<li>Arthur Gretton</li>
	<li>Carlos Guestrin</li>
</ul>
</div>
<div class="title">Parallel Gibbs Sampling: From Colored Fields to Thin Junction Trees</div><div class="venue">Artificial Intelligence and Statistics (AISTATS)</div>
<div class="year">2011</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#aistats2011_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#aistats2011_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://proceedings.mlr.press/v15/gonzalez11a.html">paper</a></li>
</ul>
</div>
<div class="cards"><div id="aistats2011_abs" class="collapse abstract"><div class="card card-body">We explore the task of constructing a parallel Gibbs sampler, to both improve mixing and the exploration of high likelihood states. Recent work in parallel Gibbs sampling has focused on update schedules which do not guarantee convergence to the intended stationary distribution. In this work, we propose two methods to construct parallel Gibbs samplers guaranteed to draw from the targeted distribution. The first method, called the Chromatic sampler, uses graph coloring to construct a direct parallelization of the classic sequential scan Gibbs sampler. In the case of 2-colorable models we relate the Chromatic sampler to the Synchronous Gibbs sampler (which draws all variables simultaneously in parallel), and reveal new ergodic properties of Synchronous Gibbs chains. Our second method, the Splash sampler, is a complementary strategy which can be used when the variables are tightly coupled. This constructs and samples multiple blocks in parallel, using a novel locking protocol and an iterative junction tree generation algorithm. We further improve the Splash sampler through adaptive tree construction. We demonstrate the benefits of our two sampling algorithms on large synthetic and real-world models using a 32 processor multi-core system.</div></div><div id="aistats2011_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{aistats2011,
 abstract = {We explore the task of constructing a parallel Gibbs sampler, to both improve mixing and the exploration of high likelihood states. Recent work in parallel Gibbs sampling has focused on update schedules which do not guarantee convergence to the intended stationary distribution. In this work, we propose two methods to construct parallel Gibbs samplers guaranteed to draw from the targeted distribution. The first method, called the Chromatic sampler, uses graph coloring to construct a direct parallelization of the classic sequential scan Gibbs sampler. In the case of 2-colorable models we relate the Chromatic sampler to the Synchronous Gibbs sampler (which draws all variables simultaneously in parallel), and reveal new ergodic properties of Synchronous Gibbs chains. Our second method, the Splash sampler, is a complementary strategy which can be used when the variables are tightly coupled. This constructs and samples multiple blocks in parallel, using a novel locking protocol and an iterative junction tree generation algorithm. We further improve the Splash sampler through adaptive tree construction. We demonstrate the benefits of our two sampling algorithms on large synthetic and real-world models using a 32 processor multi-core system.},
 author = {Joseph E. Gonzalez and Yucheng Low and Arthur Gretton and Carlos Guestrin},
 bdsk-url-1 = {http://proceedings.mlr.press/v15/gonzalez11a.html},
 booktitle = {Artificial Intelligence and Statistics (AISTATS)},
 keywords = {peerrev},
 month = {5},
 title = {Parallel Gibbs Sampling: From Colored Fields to Thin Junction Trees},
 url = {http://proceedings.mlr.press/v15/gonzalez11a.html},
 year = {2011}
}
</code></pre></div></div>
</div></div>

<div id="uai2010" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Yucheng Low</li>
	<li>Joseph E. Gonzalez</li>
	<li>Aapo Kyrola</li>
	<li>Daniel Bickson</li>
	<li>Carlos Guestrin</li>
	<li>Joseph M. Hellerstein</li>
</ul>
</div>
<div class="title">GraphLab: A New Parallel Framework for Machine Learning</div><div class="venue">Conference on Uncertainty in Artificial Intelligence (UAI)</div>
<div class="year">2010</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#uai2010_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#uai2010_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://arxiv.org/abs/1006.4990">paper</a></li>
</ul>
</div>
<div class="cards"><div id="uai2010_abs" class="collapse abstract"><div class="card card-body">Designing and implementing efficient, provably correct parallel machine learning (ML) algorithms is challenging. Existing high-level parallel abstractions like MapReduce are insufficiently expressive while low-level tools like MPI and Pthreads leave ML experts repeatedly solving the same design challenges. By targeting common patterns in ML, we developed GraphLab, which improves upon abstractions like MapReduce by compactly expressing asynchronous iterative algorithms with sparse computational dependencies while ensuring data consistency and achieving a high degree of parallel performance. We demonstrate the expressiveness of the GraphLab framework by designing and implementing parallel versions of belief propagation, Gibbs sampling, Co-EM, Lasso and Compressed Sensing. We show that using GraphLab we can achieve excellent parallel performance on large scale real-world problems.</div></div><div id="uai2010_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{uai2010,
 abstract = {Designing and implementing efficient, provably correct parallel machine learning (ML) algorithms is challenging. Existing high-level parallel abstractions like MapReduce are insufficiently expressive while low-level tools like MPI and Pthreads leave ML experts repeatedly solving the same design challenges. By targeting common patterns in ML, we developed GraphLab, which improves upon abstractions like MapReduce by compactly expressing asynchronous iterative algorithms with sparse computational dependencies while ensuring data consistency and achieving a high degree of parallel performance. We demonstrate the expressiveness of the GraphLab framework by designing and implementing parallel versions of belief propagation, Gibbs sampling, Co-EM, Lasso and Compressed Sensing. We show that using GraphLab we can achieve excellent parallel performance on large scale real-world problems.},
 author = {Yucheng Low and Joseph E. Gonzalez and Aapo Kyrola and Daniel Bickson and Carlos Guestrin and Joseph M. Hellerstein},
 bdsk-url-1 = {https://arxiv.org/abs/1006.4990},
 booktitle = {Conference on Uncertainty in Artificial Intelligence (UAI)},
 keywords = {peerrev},
 title = {GraphLab: A New Parallel Framework for Machine Learning},
 url = {https://arxiv.org/abs/1006.4990},
 year = {2010}
}
</code></pre></div></div>
</div></div>

<div id="uai2009" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Joseph E. Gonzalez</li>
	<li>Yucheng Low</li>
	<li>Carlos Guestrin</li>
	<li>David O'Hallaron</li>
</ul>
</div>
<div class="title">Distributed Parallel Inference on Large Factor Graphs</div><div class="venue">Conference on Uncertainty in Artificial Intelligence (UAI)</div>
<div class="year">2009</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#uai2009_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#uai2009_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="https://arxiv.org/pdf/1205.2645.pdf">paper</a></li>
</ul>
</div>
<div class="cards"><div id="uai2009_abs" class="collapse abstract"><div class="card card-body">As computer clusters become more common and the size of the problems encountered in the field of AI grows, there is an increasing demand for efficient parallel inference algorithms. We consider the problem of parallel inference on large factor graphs in the distributed memory setting of computer clusters. We develop a new efficient parallel inference algorithm, DBRSplash, which incorporates over-segmented graph partitioning, belief residual scheduling, and uniform work Splash operations. We empirically evaluate the DBRSplash algorithm on a 120 processor cluster and demonstrate linear to super-linear performance gains on large factor graph models.</div></div><div id="uai2009_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{uai2009,
 abstract = {As computer clusters become more common and the size of the problems encountered in the field of AI grows, there is an increasing demand for efficient parallel inference algorithms. We consider the problem of parallel inference on large factor graphs in the distributed memory setting of computer clusters. We develop a new efficient parallel inference algorithm, DBRSplash, which incorporates over-segmented graph partitioning, belief residual scheduling, and uniform work Splash operations. We empirically evaluate the DBRSplash algorithm on a 120 processor cluster and demonstrate linear to super-linear performance gains on large factor graph models.},
 author = {Joseph E. Gonzalez and Yucheng Low and Carlos Guestrin and David O'Hallaron},
 bdsk-url-1 = {https://arxiv.org/pdf/1205.2645.pdf},
 booktitle = {Conference on Uncertainty in Artificial Intelligence (UAI)},
 keywords = {peerrev},
 month = {7},
 title = {Distributed Parallel Inference on Large Factor Graphs},
 url = {https://arxiv.org/pdf/1205.2645.pdf},
 year = {2009}
}
</code></pre></div></div>
</div></div>

<div id="aistats2009" class="publication">
<div class="summary"><div class="authors">
<ul class="author">
	<li>Joseph E. Gonzalez</li>
	<li>Yucheng Low</li>
	<li>Carlos Guestrin</li>
</ul>
</div>
<div class="title">Residual Splash for Optimally Parallelizing Belief Propagation</div><div class="venue">Artificial Intelligence and Statistics (AISTATS)</div>
<div class="year">2009</div></div><div class="links">
<ul>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#aistats2009_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>
	<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#aistats2009_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>
	<li><a class="btn btn-primary btn-sm" href="http://proceedings.mlr.press/v5/gonzalez09a.html">paper</a></li>
</ul>
</div>
<div class="cards"><div id="aistats2009_abs" class="collapse abstract"><div class="card card-body">As computer architectures move towards parallelism we must build a new theoretical understanding of parallelism in machine learning. In this paper we focus on parallelizing message passing inference algorithms in graphical models. We develop a theoretical understanding of the limitations of parallelism in belief propagation and bound the optimal achievable running parallel performance on a certain class of graphical models. We demonstrate that the fully synchronous parallelization of belief propagation is highly inefficient. We provide a new parallel belief propagation which achieves optimal performance on a certain class of graphical models. Using two challenging real-world problems, we empirically evaluate the performance of our algorithm. On the real-world problems, we find that our new algorithm achieves near linear performance improvements and out performs alternative parallel belief propagation algorithms.</div></div><div id="aistats2009_bib" class="collapse bibtex-entry"><div class="card card-body"><pre><code class="language-bib" data-lang="bib">
@inproceedings{aistats2009,
 abstract = {As computer architectures move towards parallelism we must build a new theoretical understanding of parallelism in machine learning. In this paper we focus on parallelizing message passing inference algorithms in graphical models. We develop a theoretical understanding of the limitations of parallelism in belief propagation and bound the optimal achievable running parallel performance on a certain class of graphical models. We demonstrate that the fully synchronous parallelization of belief propagation is highly inefficient. We provide a new parallel belief propagation which achieves optimal performance on a certain class of graphical models. Using two challenging real-world problems, we empirically evaluate the performance of our algorithm. On the real-world problems, we find that our new algorithm achieves near linear performance improvements and out performs alternative parallel belief propagation algorithms.},
 author = {Joseph E. Gonzalez and Yucheng Low and Carlos Guestrin},
 bdsk-url-1 = {http://proceedings.mlr.press/v5/gonzalez09a.html},
 booktitle = {Artificial Intelligence and Statistics (AISTATS)},
 keywords = {peerrev},
 month = {4},
 title = {Residual Splash for Optimally Parallelizing Belief Propagation},
 url = {http://proceedings.mlr.press/v5/gonzalez09a.html},
 year = {2009}
}
</code></pre></div></div>
</div></div>

