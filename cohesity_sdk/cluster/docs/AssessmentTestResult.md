# AssessmentTestResult

The result of a test run as part of assessment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_id** | **str** | Specifies the test ID. | 
**test_kb_link** | **str** | Specifies the kb link for diagnosing test failure. | 
**test_name** | **str** | Specifies the test name. | 
**test_output** | **str** | Specifies the test output message. | 
**test_result** | **str** | Specifies the test result. | 

## Example

```python
from cohesity_sdk.cluster.models.assessment_test_result import AssessmentTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of AssessmentTestResult from a JSON string
assessment_test_result_instance = AssessmentTestResult.from_json(json)
# print the JSON string representation of the object
print(AssessmentTestResult.to_json())

# convert the object into a dict
assessment_test_result_dict = assessment_test_result_instance.to_dict()
# create an instance of AssessmentTestResult from a dict
assessment_test_result_from_dict = AssessmentTestResult.from_dict(assessment_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


