# The page

I think the idea is to have a sort of page similar to apple page products where you scroll and then things start to appear from transparent to get more solid color. Is this doable?

So the analysis will appear by section and each section must fit the whole page once the scroll down make everything solid solid and clear. 

The below are some sketches for what I want for the first couple of sections. Of course they are not well done already but we will. So for testing we will put a placeholder with just the text and the existing Figures I have here so far.

## AI in Financial Policy

The objective of this Demo is to provide a general inspection of the policy attention or polcy narrative of financial regulation and supervision regarding artificial intelligence and ingeneral the new wave of digitzalization that is rapidly expanding.

The idea is to discover among international bodies, where is the attention, how it has evolved over time, the sentiment, the identification of risks and mismatches between international bodies, policy and academia. But with th idea that the methods described here are broadly applicable and useful for the kind of work the FSI produce which is basically policy benchmarking.

Thoruhout this demo, you will find buttons that ake you to a more tehcnical documentaton for each figure produced.

This is a Demo just to show the menu of methods and tools used in modern Policy Analysis techniques. Results here must not be interpreted as hard truths, althoug, the methodology followed is solid, etc,  these results must be benchmarked and discussed against expert regulators and supervisors, hwhich is also a fundamental part of modern methods.

### Scope and data collection

387 documents were collected from five international bodies in financial regulation and supervision, covering 2018 to 2025. Each body's publications page served as the primary source: the BIS, for instance, maintains an "AI at BIS" stream, with equivalent AI-tagged collections drawn from FATF, IMF, OECD, and the World Bank. Inclusion required that a document mention "artificial intelligence" or "machine learning". Documents centred on topics outside the financial system, such as labour or health AI applications, were excluded.

-  Image:Number of documents per year. Text: The number of documents that mention artificial intelligence or machine learning grows over 2018 to 2025, with a sharp acceleration after ChatGPT's release. The three post-ChatGPT years account for roughly 70 % of the database, with 48, 86, and 112 documents in 2023, 2024, and 2025 respectively. Hovering on any bar reveals the per-body breakdown for that year. /Users/marcosfabian/Documents/Documents/GitHub/AI_in_finance/Demo/stage_2/figures/F0/F0_n_docs_per_year.html . 

-   Image: Pie of Type of doc. Text: Policy papers and academic papers each account for roughly a third of the database. Another 17 % consists of speeches and commentary, and the rest comes from stocktakes, formal standards, and country assessments. The supervisory work of these institutions and their internal research are receiving comparable attention to AI, though the content of that attention differ as shown next.
/Users/marcosfabian/Documents/Documents/GitHub/AI_in_finance/Demo/stage_2/figures/F0/F0_doc_type_pie.html

 (Button to method of how we chose the documents)

### Trends in Policy Attention

Attention to AI in these documents did not begin with ChatGPT. Documents from 2019 to 2021 already discussed AI and machine learning, often using terms like neural networks, natural language processing, and natural language processing. After ChatGPT, the discussion grew in volume and the vocabulary expanded. Generative AI, large language models, and agentic systems become standard terms in writing from 2023 onward. The interest is older than the language used to describe it.

1  Supervised. Hand-coded methods

Traditional methods measure attention to a topic by counting how often relevant words appear. The approach requires human expertise to pick the vocabulary, since the count is only as good as the list. For this demo, twenty-three terms were chosen to cover the AI and machine learning vocabulary in use across the period. Each document is then summarised by the number of times these terms appear per thousand words, which makes documents of different length comparable.

(Maybe a nice table or box with the words: artificial intelligence, machine learning, generative AI, GenAI, LLM, large language model, foundation model, ChatGPT, GPT-3, GPT-4, GPT-5, agentic AI, AI agent, deepfake, AI safety, AI alignment, AGI, frontier AI, deep learning, neural network, transformer model, NLP, computer vision)

Before ChatGPT, these terms appear at a modest rate. The dominant ones in pre-2022 writing are machine learning, neural networks, and natural language processing. From 2023 onward the rate rises sharply and remains at the higher level. The post-ChatGPT years bring new terms into common use, including generative AI, large language models, agentic systems, and ChatGPT itself.

FIGURE: 
/Users/marcosfabian/Documents/Documents/GitHub/AI_in_finance/Demo/stage_2/figures/F1/F1a_traditional.png

2 Semi-supervised. Semantic similarity method

Traditional methods are useful as a first measure but can mask real attention by depending entirely on a fixed list of words. A semi-supervised method based on transformer models compares each paragraph to a curated set of AI reference sentences and scores the similarity in meaning rather than wording. By this measure, attention to artificial intelligence and machine learning rises steadily across the period, without the sudden jump seen in the keyword count.

The shaded bands around the line are bootstrap confidence intervals which quantify how precise each year's estimate is. They also help test whether differences between periods are statistically meaningful, and whether topical dispersion narrows or widens over time. A preliminary look at this figure suggests the bands are tighter from 2023 onward, which might reflect closer semantic similarity in the topics discussed post-ChatGPT. The same overall conclusion holds whether the unit is the paragraph or the sentence.

FIGURES: 

footnote better: τ is the minimum semantic similarity between a paragraph and the closest anchor. Different sensitivities suggest the same trend.

/Users/marcosfabian/Documents/Documents/GitHub/AI_in_finance/Demo/stage_2/figures/F1/F1_paragraph_joint.png 

/Users/marcosfabian/Documents/Documents/GitHub/AI_in_finance/Demo/stage_2/figures/F1/F1_sentence_joint.png

(remember here we will have a button to a more detailed technical note)



### Does change in vocabulary mean change in risks landscape?


The supervisory register dilutes the signal. Most post-2022 GenAI mentions in this corpus are wrapped in regulatory/risk/governance language. The anchors I curated are more "what GenAI is and does" sentences. Semantic distance between "LLMs operate as black-box probability machines…" (anchor-flavoured) and "firms deploying foundation models must establish appropriate model-risk frameworks…" (corpus-flavoured) is real.

### Risk vs Tool

Sentiment analysis.


