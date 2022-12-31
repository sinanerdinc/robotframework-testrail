import xml.dom.minidom
from testrail import *
import click
from datetime import datetime


class Testrail:
    def __init__(self, url: str, user: str, pwd: str):
        self.url = url
        self.user = user
        self.pwd = pwd
        self.client = self.connect_testrail()

    def connect_testrail(self):
        _client = APIClient(self.url)
        _client.user = self.user
        _client.password = self.pwd
        return _client

    def create_test_run(self, run_name: str, project_id: str):
        payload = {"suite_id": 1, "name": f"Test run - {run_name}", "assignedto_id": 1, "include_all": "1"}
        return self.client.send_post('add_run/' + str(project_id), payload)

    def parse_result(self, file_name: str):
        msg = {}
        cidstatus = {}
        xmldoc = xml.dom.minidom.parse(file_name)
        testlist = xmldoc.getElementsByTagName('test')
        for test in testlist:
            tags = test.getElementsByTagName('tag')
            for tag in tags:
                cid_str = tag.firstChild.nodeValue
                if cid_str[:4] == "CID=":
                    cid = cid_str[4:]
                    status = test.getElementsByTagName('status')
                    if status[-1].attributes['status'].value == "PASS":
                        cidstatus[cid] = '1'
                    else:
                        cidstatus[cid] = '5'
                        for message in test.getElementsByTagName('msg'):
                            msg[cid] = message.firstChild.nodeValue
        return cidstatus, msg

    def add_result_for_case(self, file_name: str, run_info: dict):
        cidstatus, msg = self.parse_result(file_name)
        for cid in iter(cidstatus):
            payload = {"status_id": cidstatus[cid], "comment": "# Robot Framework result: #\n" + msg.get(cid, "Successful")}
            resp = self.client.send_post('add_result_for_case/' + str(run_info['id']) + '/' + str(cid), payload)


@click.command()
@click.option("--project_id", type=int, required=True, help="Set project id")
@click.option("--user", type=str, required=True, help="Set user name")
@click.option("--pwd", type=str, required=True, help="Set password")
@click.option("--url", type=str, required=True, help="Set testrail url")
@click.option("--run_name", type=str, required=False, help="Set testrail test run's name")
@click.option("--report_file", type=str, default="output.xml", required=True, help="The xml file that include test results created by robot framework.")
def run(project_id, user, pwd, url, run_name, report_file):
    if run_name is None:
        now = datetime.now()
        run_name = now.strftime("%d/%m/%Y %H:%M:%S")

    _testrail = Testrail(url, user, pwd)
    run_info = _testrail.create_test_run(run_name, project_id)
    _testrail.add_result_for_case(report_file, run_info)


if __name__ == '__main__':
    run()
