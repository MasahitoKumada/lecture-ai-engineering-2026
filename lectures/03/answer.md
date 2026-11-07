# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：
  - 素のLLM は用語集を確認せずにその場で答えようとするが、学習支援エージェントは `search_glossary` を先に使い、用語の定義と回数を確認してから返答する。
- `--trace` で見えたツール呼び出し（ツール名と引数）：
  - `search_glossary({'query': 'LoRA'})` のように、用語を1つずつ渡して検索する。
  - その後、必要に応じて `get_lecture_summary({'lecture': 3})` のように回の要点を参照する。
- 1つの質問での LLM 呼び出し回数（`requests`）：
  - 1問に対して、最初の回答前に用語確認のために複数回のモデル呼び出しが発生する。`--trace` で `requests` を確認すると、検索と回答の両方が見える。
- 追加したツールと、docstring に書いた説明：
  - この課題では発展(a) のために ADK 版の `root_agent` を作成し、Pydantic AI 側と同じ `INSTRUCTIONS` とツールを持たせた。

## 宿題

- 取り組んだレベル：発展（a）
- やったこと：
  - `app/agent.py` の `INSTRUCTIONS` と `app/tools.py` の `search_glossary` / `get_lecture_summary` をそのまま使い、`adk_agent/glossary_agent/agent.py` で ADK の `Agent` を作成した。
  - `PYTHONPATH=. uv run --with google-adk adk run adk_agent/glossary_agent` で動作確認を行った。
- 結果：
  - 最初の `gemini-2.5-flash-lite` を指定したときは 404 で失敗したが、ADK の例と同じ `gemini-3.5-flash-lite` に直すと正常に起動した。
  - つまり、ADK でも「指示とツールを渡す部分」だけが書き変わり、コアの知識とツールロジックはそのまま使えることが分かった。
- 気づき・疑問：
  - Pydantic AI は Python コード中で `agent.tool_plain(...)` のように明示的に登録するが、ADK は `tools=[...]` と宣言的に渡すため、構成が短く見える。
  - ただし、モデル名や API 仕様の変化に追従する必要があり、公開例と実際の利用可能モデル名の違いには注意が必要だと感じた。
