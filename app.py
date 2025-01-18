from flask import Flask, request, jsonify
# from downloader.youtube_downloader import download_youtube_video

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Video Bot API!"})

# @app.route('/download', methods=['POST'])
# def download_video():
#     data = request.json
#     url = data.get('url')
#     platform = data.get('platform')

#     if platform == 'youtube':
#         file_path = download_youtube_video(url)
#         return jsonify({"message": "Downloaded successfully", "file_path": file_path})
#     else:
#         return jsonify({"error": "Platform not supported"}), 400

if __name__ == '__main__':
    app.run(debug=True)
