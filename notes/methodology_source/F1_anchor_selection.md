# Anchor selection — Figure 1 modern method

The modern method depends on a small curated set of 24 anchor sentences. This note documents how those 24 were chosen, on what criteria, and what they say.

## 1. What the anchors are for

The modern method scores every paragraph in the database by its semantic similarity to a fixed reference set. The 24 anchor sentences are that reference set. A paragraph counts as AI-relevant when its highest cosine similarity to any one of the 24 anchors passes a threshold. The anchors therefore define, in concrete language, what the figure treats as AI-relevant.

## 2. Where the anchors come from

Anchors are drawn from the database itself, not invented. Every anchor is a real sentence written by one of the five international bodies covered by the database, in the supervisory or academic register those bodies actually use. The candidate pool is the segmented sentence file of all 387 in-window documents (around 161,000 sentences).

## 3. Two halves: classical and GenAI vocabulary

The 24 anchors are split into two halves of 12, distinguished by the era and vocabulary of their source documents.

The **classical half** consists of sentences from documents dated 2019 to 2022 that contain at least one classical AI or ML term and none of the GenAI-era vocabulary. The classical terms covered are *artificial intelligence*, *AI*, *machine learning*, *ML*, *deep learning*, *neural network*, *natural language processing*, *NLP*, and *computer vision*.

The **GenAI half** consists of sentences from documents dated 2023 onward that contain at least one GenAI-era term and no classical-only term that would qualify the sentence on older vocabulary alone. The GenAI terms covered are *LLM*, *large language model*, *foundation model*, *generative AI*, *GenAI*, *agentic*, *AI agent*, *ChatGPT*, *GPT-3*, *GPT-4*, *GPT-5*, *AGI*, *AI safety*, *AI alignment*, *deepfake*, *frontier model*, and *transformer architecture*.

The two halves are pooled into a single 24-anchor set for scoring. The per-half distinction is documentation, not a feature of the figure.

## 4. Selection criteria

Candidate sentences pass five filters before reaching the final 24.

**Quality.** Length between 18 and 32 words, contains a verb-like word, not dominated by title case, and not a citation, URL, or bibliography fragment.

**Domain.** GenAI candidates from off-topic content (medical, agricultural, education, employment services) are excluded so the GenAI anchors stay either finance-close or focused on AI itself.

**AML disambiguation.** A sentence whose only AI or ML hit is the abbreviation *ML* in a money-laundering context (AML, CFT, *money laundering*) is treated as a false positive and dropped.

**Per-document cap.** No more than four candidates per source document, to prevent any single document from dominating the anchor set.

**Diversity targets.** The final 24 are selected against three targets. Cross-body coverage across BIS, IMF, OECD, World Bank, FATF, and FSB. Vocabulary coverage across the classical and GenAI term lists in Section 3. Supervisory register preferred over academic or methodological detail.

## 5. Pool sizes

| Stage | Classical | GenAI |
|---|---|---|
| Sentences in source pool | 161,052 | 161,052 |
| Candidates after era and vocabulary filter | 1,277 | 576 |
| Candidates after quality and per-document cap | 323 | 576 |
| Final anchors | 12 | 12 |

## 6. The 24 anchor sentences

The complete reference set follows. Each entry shows the year and body of the source document and the AI terms the sentence is anchored on.

### Classical half

**A01.** (2021, OECD; NLP) For instance, Mexico's National Banking and Securities Commission (CNBV) has developed a prototype for a Natural Language Processing (NLP) application to detect what a suspicious…

**A02.** (2021, IMF; AI) This is a salient way of thinking about the role of data used in artificial intelligence (AI) applications.

**A03.** (2021, IMF; AI) For instance, not all data are well documented, some data suffer from coverage bias, and AI algorithms can have coding errors or could be biased.

**A04.** (2022, OECD; AI) Since 2020, the United States dedicates USD 1 billion or more annually to non-defence AI R&D and created national AI research institutes.

**A05.** (2021, OECD; AI) Just three countries account for half of the AI workforce in Europe: the United Kingdom, France and Germany (LinkedIn Economic Graph, 2019).

**A06.** (2021, IMF; ML) Because of the skip-sampling method used for the ML models, the variable importance tables also highlight potential leading or lagging indicator relationships.

**A07.** (2021, FATF; artificial intelligence, machine learning) It is an exciting time for technology with artificial intelligence, machine learning and big data analytics being developed and deployed in many fields.

**A08.** (2021, FATF; machine learning, natural language processing) Unsupervised text mining techniques such as natural language processing or supervised machine learning such as data labelling allow…

**A09.** (2022, IMF; machine learning) While DFMs have become mainstream tools to nowcast GDP growth, new techniques have emerged, based on statistical learning and machine learning.

**A10.** (2022, FATF; machine learning) Are amendments to existing legislation needed to allow the use of technologies such as machine learning and big data analytics?

**A11.** (2020, OECD; neural network) In addition, Random Forests and XGBoost regressors (which are both sparse algorithms), both with standard scikit-learn parameters, underperformed the neural network used in this paper.

**A12.** (2019, World Bank; computer vision) A different approach, the use of convolutions, has proven very successful in the field of computer vision and especially object recognition.

### GenAI half

**A13.** (2024, BIS; LLM) This special feature provides an accessible introduction to LLMs aimed at economists and offers applied researchers a practical walkthrough of their use.

**A14.** (2025, BIS; large language model, LLM) Scenario 1 involves the implementation of copilots based on large language models (LLMs) that augment rather than replace human skills and workers.

**A15.** (2025, IMF; large language model) Their success is partly due to cost-effective training methods and the open-source release of some large language models, which can help circumvent the need for top-tier hardware.

**A16.** (2024, BIS; GenAI) Several other companies use GenAI to provide financial advice to customers and help with expense management, as well as through co-pilot applications.

**A17.** (2024, World Bank; GenAI) In theory, the rise of GenAI and its potential positive impacts on labor productivity could pose a significant opportunity for developing countries.

**A18.** (2023, OECD; GenAI) Data authenticity and IP-related risks are closely related to data quality and data privacy-related considerations, and are particularly prominent in GenAI models.

**A19.** (2023, OECD; ChatGPT) ChatGPT is estimated to have around 100 million active monthly users, making it the fastest-growing consumer software application in history.

**A20.** (2025, World Bank; ChatGPT) It is estimated that a single ChatGPT query consumes 25 times more energy than a Google search query.

**A21.** (2025, OECD; AGI) While many believe AGI is still far off, some tech leaders and researchers warn of its imminent arrival and potential existential risks.

**A22.** (2023, IMF; AGI) Third, the takeoff in output and the collapse in wages in the two AGI scenarios are both driven by the same force, the substitution of scarce labor by comparatively more abundant machines.

**A23.** (2025, OECD; agentic) Although still in their infancy, agentic systems may also be able to further reduce consumer search and transaction costs.

**A24.** (2025, FATF; deepfake) Drawing on current research and expert dialogue, it offers a snapshot of developments beyond deepfakes to help anticipate potential future challenges.

## 7. Coverage of the final 24

The six bodies in the database are all represented (BIS, IMF, OECD, World Bank, FATF, FSB). Years span 2019 to 2025, with the classical half biased toward the pre-2022 period and the GenAI half toward 2023 onward by construction. Document types include policy papers, academic working papers, stocktakes, and speeches.

## 8. Limitations

Anchor selection is a researcher choice. A leave-one-out sensitivity analysis across the 24 anchors is a candidate robustness check and is not currently run.

The database is unbalanced across bodies. OECD and BIS contribute the largest share of documents. The figure reports shares per year per text unit rather than counts, but compositional change in the yearly mix is not separately controlled.

The sentence encoder was trained on web text post-dating much of the pre-2022 database. Pre-2022 text is therefore being scored against a vocabulary representation it could not have produced at the time. The shared keyword gate partially mitigates this by requiring an explicit AI or ML token in every counted unit.

Anchor curation is by one author. A second-coder agreement check is the recommended practice in the content-analysis literature and remains pending.
