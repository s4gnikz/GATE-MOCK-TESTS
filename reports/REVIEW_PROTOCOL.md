# Review and release protocol

An author creates complete question content and a worked solution. A different model reviewer re-derives the answer, evaluates every option, checks assumptions and evaluates difficulty. Initial review is not necessarily blinded: the provenance records when proposed answers were visible. No human review or empirical difficulty calibration is claimed.

For suitable finite problems, Python performs enumeration or simulation. Actual C snippets are compiled with GCC where available; SQL examples are tested using SQLite with foreign keys enabled. Such executions supplement mathematical/language-standard reasoning; they do not prove properties for arbitrary inputs or all implementations. The evidence scripts document the scope of every check.

Each review is bound to a SHA-256 digest of the question ID, stem, options, answer, NAT bounds, solution and option explanations. Editing any of these invalidates its acceptance. The importer requires agreeing answers, a passing review, no unresolved issues, and the matching digest. Utility tests deliberately tamper with these conditions to confirm rejection.

Difficulty labels are editorial estimates based on reasoning effort, not a guarantee about how a candidate will perform. Failed calibration results in a rewrite or a lower classification. A final paper still must satisfy the configured distribution; this cannot be repaired solely by changing labels.

Duplicate detection combines normalized hashes, number-normalized text, lexical and n-gram candidate search, and reviewed family/structure signatures. Signatures are editorial metadata, not theorem-proving descriptions. Embedding support is not configured. Independent editorial comparison is necessary because low lexical similarity does not prove distinct reasoning. Historical comparisons are limited to the retrieved corpus and inspected samples; no claim of global originality against every unpublished or commercial source is possible.

No released paper contains author/reviewer provenance or hidden solutions in its question section. Acceptance records, review findings, and execution logs are kept outside student papers. A full-series release remains failed until all 100 papers exist and every mandatory audit passes.
