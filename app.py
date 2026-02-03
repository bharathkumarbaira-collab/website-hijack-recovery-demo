from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>Website Hijack & Recovery Demo</h2><p>Go to /logs to view incidents.</p>"

@app.route("/logs")
def logs():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM incidents")
    rows = cursor.fetchall()
    conn.close()

    html = """
    <h2>Incident Logs</h2>
    <table border="1" cellpadding="5">
        <tr>
            <th>ID</th>
            <th>Website</th>
            <th>Attack Type</th>
            <th>Time</th>
            <th>Status</th>
        </tr>
        {% for row in rows %}
        <tr>
            <td>{{ row[0] }}</td>
            <td>{{ row[1] }}</td>
            <td>{{ row[2] }}</td>
            <td>{{ row[3] }}</td>
            <td>{{ row[4] }}</td>
        </tr>
        {% endfor %}
    </table>
    """

    return render_template_string(html, rows=rows)

if __name__ == "__main__":
    app.run(debug=True)






