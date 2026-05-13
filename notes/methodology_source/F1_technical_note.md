# Figure 1 — methodological note

## 1. Objective

Yearly attention to artificial intelligence in international supervisory documents over 2019–2025. The corpus is 336 documents from BIS, FATF, FSB, IMF, OECD, and the World Bank. Two methods are applied to the same corpus and reported as separate figures.

## 2. Traditional method (F1a)

Weighted dictionary count. For each document we compute a density per 1,000 words

$$\text{density} = \frac{2\,c_1 + c_2}{n_{\text{words}}} \cdot 1000$$

where $c_1$ counts occurrences of Tier 1 terms — *artificial intelligence*, *generative AI*, *GenAI*, *LLM*, *large language model*, *foundation model*, *ChatGPT*, *GPT-3*, *GPT-4*, *GPT-5*, *agentic AI*, *AI agent*, *deepfake*, *AI safety*, *AI alignment*, *AGI*, *frontier AI* — and $c_2$ counts occurrences of Tier 2 terms — *machine learning*, *deep learning*, *neural network*, *transformer model*, *NLP*, *computer vision*. Each term is matched as a whole word, case-insensitive, with an optional trailing *s* for plurals. "Whole word" means surrounded by non-letter characters on both sides, so e.g. *AI* matches in *generative AI* but not inside *Mumbai*. Hyphenated variants (e.g. *deep-learning*) are not matched.

The 2× weighting on Tier 1 reflects that Tier 1 terms are unambiguously AI-specific in supervisory text, whereas Tier 2 terms (e.g. *neural network*) sometimes appear in non-AI contexts. Each document contributes one density value to its year and the figure plots the yearly mean. This is a standard dictionary method (Grimmer, Roberts & Stewart 2022; Hassan et al. 2025): cheap, transparent, exact-match. A companion figure F1b uses equal weights ($w_1 = w_2 = 1$); the time-series shape is preserved and the substantive conclusion — a sharp post-2022 jump — is unchanged.

## 3. Modern method (F1)

The traditional method counts literal matches only. A paragraph that says *"the use of AI"* is counted; a paragraph that paraphrases the same idea without the keyword is missed. The modern method complements it by measuring **semantic similarity**, operationalised here as the cosine similarity of sentence-embedding vectors.

### 3.1 Tool

Each text unit and each anchor sentence is converted into a 768-dimensional vector by a pre-trained transformer-based sentence encoder, `BAAI/bge-base-en-v1.5`. The transformer is a neural-network architecture that, given a sentence, produces a vector representation in which sentences of similar meaning lie close together in the 768-dimensional space and unrelated sentences lie far apart, largely independent of surface wording (Grimmer, Roberts & Stewart 2022). The model used here was trained on hundreds of millions of sentence pairs for that property; we apply it as-is, without further fine-tuning.

Implementation details. Inputs longer than the encoder's 512-token context window are silently truncated; the BGE encoder uses the first-token (CLS) representation as the sentence vector. We do not use a query/passage instruction prefix. Output vectors are L2-normalised by us after encoding, so cosine similarity reduces to a dot product.

### 3.2 Units and anchors

The pipeline is run twice in parallel: once at the **paragraph** level (55,547 units) and once at the **sentence** level (161,052 units). Both panels are reported in the figure family. The same gate, anchors, and aggregation procedure apply to each.

Twenty-four anchor sentences are curated from the corpus itself. Twelve are drawn from documents dated 2019–2022 and use classical AI/ML vocabulary; twelve are drawn from documents dated 2023+ and use GenAI-era vocabulary. Curation balances vocabulary coverage and supervisory register. The full procedure is documented in `F1_anchor_selection.md`. The 24 anchors function as a reference set: every text unit is scored against this set.

Because the anchors are corpus-sourced, the same 24 sentences also appear in the unit pool. This is anchor leakage. The leaked units are 24 out of 55,547 paragraphs (0.04%) or 24 out of 161,052 sentences (0.01%) and are not separately excluded; the effect on yearly shares is below numerical precision. The fact is documented for transparency rather than corrected.

### 3.3 Gate

A keyword gate restricts the figure to units that explicitly mention AI. The objective is to isolate AI-specific discussions from the much broader supervisory conversation about technology in finance — fintech, payment digitalisation, data infrastructure, RegTech and SupTech generically. Cosine similarity alone does not enforce this separation: a paragraph about, say, cloud-computing risk in banking can sit close in the embedding space to a paragraph about LLM deployment without being about AI. The gate is the lexical anchor that prevents this confounding.

A unit qualifies if it contains at least one of the following tokens:

- `AI`
- `artificial intelligence`
- `machine learning`
- `GenAI`
- `agentic`
- `LLM`

Each token is matched as a **whole word**, case-insensitive, with an optional trailing *s* for plurals. "Whole word" means the token must be surrounded by non-letter characters (spaces, punctuation, parentheses, line breaks) on both sides — so `AI` matches in *generative AI*, *(AI)*, or *AI agents*, but does **not** match inside *Mumbai* or *AIDS*. Consequently a unit containing *generative AI*, *AI agents*, *AI safety*, *AI alignment*, etc. passes because `AI` is present as a standalone word. Units without any of these six tokens are not eligible, regardless of how high their embedding similarity to the anchor set. The gate defines the figure's denominator-conditional set.

### 3.4 Score

For each unit $u$ with embedding vector $\mathbf{v}_u$ and each anchor $a$ with vector $\mathbf{v}_a$, semantic similarity is the cosine of the angle between the vectors,

$$\cos(u, a) = \frac{\mathbf{v}_u \cdot \mathbf{v}_a}{\|\mathbf{v}_u\|\,\|\mathbf{v}_a\|}.$$

Both vectors are unit-normalised, so cosine equals their dot product. The unit's score is its maximum cosine across the 24 anchors,

$$s_u = \max_{a \in \mathcal{A}}\cos(u, a),$$

read as: how close to *any* of the curated AI sentences this unit lies. Cosine runs from $-1$ (opposite direction) to $+1$ (same direction). Empirically in this corpus, related supervisory text typically scores between 0.50 and 0.80; unrelated text scores below 0.40. These are observations from our runs, not properties of the encoder.

### 3.5 Aggregation

A unit is **AI-relevant at threshold $\tau$** if it passes the gate *and* $s_u \geq \tau$. For each year, the figure plots the share of all units in that year that are AI-relevant. Three thresholds $\tau \in \{0.50, 0.55, 0.60\}$ are reported as separate panels and as a joint sensitivity panel (`F1_*_joint.png`); inspection of the joint panel shows the time-series shape preserved across the three values, with absolute levels shifting modestly.

Uncertainty is expressed via a **document-cluster bootstrap** (Grimmer, Roberts & Stewart 2022). For each year and each $\tau$, documents are resampled with replacement from that year's pool — when a document is drawn, *all* its units are carried with it (proper cluster bootstrap, not unit-level resampling). The share is recomputed at each iteration; the procedure is repeated 10,000 times. The 2.5th and 97.5th percentiles of the bootstrap distribution form the 95% confidence interval. The cluster unit is the document because paragraphs and sentences within a single document share topic, register, and authorial voice — they are not independent draws.

## 4. What the two methods complement

The two figures answer related but distinct questions.

- **Traditional (F1a / F1b)** captures the **vocabulary shift**. Tier 1 terms did not exist in supervisory text before 2022, so the curve is necessarily flat pre-2022 and jumps sharply at 2023.
- **Modern (F1)** captures **lexical-and-semantic continuity**. Classical AI/ML talk was already present 2019–2021, and the embedding-based score recognises it. The curve is already substantial pre-2022 and rises further afterward.

Reading both together avoids two opposite errors. The traditional figure alone implies AI attention "began" with GenAI; the modern figure alone implies the post-2022 shift was a smooth continuation of an existing trajectory. The combined reading is narrower than either: AI/ML topics have been continuously present in the supervisory window, and the vocabulary in which they are discussed has expanded post-2022. The figure does not establish that *policy* attention to AI as a distinct policy object was equally salient pre-2022 — that question requires reading the documents themselves and is not the figure's claim.

## 5. Limitations

- **Gate false-positive rate not audited.** Some gated units may match an AI token in non-AI contexts (e.g. *AI* as an unrelated initialism). A spot-check of gated paragraphs is the recommended robustness step and is pending.
- **Document-length heterogeneity is not separately controlled.** Long documents (e.g. IMF FSAPs, OECD reports) contribute proportionally more units to the share than short FATF briefs. The figure is a corpus-level proportion, not a document-level average; this is a substantive choice but worth flagging.
- **Encoder robustness not checked.** Results have not been replicated with an alternative encoder. The reported shape is conditional on `BAAI/bge-base-en-v1.5`.
- **Single-coder anchor curation.** The 24 anchors were selected by one author; a second-coder agreement check is the recommended practice (Grimmer, Roberts & Stewart 2022) and is pending.
- **Lookahead bias in the encoder.** The model was trained on web text post-dating much of the pre-2022 corpus; pre-2022 text is being scored against a vocabulary representation it could not have produced at the time. The shared keyword gate partially mitigates this by requiring an explicit AI/ML token.
- **Anchor selection sensitivity.** Add/drop sensitivity (e.g., leave-one-out across the 24 anchors) is a possible robustness check, not currently run.

## References

Grimmer, J., Roberts, M. E., & Stewart, B. M. (2022). *Text as data: A new framework for machine learning and the social sciences.* Princeton University Press.

Hassan, T. A., Hollander, S., Kalyani, A., van Lent, L., Schwedeler, M., & Tahoun, A. (2025). Text as data in economic analysis. *Journal of Economic Perspectives*, 39(3), 191–214.
