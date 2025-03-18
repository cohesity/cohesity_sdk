# UpgradeCheckRunTestsRequest

Specifies upgrade checks request parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | **str** | Type of upgrade checks(pre/post) to run | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.upgrade_check_run_tests_request import UpgradeCheckRunTestsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeCheckRunTestsRequest from a JSON string
upgrade_check_run_tests_request_instance = UpgradeCheckRunTestsRequest.from_json(json)
# print the JSON string representation of the object
print(UpgradeCheckRunTestsRequest.to_json())

# convert the object into a dict
upgrade_check_run_tests_request_dict = upgrade_check_run_tests_request_instance.to_dict()
# create an instance of UpgradeCheckRunTestsRequest from a dict
upgrade_check_run_tests_request_from_dict = UpgradeCheckRunTestsRequest.from_dict(upgrade_check_run_tests_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


