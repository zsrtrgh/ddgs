from flask import Flask, request, jsonify
from duckduckgo_search import DDGS
import requests

app = Flask(__name__)

# Torプロキシ設定
proxy = 'socks5://127.0.0.1:9050'

@app.route('/videos', methods=['GET'])
def search():
    query = request.args.get('q')

    try:
        # DDGSライブラリを使用してDuckDuckGoの検索結果を取得
        with DDGS(proxy=proxy, timeout=20) as ddgs:
            results = list(ddgs.videos(
                keywords=query + " site:youtube.com",
                region="jp-ja",
                safesearch="off",
                resolution="high",
                max_results=20,
            ))
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e), "type": "DuckDuckGoSearchException"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)