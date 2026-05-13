# Database architecture

The database is structured so that every document is a row in a spine table, with satellite tables holding the coded answers to each analytical question. The spine and satellites join on a single document identifier. The architecture supports queries across time, institution, actor, area, and recommendation register.

## At a glance

```
documents                    (spine, one row per document)
│
├── definitions               (one row per document)
├── actors                    (one or more rows per document)
│      └── problems           (one row per document-actor pair)
└── policy_areas              (one or more rows per document)
```

Every satellite joins back to `documents` on the document identifier. The `problems` table is a sub-satellite of `actors`: each row records the problems that one actor frames within one document, so it joins on the document identifier and the actor together.

## 1. The spine

One row per document. The spine records institutional metadata (the issuing body, any sub-body within it, the date of publication, the document type, page count, the source URL, and the file path to the local copy). It is the join key for everything that follows.

## 2. Satellites

Four satellite tables sit alongside the spine, one for each analytical question. Each carries its own row cardinality and joins back to the spine on the document identifier. Every row also carries a `notes` field with the coder's rationale and a supporting quote from the document.

**Definitions.** One row per document. Records whether the document gives or borrows a formal definition of AI, the source of any borrowed definition, and which terms (artificial intelligence, generative AI, large language models, agentic AI) the document treats as interchangeable.

**Actors.** One or more rows per document. Each row identifies an actor named in the document (regulators, financial institutions, customers, technology providers, governments, and others), and assigns a dominance rank to that actor within the document. The dominance rank distinguishes the dominant framing from secondary and tertiary mentions.

**Problems.** One row per document-actor combination. Joins to the actors table on document and actor. Records the policy problems the document attributes to that actor (model risk, cyber and data security, capacity and governance, job displacement, and others), with the most dominant problem listed first.

**Policy areas.** One or more rows per document. Each row identifies a policy area the document engages with (micro-prudential, macro-prudential, supervisory process, consumer protection, AML, payments, central-bank operations, and others), with a dominance rank and an optional list of sub-areas at tool-level granularity.

## 3. The dominance principle

For every coded dimension, the coder records what is *dominant* in the document rather than every mention. The dominant elements (typically one to three) carry rank 1. Secondary mentions carry rank 2. Tertiary mentions carry rank 3. Ties at rank 1 are allowed. The principle keeps the database focused on framing rather than incidental references, and produces a single ordering signal used in downstream analysis. Absences are recorded as well. If a document does not address a coded question, a row is added with a "not addressed" note.

## 4. The manifest layer

Each body has a manifest file that tracks every document harvested, regardless of whether it was kept. The manifest stores the document identifier, title, date, sub-series within the body, the classification outcome (drop, keep clean, keep borderline, no file, or pending), the rationale for any drop or borderline call, a coding flag, and the source URL. The manifest layer sits between raw collection and the coded database. It is the audit record of what was harvested, what was kept, and why.

## 5. Conventions

The database follows three conventions worth flagging.

First, the document identifier is the original filename as downloaded, without renaming. This preserves the link back to the source document regardless of how the file is processed downstream.

Second, the `notes` field on every row is required to carry the coder's reasoning, not just a quote. The rationale must be sufficient that an auditor can verify the coding call without re-reading the source.

Third, novel terms or framings that appear with substantive density but have no home in the existing vocabulary are flagged inline in the notes with a marker that an audit script can later surface. This is a deliberate tripwire to catch emerging concepts the codebook has not yet captured.

## 6. Integrity audits

After each coding or revision batch, the database is checked against six families of constraints. Schema integrity (columns match the protocol). Codebook compliance (every code belongs to the closed vocabulary). Dominance-rank validity (ranks are integers between 1 and 3, and each document carries at least one rank-1 row in the relevant satellite). The honesty rule (empty coded fields carry a "not addressed" note). Referential integrity (no orphan rows across tables). Format conventions (dates in ISO format, valid file paths). The audit runs as a read-only check and reports pass or fail with itemised errors.
