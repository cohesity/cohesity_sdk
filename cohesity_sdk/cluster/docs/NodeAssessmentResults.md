# NodeAssessmentResults

Results of assessment tests for a node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the node. | [optional] 
**ip** | **str** | Specifies the IP address of the node. | [optional] 
**results** | [**List[AssessmentTestResult]**](AssessmentTestResult.md) | Specifies the test results for node. | [optional] 
**status** | **str** | Specifies the test run status for node. | 

## Example

```python
from cohesity_sdk.cluster.models.node_assessment_results import NodeAssessmentResults

# TODO update the JSON string below
json = "{}"
# create an instance of NodeAssessmentResults from a JSON string
node_assessment_results_instance = NodeAssessmentResults.from_json(json)
# print the JSON string representation of the object
print(NodeAssessmentResults.to_json())

# convert the object into a dict
node_assessment_results_dict = node_assessment_results_instance.to_dict()
# create an instance of NodeAssessmentResults from a dict
node_assessment_results_from_dict = NodeAssessmentResults.from_dict(node_assessment_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


