import argparse
from argparse import Namespace
from sqlite3 import Connection, Cursor

import libs.databaseConnector as DatabaseConnector
import libs.main


class SSLMetrics:
    def __init__(self) -> None:
        pass

    def arguementHandling(self) -> Namespace:
        parser = argparse.ArgumentParser(
            prog="SSL Metrics Dashboard Defect Density Module",
            usage="To collect, store, parse, and calculate information related to the Defect Density software metric.",
            description="This module will access the GitHub REST API to gather information about a specific repository pertaining to Defect Density.\n\n Afterwards, the data will be analyzed and displayed as graphs.",
            epilog="This program was created by the Loyola University Chicago Software and Systems Laboratory.",
        )

        parser.add_argument(
            "url", help="The GitHub URL of the project that is to be analyzed", type=str
        )
        parser.add_argument(
            "token",
            help="The GitHub Personal Access Token that is used to properly interact with the GitHub REST API",
        )

        return parser.parse_args()

    def stripURL(
        self,
        url: str = "https://github.com/SoftwareSystemsLaboratory/Metrics-Dashboard",
    ) -> list:
        if self.githubURL.find("github.com/") == -1:
            exit("Invalid URL Arg")

        splitURL = self.githubURL.split("/")

        if len(splitURL) != 5:
            exit("Invalid URL Arg")

        githubUserName = splitURL[-2]
        githubRepositoryName = splitURL[-1]

        return [githubUserName, githubRepositoryName]

    def launch(
        self, githubUserName: str, githubRepositoryName: str, githubRepositoryURL
    ) -> None:
        # TODO: Implement CMD Line arguements into the code here
        Master.Logic(
            username=self.githubUser,
            repository=self.githubRepo,
            token=self.githubToken,
            tokenList=self.githubTokenList,
            cursor=self.dbCursor,
            connection=self.dbConnection,
        ).program()


if __name__ == "__main__":
    s = SSLMetrics()

    args = s.arguementHandling()

    s.stripURL(url=args.url)

    s.launch()

else:
    print("SSLMetrics.py is meant to ran by itself and not imported as a module.")
