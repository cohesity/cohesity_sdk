# UpgradeCheckNodeResult

The healthcheck results for node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_ip** | **str** | The node ip | [optional] 
**node_test_results** | [**List[UpgradeCheckTestResult]**](UpgradeCheckTestResult.md) | The healthcheck test results for node | [optional] 
**node_test_status** | **str** | The healthcheck run status for node | [optional] 

## Example

```python
from cohesity_sdk.models.upgrade_check_node_result import UpgradeCheckNodeResult

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeCheckNodeResult from a JSON string
upgrade_check_node_result_instance = UpgradeCheckNodeResult.from_json(json)
# print the JSON string representation of the object
print(UpgradeCheckNodeResult.to_json())

# convert the object into a dict
upgrade_check_node_result_dict = upgrade_check_node_result_instance.to_dict()
# create an instance of UpgradeCheckNodeResult from a dict
upgrade_check_node_result_from_dict = UpgradeCheckNodeResult.from_dict(upgrade_check_node_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


