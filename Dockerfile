FROM python:3.10-slim

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y tor
RUN pip install requests[socks] Flask duckduckgo_search

# Torの設定ファイルをコピー
COPY torrc /etc/tor/torrc

# 作業ディレクトリを作成
WORKDIR /app

# Pythonスクリプトをコピー
COPY main.py .

# Torを起動してPythonスクリプトを実行する前にログを確認
CMD service tor start && sleep 5 && service tor status && python main.py