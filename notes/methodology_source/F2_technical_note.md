# Figure 2 — methodological note

## 1. Objective

This note describes how policy attention to artificial intelligence has changed pre vs post the release of ChatGPT (cutoff 1 December 2022) across the agendas of five international bodies covering AI in finance. The database is the same 387 documents used in Figures 0 and 1, drawn from BIS, FATF, FSB, IMF, OECD, and the World Bank. Two methods are applied in parallel and reported as separate panels. The first is supervised, hand-coded by an expert against a fixed codebook. The second is semi-supervised, recovering categories from the text under codebook guidance.

## 2. Supervised: hand-coded actor-problem framing

Each document is read and coded by hand against a fixed codebook of problems and actors. For each actor mentioned in the document, the coder records which problems that actor frames and how dominant that actor is in the document's framing. The dumbbell plot in the figure is built directly from these hand-coded labels.

### 2.1 Schema

Each document produces rows in three related tables. The spine table holds one row per document with institutional metadata. An actors table holds one or more rows per document, identifying the actors and ranking their dominance. A problems table holds one row per document-actor pair, listing the problems that actor frames within the document, with the most dominant problem first. The full architecture is documented in the database-architecture reference accompanying the demo.

The codebook contains eleven problem categories: capacity and governance, consumer and data protection, model risk, job displacement, staff skills, cyber and data security, operational risk, third-party risk, systemic risk, credit risk, and market risk. The seven shown in the figure are the most populated by document count. The remaining four (third-party risk, systemic risk, credit risk, market risk) are coded and enter the denominator of the share calculation, but are not plotted.

### 2.2 Dominance principle

When a document names several actors, the coder assigns each actor a rank from 1 to 3 reflecting how dominant that actor's framing is in the document. Rank 1 is the most dominant. Ties at rank 1 are allowed. Problems within an actor row are ordered with the most dominant first; their position in the list is the only ordering signal.

### 2.3 Weighting

A document with multiple actors must not double-count. The figure uses **harmonic rank weighting**, normalised per document. For a document $d$ with actors of ranks $r_1, r_2, \ldots, r_K$, actor $k$'s weight is

$$w_k = \frac{1/r_k}{\sum_{j=1}^{K} 1/r_j}, \qquad \sum_{k=1}^{K} w_k = 1.$$

So a document with one actor gives that actor weight 1. A document with two actors gives weights $2/3$ and $1/3$. A document with three actors gives weights $6/11$, $3/11$, and $2/11$. The primary actor dominates but secondary actors are heard. Actors whose problems field is empty still consume their share of the document weight, because silence by a high-rank actor is a substantive observation and should not inflate lower-rank actors.

Within an actor row with $M$ flagged problems, the actor's weight splits equally, so each problem receives $w_k / M$. This is the unit of mass in subsequent aggregation. One (document, actor, problem) cell carries weight $w_k / M$.

### 2.4 Period split

Each document is assigned to *pre* if its date is before 1 December 2022, and *post* otherwise. The cutoff is the public release of ChatGPT. Documents with month-only precision are treated as the first of the month.

### 2.5 Share computation

For each problem $p$ and period $P \in \{\text{pre}, \text{post}\}$, the mass is

$$m(p, P) = \sum_{(d, k) \,:\, P_d = P,\, p \in \text{problems}_{d,k}} \frac{w_k}{M_{d,k}},$$

and the within-period share is

$$\text{share}(p, P) = \frac{m(p, P)}{\sum_{p'} m(p', P)},$$

where the denominator runs over all eleven codebook problems, not only the seven plotted. Shares in a period therefore sum to 1 across the full codebook. The plotted rows account for the bulk but not all of the within-period mass.

### 2.6 Figure

A horizontal dumbbell, one row per plotted problem, two dots per row (pre share and post share within period) joined by a connecting line. Rows are sorted ascending by post-share so the largest post categories sit at the top. The hover reveals the raw document count contributing to each cell alongside the weighted share, so the small-N pre period is visible to the reader.

## 3. Semi-supervised topic modeling

The second panel is a 2-D bubble map of topics recovered from the AI-relevant paragraphs. The procedure complements the supervised side by letting the text suggest categories rather than imposing the codebook on it. The codebook still anchors the procedure through seed words and proxy labels, so the resulting clusters can be compared against the supervised side rather than read in isolation.

### 3.1 Tool

The topic model is fit with **BERTopic** (Grootendorst, 2022), a modular pipeline. Each paragraph is converted into a 768-dimensional vector representation of meaning using the same sentence encoder as Figure 1 (`BAAI/bge-base-en-v1.5`, L2-normalised). The high-dimensional vectors are projected to a lower-dimensional space with UMAP (McInnes, Healy & Melville, 2018). The projected points are partitioned with HDBSCAN (Campello, Moulavi & Sander, 2013). Each cluster is then summarised by a ranked vocabulary using class-based TF-IDF (defined in Section 3.4). Unlike classical topic models such as Latent Dirichlet Allocation (Blei, Ng & Jordan, 2003), BERTopic does not assume topics are probability distributions over a fixed vocabulary. Clusters emerge from the geometry of the embedding space and are described after the fact.

### 3.2 Units and pre-filter

The pipeline operates on paragraphs (55,547 units from the same paragraph corpus used in Figure 1). To restrict the model to material that discusses AI as a policy or risk concern rather than passing mentions or unrelated technical detail, a lexical-semantic pre-filter is applied. For each paragraph $u$ and each of eleven supervisory risk-register anchor sentences $a$, the maximum cosine similarity

$$s_u = \max_{a} \cos(\mathbf{v}_u, \mathbf{v}_a)$$

is computed, and paragraphs with $s_u \geq \tau = 0.63$ are retained. The procedure yields **8,032 paragraphs**, around 14 percent of the corpus.

The eleven anchors are generic supervisory risk-register sentences drawn from the database itself and selected by two independent reviewer agents whose choices were merged. They are listed below.

1. AI's potential to imitate human behavior has given rise to concerns that the technology poses a significant threat to jobs, privacy, and the nature of human society itself.
2. Threat sources include governments, groups and individuals with malicious or ill-intentioned and/or criminal purposes.
3. There is a real danger that too many standards may introduce potential conflict and fragmentation.
4. For risks that cause adverse impacts, redress mechanisms and remedial actions may be required.
5. Hazard commonly refers to something that has the potential to cause harm or damage.
6. However, they expressed concerns that less stringent regulations in some sectors could potentially attract regulated activities, posing a risk of regulatory arbitrage.
7. Model risk management standards may recommend risk mitigation techniques for challenging circumstances, such as when data are limited or unavailable.
8. The use of AI in financial services without appropriate controls and oversight could amplify certain financial vulnerabilities, with potential implications for financial stability.
9. All of these technologies pose varying degrees of risk based on likelihood and consequence, and these are shifting constantly with new evolutions in AI.
10. For regulatory capital use cases, complex AI models may be restricted to certain risk categories and exposures or subject to output floors.
11. Fragmented or narrow-scope data, by contrast, can be unhelpful and even potentially misleading, directing attention away from actual risks and vulnerabilities.

### 3.3 Guidance: seeds and proxy labels

An unsupervised pass on the filtered set produces clusters that mix actor framings, document genres, and registers in ways that do not align with the codebook. Two guidance signals are introduced to discipline the clustering toward codebook structure without dictating the result.

**Seed words.** For each of ten codebook problem categories (the thinly populated `credit_risk` and `market_risk` are merged into a single `basel_thin` category), an 8 to 10 term seed list is constructed. Each list combines hand-curated terms from the codebook definition with the most distinctive words for that category, mined from the paragraph corpus via log-odds with an informative Dirichlet prior (Monroe, Colaresi & Quinn, 2008). The seed lists raise the c-TF-IDF weight of seed terms when summarising a cluster's vocabulary. Seeds therefore affect the words that *name* a cluster, not which paragraphs cluster together. The ten seed lists used are below.

| Category | Seed words |
|---|---|
| capacity and governance | governance, oversight, accountability, framework, board, management, capacity, mandate |
| consumer and data protection | fairness, discrimination, privacy, rights, consumer, protection, sensitive, personal, human rights, data subject |
| job displacement | jobs, employment, labor, workers, occupations, automation, wages, inequality, displacement, labor market |
| model risk | validation, explainability, interpretability, accuracy, drift, compliance, mrm, model risk, model validation, lack explainability |
| cyber and data security | cyber, attack, breach, poisoning, deepfake, security, vulnerability, malicious, malicious actors, cyber security |
| third-party risk | vendor, concentration, cloud, outsourcing, provider, foundation, supply chain, service providers, third-party dependencies, third-party risk |
| staff skills | skills, training, recruitment, retention, workforce, talent, expertise, upskilling, skills gap, staff training |
| systemic risk | systemic, stability, contagion, herding, correlation, amplification, interconnected, financial stability, systemic risk |
| operational risk | operational, infrastructure, outage, process, failure, resilience, disruption, operational resilience, system failure, data quality |
| basel thin (credit + market) | credit, market, default, trading, exposure, capital, credit risk, market risk, trading book, capital adequacy |

**Proxy labels.** Each paragraph is assigned a single integer label, the index of the primary problem framed in its parent document. The primary problem is the first code listed in the row of the rank-1 actor for that document (see Section 2.2). Of the 8,032 filtered paragraphs, **7,718 (96 percent)** carry a label. The remaining 314 are marked as unlabelled. The label vector feeds UMAP's semi-supervised mode (McInnes, Healy & Melville, 2018), which combines the standard topology-preserving objective with a term that pulls together points sharing the same label. Unlabelled points are placed by the standard objective alone. The resulting low-dimensional space is biased toward codebook structure without enforcing it. Clusters can still split or merge based on embedding geometry.

### 3.4 Topic representation and post-processing

After clustering, each cluster is represented by **class-based TF-IDF** (c-TF-IDF; Grootendorst, 2022). Paragraphs assigned to topic $t$ are concatenated into a single composite document, and TF-IDF is computed across these composite documents. Words with high c-TF-IDF in topic $t$ are over-represented in topic $t$ relative to the other topics. They are the topic's distinctive vocabulary. Seed words enter this stage by being weighted up for their assigned topic.

Two post-processing steps follow the initial fit. First, paragraphs that HDBSCAN places in low-density regions are flagged as outliers (4,118 of 8,032 in the first pass). They are reassigned to the topic whose c-TF-IDF vector is most cosine-similar to them, provided the similarity exceeds 0.10. After reassignment, **1,602 paragraphs** remain unassigned. Second, the initial fit yields **36 topics**, several of which differ only in actor or genre while sharing the same codebook framing. A hierarchical merge of the most-similar topic pairs is applied with target $k = 20$. Due to ties in the merge schedule, the procedure lands at **19 topics**.

### 3.5 Audit: normalised mutual information

The **normalised mutual information** between the cluster assignment and the proxy labels is computed on labelled paragraphs only (Vinh, Epps & Bailey, 2010):

$$\text{NMI}(\text{clusters}, y) = \frac{2 \cdot I(\text{clusters}; y)}{H(\text{clusters}) + H(y)},$$

where $I$ is mutual information and $H$ is Shannon entropy. NMI ranges from 0 (independent) to 1 (perfect alignment). The 36-topic initial fit scores NMI = 0.322. The 19-topic reduced fit scores NMI = 0.240. The drop is mechanical: merging clusters whose proxy-label majorities differ reduces alignment by construction. NMI around 0.32 indicates moderate alignment. The clusters partly recover codebook categories but do not partition them cleanly. This is the intended behaviour. The model is meant to *complement* the codebook by surfacing sub-themes (for instance, distinct strands within capacity and governance), not to reproduce it. NMI is reported as an audit number, not a tuning target.

### 3.6 Figure B: bubble map

The bubble map is built from the 19-topic reduced fit, with one topic dropped as low-quality (an OCR and heading-noise cluster with top words *national policies*, *implementation oecd*). The figure shows **18 topics**.

For each topic $t$, the centroid is the mean of the embeddings of its paragraphs, re-normalised to unit length. Because the paragraph embeddings are L2-normalised, the centroid is the spherical mean direction of the topic. A separate UMAP fit is run on the 18 centroids (not on the paragraph embeddings) to produce 2-D coordinates ($n_\text{components} = 2$, $n_\text{neighbors} = 10$, $\text{min\_dist} = 0.05$, metric cosine, fixed random seed). The same 2-D coordinates are used in both panels, so a topic sits in the same position in pre and post. The panels can be read as a comparison of mass and shift rather than position.

For each topic $t$ and period $P \in \{\text{pre}, \text{post}\}$, the bubble encodes four channels.

- **Position** is the semantic neighbourhood (identical in both panels).
- **Size** is proportional to $\sqrt{n_{t,P}}$, where $n_{t,P}$ is the paragraph count of topic $t$ in period $P$. The square-root compression keeps the visual range readable given the 26/74 pre/post imbalance in the database. Raw counts appear on hover.
- **Colour** is a diverging scale on $\Delta_t = \text{share}_\text{post}(t) - \text{share}_\text{pre}(t)$: warm grey for falling, ink-blue at zero, burnt orange for rising. The same colour is used for the same topic in both panels, because $\Delta$ is a topic-level property.
- **Opacity** is reduced when $n_{t,P} = 0$, so the topic's position remains visible across panels but its absence in that period is signalled.

Each bubble carries a hand-curated three-sentence narrative for its (topic, period) pair, summarising the framing observed in a stratified sample of the paragraphs assigned to it. The figure is rendered as an interactive HTML with a static PNG fallback.

## 4. What the two methods complement

The two methods answer different questions about the same database.

The supervised method answers *how the framing within a known set of categories has rebalanced*. The codebook is closed by design, the categories are interpretable, and the resulting shares are directly comparable across periods. The cost is that the supervised method can only see the categories the codebook has defined.

The semi-supervised method answers *whether new structure has appeared that the codebook does not anticipate*. The clusters are emergent rather than pre-specified, and the model is free to suggest groupings that cross or split the codebook's lines. The cost is that the resulting clusters are noisier and less directly interpretable than codebook categories.

Read together, the two converge on a shared finding and diverge in a productive way. They agree on the broad rebalancing: consumer and data protection fell after ChatGPT while capacity and governance and labour exposure rose. They diverge on emergence. The supervised view is structurally blind to categories not in the codebook, so it cannot show that generative AI, AI-related financial-system vulnerabilities, and exposure measurement have become distinct topics in the post-2022 writing. The semi-supervised view surfaces these as separate clusters with little or no pre-2022 mass. The combination is therefore a triangulation: agreement on shared categories is a robustness check on the rebalancing finding, and the divergence on emergence is the methodological feature, not a bug.

## 5. Limitations

The post period contributes roughly three times the document mass of the pre period (74/26 split). Shares are within-period so this is not a bias, but the pre estimates rest on a small base and the confidence interval on pre shares would be wide. A bootstrap is not currently computed for the dumbbell.

The hand-coded schema has been built by one coder. A second-coder inter-rater agreement check (Krippendorff's alpha per coded field) is the recommended practice in the content-analysis literature and remains pending.

The eleven problem codes are fixed. Risks present in the documents but outside the codebook (for instance, environmental cost of compute, geopolitical fragmentation, copyright and IP) are not represented in the dumbbell. The semi-supervised figure picks up some of this material as emergent clusters.

The plotted dumbbell covers seven of eleven codes. The four omitted codes (third-party risk, systemic risk, credit risk, market risk) remain in the denominator but are not visualised. Their pre-post movement is in the underlying table.

The weighting scheme uses harmonic decay (1/k). This is a defensible default but is not audited. Alternative schemes (primary actor only, uniform across actors, linear decay) would shift the shares. A sensitivity panel comparing schemes is a candidate robustness check.

The hand-coded figure does not separate doc-type heterogeneity. Long policy papers and short stocktakes are weighted identically per document. A doc-type-stratified version of the dumbbell would test whether the pre-post shift is driven by composition (more papers of one type post-2022) or genuine reframing within type.

The topic-count choice for the bubble map is pragmatic. The target $k = 20$ is not derived from a principled criterion. The merge-cost dendrogram shows the largest jump at $k \approx 15$, so the 19-topic output is the working choice while documenting that alternative.

The clustering pipeline is non-deterministic beyond the random seed. UMAP and HDBSCAN depend on numerical and threading details, so outputs can vary slightly across hardware. The 36 and 19 topic outputs should be read as one defensible cut, not as the unique answer.

The pre-filter for the semi-supervised method depends on the eleven risk-register anchors above and the threshold $\tau = 0.63$. A leave-one-out audit over anchors and a sensitivity sweep over $\tau$ are candidate robustness checks. Neither is currently run.

## References

Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent Dirichlet allocation. *Journal of Machine Learning Research*, 3, 993–1022.

Campello, R. J. G. B., Moulavi, D., & Sander, J. (2013). Density-based clustering based on hierarchical density estimates. In *Pacific-Asia Conference on Knowledge Discovery and Data Mining* (pp. 160–172). Springer.

Grimmer, J., Roberts, M. E., & Stewart, B. M. (2022). *Text as Data: A New Framework for Machine Learning and the Social Sciences.* Princeton University Press.

Grootendorst, M. (2022). BERTopic: Neural topic modeling with a class-based TF-IDF procedure. arXiv:2203.05794.

Krippendorff, K. (2018). *Content Analysis: An Introduction to its Methodology* (4th ed.). SAGE.

McInnes, L., Healy, J., & Melville, J. (2018). UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction. arXiv:1802.03426.

Monroe, B. L., Colaresi, M. P., & Quinn, K. M. (2008). Fightin' words: Lexical feature selection and evaluation for identifying the content of political conflict. *Political Analysis*, 16(4), 372–403.

Neuendorf, K. A. (2017). *The Content Analysis Guidebook* (2nd ed.). SAGE.

Vinh, N. X., Epps, J., & Bailey, J. (2010). Information theoretic measures for clusterings comparison: Variants, properties, normalization and correction for chance. *Journal of Machine Learning Research*, 11, 2837–2854.
