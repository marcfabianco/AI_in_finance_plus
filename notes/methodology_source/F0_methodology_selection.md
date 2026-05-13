# Methodology of selection of documents

This note documents how the 387 documents in the database were chosen, collected, and screened.

## 1. Scope

The database contains documents published between 2017 and 2026 by five international bodies that work on financial regulation and supervision. These are the BIS (including its hosted committees BCBS, FSB, and FSI), FATF, IMF, OECD, and the World Bank. The substantive scope is banking regulation and supervision, with adjacent financial-stability and monetary-policy material included when the issuing body frames it through that lens. Documents on agriculture, education, health, transport, and other domains outside the financial system are excluded.

## 2. Collection

Each body's publications sit behind a different web infrastructure. The collection logic is the same in each case. The body's publications page is identified, a standard set of seed queries is run (artificial intelligence, machine learning, generative AI, large language model), a deduplicated manifest is built, the manifest is screened by scope, the kept documents are downloaded, and PDFs are converted to machine-readable text.

**BIS.** Publications, working papers, bulletins, and committee reports are hosted on the BIS site and are accessible to standard requests. The same search interface returns FSB, FSI, and BCBS material, which is collected through the same route and tagged in the database as a BIS document with the appropriate committee sub-body. The final tally is 56 documents.

**FATF.** The FATF publications site sits behind bot protection, so the search results were harvested through a browser-driven workflow that read the rendered page. The result pool is small, around eighty entries, and includes a mix of speeches, guidance documents, and mutual evaluation reports. Documents are kept or dropped at coding time rather than at collection, since the marginal cost of an extra download was lower than the risk of a silent omission. 30 documents reached the final database.

**IMF.** IMF publications are served through a single-page application protected by a bot-detection layer. Search results were harvested with browser automation and PDF URLs resolved one document at a time, since the file naming is not deterministic. The full search returned 517 hits across nine publication series (F&D Magazine, Working Papers, Policy Papers, IMF Notes, Staff Discussion Notes, Departmental Papers, GFSR, Policy Discussion Papers, and Staff Country Reports). After screening, 112 documents reached the final database, of which 22 exist only as HTML and were fetched and converted separately.

**OECD.** The OECD exposes an open search API that returned 609 unique items across three policy-area facets and the four seed queries. PDF URLs were resolved through a browser-driven step where the standard download path did not generalise. Twenty-two country chapters of the EU Coordinated Plan on AI were dropped at coding time as government strategy documents with no banking substance. 137 documents reached the final database.

**World Bank.** The Open Knowledge Repository runs an unauthenticated REST API that returned 256 unique items after deduplication. The World Bank catalog is broad, so triage was done at collection time by reading titles and abstracts from the manifest before downloading. 52 documents reached the final database, a keep rate near 20 percent.

## 3. Screening

Every document is screened in two stages. The first stage decides whether the document is worth downloading. For bodies with broad catalogs (World Bank, OECD), this stage runs on titles and abstracts at collection time. For bodies with narrow catalogs (BIS, FATF, IMF), all hits are downloaded and screened at coding time, since the cost of one extra PDF is lower than the risk of missing a relevant document. The guiding principle in both cases is loose-side bias. When in doubt, keep.

The second stage runs at coding time, after the document has been read. A document lands in one of three categories. It is *dropped* when AI is genuinely a passing footnote, with zero or near-zero substantive content despite the harvest matching on title or metadata. It is *kept with a borderline flag* when it sits on the scope boundary (for example macro-AI material with no explicit banking hook, or fiscal-authority AI) but carries enough substance to contribute to the temporal-agenda signal. It is *kept clean* when it falls squarely within scope.

Two mechanical pre-screens support the coder's decision. A keyword-density pass counts AI-related vocabulary and flags documents with zero or near-zero density. A second pass counts banking and financial-stability vocabulary and flags documents with no financial-system signal. Both are decision aids; the coder makes the final call.

A universal pre-2018 cutoff was adopted partway through the project. Uncoded documents dated before 2018 are dropped at the manifest stage, since AI density in pre-2018 supervisory text is near zero by construction. Pre-2018 documents already coded before the cutoff was adopted are kept.

## 4. Inclusion and exclusion

Documents are included when they fall within at least one of the following areas. Banking supervision, financial stability monitoring, AI in payments and AML, cyber security for banks, credit and operational risk, and macroeconomic effects of AI when the document carries a financial-stability or monetary-policy hook. Tax administration is included as an adjacent state financial function, given how closely it interacts with AML reporting and banking conduct.

Documents are excluded when their primary substance is pure development, education, healthcare, agriculture, or public-sector governance without a financial-system channel. Government AI strategy documents are excluded unless they explicitly engage banking supervision.

## 5. Final database

After collection, deduplication, and screening, the database holds 387 documents distributed across the five bodies. OECD contributes 137 documents, IMF 112, BIS 56, World Bank 52, and FATF 30. The full distribution by year and by document type is shown in the Documents section of the demo.

## Tools used

The collection and conversion pipeline combined three tools. A general-purpose coding agent ran browser-based harvesting where bot protection blocked programmatic access. Standard Python scripts handled API-based collection and PDF downloads. A neural PDF-to-markdown converter produced the machine-readable text used in subsequent coding.
