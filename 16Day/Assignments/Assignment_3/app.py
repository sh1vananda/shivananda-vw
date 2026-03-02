from flask import Flask, render_template

app = Flask(__name__)

comments = [
    {"username": "abc", "comment": "this is dumb", "likes": 100, "flagged": False},
    {"username": "def", "comment": "great idea", "likes": 73, "flagged": True},
    {"username": "ghi", "comment": "stupid long comment " * 20, "likes": 47, "flagged": False}
]

@app.route("/comments")
def feed():
    total = len(comments)
    flagged_count = len([comment for comment in comments if comment["flagged"]])
    most_liked = max(comments, key=lambda x: x["likes"])
    usernames = ", ".join(comment["username"] for comment in comments)
    return render_template("comments.html", comments=comments, total=total, most_liked=most_liked, flagged_count=flagged_count, usernames=usernames)

if __name__ == "__main__":
    app.run(debug=True)