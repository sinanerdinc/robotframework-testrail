# robotframework-testrail
<tr>
<p align="left">

  <td>
    <a href="https://hub.docker.com/r/sinanerdinc/robotframeworktestrail" target="_blank"><img src="https://img.shields.io/docker/pulls/sinanerdinc/robotframeworktestrail?style=for-the-badge" /></a>
  </td>
  <td>
    <img src="https://img.shields.io/github/issues-closed/sinanerdinc/robotframework-testrail?style=for-the-badge" />
  </td>
  <td>
    <img src="https://img.shields.io/github/issues-pr/sinanerdinc/robotframework-testrail?style=for-the-badge" />
  </td>
  <td>
    <img src="https://img.shields.io/github/license/sinanerdinc/robotframework-testrail?style=for-the-badge" />
  </td>
  <td>
    <img src="https://img.shields.io/github/contributors/sinanerdinc/robotframework-testrail?style=for-the-badge" />
  </td>
  
  
</p>  
</tr>

Import all test results to your testrail panel.

## Installation

```
pip install -r requirements.txt
```

## Usage
You must add a tag named CID to your test scenarios. 

```
*** Test Cases ***
Example Scenario
    [Tags]  CID=100
    log to console    Hello
```
CID=100 represents the case id of the scenario that you have created in Testrail.

```
python robot_testrail.py --project_id testrail_project_id --user testrail_email --pwd testrail_password --url testrail_url --include_all False --report_file output.xml  
```

## Docker
```
docker run --rm -v $(pwd)/output:/app/output sinanerdinc/robotframeworktestrail --project_id PROJECTID --user YOUREMAIL --pwd PASSWORD --url TESTRAILURL --include_all True --report_file output/output.xml
```

Don't forget to change your output directory name in the command.

## Parameters

| Name | Default | Type | Required | Description |
|--|--|--|--|--|
| project_id |  | int |  True|Testrail project id.  |
| user |  | str | True | Testrail user. |
| pwd |  | str | True | Testrail password. |
| url |  | str | True | Testrail url |
| run_name | "%d/%m/%Y %H:%M:%S" | str | False | Testrail run name. |
| include_all | True  | boolean | False  | This setting determines whether the test run to be created should include all of your scenarios or only the tagged scenarios. |
| report_file |  | str | True | Path of your output.xml file. |


