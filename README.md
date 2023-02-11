# robotframework-testrail
Import all test results to your testrail panel.

# Usage

```
pip install -r requirements.txt
```

You must add a tag named CID to your test scenarios. 

Example:

```
*** Test Cases ***
Example Scenario
    [Tags]  CID=100
    log to console    Hello
```
CID=100 represents the case id of the scenario that you have created in Testrail.

```
python robot_testrail.py --project_id testrail_project_id --user testrail_email --pwd testrail_password --url testrail_url --report_file output.xml  
```
