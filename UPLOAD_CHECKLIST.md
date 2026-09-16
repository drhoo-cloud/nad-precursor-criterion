# 업로드 체크리스트

## A. 올리기 전에 로컬에서 확인

```bash
python3 verify_values.py
```

출력의 왼쪽(계산값)과 오른쪽(논문에 적힌 값)이 모두 같아야 합니다. 하나라도 다르면
올리지 마십시오.

```bash
python3 PharmRes_Figure1.py
python3 PharmRes_figures34.py
python3 PharmRes_FigureS2_prisma.py
python3 PharmRes_GraphicalAbstract.py
```

네 스크립트가 `figures/`에 파일을 씁니다. `figures/`는 저장소에 비어 있고,
`.gitignore`가 출력물을 제외하므로 커밋되지 않습니다.

**서체**: 스크립트는 `Nimbus Sans`를 씁니다. 설치되어 있지 않으면 스크립트 머리의
`FONT` 값을 로컬에 있는 Helvetica 계열로 바꾸십시오. 레이아웃은 실측 기반이라
서체를 바꿔도 배치가 무너지지 않습니다.

## B. GitHub

저장소 이름 **`nad-precursor-criterion`** · public

```bash
git init
git add .
git commit -m "Supplementary Code S1: model, figures, literature-audit record"
git branch -M main
git remote add origin https://github.com/drhoo-cloud/nad-precursor-criterion.git
git push -u origin main
```

기존 `bjd-vitamin-b3-nad`는 **건드리지 말고 그대로 두십시오.** 이 저장소는 별개입니다.

## C. Zenodo

1. zenodo.org 로그인 → 계정 메뉴 → **GitHub**
2. `nad-precursor-criterion` 스위치 **ON**
3. **스위치를 켠 다음에** GitHub에서 릴리스를 만드십시오. 순서가 바뀌면 보관되지 않습니다.

릴리스: 태그 `v2.5.0`, 제목 `Supplementary Code S1 (Pharmacological Research, submitted version)`

발급되는 DOI 두 개 중 **Concept DOI**(모든 버전을 가리키는 쪽)를 원고에 씁니다.

## D. DOI를 받은 뒤 — 원고 4곳 교체

현재 전부 `10.5281/zenodo.XXXXXXX` 자리표시자입니다.

| 파일 | 위치 |
|---|---|
| `PharmRes_v2.5_Manuscript.docx` | 표제지 Data availability |
| `PharmRes_v2.5_Supplementary.docx` | Appendix S2 |
| `PharmRes_v2.5_Supplementary.docx` | S7.10 Availability |
| `PharmRes_v2.5_CoverLetter.docx` | 7단락 |

참고문헌에 데이터 인용도 추가합니다.

```
[dataset] Sun Z, Nguyen TTM, Kim J-W et al. Analysis code, literature-audit record
and trial extraction for: Resting NAD+ sets the ceiling, not the dose. Zenodo, 2026.
doi:10.5281/zenodo.XXXXXXX
```

## E. 개정이 있을 때

코드를 고쳐 푸시한 뒤 `v2.6.0` 릴리스를 만드십시오. Zenodo가 새 Version DOI를 발급하고
Concept DOI는 그대로 최신을 가리킵니다. 원고에 Concept DOI가 들어가 있으면 다시 고칠
필요가 없습니다.

## F. 저장소에 일부러 넣지 않은 것

- **Figure 2 작도 스크립트** — 손으로 그린 경로 도식이라 없습니다. 원자료는
  `data/figure2_trial_nodes.csv`에 있고 README에 명시했습니다.
- **원고·보충자료 본문** — 출판사 권리 대상이므로 넣지 않습니다. 코드와 자료만 MIT입니다.
- **저작권 있는 원문 PDF** — 넣지 않습니다. 감사 기록은 PMID로만 식별합니다.
