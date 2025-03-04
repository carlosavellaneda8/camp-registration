FROM python:3.12-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:0.6.4 /uv /uvx /bin/

ADD . /app
WORKDIR /app
RUN uv sync --frozen

EXPOSE 8501
ENTRYPOINT ["uv", "run", "streamlit", "run", "src/camp_registration/app.py", "--server.port=8501", "--server.address=0.0.0.0]
