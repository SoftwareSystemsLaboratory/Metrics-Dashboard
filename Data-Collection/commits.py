from libs.collector import Collector_4


class Commits(Collector_4):
    def insertData(self, dataset: dict) -> int:
        for dataPoint in range(len(dataset)):
            sha = dataset[dataPoint]["sha"]
            author = dataset[dataPoint]["commit"]["author"]["name"]
            date = dataset[dataPoint]["commit"]["committer"]["date"]
            treeSHA = dataset[dataPoint]["commit"]["tree"]["sha"]
            commentCount = dataset[dataPoint]["commit"]["comment_count"]

            sql = "INSERT OR IGNORE INTO Commits (ID, SHA, Branch, Author, Commit_Date, Tree_SHA, Comment_Count) VALUES (?,?,?,?,?,?,?);"

            self.connection.executeSQL(
                sql, (self.id, sha, self.sha, author, date, treeSHA, commentCount), True
            )

            self.id += 1
