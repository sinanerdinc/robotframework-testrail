# robotframework-testrail
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

### project_id
Represents the value of testrail project id.

### user
Represents the value of testrail user.

### pwd
Represents the value of testrail password.

### url
Represents the value of your instance of testrail url

### include_all
Default: True

This setting determines whether the test run to be created should include all of your scenarios or only the tagged scenarios.

### report_file
Represents the path of your test result file.