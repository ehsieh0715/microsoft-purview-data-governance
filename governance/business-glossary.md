# Business Glossary

## Purpose

The business glossary establishes consistent business terminology for governed data and provides shared definitions for use across analytics, reporting, data quality, and governance.

Business terms and definitions are maintained as structured metadata in [`business_glossary.csv`](../config/business_glossary.csv).

## Governance

Business terms follow a controlled lifecycle:

| Stage | Purpose |
| --- | --- |
| **1. Propose** | Introduce a new term or definition change. |
| **2. Review** | Review the definition, domain alignment, related concepts, and potential conflicts. |
| **3. Approve** | Obtain approval from the accountable governance role. |
| **4. Publish** | Make the approved definition available to data consumers. |
| **5. Maintain** | Review and update terms as business meaning or usage changes. |
| **6. Deprecate** | Retire terms that are no longer valid while preserving governance history. |

Business terms may be associated with one or more governed data elements. These relationships are maintained in [`governed_data_elements.csv`](../config/governed_data_elements.csv).

Ownership and stewardship are derived from the relevant governance domain and maintained in [`domain_ownership.csv`](../config/domain_ownership.csv).

## Production Considerations

The glossary metadata in this repository is illustrative. In a production environment, terms would typically be managed through an enterprise data catalogue or governance platform with approval workflows, ownership, versioning, search, and relationships to governed data assets.