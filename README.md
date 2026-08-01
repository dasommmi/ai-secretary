# AI Secretary

Telegram Bot 기반 개인 AI 비서. 백그라운드 모니터링(수영 강좌 빈자리 알림)과
텔레그램 커맨드 기반 AI 어시스턴트(대화, 메모, 콘텐츠 생성) 기능을 제공한다.

## Features

### 🏊 Swim Course Vacancy Monitor
`CHECK_INTERVAL`(기본 10초)마다 지정된 수영 강좌 페이지를 크롤링해서,
등록해둔 강좌(`SwimService.TARGETS`)에 빈자리가 생기면 텔레그램으로 알림을 보낸다.
앱 실행 시 백그라운드 스레드로 자동 시작된다.

### 🤖 AI Chat (`/ask`)
OpenRouter API를 통해 질문에 답변한다. (`AI_MODEL` 설정값 사용)

### 🧠 Memory (`/remember`, `/memories`)
SQLite(`assistant.db`)에 사용자별 메모를 저장하고 조회한다.

### ✍️ Content Generation (`/content restaurant`)
양식에 맞춰 답장을 보내면 프롬프트를 구성해 OpenRouter로 글을 생성하고,
검증(`ContentValidator`)에 실패하면 최대 3회까지 자동으로 재요청한 뒤
`generated/{content_type}/` 아래에 마크다운 파일로 저장한다.
현재는 `restaurant` 타입만 실제로 연결되어 있다 (`cafe`, `travel`, `development`는
`ContentType` enum에는 정의되어 있지만 템플릿/파서가 아직 없어 사용 불가).

### 📊 Status / Health (`/status`, `/health`)
현재 환경(dev/prod), 스케줄러 상태, uptime 등을 조회한다.

## Commands

| Command | 설명 |
|---|---|
| `/help` | 명령어 목록 |
| `/status` | 환경 / 스케줄러 상태 |
| `/health` | 런타임 상태 (환경, 상태, uptime) |
| `/remember <내용>` | 메모 저장 |
| `/memories` | 저장된 메모 조회 |
| `/ask <질문>` | AI에게 질문 |
| `/content restaurant` | 콘텐츠 작성 세션 시작 → 이후 텍스트 메시지로 양식 작성 시 자동 생성 |

## Tech Stack

- Python
- `python-telegram-bot` — Telegram Bot 인터페이스
- `requests`, `beautifulsoup4` — 수영 강좌 페이지 크롤링
- OpenRouter API — AI 대화 / 콘텐츠 생성 (`ai/openrouter.py`)
- SQLite — 메모 저장 (`database/db.py`)

> `google-generativeai`가 `requirements.txt`에는 남아있지만 현재 코드에서는 사용하지 않는다
> (전부 OpenRouter로 대체됨. 정리 대상).

## Project Structure

```
app.py              # 엔트리포인트 - 스케줄러 스레드 + Telegram Receiver 시작
config.py           # 환경 변수 / 설정
core/                # 런타임 상태, 스케줄러, 로거, base_service
bot/                 # Telegram 핸들러 / 수신 / 발신
services/            # 비즈니스 로직 (assistant, swim, memory, content)
content/             # 콘텐츠 생성 파이프라인 (template/parser/prompt/generator/writer/validator)
models/              # 도메인 모델 (Course, ContentSession)
database/            # SQLite 연결 및 스키마
generated/           # 생성된 콘텐츠 마크다운 결과물
```

## Known Issues / TODO

- `handlers.py`의 `content_generate_command`는 정의만 되어 있고 `receiver.py`에
  커맨드로 등록되어 있지 않다 (죽은 코드, 정리 필요)
- `content` 파이프라인에 `cafe`/`travel`/`development` 템플릿·파서 추가 필요
- `requirements.txt`에서 미사용 Google Generative AI 관련 패키지 정리 필요
- 전반적인 리팩토링 예정 (현재 소스는 일부 미정리 상태)

## Roadmap

- [x] Swim vacancy monitor
- [x] Telegram commands (help/status/health/remember/memories/ask/content)
- [x] SQLite (memories)
- [x] Content generation pipeline (restaurant)
- [ ] Content generation - cafe / travel / development
- [ ] AI Function Calling
- [ ] Docker
- [ ] GitHub Actions
