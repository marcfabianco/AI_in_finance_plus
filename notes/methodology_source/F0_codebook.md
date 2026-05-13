# Codebook

The codebook is the controlled vocabulary used to code every document in the database. Five fields take values from a closed list. New codes are added only after explicit review, so that the analytical schema remains stable across coders and across batches.

## 1. Document type

Each document is assigned one document type. The seven values cover most of the supervisory and academic literature published by the five bodies. A secondary type is recorded only when the primary type cannot stand alone.

| Code | When to apply |
|---|---|
| `policy_paper` | Standard-setter or international-organisation paper that ends in a policy direction or recommendation. Includes conceptual mapping, cross-jurisdictional comparison, operational toolkits, and executive summaries of policy reports. |
| `academic` | Research design with theory, model, or empirical analysis. The primary purpose is to contribute knowledge rather than to direct policy. |
| `stocktake` | Structured survey or mapping of what authorities or firms are doing. Primarily descriptive of the state of play across many actors. |
| `assessment_report` | Systematic backward-looking review by an institution. Covers self-assessment (annual reports of a body's own activities), country assessment (Article IV reports, FSAPs, country-program reviews), and peer assessment (FATF Mutual Evaluation Reports and analogous reviews against a standard). |
| `standard_guidance` | Official rule text or principles intended to be implemented, for example Basel principles, FATF Recommendations, or BCBS standards. |
| `speech_commentary` | Speeches, blog posts, op-eds, statements, and secretariat-written records of meetings, plenaries, forums, and consultative events. Brief, position-signalling or event-documenting. |
| `other` | Genuinely far from the six above. The notes field must explain why. |

## 2. Actor

One or more actors are coded per document. The actor codebook captures who the document treats as the relevant population for the AI question at hand. New actor codes require review before being written.

| Code | Who |
|---|---|
| `regulators_supervisors` | Banking regulators and supervisors acting in their supervisory capacity. Includes central banks when the document treats them as supervisors of banks (microprudential or system-wide supervision regimes). |
| `central_banks` | Central banks acting in non-supervisory capacities, including monetary policy, market operations, payments operation, financial-stability surveillance qua surveillance, and internal institutional matters (HR, capacity, governance). |
| `financial_institutions` | Financial institutions and supervised entities, mostly banks. Boards and senior management fold into this category. |
| `customers_users` | Customers, users, and data subjects of financial services. |
| `tech_companies` | Technology providers that supply AI infrastructure to financial institutions and authorities, including cloud-service providers, foundation-model providers, specialised AI hardware vendors, and big-tech firms. |
| `competition_authorities` | Antitrust and competition authorities when the document addresses them as the regulatory addressee of AI market-structure or concentration concerns. |
| `data_protection_authorities` | Data-protection and privacy authorities when the document addresses them as the regulatory addressee of AI data-use, profiling, automated-decisioning, or data-subject-rights concerns. |
| `governments` | Governments and public-sector administrators acting in non-financial-supervisory capacities, including line ministries, public-sector units adopting AI for service delivery, tax administration, judicial process, and infrastructure planning. |
| `system` | The financial system or the economy as a whole. |
| `other` | Anything genuinely unclassified. The notes field must name the actor. |

## 3. Problem

A list of problem codes is recorded per (document, actor) pair. The list is ordered with the most dominant problem first. Eleven problem codes cover the substantive risks and concerns the documents raise.

| Code | What |
|---|---|
| `credit_risk` | Default, probability of default, credit-underwriting risks. |
| `market_risk` | Trading-book, internal-model approach, market-movement losses. |
| `operational_risk` | IT infrastructure, data quality, process failures, system outages. |
| `model_risk` | Incorrect model use and AI-specific model-risk-management concerns, including explainability, validation, and compliance. |
| `third_party_risk` | Concentration on cloud, foundation-model, or other outsourcing providers. |
| `cyber_data_security` | Cyber attacks, model poisoning, data breaches. |
| `systemic_risk` | Financial stability, herding, correlation, contagion, deepfake-driven runs. |
| `consumer_data_protection` | Bias, discrimination, adverse action, fairness, privacy, and data-subject rights. Typically coded as a secondary problem alongside `model_risk` when a document raises bias, fairness, explainability, discrimination, or privacy as a substantive concern affecting end-users. |
| `capacity_governance` | Institutional capacity gaps other than staff skills, including governance frameworks, board and management oversight, accountability for AI use, budget rigidity, IT legacy, and data infrastructure. |
| `staff_skills` | Workforce skills gaps, recruitment, retention, and upskilling of supervisor and central-bank staff for AI adoption. The institution's own people-side capability. |
| `job_displacement` | AI's effect on the workforce as a labour-market phenomenon, including task automation, occupational shifts, wage and employment effects, and distributional consequences. Distinct from `staff_skills`, which is about an institution's own capability. |

## 4. Policy area

One or more policy areas are recorded per document, each with a dominance rank. The policy area captures the part of the AI-in-finance landscape the document operates in, regardless of which problems it raises.

| Code | What |
|---|---|
| `microprudential` | Individual firm soundness supervision. |
| `macroprudential` | System-wide stability surveillance. |
| `supervisory_process` | The supervision-of-banks regime, including supervisory frameworks, capacity, and methods. |
| `central_bank_operations` | Central banks' own operational and institutional functions, distinct from supervision of banks. |
| `consumer_protection` | The conduct and fairness regime as a whole. |
| `aml_cft` | The financial-crime regime. |
| `resolution` | Recovery, resolution, and crisis management. |
| `payments` | Payments-system oversight. |
| `empirical_evidence` | Documents whose primary character is empirical evidence about AI (surveys of attitudes or usage, randomised experiments, observational and econometric studies) that informs policy debates without operating within a regime. |
| `ai_methodology` | Documents whose primary character is the development, evaluation, or methodological deployment of AI and ML techniques. The contribution is the method itself. |
| `market_structure` | Documents whose primary character is analysis of the AI market structure, value chain, or competition dynamics. Operates upstream of prudential and conduct regimes, in competition-policy territory. |
| `cross_sector` | Documents that span multiple application sectors as parallel domains (health, education, finance, agriculture, transport), with finance as one thread among several. |
| `tax_administration` | Documents that operate within tax, customs, or revenue administration. |
| `public_sector_ai_adoption` | Public-sector adoption of AI for service delivery, government modernisation, and supervisory-adjacent state functions. |
| `other` | Anything else genuinely unclassifiable. The notes field must name and explain. |

## 5. Sub-area

A sub-area code adds tool-level or use-case granularity within a policy area. Sub-areas are grouped by the regime they sit inside. New sub-area codes require review before being written.

**Public-sector adoption**

| Code | What |
|---|---|
| `suptech` | Supervisors' adoption of AI and ML for their own supervisory work, including supervisory matching, AML cross-firm screening, ESG and climate disclosure parsing, regulatory chatbots, and supervisory-document review. |
| `supervisory_capacity_dev` | Supervisors' capacity-development for AI, including training programmes, AI competencies, organisational structures, and adoption capacity. |
| `supervisory_mrm` | Supervisory expectations on AI model risk management imposed on supervised entities, including explainability, validation, and governance requirements. |
| `cb_analytical_tools` | Central banks' use of AI and ML for monetary-policy analysis, communication mapping, sentiment analysis, and NLP on central-bank texts. |
| `statistical_compilation` | Central banks' use of AI and ML for official statistics, granular-data integration, nowcasting, and big-data sources for statistical aggregates. |
| `payments_ai_tools` | AI and ML applied to payment-system oversight, including real-time gross settlement anomaly detection, AML in correspondent banking, and fraud detection in payment flows. |
| `monetary_policy` | The monetary-policy function as a sub-area within central-bank operations, including forecasting, policy-rate transmission, communication, and the inflation-expectations channel. |

**Firm-level use cases**

| Code | What |
|---|---|
| `regtech_firms` | Financial institutions' use of AI for regulatory compliance and internal risk management, including AML and CFT detection at firms, capital-rules parsing, regulatory reporting automation, and compliance chatbots. |
| `credit_underwriting` | AI and ML for credit assessment, scoring, and loan-eligibility decisions at financial institutions. |
| `insurance_underwriting` | AI and ML for insurance risk assessment, pricing, and claims processing at insurers. |
| `customer_facing_ai` | AI in customer-facing financial services, including chatbots, robo-advising, and customer-service automation. |
| `internal_ops_efficiency` | AI for back-office automation, productivity gains, and internal process optimisation at financial institutions. |

**Macro and cross-cutting**

| Code | What |
|---|---|
| `macroeconomic_impact` | Research on AI's effect on output, inflation, productivity, and labour markets at the economy-wide level. |
| `household_adoption_research` | Survey-based empirical research on household and consumer adoption of AI, trust, and perceptions. |
| `ai_market_structure` | Analysis of the AI supply chain, vendor concentration, big-tech footprint, and foundation-model market dynamics. |
| `cyber_resilience` | AI's role in cyber security and operational resilience, including threat detection, model poisoning, and cryptographic risks. |

## 6. Conventions

The codebook is closed but extensible. A new code is added only after the coder flags a substantive density of an uncoded term, framing, or actor across multiple documents and the addition is reviewed and approved. Until promotion, novel material lives in the notes field with an explicit flag so that periodic audits can surface candidate codebook gaps.

The dominance principle governs every coded dimension. The coder records what is dominant in the document rather than every mention. Ranks 1, 2, and 3 are used, capped at three, with ties at rank 1 permitted. Absences are recorded as well, since absence in a body's writing is itself a signal worth keeping.

Every row carries a notes field with the coder's rationale and a supporting quote from the document. The rationale must be sufficient that an auditor can verify the coding call without re-reading the source.
