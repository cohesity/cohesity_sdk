# UpgradeCheckTestResult

The healthcheck test result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_id** | **str** | The healthcheck test id | [optional] 
**test_kb_link** | **str** | The kb link for diagnosing test failure | [optional] 
**test_name** | **str** | The healthcheck test name | [optional] 
**test_output** | **str** | The healthcheck test output | [optional] 
**test_result** | **str** | The healthcheck test result | [optional] 

## Example

```python
from cohesity_sdk.helios.models.upgrade_check_test_result import UpgradeCheckTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeCheckTestResult from a JSON string
upgrade_check_test_result_instance = UpgradeCheckTestResult.from_json(json)
# print the JSON string representation of the object
print(UpgradeCheckTestResult.to_json())

# convert the object into a dict
upgrade_check_test_result_dict = upgrade_check_test_result_instance.to_dict()
# create an instance of UpgradeCheckTestResult from a dict
upgrade_check_test_result_from_dict = UpgradeCheckTestResult.from_dict(upgrade_check_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


