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

### Policy attention

Non is better but complementary.

1 Traditonal methods. Expert select a set of key words. and...

This method would say that pre 2023, here was barely attention and jumped. 
This might tell us more about the change of wording.

FIGURE: 
/Users/marcosfabian/Documents/Documents/GitHub/AI_in_finance/Demo/stage_2/figures/F1/F1a_traditional.png

2 Modern methods


Here i present a semi supervised

Here we are interested in sematic proximity. Not only the strict word coding matters, but semantic proximity.

Methods based on transformers shows that attention on AI matters was there and has steadily increased over time. 

The figure shows, ...

(we might include a interactive version of F1_paragraph_joint.png and F1_sentence_joint.png)

where τ is the minimum semantic similarity between a paragraph and the closest anchor. Different sensitivities suggest the same trend.

We can see pre 2022 these matters were discussed and increasing. Standard errors measure how precise... And we can see that after 2022 standard errors also reduced, meaning a tighter attention. Early attention was more dispersed , now seems more focused. 


Cosine runs 0 (totally unrelated) to 1 (literally the same sentence). For the BGE embedding model we're using (HuggingFace card here — it's trained for retrieval), the typical range is narrow. Concrete examples on this corpus:

Attention has been there, vocabulary has expanded.

Trend but also we can interpret standard errors what does it mean?

Document-cluster bootstrap, 1,000 iterations Cameron-Gelbach-Miller (2008) 

FIGURES: 

/Users/marcosfabian/Documents/Documents/GitHub/AI_in_finance/Demo/stage_2/figures/F1/F1_paragraph_joint.png 

/Users/marcosfabian/Documents/Documents/GitHub/AI_in_finance/Demo/stage_2/figures/F1/F1_sentence_joint.png


(remember here we will have a button to a more detailed technical note, here just the intutitions)

### Does change in vocabulary mean change in risks landscape?


The supervisory register dilutes the signal. Most post-2022 GenAI mentions in this corpus are wrapped in regulatory/risk/governance language. The anchors I curated are more "what GenAI is and does" sentences. Semantic distance between "LLMs operate as black-box probability machines…" (anchor-flavoured) and "firms deploying foundation models must establish appropriate model-risk frameworks…" (corpus-flavoured) is real.

### Risk vs Tool

Sentiment analysis.


