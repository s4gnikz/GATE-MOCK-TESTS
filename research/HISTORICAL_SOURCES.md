# Historical source and access ledger

Access date: 12 October 2026. Official sources only. **Downloaded is not synonymous with read, solved, or reviewed.** Research summaries do not reproduce complete historical questions. Local source files are research references, not mock-paper content.

## Entry points

- [IIT Guwahati historical archive](https://gate2026.iitg.ac.in/download.html): opened; links extracted directly from HTML.
- [IIT Guwahati 2026 master papers and keys](https://gate2026.iitg.ac.in/QPs-answer-keys.html): opened; marking guidance read.
- [Officially linked bulk archive](https://drive.google.com/drive/folders/1sV6FgtOUDl_PGjc36Zdc0eJwK1zZ_2OF): web tool returned a minimal shell, not usable file contents.
- [IIT Kanpur historical archive](https://gate.iitk.ac.in/GATE2023/download_info.html): indexed content accessible through search; direct local network access failed DNS lookup.

## Paper reading ledger

Question numbers below follow each source, including separate technical numbering in older papers. Figures in text-only samples were not assumed fully understood.

| Year/session | Official paper | Actual reading scope | Local status |
|---|---|---|---|
| 2015 | [CS](https://gate.iitk.ac.in/GATE2023/doc/papers/2015/cs_2015.pdf) | Search-index excerpt: header and GA Q1–2 only | Full download failed; HTTP 502 via web, DNS failure locally |
| 2016 | [CS](https://gate.iitk.ac.in/GATE2023/doc/papers/2016/cs_2016.pdf) | Indexed partial key only; no question study | Full download failed |
| 2017 | [CS target attempted](https://gate.iitk.ac.in/GATE2023/doc/papers/2017/cs_2017.pdf) | Not read | HTTP 502; target not independently confirmed beyond archive year listing |
| 2018 | [CS](https://gate.iitk.ac.in/GATE2023/doc/papers/2018/cs_2018.pdf) | Indexed partial key only; no question study | Full download failed |
| 2019 | [CS](https://gate2026.iitg.ac.in/doc/download/2019/cs_2019.pdf) | Physical PDF page 11, technical Q32–35 visually read | 19-page PDF downloaded; mostly image-only |
| 2020 | [CS](https://gate2026.iitg.ac.in/doc/download/2020/cs_2020.pdf) | Physical page 11 technical Q32–34 visually read; embedded key read | 18-page PDF downloaded; stems mainly images |
| 2021 Set1 | [Combined CS](https://gate2026.iitg.ac.in/doc/download/2021/cs_2021.pdf) | Physical pages 11,12,23,32: GA Q10; technical Q1–2,26,38 visually read | 91-page combined PDF downloaded; image-only text extraction |
| 2021 other content | Same combined PDF | Not read | Downloaded only |
| 2022 CS | [CS](https://gate2026.iitg.ac.in/doc/download/2022/cs_2022.pdf) | Text samples Q21–30; complete key read/parsed | PDF and extraction retained |
| 2023 CS | [CS](https://gate2026.iitg.ac.in/doc/download/2023/cs_2023.pdf) | Text samples Q18–25; complete key read/parsed | PDF and extraction retained |
| 2024 CS1 | [CS1](https://gate2026.iitg.ac.in/doc/download/2024/CS124S5.pdf) | Text samples Q9–15; complete key read/parsed | PDF and extraction retained |
| 2024 CS2 | [CS2](https://gate2026.iitg.ac.in/doc/download/2024/CS224S6.pdf) | Key parsed; question content not read | PDF and extraction retained |
| 2025 CS1 | [CS1](https://gate2026.iitg.ac.in/doc/download/2025/CS12025.pdf) | Text samples Q1–31 and Q63–65; complete key read | PDF and extraction retained |
| 2025 CS2 | [CS2](https://gate2026.iitg.ac.in/doc/download/2025/CS22025.pdf) | Not read | PDF and extraction retained |
| 2026 CS1 | [CS1](https://gate2026.iitg.ac.in/doc/download/2026/QPs/CS1.pdf) | Text samples Q8–15 and Q39–45; complete key read/parsed | PDF and extraction retained |
| 2026 CS2 | [CS2](https://gate2026.iitg.ac.in/doc/download/2026/QPs/CS2.pdf) | Key parsed; question content not read | PDF and extraction retained |

## Official key links

- [2021 combined](https://gate2026.iitg.ac.in/doc/download/Answer_keys2021/cs_merged_2021.pdf): downloaded, image-only; not counted.
- [2022 CS](https://gate2026.iitg.ac.in/doc/download/Answer_keys2022/cs_2022.pdf).
- [2023 CS](https://gate2026.iitg.ac.in/doc/download/Answer_keys2023/CS_ANS_GATE2023.pdf).
- [2024 CS1](https://gate2026.iitg.ac.in/doc/download/2024/CS1FinalAnswerKey.pdf) and [CS2](https://gate2026.iitg.ac.in/doc/download/2024/CS2FinalAnswerKey.pdf).
- [2025 CS1](https://gate2026.iitg.ac.in/doc/download/2025_Key/CS1_Keys.pdf) and [CS2](https://gate2026.iitg.ac.in/doc/download/2025_Key/CS2_Keys.pdf): both downloaded; CS2 not reviewed.
- [2026 CS1](https://gate2026.iitg.ac.in/doc/download/2026/Keys/CS1_Keys.pdf) and [CS2](https://gate2026.iitg.ac.in/doc/download/2026/Keys/CS2_Keys.pdf).

## Reproducibility and limitations

`historical/fetch.py` obtains linked CS PDFs and extracts text with pypdf. `historical/sha256.json` records hashes. `historical/count_types.py` counts only keys that yield exactly 65 parseable rows; it does not infer subject labels, solve questions, or validate official answers. `historical/type_counts.json` stores six accepted count results. The 2025 CS1 count is separately read from the key. Failed parsers are not evidence of a defective source.

Image-only source samples were rendered with pypdfium2 and visually inspected using the image tool. A fitz import failed; no result was attributed to that failed attempt. Rendered sampled pages remain alongside the PDFs. Text extraction is not sufficient for circuit, graph, automaton, map or folding diagrams; no comprehensive diagram audit is claimed.

No human reviewer participated in this research. No empirical timing study, candidate difficulty calibration, exhaustive subject-frequency table, or full independent solution verification of historical papers has been performed.


## Follow-up retrieval update (12 October 2026)

A bounded second search found an accessible official alternate for **2018**. The [IIT Bombay GATE 2021 archive](https://gate.iitb.ac.in/G21/prev_qp.php) links [2018QP_CS.pdf](https://drive.google.com/file/d/1CboGjdOkvPzijQk8IXzsE6LdJst-xv9M/view). The public download succeeded: 23 pages, 937,797 bytes, saved as `historical/IITB_2018QP_CS.pdf` with text extraction and SHA256 manifest entry. This supersedes the earlier 2018 download-failed status, but does not imply a full-paper solution review. Actually read: GA Q1-10 text (GA Q9 diagram not inspected), technical Q1-8 and Q32-37 text. Mathematical typography in extraction may lose superscripts, so no extracted formula was reused in mock content.

The [NPTEL GATE paper-mapping page](https://gate.nptel.ac.in/gatequestionpaper.html) linked five 2015/2016 CS PDFs at `https://nptel.ac.in/content/Gate_Papers/CS/GATE_CS_2015_1.pdf` (also 2015_2,2015_3,2016_1,2016_2). All five returned HTTP 404. The [IISc 2024 archive](https://gate2024.iisc.ac.in/download/) exposed year headings through web retrieval but local fetch returned 403 and no direct older CS paper links were obtained. No new 2017 full paper was retrieved. Thus full-source access remains unresolved for 2015-2017.

Additional official search-index samples were read from IIT Madras 2015 Set2 Q1-8, Set1 Q13-19, and Set3 Q9-15; these were excerpts only, not successful PDF downloads. The indexed papers are [Set1](https://gate.iitm.ac.in/gateqps/2015/cs1.pdf), [Set2](https://gate.iitm.ac.in/gateqps/2015/cs2.pdf), and [Set3](https://gate.iitm.ac.in/gateqps/2015/cs3.pdf). Their full-paper access/review remains incomplete.
