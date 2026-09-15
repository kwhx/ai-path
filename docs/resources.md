# The Complete AI Engineer Roadmap Free Resource Map

## Py

| Topic |  Primary resource | Also good |
|---|---|---|
| Syntax, functions, classes, modules, packages, exceptions, type hints, lists/dicts/sets/tuples | [CS50P – Harvard's Intro to Programming with Python](https://cs50.harvard.edu/python/) (free, edX-hosted, also fully on YouTube via freeCodeCamp's upload) | [Python official tutorial](https://docs.python.org/3/tutorial/) |
| Iterators / generators, decorators, OOP deep-dive | [Corey Schafer's Python OOP & Generators playlists](https://www.youtube.com/@coreyms) — the most-recommended free Python YouTube channel, ever | [Real Python](https://realpython.com/) articles on generators/iterators |
| async / await | [RealPython: Async IO in Python](https://realpython.com/async-io-python/) | [Python docs – asyncio](https://docs.python.org/3/library/asyncio.html) |
| Virtual environments, pip | [Python docs – venv](https://docs.python.org/3/library/venv.html) + Corey Schafer's venv video (same channel above) | [pip docs](https://pip.pypa.io/en/stable/) |
| Exceptions, assertions, error handling | CS50P (covers this directly) | [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) — free full book online |
| File handling & I/O, reading/writing text and CSV | [Automate the Boring Stuff, Ch. 8–9, 16](https://automatetheboringstuff.com/) | CS50P Files lecture |
| Command-line arguments (`sys.argv`) | Automate the Boring Stuff | Python docs – `sys` module |
| `math`, `datetime` modules | [Python official docs](https://docs.python.org/3/library/) | CS50P |
| regex | [RealPython Regex Guide](https://realpython.com/regex-python/) | Automate the Boring Stuff Ch. 7 |
| threading | [RealPython: An Intro to Threading in Python](https://realpython.com/intro-to-python-threading/) | Python docs – `threading` |
| sqlite3 / DB-API, direct DB connectivity | [Python docs – sqlite3](https://docs.python.org/3/library/sqlite3.html) | Corey Schafer's SQLite tutorial |
| JSON | Automate the Boring Stuff Ch. 16 | Python docs – `json` |
| HTTP / API clients | [RealPython: Python `requests`](https://realpython.com/python-requests/) | Automate the Boring Stuff Ch. 17 |
| Basic testing | [RealPython: Getting Started with Testing in Python](https://realpython.com/python-testing/) (pytest) | Python docs – `unittest` |
| scikit-learn | [scikit-learn official tutorials](https://scikit-learn.org/stable/tutorial/index.html) | freeCodeCamp scikit-learn course (YouTube) |
| NumPy | [NumPy official Quickstart](https://numpy.org/doc/stable/user/quickstart.html) | Keith Galli's NumPy tutorial (YouTube) |
| Pandas | [Pandas: 10 Minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) + [Data School's Pandas playlist](https://www.youtube.com/@dataschool) | Corey Schafer's Pandas playlist |
| Jupyter | [Official Jupyter docs](https://docs.jupyter.org/) | Corey Schafer's Jupyter Notebook tutorial |
| Matplotlib, Seaborn (scatter, bar, styled line plots) | [Matplotlib official tutorials](https://matplotlib.org/stable/tutorials/index.html) + [Seaborn official tutorial](https://seaborn.pydata.org/tutorial.html) | Corey Schafer's Matplotlib playlist |

**Build this:** a small CLI tool that reads a CSV, cleans it with pandas, stores it in SQLite, exposes a tiny Flask/FastAPI HTTP endpoint, and has 3 pytest tests. That one project touches almost every bullet above.

---

## Classical / Symbolic AI 

| Topic |  Primary resource |
|---|---|
| State-space search (BFS, DFS, A*, hill climbing), CSP, adversarial search/game playing | [CS50's Introduction to AI with Python (Harvard/edX)](https://cs50.harvard.edu/ai/) — built entirely around these exact topics with runnable Python projects |
| Same topics, project-based (Pac-Man search agents) | [Berkeley CS188: Intro to AI](https://inst.eecs.berkeley.edu/~cs188/) — free lecture videos + the famous Pac-Man programming projects |
| Propositional & predicate logic, resolution, clause form conversion | [MIT 6.034 Artificial Intelligence (OpenCourseWare, Patrick Winston)](https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/) — classic, free, covers logic and resolution in depth |
| Expert systems (MYCIN), procedural vs. declarative knowledge, generate-and-test heuristic search | Same MIT 6.034 OCW lectures above — MYCIN and knowledge representation are core Winston lecture topics |
| AO* search | [GeeksforGeeks: AO* Search Algorithm](https://www.geeksforgeeks.org/ai-and-or-graph-explanation-and-algorithms/) (free reference/tutorial with Python code) |
| Toy problems: Water Jug, Monkey & Banana, Block Words | GeeksforGeeks has free worked Python implementations of each — search "[problem name] GeeksforGeeks Python"; solve them yourself as BFS/DFS exercises after CS50AI/CS188 |

**Build this:** implement the Water Jug and Monkey-and-Banana problems yourself in Python using BFS and then A*, from scratch, no copying — this is what actually cements search algorithms.

---

## ML (classical + theory)

| Topic |  Primary resource |
|---|---|
| Supervised learning: decision trees, Naïve Bayes, regression, feed-forward NN + backprop + regularization | [Andrew Ng's Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction) (Coursera, audit free) |
| Intuitive explanations of every classical ML algorithm (Naive Bayes, decision trees, PCA, EM/GMM, HMM, cross-validation, ROC-AUC, confusion matrix, precision/recall/F1) | [StatQuest with Josh Starmer](https://www.youtube.com/@statquest) — widely regarded as the best free channel for building real intuition on these exact topics |
| Unsupervised: K-Means, EM, GMM, PCA, factor analysis, dimensionality reduction | StatQuest (above) + Andrew Ng's Specialization |
| Association rule mining | [GeeksforGeeks: Apriori Algorithm / Association Rule Mining](https://www.geeksforgeeks.org/machine-learning/apriori-algorithm/) |
| Curse of dimensionality (theory) | StatQuest's PCA/dimensionality videos + [GeeksforGeeks explainer](https://www.geeksforgeeks.org/curse-of-dimensionality-in-machine-learning/) |
| Semi-supervised learning | Andrew Ng's Specialization covers the framing; [GeeksforGeeks: Semi-Supervised Learning](https://www.geeksforgeeks.org/semi-supervised-learning-in-ml/) for a quick reference |
| Reinforcement learning | [David Silver's RL Course (UCL/DeepMind)](https://www.davidsilver.uk/teaching/) — the canonical free RL course, or [Hugging Face Deep RL Course](https://huggingface.co/learn/deep-rl-course) for a more hands-on modern take |
| Probabilistic Graphical Models (theory): Bayesian Networks, Markov Random Fields, HMM, directed graphical models, exploiting independence properties, from distributions to graphs, inference | [Probabilistic Graphical Models Specialization — Daphne Koller (Coursera, audit free)](https://www.coursera.org/specializations/probabilistic-graphical-models) — this *is* the canonical course on this exact syllabus topic. Alternative: [Stanford CS228 lecture notes](https://ermongroup.github.io/cs228-notes/) (fully free, no signup) |
| Classical ML evaluation metrics (confusion matrix, precision/recall/F1, ROC-AUC, cross-validation) | StatQuest (above) — dedicated videos for each |

**Build this:** take one small tabular dataset (e.g. Titanic or a Kaggle starter set) and run it through: a decision tree, Naive Bayes, k-means clustering, and PCA for visualization — then compute confusion matrix/F1/ROC-AUC by hand once before using sklearn's built-in versions.

---

## Deep Learning

| Topic | Primary resource |
|---|---|
| Neural networks, backprop intuition | [3Blue1Brown: Neural Networks series](https://www.youtube.com/@3blue1brown) — the best visual intuition available, free |
| Neural networks from scratch (code-level, including backprop and later GPT) | [Andrej Karpathy: Neural Networks — Zero to Hero](https://www.youtube.com/@AndrejKarpathy) — you build backprop and a GPT from raw Python; extremely highly regarded |
| CNNs | [CS231n: Convolutional Neural Networks for Visual Recognition (Stanford)](http://cs231n.stanford.edu/) — free lecture videos & notes, the canonical CV/CNN course |
| RNNs / LSTMs, Transformers (NLP-flavored) | [CS224n: NLP with Deep Learning (Stanford)](https://web.stanford.edu/class/cs224n/) — free lecture videos & notes |
| Transformers (from-scratch build) | Karpathy's "Let's build GPT from scratch" (part of Zero to Hero, above) |
| Broad survey incl. multimodal models | [MIT 6.S191: Introduction to Deep Learning](http://introtodeeplearning.com/) — free lectures + labs, updated yearly, includes a Gen AI/multimodal lecture |
| Full specialization path (NN, CNN, RNN/sequence models) | [Deep Learning Specialization — Andrew Ng (Coursera, audit free)](https://www.coursera.org/specializations/deep-learning) |
| Practical, top-down deep learning | [fast.ai: Practical Deep Learning for Coders](https://course.fast.ai/) — free, code-first, very well respected |

**Build this:** train a small CNN on CIFAR-10 or MNIST from scratch (no pretrained weights), then fine-tune a pretrained model on the same data and compare — you'll feel the difference architecture and transfer learning make.

---

## Computer Vision & NLP

| Topic |  Primary resource |
|---|---|
| Classification, detection, segmentation, VLMs (CV) | [CS231n](http://cs231n.stanford.edu/) + [Hugging Face Computer Vision Course](https://huggingface.co/learn/computer-vision-course) (free) |
| OCR | Free tutorials on Tesseract/EasyOCR — [PyImageSearch OCR tutorials](https://pyimagesearch.com/category/optical-character-recognition-ocr/) (many free posts) |
| NLP: classification, embeddings, information extraction, translation, language models | [CS224n](https://web.stanford.edu/class/cs224n/) + [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course) (free, 12 chapters, hands-on with Transformers library) |
| Practical/production NLP pipelines | [spaCy course](https://course.spacy.io/) (free, industrial-strength NLP) |

**Build this:** fine-tune a small Hugging Face transformer (e.g. DistilBERT) on a text classification dataset, then build an OCR pipeline that extracts text from a scanned image and classifies it.

---

## Generative AI

| Topic | Primary resource |
|---|---|
| LLMs, tokenization, sampling (temperature, top-k/top-p), context windows, foundation models | Karpathy's "Let's build GPT from scratch" (Zero to Hero) + [Google's Generative AI Learning Path](https://www.cloudskillsboost.google/paths/118) (free intro tier) |
| Diffusion models | [Hugging Face Diffusion Models Course](https://huggingface.co/learn/diffusion-course) (free) |
| Fine-tuning, distillation | [DeepLearning.AI + Hugging Face short courses on fine-tuning](https://www.deeplearning.ai/short-courses/) (free to watch) — look for "Fine-Tuning Large Language Models" and "Efficient Fine-Tuning" |
| Applied generative AI overview | [Generative AI for Beginners (Microsoft, GitHub)](https://github.com/microsoft/generative-ai-for-beginners) — 21 free, open-source, actively maintained lessons spanning prompting through RAG and agents |

**Build this:** generate text with adjustable temperature/top-p and observe the output change; separately, run a small diffusion model locally (Stable Diffusion via a free Colab notebook) to see the denoising process.

---

## LLM Engineering (prompting, structured outputs, models landscape)

| Topic |  Primary resource |
|---|---|
| Prompt engineering fundamentals | [ChatGPT Prompt Engineering for Developers — DeepLearning.AI/OpenAI](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) (free) |
| Prompting specifically for Claude/Anthropic models | [Anthropic's Prompt Engineering Interactive Tutorial](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview) (free, ~9 chapters, hands-on) |
| System instructions, role separation, structured prompting, few-shot, output constraints, reasoning strategies | Both resources above cover this directly |
| Building multi-step LLM systems, basic evaluation | [Building Systems with the ChatGPT API — DeepLearning.AI](https://www.deeplearning.ai/short-courses/building-systems-with-chatgpt/) (free) |
| Structured outputs & function calling | [Functions, Tools and Agents with LangChain — DeepLearning.AI](https://www.deeplearning.ai/short-courses/functions-tools-agents-langchain/) (free) |
| Prompt injection / adversarial inputs (as a prompting concept) | Covered directly in Anthropic's tutorial above; deeper security treatment in Phase 10 below |
| Models landscape (OpenAI, Anthropic, Google, open-source, hosted vs. local inference) | [Anthropic Academy](https://anthropic.skilljar.com/) (free, certificates included — covers Claude/API in depth) + [Hugging Face Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) to survey open models + [Ollama docs](https://github.com/ollama/ollama) for local inference |

**Build this:** write the same task as three different prompts (naive, few-shot, structured/chain-of-thought) against a real API and compare output quality — you'll internalize why prompt structure matters more than most people expect.

---

## Embeddings

| Topic |  Primary resource |
|---|---|
| Embedding models, cosine similarity, vector search, nearest-neighbor search, semantic search | [Vector Databases: from Embeddings to Applications — DeepLearning.AI](https://www.deeplearning.ai/short-courses/vector-databases-embeddings-applications/) (free, ~90 min, vendor-agnostic) |
| Vector databases, indexing, chunking | [Building Applications with Vector Databases — DeepLearning.AI](https://www.deeplearning.ai/short-courses/building-applications-vector-databases/) (free) + [Pinecone Learn](https://www.pinecone.io/learn/) (free, continuously updated, code-heavy — James Briggs' material here is excellent) |

**Build this:** embed 100 short documents with an open embedding model, store them in a free local vector store (Chroma), and write a script that returns the top-5 nearest neighbors for a query — no framework, just the raw vector math first.

---

## RAG 

| Topic |  Primary resource |
|---|---|
| Document ingestion, parsing, chunking, embedding, retrieval, context construction | [LangChain: Chat with Your Data — DeepLearning.AI](https://www.deeplearning.ai/short-courses/langchain-chat-with-your-data/) (free) |
| Reranking, hybrid search, metadata filtering, agentic RAG (query routing, multi-step reasoning) | [Building Agentic RAG with LlamaIndex — DeepLearning.AI](https://www.deeplearning.ai/short-courses/building-agentic-rag-with-llamaindex/) (free) |
| Citation, hallucination mitigation | Covered in both courses above + Pinecone Learn's RAG section (free) |
| RAG evaluation (retrieval quality, context relevance, groundedness, citation accuracy, answer correctness, hallucination rate) | [Building and Evaluating Advanced RAG — DeepLearning.AI](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) (free) — see Phase 12 for general evaluation resources too |

**Build this:** build a RAG pipeline over a folder of your own PDFs (lecture notes, docs) end-to-end: ingest → chunk → embed → retrieve → generate with citations. Then deliberately ask it something not in the documents and confirm it says so instead of hallucinating.

---

## Tool Calling & MCP

| Topic | Primary resource |
|---|---|
| Function calling, tool schemas, API integration, input validation, error handling, tool selection | [Functions, Tools and Agents with LangChain — DeepLearning.AI](https://www.deeplearning.ai/short-courses/functions-tools-agents-langchain/) (free) + [Anthropic tool-use docs](https://docs.claude.com/en/docs/build-with-claude/tool-use/overview) (free) |
| MCP clients/servers, tools/resources/prompts, schemas, capability negotiation, transport, auth | [MCP: Build Rich-Context AI Apps with Anthropic — DeepLearning.AI](https://www.deeplearning.ai/short-courses/mcp-build-rich-context-ai-apps-with-anthropic/) (free) + [Anthropic Academy's "Introduction to Model Context Protocol" and "MCP: Advanced Topics"](https://anthropic.skilljar.com/) (free, certificates) + [Hugging Face MCP Course](https://huggingface.co/learn/mcp-course) (free) |
| The official protocol spec itself | [modelcontextprotocol.io](https://modelcontextprotocol.io/) (free, canonical reference) |

**Build this:** write one custom MCP server that exposes a tool (e.g. querying a small local database) and connect it to Claude — this alone will make tool schemas, transport, and permissions concrete instead of abstract.

---

## AI Agents

| Topic | Primary resource |
|---|---|
| What an agent is, tool use, planning, memory, multi-step workflows, evaluation, deployment | [Hugging Face Agents Course](https://huggingface.co/learn/agents-course) (free, ~25 hours, certificate) — the current canonical "start here" for agents |
| Agent design patterns: reflection, tool use, planning, multi-agent collaboration | [AI Agentic Design Patterns — DeepLearning.AI](https://www.deeplearning.ai/short-courses/) (free to watch; search this catalog) |
| Building agents as state machines, persistent memory, human-in-the-loop, streaming | [LangGraph course — LangChain Academy](https://academy.langchain.com/) (free) |
| Practical engineering perspective on when/how to build agents | ["Building Effective Agents" — Anthropic engineering blog](https://www.anthropic.com/research/building-effective-agents) (free, widely cited) |
| Computer-use agents, multi-agent systems, orchestration, failure recovery, long-running agents | Covered across the Hugging Face Agents Course + LangGraph course above; for computer-use specifically, see [Anthropic's computer-use documentation](https://docs.claude.com/en/docs/agents-and-tools/tool-use/computer-use-tool) (free) |

**Build this:** build a small agent that has 2–3 real tools (e.g. web search, a calculator, a file reader) and can decide which to call and when — then deliberately break it (give it a task one tool can't handle) and watch how it fails, so you understand failure modes, not just happy paths.

---

## Multimodal AI

| Topic | Primary resource |
|---|---|
| Multimodal RAG (text + images + video), contrastive learning, visual instruction tuning | [Multimodal RAG: Chat with Videos — DeepLearning.AI/Intel](https://www.deeplearning.ai/short-courses/multimodal-rag-chat-with-videos/) (free) and [Building Multimodal Search and RAG — DeepLearning.AI/Weaviate](https://www.deeplearning.ai/short-courses/building-multimodal-search-and-rag/) (free; check availability, it has occasionally been under maintenance) |
| Vision-language models, image/video understanding | [Hugging Face Computer Vision Course](https://huggingface.co/learn/computer-vision-course) (free) + MIT 6.S191's Gen AI/multimodal lecture (free) |
| Speech recognition/synthesis, document intelligence | Whisper (OpenAI, free/open-source) documentation and tutorials; covered practically inside the Multimodal RAG course above |

**Build this:** build a "chat with my video" tool using Whisper for transcription + a vision-language model for frame captioning + a vector store — the DeepLearning.AI course above walks this exact build.

---

## Evaluation

| Topic |  Primary resource |
|---|---|
| Test/golden datasets, benchmark design, accuracy, relevance, groundedness, hallucination rate, regression testing | [Evaluating AI Agents — DeepLearning.AI](https://learn.deeplearning.ai/courses/evaluating-ai-agents) (free) |
| LLM-as-judge, alignment, automatic evaluators | [Weights & Biases: LLM Apps – Evaluation](https://wandb.ai/site/courses/evals/) (free) + [Arize: LLM Evaluation Basics](https://courses.arize.com/l/pdp/llm-evaluation-basics) (free, ~1 hour, certificate) |
| Broad conceptual grounding for product/eval teams | [Evidently AI's free 7-day LLM Evaluations email course](https://www.evidentlyai.com/llm-evaluations-course) (free) |
| Toxicity, safety, latency, cost tradeoffs, observability | Covered across the courses above; observability tooling itself is worth exploring via Arize Phoenix and Weights & Biases (both free tiers) |
| Classical ML metrics (confusion matrix, precision/recall/F1, ROC-AUC, cross-validation) | [StatQuest](https://www.youtube.com/@statquest) — see Phase 2 |

**Build this:** take your RAG pipeline from Phase 8 and write an actual eval script: 20 test questions with expected answers, a code-based check for retrieval hit-rate, and an LLM-as-judge scoring rubric for answer quality. This is the single most job-relevant skill in this whole list — most teams don't do it well.

---

## AI Security

| Topic | Primary resource |
|---|---|
| The canonical free reference for LLM-specific vulnerabilities (prompt injection, data poisoning, supply-chain, excessive agency, etc.) | [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) (free, living industry-standard document) |
| Prompt injection & indirect prompt injection — hands-on practice | [Gandalf by Lakera](https://gandalf.lakera.ai/) (free, interactive game — genuinely the best hands-on intro to how injection actually works) |
| Deep, continually-updated writing on prompt injection from a leading independent researcher | [Simon Willison's prompt injection series](https://simonwillison.net/series/prompt-injection/) (free blog, extremely well-regarded in the field) |
| Excessive agency, tool abuse, privilege escalation, sensitive-data handling | Anthropic's and OpenAI's safety/guardrails documentation (free) — [docs.claude.com](https://docs.claude.com/) safety section |
| Structured, guided course on AI red-teaming concepts | [Learn Prompting: AI Red Teaming](https://learnprompting.org/) (has free tier content) |
| Memory poisoning, MCP server security, agent trust boundaries | Covered in the Anthropic Academy MCP tracks (Phase 9) and reinforced in the OWASP LLM Top 10 |

**Build this:** take the RAG or agent project you already built and try to prompt-inject it yourself — plant a malicious instruction inside a document it retrieves and see if you can get it to ignore its system prompt. Then fix it. Attacking your own system is the fastest way to internalize this.

---

## AI Infrastructure / MLOps

| Topic | Primary resource |
|---|---|
| Training, serving, GPUs, distributed computing, model monitoring, data pipelines, production concerns end-to-end | [Full Stack Deep Learning](https://fullstackdeeplearning.com/) (free, course + free videos) |
| Production ML engineering practices, project structure, CI for ML | [Made With ML — Goku Mohandas](https://madewithml.com/) (free, excellent, code-first) |
| Evaluation/observability in production | Same tools as Phase 12 (Arize, Weights & Biases free tiers) |

**Build this:** take your RAG or agent project and actually deploy it — a small FastAPI service behind Docker, logged with basic observability, is enough to learn the real gap between "notebook works" and "service runs."

---

## master resource bank since theres no time for above bs:

## TRACK A — Applied AI Engineer

### 1. Python (refresher, not a course)
| Resource | Covers |
|---|---|
| **[Real Python](https://realpython.com/)** (~15h, article-by-article, not the whole site) | syntax refresher, functions, classes/OOP, modules/packages, exceptions, type hints, lists/dicts/sets/tuples, iterators/generators, async/await, venv, pip, regex, threading, sqlite3/DB-API, JSON, HTTP/requests, testing (pytest) |
| **[Python Data Science Handbook — Jake VanderPlas](https://jakevdp.github.io/PythonDataScienceHandbook/)** (free, full book online, ~15h skimmed) | NumPy, Pandas, Jupyter, Matplotlib, Seaborn, scikit-learn — all in one book, one author, consistent examples |

### 2. Generative AI + LLM Engineering
| Resource | Covers |
|---|---|
| **[Karpathy: Neural Networks — Zero to Hero](https://www.youtube.com/@AndrejKarpathy)** — just the micrograd + makemore + "Let's build GPT" videos (~15h) | LLM/transformer foundations, tokenization, sampling, from-scratch backprop |
| **[Anthropic's Prompt Engineering Interactive Tutorial](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)** (~4h) | system instructions, role separation, structured prompting, few-shot, output constraints, reasoning strategies, prompt injection as a prompting concept |
| **[Hugging Face NLP Course](https://huggingface.co/learn/nlp-course)** (~18h) | fine-tuning, distillation, classification, translation, language models, embeddings basics, hands-on with real models |
| **[Hugging Face Diffusion Models Course](https://huggingface.co/learn/diffusion-course)** (~9h) | diffusion models, image generation, denoising |

*Models landscape (OpenAI/Anthropic/Google/open-source/local) doesn't need a course — that's a 1h skim of the [Hugging Face Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) + [Ollama docs](https://github.com/ollama/ollama) whenever you need it.*

### 3. Embeddings + RAG
| Resource | Covers |
|---|---|
| **[DeepLearning.AI: Vector Databases — from Embeddings to Applications](https://www.deeplearning.ai/short-courses/vector-databases-embeddings-applications/)** + **[Pinecone Learn](https://www.pinecone.io/learn/)** (~5h combined) | embedding models, cosine similarity, vector search, nearest-neighbor search, semantic search, vector DBs, indexing, chunking |
| **[DeepLearning.AI: Building Agentic RAG with LlamaIndex](https://www.deeplearning.ai/short-courses/building-agentic-rag-with-llamaindex/)** (~2h) | document ingestion, parsing, chunking, embedding, retrieval, reranking, hybrid search, metadata filtering, agentic/multi-step RAG, citation, hallucination mitigation |

*2 resources. Note: DLAI short courses run 1-2h each — they're dense, not padded.*

### 4. Tool Calling + MCP
| Resource | Covers |
|---|---|
| **[Anthropic Tool Use docs](https://docs.claude.com/en/docs/build-with-claude/tool-use/overview)** (~3h) | function calling, tool schemas, structured outputs, input validation, error handling, tool selection |
| **[DeepLearning.AI: MCP — Build Rich-Context AI Apps with Anthropic](https://www.deeplearning.ai/short-courses/mcp-build-rich-context-ai-apps-with-anthropic/)** (~2h) | MCP clients/servers, tools/resources/prompts, schemas, capability negotiation, transport, auth |

*Keep [modelcontextprotocol.io](https://modelcontextprotocol.io/) bookmarked as the reference spec, not something you "study."*

### 5. AI Agents
| Resource | Covers |
|---|---|
| **[Hugging Face Agents Course](https://huggingface.co/learn/agents-course)** (~20h, you can skip redundant intro units) | tool use, planning, memory, multi-step workflows, evaluation, deployment, multi-agent systems |
| **["Building Effective Agents" — Anthropic engineering blog](https://www.anthropic.com/research/building-effective-agents)** (~1h) | practical design patterns: when to use an agent vs. a workflow, reflection, orchestration, failure recovery |

*For computer-use agents specifically, [Anthropic's computer-use docs](https://docs.claude.com/en/docs/agents-and-tools/tool-use/computer-use-tool) are a reference, not a course — read them when you build one.*

### 6. Multimodal AI
| Resource | Covers |
|---|---|
| **[Hugging Face Computer Vision Course](https://huggingface.co/learn/computer-vision-course)** (~12h, selective) | vision-language models, image/video understanding, document intelligence |
| **[DeepLearning.AI: Multimodal RAG — Chat with Videos](https://www.deeplearning.ai/short-courses/multimodal-rag-chat-with-videos/)** (~2h) | Whisper speech transcription, VLM frame captioning, multimodal vector store — an actual working "chat with video" build |

*OCR (Tesseract/EasyOCR) is a 1-2h tool-docs read when you need it, not a dedicated resource.*

### 7. Evaluation
| Resource | Covers |
|---|---|
| **[DeepLearning.AI: Evaluating AI Agents](https://learn.deeplearning.ai/courses/evaluating-ai-agents)** (~4h) | golden datasets, benchmark design, accuracy/relevance/groundedness/hallucination rate, regression testing, LLM-as-judge |

*Classical metrics (confusion matrix, precision/recall/F1, ROC-AUC, cross-validation) are already covered by StatQuest in Track B's ML section — no second resource needed here.*

### 8. AI Security
| Resource | Covers |
|---|---|
| **[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)** (~4h, living doc) | prompt injection, indirect injection, data poisoning, supply-chain risk, excessive agency, tool abuse, privilege escalation, sensitive-data handling — maps almost 1:1 to your entire security list |
| **[Gandalf by Lakera](https://gandalf.lakera.ai/)** (~2h) | hands-on injection practice — actually attacking a system beats reading about it |

*[Simon Willison's prompt injection series](https://simonwillison.net/series/prompt-injection/) is worth following as ongoing reading, not a one-time study item.*

**Track A subtotal: 16 resources, ~118 hours.**

---

## TRACK B — Academic / Syllabus (Classical AI, ML theory, toy problems)

| Resource | Covers |
|---|---|
| **[MIT 6.034 — Patrick Winston (OCW)](https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/)** (~20h) | state-space search (BFS/DFS/A*, hill climbing, generate-and-test), CSP, adversarial search, propositional/predicate logic, resolution, clause form conversion, expert systems (MYCIN), procedural vs. declarative knowledge — covers nearly your whole Classical AI list in one course |
| **AO\*, Water Jug, Monkey & Banana, Block Words** — these are practice problems, not lecture topics. Read the problem statement once (GeeksforGeeks has all four), then implement each yourself with BFS/A* from the Winston course. (~4h total, not a "resource" you study) |
| **[Stanford CS228 lecture notes](https://ermongroup.github.io/cs228-notes/)** (free, no signup, ~12h) | Bayesian Networks, Markov Random Fields, HMM, directed graphical models, exploiting independence properties, distributions-to-graphs, inference — this single notes site is literally built around your exact PGM syllabus list |
| **[StatQuest with Josh Starmer](https://www.youtube.com/@statquest)** (~12h, pick relevant videos) | decision trees, Naive Bayes, PCA, EM/GMM, curse of dimensionality, confusion matrix, precision/recall/F1, ROC-AUC, cross-validation — reused for Track A's Evaluation section too |
| **[Andrew Ng: Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction)** (audit free, ~30h) | supervised learning end-to-end (regression, NN, decision trees), unsupervised (k-means, anomaly detection), basic reinforcement learning |
| **Association rule mining** — one [GeeksforGeeks read](https://www.geeksforgeeks.org/machine-learning/apriori-algorithm/) (~1h). It's a small enough topic that a dedicated course would be padding. |

**Track B subtotal: 6 resources (~5 courses + 1 practice block), ~65 hours.**