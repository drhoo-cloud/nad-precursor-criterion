# 업로드 체크리스트

현재 상태: GitHub `drhoo-cloud/nad-precursor-criterion`에 공개 중.
Zenodo 보관 완료 — **Concept DOI `10.5281/zenodo.22783930`**.

| 릴리스 | 버전 DOI |
|---|---|
| v2.5.0 | 10.5281/zenodo.22783931 |
| v2.5.1 | 10.5281/zenodo.22784277 |
| **v3.0.0** | 이번에 발행 |

원고에는 **Concept DOI**를 쓴다. 버전이 늘어도 바뀌지 않는다.

## A. 올리기 전에 로컬에서 확인

```bash
python3 verify_values.py
```

출력의 왼쪽(계산값)과 오른쪽(논문에 적힌 값)이 모두 같아야 한다. 하나라도 다르면 올리지 않는다.

```bash
python3 PharmRes_Figure1.py
python3 PharmRes_figures34.py
python3 PharmRes_FigureS2_prisma.py
python3 PharmRes_GraphicalAbstract.py
```

네 스크립트가 `figures/`에 파일을 쓴다. `figures/`는 저장소에 비어 있고 `.gitignore`가
출력물을 제외하므로 커밋되지 않는다.

**서체** — 스크립트는 `Nimbus Sans`를 쓰고, `_fontreg.py`가 Ghostscript에 딸려 오는
URW base-35 세트에서 이를 등록한다. 둘 다 없으면 스크립트 머리의 `FONT` 값을 로컬에 있는
Helvetica 계열로 바꾼다. 레이아웃은 실측 기반이라 서체를 바꿔도 배치가 무너지지 않는다.

## B. v3.0.0 반영 사항

제목이 바뀌었으므로 README · CITATION.cff · .zenodo.json을 갱신했다.

> Vitamin B3 precursors: only the acid branch raises NAD⁺, and only a deficit makes it count

## C. 커밋과 릴리스

```bash
git add -A
git commit -m "v3.0: new title and abstract; Nimbus Sans font registration; figure legend corrections"
git push
```

Releases → Draft a new release
- Tag `v3.0.0` → **Create new tag: v3.0.0 on publish**
- Title `Supplementary Code S1 (Pharmacological Research, submitted version)`
- 본문에 제목 변경을 한 줄 적는다

**Zenodo 스위치는 이미 ON이므로** 릴리스를 발행하면 자동으로 보관되고, Concept DOI는
새 버전을 가리킨다. 원고의 DOI는 고칠 필요가 없다.

## D. 원고 쪽 DOI — 이미 반영됨

| 파일 | 위치 |
|---|---|
| `PharmRes_v3.0_Manuscript.docx` | 표제지 Data availability · 참고문헌 말미 `[dataset]` |
| `PharmRes_v3.0_Supplementary.docx` | Appendix S2 · S7.10 Availability |
| `PharmRes_v3.0_CoverLetter.docx` | 7단락 |

참고문헌 말미의 데이터 인용은 번호 목록 밖에 둔다(Elsevier는 조판 시 `[dataset]` 태그를 제거한다).

```
[dataset] Sun Z, Nguyen TTM, Kim J-W et al. Analysis code, literature-audit record
and trial extraction for: Vitamin B3 precursors — only the acid branch raises NAD+,
and only a deficit makes it count. Zenodo, 2026. doi:10.5281/zenodo.22783930.
```

## E. 저장소에 일부러 넣지 않은 것

- **Figure 2 작도 스크립트** — 손으로 그린 경로 도식. 원자료는 `data/figure2_trial_nodes.csv`
- **원고·보충자료 본문** — 출판사 권리 대상. 코드와 자료만 MIT
- **저작권 있는 원문 PDF** — 감사 기록은 PMID로만 식별한다
