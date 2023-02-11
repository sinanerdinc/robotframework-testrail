# robotframework-testrail
Import all test results to your testrail panel.

# Usage

You must add a tag named CID to your test scenarios. Example CID=100 , the value 100 here represents the id of the scenario that you have created in Testrail."

```
*** Test Cases ***
Example Scenario
    [Tags]  CID=100
    log to console    Hello
```


```
python robot_testrail.py --project_id testrail_project_id --user testrail_email --pwd testrail_password --url testrail_url --report_file output.xml  
```
